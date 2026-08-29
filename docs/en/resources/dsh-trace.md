---
title: "dsh-trace"
description: "DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP."
keywords: "dsh-trace, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-trace

> ⭐ 2 · ✅ active · plugin

## One-liner

DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP.

## About

`dsh-trace` stores DeepSeek Harness session telemetry in a local embedded yiTrace database. It observes records after the host's `telemetry/record` waterfall, projects each DSH turn into one yiTrace trace, and writes SDK-native start, log, and end events through yiTrace's Node-API database. No HTTP server, port, or token is required. The plugin is opt-in, adds no model-visible context, and lives outside the DeepSeek Harness monorepo.

## Author
**[vibeinging](https://github.com/vibeinging)**

## Links

- [GitHub Repository](https://github.com/vibeinging/dsh-trace)
- [Full README](https://github.com/vibeinging/dsh-trace#readme)
- [Back to the Plugins list](../plugins.md)
