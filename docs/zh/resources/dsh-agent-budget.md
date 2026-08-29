---
title: "dsh-agent-budget"
description: "Native Harness agent-tree token budget plugin"
keywords: "dsh-agent-budget, developer, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-agent-budget

> ⭐ 2 · ✅ 活跃 · 插件

## 一句话介绍

Native Harness agent-tree token budget plugin

## 详细介绍

`dsh-agent-budget` gives one live agent session, or its complete local descendant tree, a durable Token limit and absolute deadline. It reserves capacity before every attributed `llm/stream` provider attempt and replaces that estimate with provider-reported usage after the stream settles, so concurrent child agents cannot all spend the same remaining balance. The plugin is an out-of-tree DSH bundle for one Host process. A hard budget refuses new provider attempts before dispatch; it is not an ex

## 作者
**[vibeinging](https://github.com/vibeinging)**

## 链接

- [GitHub 仓库](https://github.com/vibeinging/dsh-agent-budget)
- [完整 README](https://github.com/vibeinging/dsh-agent-budget#readme)
- [返回dsh-agent-budget所在分类](../plugins.md)
