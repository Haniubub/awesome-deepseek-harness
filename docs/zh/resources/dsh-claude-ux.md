---
title: "dsh-claude-ux"
description: "DSH plugin: Claude-style Chinese risk control & conversation autonomy for DeepSeek Harness web"
keywords: "dsh-claude-ux, search, plugin, coding, deepseek harness, dsh"
---
# dsh-claude-ux

> ⭐ 56 · ✅ 活跃 · 插件

## 一句话介绍

DSH plugin: Claude-style Chinese risk control & conversation autonomy for DeepSeek Harness web

## 详细介绍

Claude 式「区域风控 + 自主结束对话」插件 —— 适用于 DeepSeek Harness 的 web profile。 复刻 Anthropic/Claude 的两类行为，**除两个默认关闭的可选外部调用外全部本地判定**（详见 [docs/PRIVACY.md](docs/PRIVACY.md)）： - **区域风控（可反向）**：检测目标用户（时区、系统/浏览器语言、中文字体、代理、代理/中转域名黑名单、公网 IP 归属、WebRTC IP 一致性）。`regionTarget` 选 `cn` = 风控中国用户（Claude 原版行为），选 `non-cn` = **反向风控**（检测到不是中国人就风控）。命中后按惩罚阶梯处置：拒绝文案（带尝试计数）→ 达到 `refusalEndsAfter` 次数后结束会话（Chat ended 面板 + 服务端持续拒绝，重启后依然生效）→ 系统提示词注入模型级区域指令。 - **自主性**：用户持续辱骂或反复要求严重有害内容时，先警告、再主动结束对话；自伤/他伤风险消息永不触发结束（对齐 Claude 的公开限制）。辱骂结束与严重有

## 作者
**[eri64](https://github.com/eri64)**

## 链接

- [GitHub 仓库](https://github.com/eri64/dsh-claude-ux)
- [完整 README](https://github.com/eri64/dsh-claude-ux#readme)
- [返回dsh-claude-ux所在分类](../plugins.md)
