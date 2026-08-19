---
title: "dsh-plugin-guard"
description: "Install safety net for DeepSeek Harness: pre-install snapshots, one-click/automatic rollback, guarded boot, and incident reports that auto-trigger agent analysis. 中文: DeepSeek Harness 插件安装安全网（安装前自动快照、一键/自动回退、守护启动、事故报告自动触发 Agent 分析）。"
keywords: "dsh-plugin-guard, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin-guard

> ⭐ 27 · ✅ active · plugin

## One-liner

Install safety net for DeepSeek Harness: pre-install snapshots, one-click/automatic rollback, guarded boot, and incident reports that auto-trigger agent analysis. 中文: DeepSeek Harness 插件安装安全网（安装前自动快照、一键/自动回退、守护启动、事故报告自动触发 Agent 分析）。

## About

A bad plugin install can leave the app unable to boot, and fixing it by hand usually means digging through config files. This plugin automates the whole chain: Install a plugin (any method) │ tools.guard hook: automatic snapshot BEFORE the install (in-process) ▼ Guarded boot (boot-guard script) │ snapshot before boot → start dsh web → health check ├─ healthy ─────────────────────────────► passes through untouched └─ unhealthy ─► auto-rollback to last good snapshot → retry once → write an inciden

## Author
**[lxzy-7](https://github.com/lxzy-7)**

## Links

- [GitHub Repository](https://github.com/lxzy-7/dsh-plugin-guard)
- [Full README](https://github.com/lxzy-7/dsh-plugin-guard#readme)
- [Back to the Plugins list](../plugins.md)
