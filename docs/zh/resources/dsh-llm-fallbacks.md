---
title: "dsh-llm-fallbacks"
description: "An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件"
keywords: "dsh-llm-fallbacks, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-llm-fallbacks

> ⭐ 20 · ✅ 活跃 · 插件

## 一句话介绍

An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件

## 详细介绍

[English](README.md) | [中文](README.zh-CN.md) Automatic provider/model fallback chains for dsh (DeepSeek Harness): when an agent's LLM requests keep failing — retries exhausted, auth errors, quota exceeded, rate limiting (429) — the plugin switches provider/model along the fallback chain for the current role, and the current step/turn continues on the target model: tasks are not interrupted by model problems. Install with a single command (see [Install](#install)): dsh plugin --profile web add ds

## 作者
**[omdsh-dev](https://github.com/omdsh-dev)**

## 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-llm-fallbacks)
- [完整 README](https://github.com/omdsh-dev/dsh-llm-fallbacks#readme)
- [返回dsh-llm-fallbacks所在分类](../plugins.md)
