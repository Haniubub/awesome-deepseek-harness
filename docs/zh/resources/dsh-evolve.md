---
title: "dsh-evolve"
description: "自进化插件：agent 在 session 内随对话给自己长出/剪掉能力 —— evolve_add 热挂载持久化 cordis 插件（下一 step 工具即可见），evolve_remove 可逆卸载，重启自动恢复"
keywords: "dsh-evolve, developer, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-evolve

> ⭐ 12 · ✅ 活跃 · 插件

## 一句话介绍

自进化插件：agent 在 session 内随对话给自己长出/剪掉能力 —— evolve_add 热挂载持久化 cordis 插件（下一 step 工具即可见），evolve_remove 可逆卸载，重启自动恢复

## 详细介绍

自进化 harness 插件：**agent 在 session 内随对话给自己长出/剪掉能力**。用户的表述暴露出一个缺口（反复要查的表、天天要算的换算、老要看的端点），agent 现场写一个 cordis 插件挂载给自己——新工具在**下一个 step**就可调用；不再需要时可逆卸载；重启自动恢复。 进化不限于工具。evolution 是完整的 cordis 插件：常驻 system prompt 规则、`agent/step` / `agent/settled` 事件钩子、定时器主动唤醒 agent——**改行为、而不只是加能力**的进化，同样一次 `evolve_add` 完成（[三条非工具实录](#不止工具改行为的进化)）。 依据的机制：dsh 的工具列表每个 step 都从当前挂载的插件实时重算（无 session 级快照），cordis 4 的 fiber 具有可回滚 effect——挂载即生效，dispose 即净。

## 作者
**[william-jin-cmu](https://github.com/william-jin-cmu)**

## 链接

- [GitHub 仓库](https://github.com/william-jin-cmu/dsh-evolve)
- [完整 README](https://github.com/william-jin-cmu/dsh-evolve#readme)
- [返回dsh-evolve所在分类](../plugins.md)
