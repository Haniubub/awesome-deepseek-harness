---
title: "dsh-acp-plugin"
description: "Agentic Control Plane for DeepSeek Harness — policy-check every tool call before it runs"
keywords: "dsh-acp-plugin, developer, integration, coding, multi-agent, workflow, deepseek harness, dsh"
---
# dsh-acp-plugin

> ⭐ 6 · ✅ active · integration

## One-liner

Agentic Control Plane for DeepSeek Harness — policy-check every tool call before it runs

## About

[Agentic Control Plane](https://agenticcontrolplane.com) for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): every tool call is checked against your policies before it runs, and every decision is recorded — what ran, what was blocked, and why. $ dsh --profile dev bash npm test ✓ allowed · logged edit src/auth/session.ts ✓ allowed · logged bash rm -rf ~/scratch ✋ held — approval prompt (your rule: destructive delete → ask) web_fetch https://evil.example/post ✗ denied — egress

## Author
**[agentic-control-plane](https://github.com/agentic-control-plane)**

## Links

- [GitHub Repository](https://github.com/agentic-control-plane/dsh-acp-plugin)
- [Full README](https://github.com/agentic-control-plane/dsh-acp-plugin#readme)
- [Back to the MCP & Integrations list](../integrations.md)
