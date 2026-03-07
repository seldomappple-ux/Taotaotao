# 跨 IDE Vibe Coding 治理体系

这个仓库不是在堆一套“神 Prompt”, 而是在把一套稳定的 AI 协作框架固化到本地文件里。

它现在已经做成了三件关键事:

1. 用 `Python CLI` 做确定性生成, 不让大模型临时“翻译规则”.
2. 用 `.agents/` 保存项目事实、规则、经验、版本上下文和同步快照.
3. 用 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`.cursor/`、`.github/`、`.opencode/` 把同一套治理逻辑发给不同 IDE 和 agent.

所以它的目标不只是“脱离某一个聊天会话”, 更是把一套通行的对话框架固定下来: 人和 AI 每次接手项目, 都按同一套顺序对齐意图、读取规则、执行变更、沉淀经验。

## 这个项目真正解决什么问题

- 新账号、新 AI、新设备接手时, 不再依赖任何云端聊天记忆.
- 不同 IDE 下的 agent 不再各写各的流程, 都从同一套本地真源出发.
- 规则、经验、版本和迁移信息不再散在聊天记录里, 而是可追溯地落在仓库里.
- 后续你要拆嵌入式版、纯软件版、前端版、后端版时, 可以基于同一个治理内核继续演化.

## 当前仓库已经落地的能力

- `init / render / validate / sync / progress` 这套治理 CLI.
- `.agents/profile.yaml` 作为项目级机器可读事实源.
- `rule-catalog.yaml + templates` 作为 canonical 规则和适配模板.
- 根目录 AI 文件、`.cursor/`、`.github/`、`.opencode/` 的确定性生成.
- `PROGRESS` 滑动窗口、override 白名单、immutable 规则拦截、同步快照校验.

## 第一次接手时怎么读

建议按这个顺序走, 不要跳:

1. [QUICKSTART.md](./QUICKSTART.md): 先把仓库校验跑通.
2. [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md): 先理解这套项目是从哪三篇原文抽出来的.
3. [ARCHITECTURE.md](./ARCHITECTURE.md): 再看为什么要拆成“解释层 + 真源层 + 生成层 + 适配层”.
4. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md): 再确认每个目录给谁读、能不能改、改错会怎样.
5. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md) 和 [CHANGELOG.md](./CHANGELOG.md): 再看边界和演进.
6. [`.agents/profile.yaml`](./.agents/profile.yaml)、[`.agents/RULES.md`](./.agents/RULES.md)、[`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)、[`.agents/PROGRESS.md`](./.agents/PROGRESS.md): 最后看本地真源和当前状态.
7. [`AGENTS.md`](./AGENTS.md)、[`CLAUDE.md`](./CLAUDE.md)、[`GEMINI.md`](./GEMINI.md): 确认不同 agent 看到的适配层结果.

## 3 分钟自检

当前仓库已经自举完成, 你不需要手动创建 `.agents/` 骨架。直接在根目录运行:

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

这三条命令分别解决:

1. `validate`: 当前配置、override、生成结果是否健康.
2. `render`: 按 `.agents/` 真源重建生成层.
3. `sync --dry-run`: 当前规则目录和上游快照是否存在 `rule_id` 级差异.

## 文档导航

- [QUICKSTART.md](./QUICKSTART.md): 5 分钟快速接手.
- [USAGE_GUIDE.md](./USAGE_GUIDE.md): 项目从初始化到迭代的完整使用手册.
- [ARCHITECTURE.md](./ARCHITECTURE.md): 核心设计为什么这样拆.
- [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md): 每个目录和核心文件的作用.
- [CODE_WALKTHROUGH.md](./CODE_WALKTHROUGH.md): 生成器代码从哪里读、从哪里改.
- [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md): 规则治理原则、优先级和冲突 SOP.
- [CONTRIBUTING.md](./CONTRIBUTING.md): 参与迭代和提交变更的标准流程.
- [CHANGELOG.md](./CHANGELOG.md): 版本级历史与基线.
- [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md): 换账号、换 AI、换设备时的迁移说明.
- [EMBEDDED_GUIDE.md](./EMBEDDED_GUIDE.md): 嵌入式项目接入时的当前做法和边界.

## 原始资料入口

这套仓库的设计不是拍脑袋来的。三篇原文已经纳入项目资料:

- [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md): 原文定位、中心思想和与当前实现的映射.
- [references/original-articles/01-caoxin-vibe-coding.html](./references/original-articles/01-caoxin-vibe-coding.html): 《关于 Vibe Coding 的思考与探索》网页快照.
- [references/original-articles/02-caoxin-project-init.html](./references/original-articles/02-caoxin-project-init.html): 《项目初始化 Prompt》网页快照.
- [references/original-articles/03-zhihu-managing-10-claude-code.html](./references/original-articles/03-zhihu-managing-10-claude-code.html): 《如何有效地给 10 个 Claude Code 打工》网页快照.

## 环境要求

- Python 3.11 或更高版本
- `pip`
- `git`
- 一个能打开本地仓库的 IDE, 例如 VS Code、Cursor, 或其他支持读取项目根目录说明文件的 AI IDE

## 最后记住一句话

这个仓库里:

- 根目录说明文档负责把事情讲清楚.
- `.agents/` 负责保存项目事实和长期记忆.
- `vibe_governance/` 负责把真源变成受管输出.
- 各 IDE 适配文件只负责接收同一套规则, 不负责重新定义流程.
