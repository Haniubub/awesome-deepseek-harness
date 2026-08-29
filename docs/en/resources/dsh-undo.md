---
title: "dsh-undo"
description: "Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again."
keywords: "dsh-undo, registry, awesome-list, coding, context, deepseek harness, dsh"
---
# dsh-undo

> ⭐ 4 · ✅ active · awesome-list

## One-liner

Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again.

## About

Durable, multi-level undo/redo for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). It rewinds model context by real user turn and restores workspace files changed by tools in that turn. The commands are handled locally and are never sent to the model: - **`/undo`** rewinds the latest visible real user message and every surface message after it. - **`/undo <user-seq>`** rewinds from a specific visible user message, including all later turns. - **`/redo`** restores the

## Author
**[LingLambda](https://github.com/LingLambda)**

## Links

- [GitHub Repository](https://github.com/LingLambda/dsh-undo)
- [Full README](https://github.com/LingLambda/dsh-undo#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
