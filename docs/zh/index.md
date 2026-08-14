# Awesome DeepSeek Harness 🐋

> 官方 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 生态精选：
> **插件 · 技能 · 工作流 · 智能体 · 客户端 · 工具 · 示例 · 教程**。

DeepSeek Harness（`dsh`）是 DeepSeek AI 开源的智能体 Harness，围绕一个简单理念构建：

> **一切皆插件（Everything is a Plugin）。**

本站收录围绕官方 `deepseek-ai/deepseek-harness` 项目的完整生态。

## 快速开始

```bash
# 运行 DSH
npx @deepseek-ai/dsh web        # Web UI 位于 http://127.0.0.1:3080

# 安装插件
dsh plugin --profile web add <package>
```

插件的官方发现约定是 GitHub 主题标签：[`dsh-plugin`](https://github.com/topics/dsh-plugin)。

> ⚠️ DeepSeek Harness 处于开发者预览阶段，迭代极快，兼容性可能随时变化——安装前请先查看对应仓库。

## 🔥 全网 Top 20

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | ⭐80,001 | 字节跳动开源的长时间跨度 SuperAgent harness：技能、记忆、沙箱、子代理、工具与消息网关。 | ✅ 活跃 |
| 2 | [petdex](https://github.com/crafter-station/petdex) | ⭐3,777 | A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. | ✅ 活跃 |
| 3 | [Cordis](https://github.com/cordiverse/cordis) | ⭐3,182 | 时空可组合性元框架——DeepSeek Harness 底层的插件运行时。 | ✅ 活跃 |
| 4 | [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) | ⭐2,324 | 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） | ✅ 活跃 |
| 5 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | ⭐1,697 | DSH Web 大型插件与皮肤集合：任务看板、Git 图、侧栏、远程/移动 UI、宠物、Token 统计与主题。 | ✅ 活跃 |
| 6 | [modlens](https://github.com/liustack/modlens) | ⭐1,158 | DSH 首个视觉插件，也是所有纯文本编码 Agent 的视觉桥梁：粘贴图片即可用。 | ✅ 活跃 |
| 7 | [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) | ⭐962 | 为 DeepSeek Harness 生态打造的现代化桌面端体验（插件）。 | ✅ 活跃 |
| 8 | [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | ⭐793 | Claude Code 风格全屏交互终端插件：像素鲸鱼顶栏、实时状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。 | ✅ 活跃 |
| 9 | [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) | ⭐758 | 面向编码的 MCP 工具集：让任何 AI Agent 获得编码能力。 | ✅ 活跃 |
| 10 | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | ⭐751 | 大型 DSH 插件精选目录（双语）。 | ✅ 活跃 |
| 11 | [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) | ⭐751 | 雷达索引仓库：自动扫描发现的所有 dsh 插件候选，带证据驱动的兼容性矩阵。 | ✅ 活跃 |
| 12 | [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | ⭐684 | 工作台式侧边栏：文件渲染/编辑、终端、Git、子代理，支持三方扩展 Tab。 | ✅ 活跃 |
| 13 | [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | ⭐573 | 开源 CMA 兼容的任意模型 Agent 运行时：MCP 工具、沙箱会话、审计与回放。 | ✅ 活跃 |
| 14 | [museai](https://github.com/yejiming/MuseAI) | ⭐538 | 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用） | ✅ 活跃 |
| 15 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | ⭐506 | DSH Web 鲸鱼娘皮肤系列（CC BY-NC-SA 4.0）。 | ✅ 活跃 |
| 16 | [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) | ⭐465 | 《DeepSeek Harness 橙皮书》：完整系统提示词、129 行启动清单、三份原始会话日志——官方文档没有的一手实测。PDF/EPUB/HTML 免费下载。 | ✅ 活跃 |
| 17 | [mnemon](https://github.com/mnemon-dev/mnemon) | ⭐430 | LLM 监督的 Agent 持久记忆：图召回与跨会话知识，单二进制。 | ✅ 活跃 |
| 18 | [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) | ⭐360 | DSH 生态目录：来自 dsh-external/hub 与公开 dsh-plugin 主题的插件、工具与基础设施精选。 | ✅ 活跃 |
| 19 | [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) | ⭐309 | 整活插件：2005 中文站点风格广告层，侧栏广告/对话内信息流/角落弹窗。 | ✅ 活跃 |
| 20 | [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) | ⭐302 | 让纯文本模型更好的视觉工具箱：带意图图片问答、长截图 OCR、UI 还原、grounding、像素 diff。 | ✅ 活跃 |

## 浏览生态

- [插件](plugins.md) — 发现、记忆、搜索、开发者工具、界面、视觉、娱乐
- [技能](skills.md) — 可复用的智能体流程与知识
- [工作流与自动化](workflows.md) — 深度研究、计划→执行、自动化
- [智能体与多智能体](agents.md) — 团队、跨会话、子代理、桥接
- [客户端（桌面与终端）](clients.md) — 桌面应用、终端客户端、移动端
- [MCP 与集成](integrations.md) — MCP 服务器、IDE、浏览器、渠道、ACP
- [示例与模板](examples.md) — 几分钟即可运行的模板
- [教程与学习](tutorials.md) — 书籍、手册与课程
- [精选列表与注册表](awesome-lists.md) — 目录与索引
- [相关 Agent Harness](related.md) — 更广泛的 Harness 生态

## 项目说明

- 源仓库：[awesome-deepSeek-harness](https://github.com/awesome-deepSeek-harness)
- 数据注册表：`data/*.json`（机器可读，CI 校验）
- [English](/index.html)
