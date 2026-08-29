---
title: "dsh-advisor"
description: "Advisor - Pair a second model that passively reviews each turn and injects notes.  搭配一个会在每轮对话被动注入见解和审查的副模型。"
keywords: "dsh-advisor, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-advisor

> ⭐ 16 · ✅ active · plugin

## One-liner

Advisor - Pair a second model that passively reviews each turn and injects notes.  搭配一个会在每轮对话被动注入见解和审查的副模型。

## About

A standalone dsh plugin bundle porting the omp "advisor" subsystem: a per-session reviewer model that observes the primary transcript, reviews each stepped turn with an explicitly configured model (provider + model are required), and injects severity-ranked advice (nit / concern / blocker) back into the session — without polluting or recursively reviewing itself. Install with a single command: dsh plugin --profile web add dsh-advisor # <name> = your profile name **Advisory only.** The advisor ne

## Author
**[omdsh-dev](https://github.com/omdsh-dev)**

## Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-advisor)
- [Full README](https://github.com/omdsh-dev/dsh-advisor#readme)
- [Back to the Plugins list](../plugins.md)
