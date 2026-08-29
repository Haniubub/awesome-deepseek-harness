---
title: "dsh-capability-receipt"
description: "Content-addressed receipts for skills actually loaded by DeepSeek Harness"
keywords: "dsh-capability-receipt, learning, skill, coding, deepseek harness, dsh"
---
# dsh-capability-receipt

> ⭐ 4 · ✅ 活跃 · 技能

## 一句话介绍

Content-addressed receipts for skills actually loaded by DeepSeek Harness

## 详细介绍

`dsh-capability-receipt` proves which skill DeepSeek Harness actually loaded. It hashes the effective instruction body returned by `ctx.skills.get()`, records the winning provider/source/invocation policy, and—when the resource base is local—hashes a bounded resource-directory closure. It can then compare that runtime observation with hashes pinned by a trusted source artifact and write a deterministic content-addressed receipt. This is deliberately not another skill package format, dependency r

## 作者
**[dongsheng123132](https://github.com/dongsheng123132)**

## 链接

- [GitHub 仓库](https://github.com/dongsheng123132/dsh-capability-receipt)
- [完整 README](https://github.com/dongsheng123132/dsh-capability-receipt#readme)
- [返回dsh-capability-receipt所在分类](../skills.md)
