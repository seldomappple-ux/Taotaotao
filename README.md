# 跨 IDE Vibe Coding 本地项目启动器

这个仓库现在的正确定位是：

- `Taotaotao` 是本机常驻的治理工具仓
- 新的业务项目在新的 IDE 里创建
- 新的 IDE 通过命令调用 `Taotaotao`
- 新项目里的 AI 先读本地 `START_HERE.md`

也就是说，日常开发时你主要工作在“新项目目录”里，不是一直工作在这个治理仓里。

<<<<<<< HEAD
**当前版本**: `v1.3.2`

## 先看这 6 个根目录文件
=======
## 最推荐的真实使用方式
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a

### 第一次，只做一次安装

先在 `Taotaotao` 根目录执行：

```bash
cd "d:\code\VS Code\Taotaotao"
python -m pip install -e .
```

这样以后任何新的 IDE、新的终端里，都能直接调用：

```bash
vibe-governance
```

### 每次新开一个项目时

1. 在新的 IDE 里新建一个空项目目录并打开它。
2. 在那个新 IDE 的终端里运行：

```bash
vibe-governance bootstrap --type embedded --target .
```

3. 然后对那个新 IDE 里的 AI 说：

```text
请先阅读 START_HERE.md，然后严格按里面的本地读取顺序读取文件，再开始工作。先不要修改任何文件，先输出：
1. 项目定位
2. 当前规则和红线
3. 当前版本和最近进展
4. 如果继续开发，应该改哪一层
5. 我现在最适合做的下一步
```

这才是当前版本最推荐、也最符合你原始设想的用法。

## 给新 IDE 里的 AI 的固定提示词

如果你不想每次自己组织话术，直接把根目录的 [`AI_QUICKSTART.md`](./AI_QUICKSTART.md) 整段复制给新 IDE 里的 AI。

它的作用不是替代 `QUICKSTART.md`，而是把“AI 应该如何调用 Taotaotao、何时 bootstrap、何时读取本地 `START_HERE.md`”固定成一段可复用提示词。

## 这套流程为什么这样设计

原因很简单：

- `Taotaotao` 负责保存规则、模板、项目类型、生成逻辑
- 新项目负责保存自己的本地事实、规则和代码
- AI 在新项目里工作时，应该先被“当前项目本地文件”约束住
- 如果 AI 需要理解启动器本身，再回看本机 `Taotaotao` 的根目录文档

## 当前最重要的命令

日常最重要的是这 4 条：

```bash
vibe-governance bootstrap --type embedded --target .
vibe-governance validate --target .
vibe-governance render --target .
vibe-governance smoke
```

含义分别是：

- `bootstrap`: 在当前新项目目录里直接落骨架
- `validate`: 校验当前项目是否合法
- `render`: 根据真源重建受管文件
- `smoke`: 在治理仓里跑一次一键冒烟测试

## 当前支持的项目类型

- `governance`
- `software`
- `backend`
- `frontend`
- `embedded`

## 先读哪几个文件

第一次接手这个治理仓时，先按这个顺序读：

1. [README.md](./README.md)
2. [QUICKSTART.md](./QUICKSTART.md)
3. [ARCHITECTURE.md](./ARCHITECTURE.md)
4. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
5. [CHANGELOG.md](./CHANGELOG.md)
6. [TEMPLATES.md](./TEMPLATES.md)

<<<<<<< HEAD
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
- 根据本地真源生成多 IDE 适配文件
- 校验配置、override、progress 和受管输出
- 比较当前规则目录和上游快照
- 把项目经验沉淀进 `PROGRESS` 体系
- 管理增量决议与迭代基线

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
=======
更深的资料在 [`docs/`](./docs/)。
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a
