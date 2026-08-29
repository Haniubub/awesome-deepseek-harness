---
title: "dsh-toy"
description: "Toy Control Protocol for DSH"
keywords: "dsh-toy, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-toy

> ⭐ 64 · ✅ 活跃 · 插件

## 一句话介绍

Toy Control Protocol for DSH

## 详细介绍

`dsh-toy` is a DeepSeek Harness plugin for connecting small toys to DSH. At connection time, the agent first asks for the brand and model, then selects the connection method automatically. If the user genuinely does not know, the agent starts unknown-hardware discovery: - On macOS, unknown hardware first uses read-only raw **CoreBluetooth** advertisement discovery, without starting Intiface or connecting to devices. - Regular Bluetooth, serial, and USB models use **Buttplug / Intiface**. The plu

## 作者
**[c3ll256](https://github.com/c3ll256)**

## 链接

- [GitHub 仓库](https://github.com/c3ll256/dsh-toy)
- [完整 README](https://github.com/c3ll256/dsh-toy#readme)
- [返回dsh-toy所在分类](../plugins.md)
