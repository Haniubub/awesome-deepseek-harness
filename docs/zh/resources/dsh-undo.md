---
title: "dsh-undo"
description: "Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again."
keywords: "dsh-undo, registry, awesome-list, coding, context, deepseek harness, dsh"
---
# dsh-undo

> ⭐ 4 · ✅ 活跃 · 精选列表

## 一句话介绍

Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again.

## 详细介绍

Durable, multi-level undo/redo for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). It rewinds model context by real user turn and restores workspace files changed by tools in that turn. The commands are handled locally and are never sent to the model: - **`/undo`** rewinds the latest visible real user message and every surface message after it. - **`/undo <user-seq>`** rewinds from a specific visible user message, including all later turns. - **`/redo`** restores the

## 作者
**[LingLambda](https://github.com/LingLambda)**

## 链接

- [GitHub 仓库](https://github.com/LingLambda/dsh-undo)
- [完整 README](https://github.com/LingLambda/dsh-undo#readme)
- [返回dsh-undo所在分类](../awesome-lists.md)
