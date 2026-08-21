---
title: "dsh-routed-subagent"
description: "Run a one-shot subagent fully mounted on any agent preset from any session, with per-call model/provider override, a model-availability pre-check, and external CLI engines (codex / claude / codebuddy) with background jobs, live progress, kill, and continuable sessions."
keywords: "dsh-routed-subagent, developer, plugin, multi-agent, deepseek harness, dsh"
---
# dsh-routed-subagent

> ⭐ 0 · ✅ active · plugin

## One-liner

Run a one-shot subagent fully mounted on any agent preset from any session, with per-call model/provider override, a model-availability pre-check, and external CLI engines (codex / claude / codebuddy) with background jobs, live progress, kill, and continuable sessions.

## About

A global [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that lets **any session dispatch a one-shot subagent fully mounted on ANY agent preset**, with **per-call model/provider override** and a **model-availability pre-check**. The stock `subagent` / `subagent_fork` tools force children to inherit the PARENT's preset. This plugin replaces that with a custom subagent provider whose async child setup calls `agentPresets.mount(childCtx, <preset>)` — so the child adopts t

## Author
**[bpc-oss](https://github.com/bpc-oss)**

## Links

- [GitHub Repository](https://github.com/bpc-oss/dsh-routed-subagent)
- [Full README](https://github.com/bpc-oss/dsh-routed-subagent#readme)
- [Back to the Plugins list](../plugins.md)
