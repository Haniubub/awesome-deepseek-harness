---
title: "dsh-routed-subagent"
description: "从任意会话派发一个完整挂载到任意 agent preset 的一次性子代理，支持按次指定模型/provider、模型可用性预检，以及外部 CLI 引擎（codex / claude / codebuddy），支持后台任务、实时进度、终止与可续会话。"
keywords: "dsh-routed-subagent, developer, plugin, multi-agent, deepseek harness, dsh"
---
# dsh-routed-subagent

> ⭐ 0 · ✅ 活跃 · 插件

## 一句话介绍

从任意会话派发一个完整挂载到任意 agent preset 的一次性子代理，支持按次指定模型/provider、模型可用性预检，以及外部 CLI 引擎（codex / claude / codebuddy），支持后台任务、实时进度、终止与可续会话。

## 详细介绍

A global [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin that lets **any session dispatch a one-shot subagent fully mounted on ANY agent preset**, with **per-call model/provider override** and a **model-availability pre-check**. The stock `subagent` / `subagent_fork` tools force children to inherit the PARENT's preset. This plugin replaces that with a custom subagent provider whose async child setup calls `agentPresets.mount(childCtx, <preset>)` — so the child adopts t

## 作者
**[bpc-oss](https://github.com/bpc-oss)**

## 链接

- [GitHub 仓库](https://github.com/bpc-oss/dsh-routed-subagent)
- [完整 README](https://github.com/bpc-oss/dsh-routed-subagent#readme)
- [返回dsh-routed-subagent所在分类](../plugins.md)
