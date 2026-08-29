---
title: "dsh-claude-cli"
description: "DeepSeek Harness LLM provider that runs your installed Claude Code CLI as the model backend — no API key."
keywords: "dsh-claude-cli, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-claude-cli

> ⭐ 6 · ✅ 活跃 · 插件

## 一句话介绍

DeepSeek Harness LLM provider that runs your installed Claude Code CLI as the model backend — no API key.

## 详细介绍

Use the Claude Code CLI you already have installed as a DeepSeek Harness LLM provider. No API key. The plugin runs `claude` as a subprocess and streams its output back through the harness's LLM seam, so requests authenticate as whatever `claude` is already logged in as — a login you should check your plan's [usage terms](#usage-terms) against before automating. The harness stays the agent. The CLI's own agent loop, tools, settings, memory files, and MCP servers are all switched off; what is left

## 作者
**[katsos](https://github.com/katsos)**

## 链接

- [GitHub 仓库](https://github.com/katsos/dsh-claude-cli)
- [完整 README](https://github.com/katsos/dsh-claude-cli#readme)
- [返回dsh-claude-cli所在分类](../plugins.md)
