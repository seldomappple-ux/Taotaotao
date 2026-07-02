# 跨 IDE Vibe Coding 本地项目启动器

这个仓库现在的准确定位是:

- `Taotaotao` 是本机常驻的治理工具仓
- 新的业务项目在新的 IDE 里创建
- 新的 IDE 通过 `vibe-governance bootstrap` 调用 `Taotaotao`
- 新项目里的 AI 先读本地 `START_HERE.md`

也就是说, 日常业务开发时你主要工作在“新项目目录”里, 不是一直工作在这个治理仓里。

**当前版本**: `v1.3.2`

## 先看这 6 个根目录文件

如果你第一次打开这个仓库, 只按这个顺序读:

1. [README.md](./README.md)
2. [QUICKSTART.md](./QUICKSTART.md)
3. [ARCHITECTURE.md](./ARCHITECTURE.md)
4. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
5. [CHANGELOG.md](./CHANGELOG.md)
6. [TEMPLATES.md](./TEMPLATES.md)

根目录只保留这 6 个给人看的入口文件。更深的说明已经下沉到 [`docs/`](./docs/)。

## v1.3.2 主线能力

- **统一版本号策略**: 工具版本与项目版本保持一致，版本号只能递增
- **增量决议机制**: 通过 `DELTA_DECISIONS.md` 管理修复后的增量变化
- **下一轮迭代索引**: 通过 `NEXT_ITERATION_BASELINE.md` 明确下一轮必读文件
- **判定决策树**: L0/L1/L2 分级规则，明确何时回写上游真源
- **Git 提交模板**: 自动配置提交信息格式，规范版本号管理
- **模板库主线化**: 将轻量模板库与最小多 agent 入口层纳入当前主线承接路径

## 这个仓库现在已经能做什么

- 初始化 `.agents/` 治理骨架
- 在新项目空目录里通过 `bootstrap` 生成 `START_HERE.md`、项目类型目录和本地 skills
- 根据本地真源生成多 IDE 适配文件
- 校验配置、override、progress 和受管输出
- 比较当前规则目录和上游快照
- 把项目经验沉淀进 `PROGRESS` 体系
- 管理增量决议与迭代基线

## 当前最重要的命令

```bash
vibe-governance bootstrap --type embedded --target .
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance smoke --target .
python -m vibe_governance sync --target . --dry-run --json
```

它们分别代表:

1. 在一个新的空项目目录里落治理和项目类型骨架
2. 现在这个仓库是不是健康的
3. 受管输出能不能被正确重建
4. 跑一次当前仓库和新生成项目的最短端到端检查
5. 本地规则和上游快照有没有差异

`bootstrap` 是给新项目的推荐入口。`init` 仍保留为底层兼容入口, 主要用于已有迁移流程或只需要 `.agents` 骨架的场景。

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

如果你现在要承接当前 `1.3.2` 主线治理上下文, 建议按这个顺序看:

1. [docs/upgrades/v1.3.2-summary.md](./docs/upgrades/v1.3.2-summary.md)
2. [docs/upgrades/v1.3.2-plan.md](./docs/upgrades/v1.3.2-plan.md)
3. [docs/DELTA_DECISIONS.md](./docs/DELTA_DECISIONS.md)
4. [docs/NEXT_ITERATION_BASELINE.md](./docs/NEXT_ITERATION_BASELINE.md)
5. [CHANGELOG.md](./CHANGELOG.md)

## 最后只记住一句话

这个仓库不是靠聊天记忆接力, 而是靠本地文件接力:

- 根目录 6 个入口文件负责讲清楚
- `.agents/` 负责保存事实
- `vibe_governance/` 负责驱动生成
- `templates/` 负责沉淀可复用项目模板
- `AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 等适配文件只负责给 IDE / agent 读取
