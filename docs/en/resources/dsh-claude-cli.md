---
title: "dsh-claude-cli"
description: "DeepSeek Harness LLM provider that runs your installed Claude Code CLI as the model backend — no API key."
keywords: "dsh-claude-cli, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-claude-cli

> ⭐ 6 · ✅ active · plugin

## One-liner

DeepSeek Harness LLM provider that runs your installed Claude Code CLI as the model backend — no API key.

## About

Use the Claude Code CLI you already have installed as a DeepSeek Harness LLM provider. No API key. The plugin runs `claude` as a subprocess and streams its output back through the harness's LLM seam, so requests authenticate as whatever `claude` is already logged in as — a login you should check your plan's [usage terms](#usage-terms) against before automating. The harness stays the agent. The CLI's own agent loop, tools, settings, memory files, and MCP servers are all switched off; what is left

## Author
**[katsos](https://github.com/katsos)**

## Links

- [GitHub Repository](https://github.com/katsos/dsh-claude-cli)
- [Full README](https://github.com/katsos/dsh-claude-cli#readme)
- [Back to the Plugins list](../plugins.md)
