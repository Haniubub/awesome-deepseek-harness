---
title: "dsh-vision"
description: "Near-native image understanding for DeepSeek Harness"
keywords: "dsh-vision, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-vision

> ⭐ 88 · ✅ active · plugin

## One-liner

Near-native image understanding for DeepSeek Harness

## About

给纯文本的 DeepSeek 加上眼睛。Vision for text-only DeepSeek. deepseek-v4 看不了图。本插件注册一个 `view_image` 工具：模型带着问题调用它（OCR、数数、读图表、看 UI 布局……任意视觉问题），插件把图片和问题转发给任意 **OpenAI 兼容的 VLM 端点**，答案以文本返回。装上之后，dsh 的所有入口（web、TUI、远程通道）同时获得视觉。 用户: 看下 ~/Desktop/error.png 是什么报错 模型 → view_image(source="/Users/me/Desktop/error.png", question="这个报错的完整文本是什么？") ← "TypeError: Cannot read properties of undefined (reading 'map') at …" 模型: 这是一个 … 建议 …

## Author
**[oil-oil](https://github.com/oil-oil)**

## Links

- [GitHub Repository](https://github.com/oil-oil/dsh-vision)
- [Full README](https://github.com/oil-oil/dsh-vision#readme)
- [Back to the Plugins list](../plugins.md)
