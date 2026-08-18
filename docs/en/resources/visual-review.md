---
title: "visual-review"
description: "Renders pasted/uploaded images inline in the DSH Web chat and gives text-only models vision: cloud multimodal API first, local Qwen3-VL fallback."
keywords: "visual-review, vision, plugin, multimodal, deepseek harness, dsh"
---
# visual-review

> ⭐ 2 · ✅ active · plugin

## One-liner

Renders pasted/uploaded images inline in the DSH Web chat and gives text-only models vision: cloud multimodal API first, local Qwen3-VL fallback.

## About

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）Web 界面打造的**双面插件**：让聊天界面直接**显示图片**，并让模型**解读图片**。 - **图片显示**：用户粘贴 / 上传的图片（PNG / JPEG / WebP / GIF）会直接渲染在对话气泡里。 - **视觉解读**：`visual_review` 工具调用视觉多模态模型，返回图片的中文文字描述（文字、物体、人物、场景、图表等）。 - **双引擎**：云端优先（任意 OpenAI 兼容的多模态 `chat/completions` API，零本地依赖）；未配置时自动回退本机 Qwen3-VL-8B（数据不出本机）。 - **无需更换模型**：插件在发送路径上把「图片块」转换成「带附件 ID 的文本注解」，任何本身看不到图片的文本模型都能配合工作。 ---

## Author
**[wang-bool](https://github.com/wang-bool)**

## Links

- [GitHub Repository](https://github.com/wang-bool/visual-review)
- [Full README](https://github.com/wang-bool/visual-review#readme)
- [Back to the Plugins list](../plugins.md)
