---
title: "dsh-vision-tools"
description: "Full vision-capability bundle for DeepSeek Harness: a vision_understand tool (OpenAI-compatible vision APIs, free Zhipu GLM-4V-Flash by default) plus paste/drag-and-drop/button entry points for image recognition."
keywords: "dsh-vision-tools, vision, plugin, multimodal, deepseek harness, dsh"
---
# dsh-vision-tools

> ⭐ 3 · ✅ active · plugin

## One-liner

Full vision-capability bundle for DeepSeek Harness: a vision_understand tool (OpenAI-compatible vision APIs, free Zhipu GLM-4V-Flash by default) plus paste/drag-and-drop/button entry points for image recognition.

## About

DeepSeek Harness（DSH）视觉能力全家桶 —— 让 DeepSeek 纯文本模型"看得见"。 - **vision_understand 工具**：调用 OpenAI 兼容视觉大模型 API 理解本地图片（描述画面、识别文字、回答问题），注册为全局工具，所有会话可用。 - **三入口识图**：`Cmd/Ctrl+V` 粘贴截图、拖图到按钮、点按钮选文件 → 图片自动落盘到 `$DSH_HOME/pasted-images/` → 输入框填入 `请识别这张图片：<路径>` → 发送后模型自动调用识图工具。 默认使用**智谱 GLM-4.6V-Flash（免费）**，支持 4 家 provider 切换。被限流时**自动降级到 GLM-4V（glm-4v-flash）**重试，免费模型高峰期也不容易失败。

## Author
**[moon09300731](https://github.com/moon09300731)**

## Links

- [GitHub Repository](https://github.com/moon09300731/dsh-vision-tools)
- [Full README](https://github.com/moon09300731/dsh-vision-tools#readme)
- [Back to the Plugins list](../plugins.md)
