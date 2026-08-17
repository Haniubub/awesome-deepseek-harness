---
title: "dsh_workflow"
description: "把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层"
keywords: "dsh_workflow, workflow, coding, multi-agent, deepseek harness, dsh"
---
# dsh_workflow

> ⭐ 72 · ✅ active · workflow

## One-liner

把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层

## About

DSH 已经有很强的 Harness 基础设施：模型路由、子 Agent provider、工具权限、审批、Session 日志、后台 jobs 与 UI 事件。但仅有这些“执行原语”，团队仍需在每次会话里重新描述如何拆解、并发、验证和汇总。 对 DSH 项目本身，这个插件的价值是把已有 Harness 能力串成完整闭环： flowchart LR A["DSH providers / models"] --> W["DSH Workflow"] B["tool filters / approval"] --> W C["Session / jobs / commands"] --> W W --> D["reusable capsules"] W --> E["durable run graph"] W --> F["resume / governance / evidence"] 因此，DSH 不只会“调用 Agent”，还可以承载长期维护的 Agent 工作流库。

## Author
**[omdsh-dev](https://github.com/omdsh-dev)**

## Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh_workflow)
- [Full README](https://github.com/omdsh-dev/dsh_workflow#readme)
- [Back to the Workflows & Automation list](../workflows.md)
