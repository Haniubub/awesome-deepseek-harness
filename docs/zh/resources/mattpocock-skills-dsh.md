---
title: "mattpocock-skills-dsh"
description: "Matt Pocock 完整发布技能集（25 个 SKILL.md：grilling、writing-for-agents、wait-what、TDD、code-review、wayfinder、ask-matt 路由等）的 DSH 移植。"
keywords: "mattpocock-skills-dsh, coding, skill, deepseek harness, dsh"
---
# mattpocock-skills-dsh

> ⭐ 1 · ✅ 活跃 · 技能

## 一句话介绍

Matt Pocock 完整发布技能集（25 个 SKILL.md：grilling、writing-for-agents、wait-what、TDD、code-review、wayfinder、ask-matt 路由等）的 DSH 移植。

## 详细介绍

<div align="center"> [English](README.en.md) | **简体中文** </div> 为 **DeepSeek Harness (DSH)** 打造的 Matt Pocock 技能插件包:把 [mattpocock/skills](https://github.com/mattpocock/skills)(来自 [aihero.dev/skills](https://www.aihero.dev/skills) 的"真实工程师"技能集) 移植到 DSH 的 Cordis 插件架构上。 插件会向 `ctx.skills` 注册表的 **host 层** 注册一个技能提供者,因此每个 agent preset 的作用域链都会合并这些技能。技能正文随包分发 (`skills/<name>/SKILL.md`),通过 `import.meta.url` 定位——这是包的 组装事实,不需要任何用户配置。

## 作者
**[gongyijie85](https://github.com/gongyijie85)**

## 链接

- [GitHub 仓库](https://github.com/gongyijie85/mattpocock-skills-dsh)
- [完整 README](https://github.com/gongyijie85/mattpocock-skills-dsh#readme)
- [返回mattpocock-skills-dsh所在分类](../skills.md)
