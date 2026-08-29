---
title: "dsh-agent-message"
description: "DeepSeek Harness 跨会话 Agent 通信插件｜Cross-session agent-to-agent messaging with offline delivery, receipts and session navigation for DeepSeek Harness."
keywords: "dsh-agent-message, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-agent-message

> ⭐ 6 · ✅ 活跃 · 插件

## 一句话介绍

DeepSeek Harness 跨会话 Agent 通信插件｜Cross-session agent-to-agent messaging with offline delivery, receipts and session navigation for DeepSeek Harness.

## 详细介绍

在 DeepSeek Harness 里，一个进程会同时挂着多个 Agent 会话。本插件给每个会话装上三个工具，让它们能互相"发消息"： - 发消息前，先**列出所有可发送的独立会话**（未归档、排除真实子代理，含离线未打开的），按标题找到目标； - 找到后，**把消息投递到目标会话**——普通消息统一进入独立的新 turn；目标离线（进程重启后还没打开）时，插件通过 Harness 公开接口恢复会话、投递，并保持加载供后续通信，插件卸载时再释放 handle； - 需要时，可以**按需查询**某条消息的送达状态（排队中/已认领/被丢弃/未知），并单独查看目标是否正在运行，供监督场景使用。 典型场景：编排者 Agent 给开发 Agent 派活、两个 Agent 协作接力、主会话给测试会话发指令、监督者 Agent 盯梢多个 worker。

## 作者
**[GengDaPeng](https://github.com/GengDaPeng)**

## 链接

- [GitHub 仓库](https://github.com/GengDaPeng/dsh-agent-message)
- [完整 README](https://github.com/GengDaPeng/dsh-agent-message#readme)
- [返回dsh-agent-message所在分类](../plugins.md)
