---
title: "dsh-guardian"
description: "Agent security guardrail: intercepts and audits every tool call, requiring human confirmation on sensitive operations."
keywords: "dsh-guardian, security, plugin, deepseek harness, dsh"
---
# dsh-guardian

> ⭐ 4 · ✅ active · plugin

## One-liner

Agent security guardrail: intercepts and audits every tool call, requiring human confirmation on sensitive operations.

## About

LLM Agent（Claude Code / DeepSeek Harness）能自主执行 shell、读写文件、发网络请求。一旦被**提示注入**、**工具投毒**或**模型误判**带偏，可能在你不知情时 `rm -rf`、读取 `.ssh/id_rsa`、把密钥外泄到远程。本插件是一道**运行时安全网**： Agent 想执行工具 → guardian/check 前置审查 → 命中规则 → 拦截 / 人工批准 → 才放行

## Author
**[cdxiaodong](https://github.com/cdxiaodong)**

## Links

- [GitHub Repository](https://github.com/cdxiaodong/dsh-guardian)
- [Full README](https://github.com/cdxiaodong/dsh-guardian#readme)
- [Back to the Plugins list](../plugins.md)
