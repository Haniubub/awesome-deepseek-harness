---
title: "dsh-task-status"
description: "DSH 插件：后台任务状态条（对话页任务进度 + 实时输出 tail）。官方 bundle 插件，dsh plugin --profile web add 安装"
keywords: "dsh-task-status, learning, skill, coding, deepseek harness, dsh"
---
# dsh-task-status

> ⭐ 9 · ✅ 活跃 · 技能

## 一句话介绍

DSH 插件：后台任务状态条（对话页任务进度 + 实时输出 tail）。官方 bundle 插件，dsh plugin --profile web add 安装

## 详细介绍

**UI** (chat-page dock slot): **Routes** (Node half): **Output tail contention semantics** (official 0809 API constraint): `tasks.read` is a consumptive, incremental read (one shared cursor per task). This plugin applies a **mirror patch** to `ctx.tasks.read` — the official read becomes buffered mirror (increments already read by others, not re-consumed) + direct read of the latest (normal consumption); the plugin's own reads go straight to the underlying rawRead. The official tool and the plugi

## 作者
**[vlln](https://github.com/vlln)**

## 链接

- [GitHub 仓库](https://github.com/vlln/dsh-task-status)
- [完整 README](https://github.com/vlln/dsh-task-status#readme)
- [返回dsh-task-status所在分类](../skills.md)
