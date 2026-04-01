# 跨 IDE Vibe Coding 治理体系

这个仓库现在更准确的定位是:

- 一个治理内核原型
- 一个自举示例仓

它已经能帮你把 AI 协作规则、项目事实、适配层生成和经验闭环固化到本地文件里, 但它还不是最终的一键业务脚手架产品。

## 先看这 5 个根目录文件

如果你第一次打开这个仓库, 只按这个顺序读:

1. [README.md](./README.md)
2. [QUICKSTART.md](./QUICKSTART.md)
3. [ARCHITECTURE.md](./ARCHITECTURE.md)
4. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
5. [CHANGELOG.md](./CHANGELOG.md)

根目录只保留这 5 个给人看的入口文件。更深的说明已经下沉到 [`docs/`](./docs/)。

## 这个仓库现在已经能做什么

- 初始化 `.agents/` 治理骨架
- 根据本地真源生成多 IDE 适配文件
- 校验配置、override、progress 和受管输出
- 比较当前规则目录和上游快照
- 把项目经验沉淀进 `PROGRESS` 体系

## 3 条最重要的命令

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

它们分别代表:

1. 现在这个仓库是不是健康的
2. 受管输出能不能被正确重建
3. 本地规则和上游快照有没有差异

## 如果你想继续深挖

深度资料现在都在 [`docs/`](./docs/) 里:

- [docs/SOURCE_MATERIALS.md](./docs/SOURCE_MATERIALS.md)
- [docs/UPGRADE_FEEDBACK.md](./docs/UPGRADE_FEEDBACK.md)
- [docs/UPGRADE_SUMMARY.md](./docs/UPGRADE_SUMMARY.md)
- [docs/DELTA_DECISIONS.md](./docs/DELTA_DECISIONS.md)
- [docs/NEXT_ITERATION_BASELINE.md](./docs/NEXT_ITERATION_BASELINE.md)
- [docs/USAGE_GUIDE.md](./docs/USAGE_GUIDE.md)
- [docs/GOVERNANCE_RULES.md](./docs/GOVERNANCE_RULES.md)
- [docs/CODE_WALKTHROUGH.md](./docs/CODE_WALKTHROUGH.md)
- [docs/CONTEXT_MIGRATION.md](./docs/CONTEXT_MIGRATION.md)
- [docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md)
- [docs/EMBEDDED_GUIDE.md](./docs/EMBEDDED_GUIDE.md)

## 当前迭代先看哪里

如果你现在要承接 `v1.2.0`, 建议按这个顺序看:

1. [docs/upgrades/v1.2.0-summary.md](./docs/upgrades/v1.2.0-summary.md)
2. [docs/upgrades/v1.2.0-plan.md](./docs/upgrades/v1.2.0-plan.md)
3. [docs/DELTA_DECISIONS.md](./docs/DELTA_DECISIONS.md)
4. [docs/NEXT_ITERATION_BASELINE.md](./docs/NEXT_ITERATION_BASELINE.md)

## 最后只记住一句话

这个仓库不是靠聊天记忆接力, 而是靠本地文件接力:

- 根目录 5 个入口文件负责讲清楚
- `.agents/` 负责保存事实
- `vibe_governance/` 负责驱动生成
- `AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 等适配文件只负责给 IDE / agent 读取
