---
title: "dsh-swarm-router"
description: "DSH plugin: sub-agent matrix swarm — routes heterogeneous tasks to the most suitable model (OpenRouter-like + cfgpu.com/llm/square), dispatches each via in-process subagents. 32/32 benchmark green."
keywords: "dsh-swarm-router, multi-agent, agent, coding, ui, deepseek harness, dsh"
---
# dsh-swarm-router

> ⭐ 2 · ✅ 活跃 · 智能体

## 一句话介绍

DSH plugin: sub-agent matrix swarm — routes heterogeneous tasks to the most suitable model (OpenRouter-like + cfgpu.com/llm/square), dispatches each via in-process subagents. 32/32 benchmark green.

## 详细介绍

[English](README.md) | [中文](README.zh.md) A DeepSeek Harness **bundle** that turns a batch of heterogeneous tasks into a **sub-agent matrix swarm**: it routes each task to the most suitable model from an OpenRouter-like gateway plus the `cfgpu.com/llm/square` catalog, then dispatches each assignment in parallel as a real in-process subagent (or a direct `ctx.llm` call) pinned to that model — quick tasks land on fast/cheap models, hard tasks on strong reasoning models. A formal design write-up li

## 作者
**[r600a-code](https://github.com/r600a-code)**

## 链接

- [GitHub 仓库](https://github.com/r600a-code/dsh-swarm-router)
- [完整 README](https://github.com/r600a-code/dsh-swarm-router#readme)
- [返回dsh-swarm-router所在分类](../agents.md)
