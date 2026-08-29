---
title: "dsh-api-balance"
description: "安装在deepseek的插件，能够实时显示当前api的余额，30秒自动刷新一次"
keywords: "dsh-api-balance, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-api-balance

> ⭐ 8 · ✅ 活跃 · 插件

## 一句话介绍

安装在deepseek的插件，能够实时显示当前api的余额，30秒自动刷新一次

## 详细介绍

实时显示 DeepSeek API 账户余额的 DeepSeek Harness（dsh web）插件。 Real-time DeepSeek API account balance readout for the DeepSeek Harness web GUI. 在会话输入框下方的读数带（`conversation.composer.dock`）显示： API 余额 CNY 18.22 · 可用 · 14:32:05 更新 - 每 30 秒自动刷新（挂载时立即查询一次） - **刷新模式可选**：手动刷新 / 每 10 秒 / 每 30 秒 / 每 1 分钟 / 每 5 分钟 / 自定义间隔；选择「自定义…」会弹出输入窗口（范围 **5–3600 秒**，含校验与错误提示），偏好保存在浏览器 localStorage，刷新页面后仍保留 - 手动模式下点击「刷新」按钮即时刷新；自定义间隔确认后即时生效 - 刷新失败时保留上次数据并显示黄色「刷新失败」，悬停可见具体原因，下一次自动轮询自动恢复 - 余额不可用时显示红色「不可用」 - API 密钥通过 dsh 的 credentials

## 作者
**[02Muller25](https://github.com/02Muller25)**

## 链接

- [GitHub 仓库](https://github.com/02Muller25/dsh-api-balance)
- [完整 README](https://github.com/02Muller25/dsh-api-balance#readme)
- [返回dsh-api-balance所在分类](../plugins.md)
