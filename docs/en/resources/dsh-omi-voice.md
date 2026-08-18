---
title: "dsh-omi-voice"
description: "Immersive voice reading plugin: in-chat read/pause/resume with Doubao TTS natural voices (BYOK), reads only the final answer, filters code/tables/graphics."
keywords: "dsh-omi-voice, ui, plugin, multimodal, deepseek harness, dsh"
---
# dsh-omi-voice

> ⭐ 2 · ✅ active · plugin

## One-liner

Immersive voice reading plugin: in-chat read/pause/resume with Doubao TTS natural voices (BYOK), reads only the final answer, filters code/tables/graphics.

## About

1. 安装插件 + 构建并打开 Omi 引擎（见下方「获取豆包 API Key」与「安装」）。 2. 在 Omi 引擎设置页保存一次豆包 API Key。 3. 在 DSH 对话里点 AI 回复旁的 🔊，即可朗读。 flowchart LR A[点 🔊] --> B[插件取回复的最终回答文本] B --> C[POST 127.0.0.1:8765/v1/speak] C --> D[Omi 引擎清洗 + 分段] D --> E[豆包 TTS 流式合成] E --> F[本机扬声器播放]

## Author
**[PolinniZhong](https://github.com/PolinniZhong)**

## Links

- [GitHub Repository](https://github.com/PolinniZhong/dsh-omi-voice)
- [Full README](https://github.com/PolinniZhong/dsh-omi-voice#readme)
- [Back to the Plugins list](../plugins.md)
