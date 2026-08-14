# Contributing to Awesome DeepSeek Harness

Thanks for helping grow the DeepSeek Harness ecosystem directory! 🐋

## What we accept

* Plugins, skills, workflows, agents, clients, tools and integrations for the **official** [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)
* Clearly useful surrounding tooling (docs, examples, registries)
* Fixes: outdated entries, broken links, incorrect descriptions, wrong statuses

We do **not** list dead repositories. Every entry is verified against the live GitHub API.

## How to add a project

1. Fork the repo.
2. Open the matching file in `data/`:
   * `plugins.json` — runtime plugins (discovery, memory, search, developer tools, UI, vision, fun)
   * `skills.json` — reusable agent skills/procedures
   * `workflows.json` — workflows and automation
   * `agents.json` — agents and multi-agent tooling
   * `clients.json` — desktop apps, terminal clients, mobile
   * `integrations.json` — MCP servers, IDE/browser/channel integrations, ACP
   * `examples.json` — templates and runnable starters
   * `tutorials.json` — books, handbooks, courses
   * `awesome-lists.json` — other registries/directories
   * `related.json` — other agent harnesses (non-DSH)
3. Add an entry following the schema in `schemas/resource.schema.json`:

```json
{
  "id": "kebab-case-unique",
  "name": "project-name",
  "type": "plugin",
  "category": "ui",
  "repository": "https://github.com/owner/repo",
  "description": "One-line English description.",
  "description_zh": "一句话中文描述。",
  "capabilities": ["ui"],
  "status": "experimental",
  "verified": false,
  "stars": 0
}
```

4. Run the checks locally (Python 3, no dependencies):

```bash
python3 scripts/validate.py
python3 scripts/generate-readme.py
python3 scripts/generate-docs.py
```

5. Commit both the `data/` change and the regenerated `README.md` / `README.zh-CN.md` / `docs/` files. Keep the PR small and focused.

## Entry checklist

* `repository` is a public GitHub URL that exists (we run `check-links.py` in CI)
* `description` and `description_zh` are one line each and describe what the project *does*
* `capabilities` are taken from the schema enum
* `status` reflects reality: `active` (recent pushes) / `experimental` (very new or unstable) / `wip` / `inactive`
* `verified` is `false` unless a maintainer has manually confirmed install instructions + code

## Submission template

See [.github/ISSUE_TEMPLATE/submit-project.yml](.github/ISSUE_TEMPLATE/submit-project.yml) for the full issue form.

## Scripts

| Script | Purpose |
|---|---|
| `validate.py` | Validate `data/` against the schema (required before PR) |
| `check-links.py` | Verify every repository URL is reachable |
| `discover-github.py` | Search GitHub for new ecosystem candidates |
| `update-metadata.py` | Refresh star counts, descriptions, archive status |
| `generate-readme.py` | Regenerate resource tables in both READMEs |
| `generate-docs.py` | Regenerate the MkDocs site under `docs/` |

## Style

* Keep descriptions factual and concise — no marketing language
* One entry per repository
* Sort order inside files is by stars, descending (the generators do this automatically)
* Never edit the tables between `<!-- AUTO:resources:START -->` markers by hand — edit `data/`, then regenerate
