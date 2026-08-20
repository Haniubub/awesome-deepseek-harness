---
title: "deepseek-harness-desktop"
description: "Unofficial in-process desktop app for DeepSeek Harness: the host composition boots inside the Electron main process with zero ports and an IPC bridge. Not affiliated with DeepSeek."
keywords: "deepseek-harness-desktop, desktop, client, coding, deepseek harness, dsh"
---
# deepseek-harness-desktop

> ⭐ 3 · ✅ 活跃 · 客户端

## 一句话介绍

Unofficial in-process desktop app for DeepSeek Harness: the host composition boots inside the Electron main process with zero ports and an IPC bridge. Not affiliated with DeepSeek.

## 详细介绍

多数社区桌面版是**拉起 `dsh web` 子进程**、再把浏览器窗口指到 `127.0.0.1:3080`。本项目的做法不同：整份官方组合**跑在 Electron 主进程内部**（进程内集成），前端从本地加载，全部 `/api` 请求与事件走 **IPC 桥**——**零端口、零子进程、无本地 HTTP 服务**。会话、目标、后台任务、插件都是应用内的一等状态：关掉窗口（驻留托盘）它们照常运行。

## 作者
**[Easyhoov](https://github.com/Easyhoov)**

## 链接

- [GitHub 仓库](https://github.com/Easyhoov/deepseek-harness-desktop-windows)
- [完整 README](https://github.com/Easyhoov/deepseek-harness-desktop-windows#readme)
- [返回deepseek-harness-desktop所在分类](../clients.md)
