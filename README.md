# 跨 IDE Vibe Coding 治理体系

这是一个给人和 AI 一起用的治理仓库。

它现在已经落地了三件核心事:

1. 用 `Python CLI` 做确定性生成, 不靠大模型“翻译规则”.
2. 用 `.agents/` 固化项目状态、规则、经验和版本上下文.
3. 用 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`.cursor/`、`.github/`、`.opencode/` 把同一套治理规则分发给不同 IDE 和 agent.

如果你把这个仓库发给一个新同事、一个新账号、一个新的 AI 实例, 对方不需要任何聊天记录, 只要打开项目目录, 就能从本地文件把项目完整接起来。

## 这个项目能做什么

- 初始化一个带 `.agents/` 治理骨架的新项目.
- 根据本地配置生成 IDE 适配文件.
- 检查配置、override、生成结果有没有漂移.
- 比较当前项目和上游规则目录有没有差异.
- 把项目经验写进 `PROGRESS` 体系, 方便回溯和升级.

## 先看什么

- 5 分钟上手: [QUICKSTART.md](./QUICKSTART.md)
- 完整使用流程: [USAGE_GUIDE.md](./USAGE_GUIDE.md)
- 架构为什么这样设计: [ARCHITECTURE.md](./ARCHITECTURE.md)
- 目录每个文件是干什么的: [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
- 代码从哪里改起: [CODE_WALKTHROUGH.md](./CODE_WALKTHROUGH.md)
- 治理和同步规则: [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
- 如何参与后续迭代: [CONTRIBUTING.md](./CONTRIBUTING.md)
- 版本和历史: [CHANGELOG.md](./CHANGELOG.md)
- 换账号/换 AI/换设备怎么接手: [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)
- 嵌入式项目怎么接入: [EMBEDDED_GUIDE.md](./EMBEDDED_GUIDE.md)

## 环境要求

- Python 3.11 或更高版本
- `pip`
- `git`
- 一个能打开本地仓库的 IDE, 例如 VS Code、Cursor, 或者支持读取根目录说明文件的其他 AI IDE

当前仓库已经自举完成, 所以你现在不需要再手动创建 `.agents/` 结构, 直接校验和阅读即可。

## 极速上手

在项目根目录运行:

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

这三步的含义很简单:

1. `validate`: 看配置和生成结果是不是健康.
2. `render`: 按当前 `.agents/` 真源重新生成 IDE 适配层.
3. `sync --dry-run`: 看当前工作区和上游规则快照有没有差异, 先看报告, 不直接改.

## 新账号 / 新 AI 快速接手入口

如果你是第一次接这个仓库, 按这个顺序看:

1. 先看本文件, 了解项目定位和入口.
2. 再看 [QUICKSTART.md](./QUICKSTART.md), 把环境跑通.
3. 再看 [ARCHITECTURE.md](./ARCHITECTURE.md) 和 [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md), 搞清楚项目是怎么分层的.
4. 再看 [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md) 和 [CHANGELOG.md](./CHANGELOG.md), 了解规则边界和版本演进.
5. 然后打开这些本地真源文件:
   - [`.agents/profile.yaml`](./.agents/profile.yaml)
   - [`.agents/RULES.md`](./.agents/RULES.md)
   - [`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)
   - [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
6. 最后再看给 AI 用的适配文件:
   - [`AGENTS.md`](./AGENTS.md)
   - [`CLAUDE.md`](./CLAUDE.md)
   - [`GEMINI.md`](./GEMINI.md)

做到这一步, 新账号和新 AI 就已经能无缝接管当前项目。

## 这套体系最重要的原则

- 所有关键状态都落在本地文件里, 不依赖任何云端聊天记忆.
- 生成文件不直接改, 要改就回到 `.agents/` 或 `vibe_governance/resources/`.
- 经验先写 `PROGRESS`, 再决定要不要升级成版本变更或上游规则.
- 当前仓库既是“治理工具仓”, 也是“治理体系自举示例仓”.

## 下一步看哪里

- 想马上开始操作: [QUICKSTART.md](./QUICKSTART.md)
- 想按生命周期做事: [USAGE_GUIDE.md](./USAGE_GUIDE.md)
- 想改代码或扩展功能: [CODE_WALKTHROUGH.md](./CODE_WALKTHROUGH.md)
