---
title: "dsh-vision-tools"
description: "DeepSeek Harness 视觉能力全家桶：vision_understand 工具（OpenAI 兼容视觉 API，默认免费智谱 GLM-4V-Flash）+ 粘贴/拖拽/按钮三入口识图。"
keywords: "dsh-vision-tools, vision, plugin, multimodal, deepseek harness, dsh"
---
# dsh-vision-tools

> ⭐ 3 · ✅ 活跃 · 插件

## 一句话介绍

DeepSeek Harness 视觉能力全家桶：vision_understand 工具（OpenAI 兼容视觉 API，默认免费智谱 GLM-4V-Flash）+ 粘贴/拖拽/按钮三入口识图。

## 详细介绍

DeepSeek Harness（DSH）视觉能力全家桶 —— 让 DeepSeek 纯文本模型"看得见"。 - **vision_understand 工具**：调用 OpenAI 兼容视觉大模型 API 理解本地图片（描述画面、识别文字、回答问题），注册为全局工具，所有会话可用。 - **三入口识图**：`Cmd/Ctrl+V` 粘贴截图、拖图到按钮、点按钮选文件 → 图片自动落盘到 `$DSH_HOME/pasted-images/` → 输入框填入 `请识别这张图片：<路径>` → 发送后模型自动调用识图工具。 默认使用**智谱 GLM-4.6V-Flash（免费）**，支持 4 家 provider 切换。被限流时**自动降级到 GLM-4V（glm-4v-flash）**重试，免费模型高峰期也不容易失败。

## 作者
**[moon09300731](https://github.com/moon09300731)**

## 链接

- [GitHub 仓库](https://github.com/moon09300731/dsh-vision-tools)
- [完整 README](https://github.com/moon09300731/dsh-vision-tools#readme)
- [返回dsh-vision-tools所在分类](../plugins.md)
