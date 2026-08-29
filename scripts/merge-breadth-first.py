#!/usr/bin/env python3
"""Breadth-first merge: parse every discovered awesome-list README, resolve
redirects, dedupe against the registry, classify and merge new entries.

Usage:
    python3 scripts/merge-breadth-first.py [--token gho_xxx] [--dry-run]
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
BF_READMES = str(ROOT / "work" / "readmes_all.json")

URL_RE = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
HAS_CJK = re.compile(r"[\u4e00-\u9fff]")

EXCLUDE = {
    "henryz838978/deepseek-harness", "devin-axis/ipollowork", "pm-shawn/abu-cowork",
    "morlay/deepseek-harness", "octo-o-o-o/deepseek-harness-applicants",
    "deepseek-ai/deepseek-harness", "deepseek-ai/deepseek-harness.git",
    "fendouai/awesome-deepseek-harness",
}

# awesome lists themselves worth registering (name -> description_zh hint)
AWESOME_LISTS = [
    ("wgd753/awesome-dsh-plugin", "DSH 插件大集合（2000+ 链接）"),
    ("kingselyjoe/awesome-dsh-list", "DSH 综合资源列表（1000+ 链接）"),
    ("oslook/awesome-dsh-plugins", "DSH 插件精选列表"),
    ("coolbat/awesome-dsh-plugins", "DSH 插件大目录（500+ 链接）"),
    ("weekend-project-space/deepseek-harness-awesome-top-500", "DeepSeek Harness Top 500 资源索引"),
    ("dshworks/awesome-dsh-plugins", "DSH 插件目录"),
    ("dshworks/awesome-dsh-themes", "DSH 主题/皮肤目录"),
    ("web-casa/awesome-deepseek-harness-plugins", "DeepSeek Harness 插件精选"),
    ("vvlife/awesome-deepseek-harness-plugins", "DeepSeek Harness 插件目录"),
    ("cccakeee/awesome-dsh-plugins", "DSH 插件列表"),
    ("harris1121/awesome-deepseek-harness", "DeepSeek Harness 资源精选"),
    ("xiaomingx/awesome-deepseek-harness", "DeepSeek Harness 资源列表"),
    ("rodert/awesome-deepseek-harness", "DeepSeek Harness 精选资源"),
    ("herdeny/awesome-dsh-plugins-2026", "2026 DSH 插件列表"),
    ("sihanteng/awesome-deepseek-harness-plugins", "DeepSeek Harness 插件精选"),
    ("awesome-deepseekharness/awesome-deepseek-harness", "DSH 社区目录"),
    ("dongsheng123132/awesome-dsh-plugins", "DSH 插件精选"),
    ("deepseek-ai/awesome-deepseek-integration", "官方：DeepSeek 生态集成目录"),
    ("deepseek-ai/awesome-deepseek-coder", "官方：DeepSeek 编码资源"),
    ("walkinglabs/awesome-harness-engineering", "Harness 工程精选（跨生态）"),
    ("jiji262/awesome-harness-engineering", "Harness 工程精选（中文）"),
    ("jqueryscript/awesome-dsh-plugins", "DSH 插件列表"),
    ("yytbit/awesome-dsh-bridges", "DSH 桥接集成目录"),
    ("hackerfish/awesome-dsh-skills", "DSH 技能目录"),
    ("hackerfish/awesome-dsh-presets", "DSH 预设目录"),
]


_NO_PROXY_OPENER = None


def api_get(url, token):
    global _NO_PROXY_OPENER
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "bf-merge"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if _NO_PROXY_OPENER is None:
        _NO_PROXY_OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with _NO_PROXY_OPENER.open(req, timeout=20) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (403, 429):
                time.sleep(5 * (i + 1))
            else:
                return None
        except Exception:  # noqa: BLE001
            time.sleep(2)
    return None


def is_noise(name, desc):
    """Filter repos that use 'dsh'/'deepseek' but are unrelated to the Harness."""
    n = name.lower()
    repo = n.split("/")[-1]  # check the repo name, not the owner
    d = (desc or "").lower()
    if "dsh-external" in n:
        return True  # dead org namespace (redirects handled separately)
    if "dsharp" in n or "discord" in d:
        return True  # DSharpPlus etc.
    if n in EXCLUDE:
        return True
    # keep only strongly-DSH-related signals
    return not (
        repo.startswith("dsh")
        or repo.startswith("deepseek-harness")
        or "deepseek harness" in d
        or "dsh-plugin" in d
        or " dsh " in d
        or d.startswith("dsh ")
        or "for deepseek harness" in d
        or "deepseek harness" in d
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--batch-start", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=2000)
    args = parser.parse_args()
    token = args.token or os.environ.get("GH_TOKEN")

    readmes = json.loads(Path(BF_READMES).read_text())

    # 1. collect all links
    pool = {}
    print(f"readmes: {len(readmes)}", flush=True)
    for list_repo, md in readmes.items():
        for m in URL_RE.finditer(md):
            full = m.group(1).rstrip("/")
            parts = full.split("/")
            if len(parts) != 2:
                continue
            key = full.lower()
            pool.setdefault(key, {"list": list_repo})

    print(f"pool links: {len(pool)}", flush=True)
    # 2. resolve dsh-external redirects
    external = [k for k in pool if k.startswith("dsh-external/")]
    # dsh-external org was emptied; redirect targets were resolved in earlier
    # rounds and are already in the registry — drop the dead namespace.
    for key in external:
        pool.pop(key, None)

    # 3. dedupe vs registry
    existing = set()
    for f in DATA_DIR.glob("*.json"):
        if f.name in ("candidates.json", "readmes.json", "official-guides.json"):
            continue
        for e in json.loads(f.read_text()):
            if isinstance(e, dict) and "repository" in e:
                existing.add(e["repository"].replace("https://github.com/", "").lower())

    # 4. fetch metadata for new candidates
    new_pool = {k: v for k, v in pool.items() if k not in existing and not is_noise(k, "")}
    print(f"new candidates to fetch: {len(new_pool)}", flush=True)
    cache_path = ROOT / "work" / "metas_cache.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    todo = [k for k in new_pool if k not in cache]
    todo = todo[args.batch_start:args.batch_start + args.batch_size]
    print(f"cache hits: {len(new_pool) - len(todo)}, to fetch: {len(todo)} (batch {args.batch_start}+{args.batch_size})", flush=True)
    metas = dict(cache)
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(api_get, f"https://api.github.com/repos/{k}", token): k for k in todo}
        done = 0
        try:
            for fut in as_completed(futs):
                k = futs[fut]
                m = fut.result()
                if m:
                    cache[k] = m
                    if not m.get("archived"):
                        metas[k] = m
                done += 1
                if done % 100 == 0:
                    print(f"  fetched {done}/{len(todo)}", flush=True)
                    cache_path.parent.mkdir(exist_ok=True)
                    cache_path.write_text(json.dumps(cache, ensure_ascii=False))
                time.sleep(0.01)
        except Exception:
            import traceback
            traceback.print_exc()
            print(f"  ERROR after {done} fetches", flush=True)
        cache_path.parent.mkdir(exist_ok=True)
        cache_path.write_text(json.dumps(cache, ensure_ascii=False))

    # 5. filter noise with real descriptions, then classify
    fresh = [m for m in metas.values() if (m.get("description") or "").strip() and not is_noise(m["full_name"], m.get("description"))]
    print(f"pool: {len(pool)} | new candidates: {len(new_pool)} | fresh with description: {len(fresh)}")

    if args.dry_run:
        for m in sorted(fresh, key=lambda x: -x["stargazers_count"])[:40]:
            print(f"  {m['stargazers_count']:>6}  {m['full_name']}  {(m.get('description') or '')[:60]}")
        return 0

    # 6. classify + merge
    import collections
    import importlib.util
    _spec = importlib.util.spec_from_file_location("aggregate_mod", ROOT / "scripts" / "aggregate.py")
    _agg = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_agg)
    classify = _agg.classify
    groups = collections.defaultdict(list)
    for m in fresh:
        e = {
            "id": re.sub(r"[^a-z0-9]+", "-", m["full_name"].split("/")[1].lower()).strip("-"),
            "name": m["full_name"].split("/")[1],
            "type": "plugin",
            "category": "developer",
            "repository": m["html_url"],
            "description": (m.get("description") or "").strip(),
            "description_zh": (m.get("description") or "").strip() if HAS_CJK.search(m.get("description") or "") else (m.get("description") or "").strip(),
            "capabilities": ["coding"],
            "status": "active",
            "verified": False,
            "stars": m["stargazers_count"],
        }
        classify([e])
        groups[e.pop("_file")].append(e)

    for fname, entries in groups.items():
        data = json.loads((DATA_DIR / fname).read_text())
        before = len(data)
        data.extend(entries)
        data.sort(key=lambda x: -x.get("stars", 0))
        (DATA_DIR / fname).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        print(f"  {fname}: +{len(data) - before} (now {len(data)})")

    # 7. register DSH-relevant awesome lists dynamically
    al = json.loads((DATA_DIR / "awesome-lists.json").read_text())
    al_have = {e["repository"].replace("https://github.com/", "").lower() for e in al}
    registered = 0
    for list_repo, md in readmes.items():
        key = list_repo.lower()
        if key in al_have or not key.startswith("awesome"):
            continue
        links = set(URL_RE.findall(md))
        dsh_links = [l for l in links if l.lower().startswith("dsh") or "deepseek-harness" in l.lower()]
        if len(dsh_links) >= 5 or (len(links) >= 20 and ("dsh" in key or "harness" in key or "deepseek" in key)):
            m = api_get(f"https://api.github.com/repos/{list_repo}", token)
            if not m:
                continue
            desc = (m.get("description") or "").strip() or f"Awesome list: {list_repo}"
            al.append({
                "id": re.sub(r"[^a-z0-9]+", "-", list_repo.split("/")[1].lower()).strip("-") + "-" + list_repo.split("/")[0].lower(),
                "name": list_repo.split("/")[1],
                "type": "awesome-list",
                "category": "registry",
                "repository": m["html_url"],
                "description": desc,
                "description_zh": desc,
                "capabilities": ["search"],
                "status": "active",
                "verified": False,
                "stars": m["stargazers_count"],
            })
            al_have.add(key)
            registered += 1
    al.sort(key=lambda x: -x.get("stars", 0))
    (DATA_DIR / "awesome-lists.json").write_text(json.dumps(al, ensure_ascii=False, indent=2) + "\n")
    print(f"  awesome-lists.json: {len(al)} (+{registered} dynamic)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
