# Awesome DeepSeek Harness 🐋

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

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | ⭐80,001 | Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway. | ✅ active |
| 2 | [petdex](https://github.com/crafter-station/petdex) | ⭐3,777 | A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. | ✅ active |
| 3 | [Cordis](https://github.com/cordiverse/cordis) | ⭐3,182 | Meta-Framework of Spatiotemporal Composability — the plugin runtime DeepSeek Harness is built on. | ✅ active |
| 4 | [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) | ⭐2,324 | 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） | ✅ active |
| 5 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | ⭐1,697 | Large plugin and skin collection for DSH Web: task board, git graph, side panels, remote/mobile UI, pets, token stats and themes. | ✅ active |
| 6 | [modlens](https://github.com/liustack/modlens) | ⭐1,158 | The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works. | ✅ active |
| 7 | [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) | ⭐962 | Modern desktop experience built for the DeepSeek Harness ecosystem (plugin). | ✅ active |
| 8 | [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | ⭐793 | Claude Code-style full-screen terminal plugin: pixel-whale top bar, live status line, streaming thoughts, double-Esc rollback, context progress bar and TPS meter. | ✅ active |
| 9 | [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) | ⭐758 | Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code. | ✅ active |
| 10 | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | ⭐751 | Large curated list of installable DSH plugins (bilingual). | ✅ active |
| 11 | [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) | ⭐751 | Radar index repo: auto-scanning all discovered dsh plugin candidates with an evidence-based compatibility matrix. | ✅ active |
| 12 | [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | ⭐684 | Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs. | ✅ active |
| 13 | [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | ⭐573 | Open-source CMA-compatible agent runtime for any model: MCP tools, sandboxed sessions, audit, replay. | ✅ active |
| 14 | [museai](https://github.com/yejiming/MuseAI) | ⭐538 | 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用） | ✅ active |
| 15 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | ⭐506 | Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0). | ✅ active |
| 16 | [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) | ⭐465 | Community Orange Book: complete system prompts, a 129-line startup checklist and three raw session logs — first-hand testing the official docs lack. Free PDF/EPUB/HTML. | ✅ active |
| 17 | [mnemon](https://github.com/mnemon-dev/mnemon) | ⭐430 | LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary. | ✅ active |
| 18 | [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) | ⭐360 | Curated DSH ecosystem directory: plugins, tools and infrastructure from dsh-external/hub and the public dsh-plugin topic. | ✅ active |
| 19 | [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) | ⭐309 | Joke plugin: 2005 Chinese-web-style ad layer with sidebar banners, in-chat feed ads and corner popups. | ✅ active |
| 20 | [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) | ⭐302 | Vision toolkit for text-only models: intent-aware image Q&A, long-screenshot OCR, UI restoration, grounding and pixel diff. | ✅ active |

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
