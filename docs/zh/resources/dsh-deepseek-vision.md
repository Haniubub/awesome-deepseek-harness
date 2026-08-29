---
title: "dsh-deepseek-vision"
description: "Vision-language gateway plugin for DeepSeek Harness - paste an image, DeepSeek sees text"
keywords: "dsh-deepseek-vision, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-deepseek-vision

> ⭐ 8 · ✅ 活跃 · 插件

## 一句话介绍

Vision-language gateway plugin for DeepSeek Harness - paste an image, DeepSeek sees text

## 详细介绍

**安装：** `dsh plugin --profile web add dsh-deepseek-vision` **dsh-deepseek-vision 是给 DeepSeek Harness 的视觉语言网关插件。** 纯文本的 DeepSeek 编程模型 通过一个"网关"provider 路由获得贴图能力：目录声明支持 image 的模型（官方 `deepseek-v4-flash-vision-exp`）图片直通原生视觉端点；其余模型先由可配置的视觉模型 （默认 Qwen-VL）逐字描述成文字，再交给 DeepSeek 继续写代码。官方仓库零改动、跨机器 安装不锁官方版本。同类方案里它是**最薄的桥**：不注入 agent 工具、不经过第三方中转、 不依赖本地模型。 [English](README.en.md) | [中文](README.md)

## 作者
**[siegfly](https://github.com/siegfly)**

## 链接

- [GitHub 仓库](https://github.com/siegfly/dsh-deepseek-vision)
- [完整 README](https://github.com/siegfly/dsh-deepseek-vision#readme)
- [返回dsh-deepseek-vision所在分类](../plugins.md)
