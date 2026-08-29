---
title: "dsh-ha-orchestrator"
description: "DeepSeek Harness（dsh）动态 Cordis 插件：模型高可用回退 + 五种模式子智能体编排（fanout / pipeline / supervisor / map-reduce / router）"
keywords: "dsh-ha-orchestrator, multi-agent, agent, coding, deepseek harness, dsh"
---
# dsh-ha-orchestrator

> ⭐ 7 · ✅ 活跃 · 智能体

## 一句话介绍

DeepSeek Harness（dsh）动态 Cordis 插件：模型高可用回退 + 五种模式子智能体编排（fanout / pipeline / supervisor / map-reduce / router）

## 详细介绍

HA Orchestrator 是 [DeepSeek Harness](https://github.com/deepseek-ai/dsh)（dsh）的插件： - 模型调用中途出错时，自动改用备用模型重试，任务继续跑下去。 - 提供一个 `orchestrate` 工具，模型遇到适合的任务会自己调用它，把工作拆给多个子智能体并行执行（`fanout`）、分阶段执行（`pipeline`），或进行评审/归约（`supervisor`、`map-reduce`、`router`）。 配置页里还能定义自己的子智能体（也可以一句话让 AI 生成）；界面和提示词文案支持中英文，跟随 DSH 语言。 [English](README.en.md) **特别适合：** 深度调研、大型代码库阅读、批量审查、多方案对比和实现计划编排。

## 作者
**[Saktawdi](https://github.com/Saktawdi)**

## 链接

- [GitHub 仓库](https://github.com/Saktawdi/dsh-ha-orchestrator)
- [完整 README](https://github.com/Saktawdi/dsh-ha-orchestrator#readme)
- [返回dsh-ha-orchestrator所在分类](../agents.md)
