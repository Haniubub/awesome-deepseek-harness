#!/usr/bin/env python3
"""Generate the MkDocs documentation site (docs/) from the data registries.

Produces bilingual markdown pages under docs/en/ and docs/zh/ using the
mkdocs-static-i18n layout. Run `mkdocs build` afterwards to render the site.

Usage:
    python3 scripts/generate-docs.py
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DOCS = ROOT / "docs"

SECTIONS = [
    ("plugins", "Plugins", "plugins.json"),
    ("skills", "Skills", "skills.json"),
    ("workflows", "Workflows & Automation", "workflows.json"),
    ("agents", "Agents & Multi-Agent", "agents.json"),
    ("clients", "Clients (Desktop & TUI)", "clients.json"),
    ("integrations", "MCP & Integrations", "integrations.json"),
    ("examples", "Examples & Starters", "examples.json"),
    ("tutorials", "Tutorials & Learning", "tutorials.json"),
    ("awesome-lists", "Awesome Lists & Registries", "awesome-lists.json"),
    ("related", "Related Agent Harnesses", "related.json"),
]

CATEGORY_EN = {
    "discovery": "Plugin discovery",
    "memory": "Memory & context",
    "search": "Search & research",
    "developer": "Developer tools",
    "ui": "UI & experience",
    "vision": "Vision & multimodal",
    "fun": "Fun & lifestyle",
    "input-editing": "Input & editing",
    "notifications": "Notifications",
    "browser": "Browser control",
    "workflow": "Workflows",
    "automation": "Automation",
    "research": "Research",
    "multi-agent": "Multi-agent",
    "desktop": "Desktop",
    "terminal": "Terminal",
    "mobile": "Mobile",
    "mcp": "MCP",
    "ide": "IDE & editors",
    "channel": "Channels",
    "acp": "ACP",
    "learning": "Learning",
    "registry": "Registries",
    "harness": "Harness",
    "coding": "Coding",
    "security": "Security",
}
CATEGORY_ZH = {
    "discovery": "插件发现",
    "memory": "记忆与上下文",
    "search": "搜索与研究",
    "developer": "开发者工具",
    "ui": "界面与体验",
    "vision": "视觉与多模态",
    "fun": "娱乐与生活",
    "input-editing": "输入与编辑",
    "notifications": "通知",
    "browser": "浏览器控制",
    "workflow": "工作流",
    "automation": "自动化",
    "research": "研究",
    "multi-agent": "多智能体",
    "desktop": "桌面端",
    "terminal": "终端",
    "mobile": "移动端",
    "mcp": "MCP",
    "ide": "IDE 与编辑器",
    "channel": "渠道",
    "acp": "ACP",
    "learning": "学习",
    "registry": "注册表",
    "harness": "Harness",
    "coding": "编码",
    "security": "安全",
}

STATUS_EN = {"active": "✅ active", "experimental": "🧪 experimental", "wip": "🚧 WIP", "inactive": "💤 inactive"}
STATUS_ZH = {"active": "✅ 活跃", "experimental": "🧪 实验性", "wip": "🚧 进行中", "inactive": "💤 停更"}


def badge(e, zh):
    return (STATUS_ZH if zh else STATUS_EN)[e["status"]]


def row(e, zh):
    desc = e["description_zh"] if zh else e["description"]
    stars = f"⭐{e['stars']:,}" if e["stars"] else "–"
    return f"| [{e['name']}]({e['repository']}) | {stars} | {desc} | {badge(e, zh)} |"


def top_table(entries, zh, limit=10):
    if zh:
        head = "| # | 项目 | 星数 | 说明 | 状态 |\n|---|---|---|---|---|"
    else:
        head = "| # | Project | Stars | Description | Status |\n|---|---|---|---|---|"
    rows = [head]
    for i, e in enumerate(sorted(entries, key=lambda x: (-x["stars"], x["name"].lower()))[:limit], 1):
        desc = e["description_zh"] if zh else e["description"]
        b = (STATUS_ZH if zh else STATUS_EN)[e["status"]]
        rows.append(f"| {i} | [{e['name']}]({e['repository']}) | ⭐{e['stars']:,} | {desc} | {b} |")
    return "\n".join(rows)


def page_en(slug, title, entries):
    groups = {}
    for e in entries:
        groups.setdefault(e["category"], []).append(e)
    n = len(entries)
    lines = [f"# {title}", "",
             f"## 🔥 Top {min(10, n)}", "", top_table(entries, zh=False, limit=10),
             "", f"## Complete list ({n})", ""]
    for cat in sorted(groups):
        lines.append(f"\n**{CATEGORY_EN.get(cat, cat)}**\n")
        lines.append("| Project | Stars | Description | Status |")
        lines.append("|---|---|---|---|")
        for e in sorted(groups[cat], key=lambda x: (-x["stars"], x["name"].lower())):
            lines.append(row(e, zh=False))
    lines.append("")
    return "\n".join(lines)


def page_zh(slug, title, entries):
    groups = {}
    for e in entries:
        groups.setdefault(e["category"], []).append(e)
    n = len(entries)
    lines = [f"# {title}", "",
             f"## 🔥 Top {min(10, n)}", "", top_table(entries, zh=True, limit=10),
             "", f"## 完整列表（{n}）", ""]
    for cat in sorted(groups):
        lines.append(f"\n**{CATEGORY_ZH.get(cat, cat)}**\n")
        lines.append("| 项目 | 星数 | 说明 | 状态 |")
        lines.append("|---|---|---|---|")
        for e in sorted(groups[cat], key=lambda x: (-x["stars"], x["name"].lower())):
            lines.append(row(e, zh=True))
    lines.append("")
    return "\n".join(lines)


def global_top(zh, limit=20):
    all_entries = []
    for slug, title, fname in SECTIONS:
        all_entries += json.loads((DATA_DIR / fname).read_text())
    return top_table(all_entries, zh, limit=limit)


def main():
    shutil.rmtree(DOCS, ignore_errors=True)
    (DOCS / "en").mkdir(parents=True)
    (DOCS / "zh").mkdir(parents=True)
    (DOCS / "assets").mkdir(parents=True)

    for slug, title, fname in SECTIONS:
        entries = json.loads((DATA_DIR / fname).read_text())
        (DOCS / "en" / f"{slug}.md").write_text(page_en(slug, title, entries), encoding="utf-8")
        (DOCS / "zh" / f"{slug}.md").write_text(page_zh(slug, title, entries), encoding="utf-8")

    (DOCS / "en" / "index.md").write_text(INDEX_EN.replace("{{TOP}}", global_top(zh=False)), encoding="utf-8")
    (DOCS / "zh" / "index.md").write_text(INDEX_ZH.replace("{{TOP}}", global_top(zh=True)), encoding="utf-8")
    print("docs/ generated")
    return 0


INDEX_EN = """# Awesome DeepSeek Harness 🐋

> A curated ecosystem of **plugins, skills, workflows, agents, clients, tools and examples**
> for the official [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).

DeepSeek Harness (`dsh`) is DeepSeek AI's open-source agent harness built around a simple idea:

> **Everything is a Plugin.**

This site tracks the ecosystem around the official `deepseek-ai/deepseek-harness` project:
**Plugins · Skills · Workflows · Agents · Tools · Desktop · TUI · Integrations · Examples · Tutorials**.

## Getting started

```bash
# Run DSH
npx @deepseek-ai/dsh web        # Web UI at http://127.0.0.1:3080

# Install a plugin
dsh plugin --profile web add <package>
```

Plugins are discovered via the official GitHub topic: [`dsh-plugin`](https://github.com/topics/dsh-plugin).

> ⚠️ DeepSeek Harness is in developer preview and evolving rapidly. Compatibility may change — always check the linked repository before installing.

## 🔥 Global Top 20

{{TOP}}

## Browse the ecosystem

- [Plugins](plugins.md) — discovery, memory, search, developer tools, UI, vision, fun
- [Skills](skills.md) — reusable agent procedures and knowledge
- [Workflows & Automation](workflows.md) — deep research, plan → execute, automation
- [Agents & Multi-Agent](agents.md) — teams, crosstalk, subagents, bridges
- [Clients (Desktop & TUI)](clients.md) — desktop apps, terminal clients, mobile
- [MCP & Integrations](integrations.md) — MCP servers, IDE, browser, channels, ACP
- [Examples & Starters](examples.md) — templates you can run in minutes
- [Tutorials & Learning](tutorials.md) — books, handbooks and courses
- [Awesome Lists & Registries](awesome-lists.md) — directories and indexes
- [Related Agent Harnesses](related.md) — the broader harness ecosystem

## Project

- Source repository: [awesome-deepseek-harness](https://github.com/fendouai/awesome-deepseek-harness)
- Data registries: `data/*.json` (machine-readable, validated by CI)
- [简体中文](/zh/) · [English](/index.html)
"""

INDEX_ZH = """# Awesome DeepSeek Harness 🐋

> 官方 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 生态精选：
> **插件 · 技能 · 工作流 · 智能体 · 客户端 · 工具 · 示例 · 教程**。

DeepSeek Harness（`dsh`）是 DeepSeek AI 开源的智能体 Harness，围绕一个简单理念构建：

> **一切皆插件（Everything is a Plugin）。**

本站收录围绕官方 `deepseek-ai/deepseek-harness` 项目的完整生态。

## 快速开始

```bash
# 运行 DSH
npx @deepseek-ai/dsh web        # Web UI 位于 http://127.0.0.1:3080

# 安装插件
dsh plugin --profile web add <package>
```

插件的官方发现约定是 GitHub 主题标签：[`dsh-plugin`](https://github.com/topics/dsh-plugin)。

> ⚠️ DeepSeek Harness 处于开发者预览阶段，迭代极快，兼容性可能随时变化——安装前请先查看对应仓库。

## 🔥 全网 Top 20

{{TOP}}

## 浏览生态

- [插件](plugins.md) — 发现、记忆、搜索、开发者工具、界面、视觉、娱乐
- [技能](skills.md) — 可复用的智能体流程与知识
- [工作流与自动化](workflows.md) — 深度研究、计划→执行、自动化
- [智能体与多智能体](agents.md) — 团队、跨会话、子代理、桥接
- [客户端（桌面与终端）](clients.md) — 桌面应用、终端客户端、移动端
- [MCP 与集成](integrations.md) — MCP 服务器、IDE、浏览器、渠道、ACP
- [示例与模板](examples.md) — 几分钟即可运行的模板
- [教程与学习](tutorials.md) — 书籍、手册与课程
- [精选列表与注册表](awesome-lists.md) — 目录与索引
- [相关 Agent Harness](related.md) — 更广泛的 Harness 生态

## 项目说明

- 源仓库：[awesome-deepseek-harness](https://github.com/fendouai/awesome-deepseek-harness)
- 数据注册表：`data/*.json`（机器可读，CI 校验）
- [English](/index.html)
"""


if __name__ == "__main__":
    raise SystemExit(main())
