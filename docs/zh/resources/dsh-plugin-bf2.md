---
title: "dsh-plugin"
description: "OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend."
keywords: "dsh-plugin, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin

> ⭐ 14 · ✅ 活跃 · 插件

## 一句话介绍

OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend.

## 详细介绍

`@loongsuite/dsh-plugin` is a standalone, open-source observability plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). It observes DSH's native session, agent loop, LLM stream, and tool lifecycle, converts them into OpenTelemetry GenAI traces and metrics, and exports standard OTLP/HTTP protobuf to any compatible backend. LoongSuite is an open-source observability collection ecosystem built on OpenTelemetry. This repository is its native DSH integration. The p

## 作者
**[loongsuite](https://github.com/loongsuite)**

## 链接

- [GitHub 仓库](https://github.com/loongsuite/dsh-plugin)
- [完整 README](https://github.com/loongsuite/dsh-plugin#readme)
- [返回dsh-plugin所在分类](../plugins.md)
