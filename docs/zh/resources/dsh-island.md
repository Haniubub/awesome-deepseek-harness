---
title: "dsh-island"
description: "通过 Unix socket 把 DSH agent 的会话、工具调用与审批实时桥接到 CodeIsland macOS 刘海面板，可直接在面板上批准/拒绝。"
keywords: "dsh-island, notifications, plugin, deepseek harness, dsh"
---
# dsh-island

> ⭐ 5 · ✅ 活跃 · 插件

## 一句话介绍

通过 Unix socket 把 DSH agent 的会话、工具调用与审批实时桥接到 CodeIsland macOS 刘海面板，可直接在面板上批准/拒绝。

## 详细介绍

开发 AI agent 时，最常见的烦恼是「切窗口看它到底在干嘛、是不是卡在审批」。**dsh-island 把 DSH 的实时状态带进 macOS 菜单栏**： - 插件 apply 时**自动拉起原生 Swift 面板**（`bin/dsh-island-panel`，NSStatusItem + NSPopover + SwiftUI，借鉴 [CodeIsland](https://github.com/wxtsky/CodeIsland) 的实现） - 菜单栏按钮文案**随状态动态变化**：`🐋 DSH`（空闲）→ `🔧 运行中 / 🔧 <工具>`（执行中）→ `🛡️ 需要授权`（审批中） - 点击菜单栏图标 → 弹出毛玻璃灵动岛面板：会话、工具调用、事件流 - 审批请求直接在面板上点「允许 / 拒绝」，决策回写 DSH DSH 进程 └─ dsh-island 插件（cordis） ├─ apply() 时 spawn → bin/dsh-island-panel（Swift 原生，常驻菜单栏） ├─ 监听 DSH 事件（session/tools/approval/suba

## 作者
**[cdxiaodong](https://github.com/cdxiaodong)**

## 链接

- [GitHub 仓库](https://github.com/cdxiaodong/dsh-island)
- [完整 README](https://github.com/cdxiaodong/dsh-island#readme)
- [返回dsh-island所在分类](../plugins.md)
