---
title: "dsh-slack"
description: "DeepSeek Harness Slack 插件：slack_notify/channels/inbox/reply 四工具，Socket Mode 免公网回调收消息，收件箱队列 + 线程回复，支持自定义 slackApiUrl 对接代理网关；内置假 Slack 服务器做协议级验收测试。· Two-way Slack messaging for DeepSeek Harness agents."
keywords: "dsh-slack, channel, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-slack

> ⭐ 4 · ✅ active · integration

## One-liner

DeepSeek Harness Slack 插件：slack_notify/channels/inbox/reply 四工具，Socket Mode 免公网回调收消息，收件箱队列 + 线程回复，支持自定义 slackApiUrl 对接代理网关；内置假 Slack 服务器做协议级验收测试。· Two-way Slack messaging for DeepSeek Harness agents.

## About

- `slack_notify`：向指定频道（或线程）发送一条 Markdown 文本消息，返回消息 `ts`。 - `slack_channels`：列出机器人当前可见的频道（`conversations.list`，自动沿 `next_cursor` 翻页拉全）。 - `slack_inbox`：读取通过 Socket Mode 收到的消息（内存队列，最多保留 200 条；自动去重，`markRead=true` 原子消费）。 - `slack_reply`：以线程回复形式回复某条收件箱消息（`chat.postMessage` 带 `thread_ts`）。 - WebClient 按 `token + slackApiUrl` 缓存复用，配置变更时自动重建。 - 配置走 `cordis.patch.yml`，令牌支持环境变量回退（`DSH_SLACK_TOKEN` / `DSH_SLACK_APP_TOKEN`）。

## Author
**[STARDUSTLC666](https://github.com/STARDUSTLC666)**

## Links

- [GitHub Repository](https://github.com/STARDUSTLC666/dsh-slack)
- [Full README](https://github.com/STARDUSTLC666/dsh-slack#readme)
- [Back to the MCP & Integrations list](../integrations.md)
