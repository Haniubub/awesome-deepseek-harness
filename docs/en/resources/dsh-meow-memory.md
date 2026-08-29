---
title: "dsh-meow-memory"
description: "Cross-session memory plugin for DeepSeek Harness: seven-layer SQLite store (soul/user/project/fact/lesson/topic/rules), BM25 retrieval, per-window dream consolidation. 跨会话七层长期记忆插件。"
keywords: "dsh-meow-memory, registry, awesome-list, coding, memory, deepseek harness, dsh"
---
# dsh-meow-memory

> ⭐ 58 · ✅ active · awesome-list

## One-liner

Cross-session memory plugin for DeepSeek Harness: seven-layer SQLite store (soul/user/project/fact/lesson/topic/rules), BM25 retrieval, per-window dream consolidation. 跨会话七层长期记忆插件。

## About

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）打造的跨会话记忆插件。 **核心理念**：每个工作区维护一份结构化记忆数据库（`.dsh-meow/memory.db`，基于 `node:sqlite`）。 静态记忆手册（数据总览 + 工具用法 + 写作准则）以固定 section 的形式放在 **system prompt** 里—— 文本恒定，因此不会破坏 LLM provider 的 KV/上下文缓存。动态内容（soul/user 全量、设计原则、 记忆导引）作为**第一条用户消息的前缀**注入，且首轮只注入长期记忆、不做关键词命中； 从第二轮起每条用户消息做关键词命中（top-2）。模型按需用 `memory_search` / `memory_project` 深入检索。每个窗口由自己的主 agent 在空闲时（"dream"）整理记忆 （本窗口建立 + 提取过的记忆），以窗口最后一次对话时间戳冻结其知识。

## Author
**[Phant0Meow](https://github.com/Phant0Meow)**

## Links

- [GitHub Repository](https://github.com/Phant0Meow/dsh-meow-memory)
- [Full README](https://github.com/Phant0Meow/dsh-meow-memory#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
