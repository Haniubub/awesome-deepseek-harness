---
title: "dsh-docker"
description: "隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。"
keywords: "dsh-docker, mcp, integration, coding, deepseek harness, dsh"
---
# dsh-docker

> ⭐ 0 · ✅ 活跃 · 集成

## 一句话介绍

隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。

## 详细介绍

Isolated installability **and MCP loopback** sandbox for DeepSeek Harness plugins. Org: [dshoneys](https://github.com/dshoneys) · sister tool: [mcp_guard](https://github.com/dshoneys/mcp_guard) The image pins `@deepseek-ai/dsh`, keeps `$DSH_HOME` on a tmpfs (never your host `~/.dsh`), and proves a plugin composed with `--dump-config`. That step does not boot a model, so it does not spend tokens.

## 作者
**[dshoneys](https://github.com/dshoneys)**

## 链接

- [GitHub 仓库](https://github.com/dshoneys/dsh-docker)
- [完整 README](https://github.com/dshoneys/dsh-docker#readme)
- [返回dsh-docker所在分类](../integrations.md)
