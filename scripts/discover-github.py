#!/usr/bin/env python3
"""Discover new DeepSeek Harness ecosystem candidates on GitHub.

Queries the GitHub Search API for the official discovery signals and writes
new candidates (not already present in data/) to data/candidates.json.

Usage:
    python3 scripts/discover-github.py [--token gho_xxx] [--limit 50]
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
OUT = DATA_DIR / "candidates.json"

QUERIES = [
    'topic:dsh-plugin',
    '"DeepSeek Harness" in:name,description',
    'dsh-plugin in:name',
    'dsh in:name "harness" in:description',
    '"@deepseek-ai/dsh" in:readme',
]


def known_repos():
    repos = set()
    for f in DATA_DIR.glob("*.json"):
        if f.name == "candidates.json":
            continue
        try:
            for e in json.loads(f.read_text()):
                repos.add(e["repository"].replace("https://github.com/", "").lower())
        except Exception:  # noqa: BLE001
            pass
    return repos


def search(query, token, per_page=100):
    url = ("https://api.github.com/search/repositories?q="
           + urllib.parse.quote(query) + f"&sort=stars&order=desc&per_page={per_page}")
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "awesome-dsh-discover"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read()).get("items", [])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=None)
    parser.add_argument("--limit", type=int, default=60)
    args = parser.parse_args()

    known = known_repos()
    candidates, seen = {}, set()
    for q in QUERIES:
        print(f"query: {q}")
        try:
            items = search(q, args.token)
        except Exception as e:  # noqa: BLE001
            print(f"  error: {e}")
            continue
        for it in items:
            name = it["full_name"].lower()
            if name in known or name in seen:
                continue
            seen.add(name)
            candidates[name] = {
                "repository": it["html_url"],
                "stars": it["stargazers_count"],
                "description": (it.get("description") or "")[:120],
                "updated": it.get("updated_at", "")[:10],
            }

    new = sorted(candidates.values(), key=lambda c: -c["stars"])
    OUT.write_text(json.dumps(new, ensure_ascii=False, indent=2) + "\n")
    print(f"found {len(new)} new candidates -> {OUT}")
    for c in new[:args.limit]:
        print(f"  {c['repository']}  ⭐{c['stars']}  {c['description'][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
