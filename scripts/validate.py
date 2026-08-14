#!/usr/bin/env python3
"""Validate the data registries against schemas/resource.schema.json.

Usage:
    python3 scripts/validate.py [--strict]
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SCHEMA_PATH = ROOT / "schemas" / "resource.schema.json"

VALID_TYPES = {"plugin", "skill", "workflow", "agent", "client", "tool",
               "integration", "example", "tutorial", "awesome-list", "related"}
VALID_STATUS = {"active", "experimental", "wip", "inactive"}

REPO_RE = re.compile(r"^https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")

FILE_TYPES = {
    "plugins.json": "plugin",
    "skills.json": "skill",
    "workflows.json": "workflow",
    "agents.json": "agent",
    "clients.json": "client",
    "integrations.json": "integration",
    "examples.json": "example",
    "tutorials.json": "tutorial",
    "awesome-lists.json": "awesome-list",
    "related.json": "related",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                        help="Treat warnings as errors (used in CI).")
    args = parser.parse_args()

    schema = json.loads(SCHEMA_PATH.read_text())
    errors, warnings = [], []

    # Load schema definitions for quick checks
    schema_props = schema.get("properties", {})
    type_enum = set(schema_props["type"]["enum"])
    cat_enum = set(schema_props["category"]["enum"])
    cap_enum = set(schema_props["capabilities"]["items"]["enum"])

    seen_ids = {}
    seen_repos = {}
    counts = {}

    for fname, expected_type in FILE_TYPES.items():
        path = DATA_DIR / fname
        if not path.exists():
            errors.append(f"missing data file: {fname}")
            continue
        entries = json.loads(path.read_text())
        counts[fname] = len(entries)
        if not isinstance(entries, list):
            errors.append(f"{fname}: expected a JSON array")
            continue
        for i, e in enumerate(entries):
            loc = f"{fname}[{i}]"
            if not isinstance(e, dict):
                errors.append(f"{loc}: not an object")
                continue

            for field in ("id", "name", "type", "category", "repository",
                          "description", "description_zh", "capabilities",
                          "status", "verified", "stars"):
                if field not in e:
                    errors.append(f"{loc}: missing required field '{field}'")
            for field in ("id", "name", "repository", "description", "description_zh"):
                if field in e and not isinstance(e[field], str):
                    errors.append(f"{loc}.{field}: must be a string")
            if "id" in e and not ID_RE.match(e["id"]):
                errors.append(f"{loc}.id: bad id '{e.get('id')}'")
            if "id" in e:
                if e["id"] in seen_ids:
                    errors.append(f"{loc}.id: duplicate id '{e['id']}' (also {seen_ids[e['id']]})")
                else:
                    seen_ids[e["id"]] = loc
            if "repository" in e and not REPO_RE.match(e["repository"]):
                errors.append(f"{loc}.repository: bad URL '{e.get('repository')}'")
            if "repository" in e:
                if e["repository"] in seen_repos:
                    errors.append(f"{loc}.repository: duplicate repo {e['repository']} (also {seen_repos[e['repository']]})")
                else:
                    seen_repos[e["repository"]] = loc
            if "type" in e and e["type"] not in type_enum:
                errors.append(f"{loc}.type: invalid type '{e.get('type')}'")
            # "plugin" resources may live in any file (the ecosystem is plugin-dominated);
            # other types must match the file they live in.
            if "type" in e and e["type"] not in ("plugin", expected_type):
                errors.append(f"{loc}.type: '{e.get('type')}' does not match file type '{expected_type}'")
            if "category" in e and e["category"] not in cat_enum:
                errors.append(f"{loc}.category: invalid category '{e.get('category')}'")
            if "status" in e and e["status"] not in VALID_STATUS:
                errors.append(f"{loc}.status: invalid status '{e.get('status')}'")
            if "verified" in e and not isinstance(e["verified"], bool):
                errors.append(f"{loc}.verified: must be boolean")
            if "stars" in e and (not isinstance(e["stars"], int) or e["stars"] < 0):
                errors.append(f"{loc}.stars: must be a non-negative integer")
            if "capabilities" in e:
                caps = e["capabilities"]
                if not isinstance(caps, list) or not caps:
                    errors.append(f"{loc}.capabilities: must be a non-empty array")
                else:
                    for c in caps:
                        if c not in cap_enum:
                            errors.append(f"{loc}.capabilities: invalid capability '{c}'")
                    if len(set(caps)) != len(caps):
                        errors.append(f"{loc}.capabilities: duplicates present")

    total = sum(counts.values())
    print(f"entries: {total} across {len(FILE_TYPES)} files")
    for fname, n in counts.items():
        print(f"  {fname}: {n}")

    if errors:
        print("\nERRORS:")
        for err in errors:
            print(f"  [x] {err}")
    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"  [!] {w}")

    ok = not errors and (not args.strict or not warnings)
    print(f"\n{'PASS' if ok else 'FAIL'} ({len(errors)} errors, {len(warnings)} warnings)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
