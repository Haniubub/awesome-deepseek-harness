---
title: "dsh-guardian"
description: "Agent 安全护栏：拦截并审计所有工具调用，命中敏感操作就要求人工确认。"
keywords: "dsh-guardian, security, plugin, deepseek harness, dsh"
---
# dsh-guardian

> ⭐ 4 · ✅ 活跃 · 插件

## 一句话介绍

Agent 安全护栏：拦截并审计所有工具调用，命中敏感操作就要求人工确认。

## 详细介绍

LLM Agent（Claude Code / DeepSeek Harness）能自主执行 shell、读写文件、发网络请求。一旦被**提示注入**、**工具投毒**或**模型误判**带偏，可能在你不知情时 `rm -rf`、读取 `.ssh/id_rsa`、把密钥外泄到远程。本插件是一道**运行时安全网**： Agent 想执行工具 → guardian/check 前置审查 → 命中规则 → 拦截 / 人工批准 → 才放行

## 作者
**[cdxiaodong](https://github.com/cdxiaodong)**

## 链接

- [GitHub 仓库](https://github.com/cdxiaodong/dsh-guardian)
- [完整 README](https://github.com/cdxiaodong/dsh-guardian#readme)
- [返回dsh-guardian所在分类](../plugins.md)
