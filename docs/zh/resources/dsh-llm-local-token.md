---
title: "dsh-llm-local-token"
description: "复用本机 Codex CLI 与 Claude Code OAuth 凭据的 DSH 模型提供方路由，无需另配 API Key。"
keywords: "dsh-llm-local-token, developer, plugin, security, observability, deepseek harness, dsh"
---
# dsh-llm-local-token

> ⭐ 0 · ✅ 活跃 · 插件

## 一句话介绍

复用本机 Codex CLI 与 Claude Code OAuth 凭据的 DSH 模型提供方路由，无需另配 API Key。

## 详细介绍

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that serves LLM calls with the OAuth tokens your **local CLIs already hold** — no separate API key, no extra login. If you are signed in to the Codex CLI or to Claude Code, those subscriptions become usable model routes inside DSH. Both routes appear in the model picker as soon as the plugin loads. A route whose credential is missing is skipped instead of failing the boot. <table> <tr> <td align="center" width="50%"><su

## 作者
**[tianxia--](https://github.com/tianxia--)**

## 链接

- [GitHub 仓库](https://github.com/tianxia--/dsh-llm-local-token)
- [完整 README](https://github.com/tianxia--/dsh-llm-local-token#readme)
- [返回dsh-llm-local-token所在分类](../plugins.md)
