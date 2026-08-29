---
title: "dsh-trace"
description: "DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP."
keywords: "dsh-trace, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-trace

> ⭐ 2 · ✅ 活跃 · 插件

## 一句话介绍

DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP.

## 详细介绍

`dsh-trace` stores DeepSeek Harness session telemetry in a local embedded yiTrace database. It observes records after the host's `telemetry/record` waterfall, projects each DSH turn into one yiTrace trace, and writes SDK-native start, log, and end events through yiTrace's Node-API database. No HTTP server, port, or token is required. The plugin is opt-in, adds no model-visible context, and lives outside the DeepSeek Harness monorepo.

## 作者
**[vibeinging](https://github.com/vibeinging)**

## 链接

- [GitHub 仓库](https://github.com/vibeinging/dsh-trace)
- [完整 README](https://github.com/vibeinging/dsh-trace#readme)
- [返回dsh-trace所在分类](../plugins.md)
