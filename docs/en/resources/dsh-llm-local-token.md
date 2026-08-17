---
title: "dsh-llm-local-token"
description: "DeepSeek Harness provider routes that reuse local Codex CLI and Claude Code OAuth tokens instead of API keys."
keywords: "dsh-llm-local-token, developer, plugin, security, observability, deepseek harness, dsh"
---
# dsh-llm-local-token

> ⭐ 0 · ✅ active · plugin

## One-liner

DeepSeek Harness provider routes that reuse local Codex CLI and Claude Code OAuth tokens instead of API keys.

## About

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that serves LLM calls with the OAuth tokens your **local CLIs already hold** — no separate API key, no extra login. If you are signed in to the Codex CLI or to Claude Code, those subscriptions become usable model routes inside DSH. Both routes appear in the model picker as soon as the plugin loads. A route whose credential is missing is skipped instead of failing the boot. <table> <tr> <td align="center" width="50%"><su

## Author
**[tianxia--](https://github.com/tianxia--)**

## Links

- [GitHub Repository](https://github.com/tianxia--/dsh-llm-local-token)
- [Full README](https://github.com/tianxia--/dsh-llm-local-token#readme)
- [Back to the Plugins list](../plugins.md)
