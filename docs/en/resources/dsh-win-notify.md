---
title: "dsh-win-notify"
description: "DSH 插件：代理任务完成时弹出带声音的 Windows Toast 通知，点击通知即可直接切回并前台显示 DSH 标签页"
keywords: "dsh-win-notify, notifications, plugin, coding, deepseek harness, dsh"
---
# dsh-win-notify

> ⭐ 4 · ✅ active · plugin

## One-liner

DSH 插件：代理任务完成时弹出带声音的 Windows Toast 通知，点击通知即可直接切回并前台显示 DSH 标签页

## About

一个 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（dsh）插件：代理任务完成时在 Windows 上弹出**带声音的 Toast 通知**。 - 通知显示应用名 **DeepSeek** 与官方鲸鱼图标 - **顶层**代理回合完成（running → idle）时通知；子代理回合保持静默 - 通知正文显示最近一条用户提示词 - 任务出错时也会通知（可配置） - **点击通知直接切换并前台显示现有 GUI 标签** —— 不产生临时浏览器标签；仅当没有存活 GUI 时才新开标签（`?session=<id>` 深链） - 等待沙箱/权限审批时也会通知（可配置） - 代理通过 `ask_user_question` 提问等待回复时也会通知（可配置） - **聚焦感知：** GUI 页面处于前台且正显示触发事件的会话时，抑制该会话的通知 —— 你正在查看时不会被打扰 - 手动停止的任务**不算**完成 —— 不弹通知 - 仅依赖 Windows 自带的 PowerShell 5.1 —— 无额外依赖

## Author
**[MuziIsabel](https://github.com/MuziIsabel)**

## Links

- [GitHub Repository](https://github.com/MuziIsabel/dsh-win-notify)
- [Full README](https://github.com/MuziIsabel/dsh-win-notify#readme)
- [Back to the Plugins list](../plugins.md)
