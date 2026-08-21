---
title: "dsh-docker"
description: "隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。"
keywords: "dsh-docker, mcp, integration, coding, deepseek harness, dsh"
---
# dsh-docker

> ⭐ 0 · ✅ active · integration

## One-liner

隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。

## About

Isolated installability **and MCP loopback** sandbox for DeepSeek Harness plugins. Org: [dshoneys](https://github.com/dshoneys) · sister tool: [mcp_guard](https://github.com/dshoneys/mcp_guard) The image pins `@deepseek-ai/dsh`, keeps `$DSH_HOME` on a tmpfs (never your host `~/.dsh`), and proves a plugin composed with `--dump-config`. That step does not boot a model, so it does not spend tokens.

## Author
**[dshoneys](https://github.com/dshoneys)**

## Links

- [GitHub Repository](https://github.com/dshoneys/dsh-docker)
- [Full README](https://github.com/dshoneys/dsh-docker#readme)
- [Back to the MCP & Integrations list](../integrations.md)
