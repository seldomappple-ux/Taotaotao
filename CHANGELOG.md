# 版本更新日志

这份文件只做两件事：

1. 记录正式版本。
2. 解释当前工作区相对最近版本的关键变化。

更细的上下文不写在这里，而是在：

- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- `.agents/progress/entries/`

## 当前工作区相对 `0.1.0` 的关键变化

<<<<<<< HEAD
每次正式发版时, 至少要同步更新这四处:

- [`pyproject.toml`](./pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)
- [`.agents/profile.yaml`](./.agents/profile.yaml)
- 本文件
=======
当前工作区相对 `0.1.0`，最重要的变化有 5 类。

### 1. 根目录人读入口文档被收敛到 5 个
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a

根目录现在只保留：

- `README.md`
- `QUICKSTART.md`
- `ARCHITECTURE.md`
- `DIRECTORY_STRUCTURE.md`
- `CHANGELOG.md`

<<<<<<< HEAD
## 版本口径说明

当前仓库只维护一套正式版本号。

- 当前正式版本号: `1.3.2`
- 机器真源同步点:
  - [`pyproject.toml`](./pyproject.toml) 的 `[project].version`
  - [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml) 的 `version`
  - [`.agents/profile.yaml`](./.agents/profile.yaml) 的 `project_version`
- 展示层可以写 `v1.3.2`
- Git tag 也可以使用 `v1.3.2`

注意:

- `v1.3.2` 只是 `1.3.2` 的展示写法, 不是第二套版本号
- 默认不自动升版, 必须人工改真源后再执行 `render`

## [Unreleased]

当前无未发布主线变更。

## [1.3.2] - 2026-06-02

### 版本定位

这一版用于把 `1.3.2` 提升为当前正式主线, 让版本真源、根目录入口、升级总索引和下一轮承接索引不再停留在 `1.2.x` 语境。

它承接了 `1.2.1` 的统一版本号策略, 并把此前工作区中的模板库与最小多 agent 入口层补强纳入当前主线。

### 本版完成内容

- 新增根目录模板入口文件 `TEMPLATES.md`, 正式把根目录给人看的入口文件从 5 个扩展为 6 个
- 新增 `templates/` 项目模板库目录, 用于沉淀和分发可复用项目模板
- 新增首个模板 `templates/lightweight-comparison-test/README.md`, 用于承接从轻量对比测试项目提炼出的半抽象模板
- 同步更新根目录入口口径、目录说明和使用手册, 明确根级 `templates/` 与 `vibe_governance/resources/templates/` 不是同一层能力
- 补强两个轻量模板的 `.agents` 最小治理骨架说明, 明确 `progress/entries/` 是治理闭环的一部分, 避免手工引入时只带目录名不带治理内核
- 补强轻量模板的“触发即记”规则与最小多 agent 入口层口径, 明确 bug / 异常、关键操作需要落 progress entry, 且最小多 agent 适配不等于多 IDE 扩展层
- 保持 `pyproject.toml`、`release-manifest.yaml`、`.agents/profile.yaml` 和 `vibe_governance.__version__` 的版本口径一致
- 新增 `docs/upgrades/v1.3.2-summary.md` 与 `docs/upgrades/v1.3.2-plan.md`
- 更新 `docs/NEXT_ITERATION_BASELINE.md` 与 `docs/DELTA_DECISIONS.md`, 将当前承接主线切换到 `1.3.2`

### 发布锚点

- 正式版本号: `1.3.2`
- 展示标签: `v1.3.2`
- 发布清单: [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)
- 主线提升条目: [`.agents/progress/entries/2026/2026-06-02-1.md`](./.agents/progress/entries/2026/2026-06-02-1.md)

## [1.2.1] - 2026-04-01

### 版本定位

这一版用于把仓库正式版本号、工具版本号和解释层文档口径重新收口到同一套 `1.2.1` 真源。

它承接了 `v1.2.0` 已完成的治理机制升级, 但额外解决了一个新问题:

- 机器真源已经升到 `1.2.1`, 历史文档里仍残留“当前正式版本号是 `1.0.0`”的现在时表述

### 本版完成内容

- 保持 `pyproject.toml`、`release-manifest.yaml` 和 `.agents/profile.yaml` 三处版本真源一致
- 明确 `v1.2.0` 是治理迭代标签, `1.2.1` 是当前正式版本号
- 修正 `CHANGELOG.md`、`docs/UPGRADE_SUMMARY.md`、`docs/upgrades/v1.2.0-summary.md` 中会误导当前状态判断的旧表述
- 在 `docs/DELTA_DECISIONS.md` 与 `docs/NEXT_ITERATION_BASELINE.md` 中补充“迭代标签”和“正式版本号”的区分
- 更新 `vibe_governance.__version__`, 让受管输出头信息与当前版本口径一致

### 发布锚点

- 正式版本号: `1.2.1`
- 展示标签: `v1.2.1`
- 发布清单: [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)
- 版本策略条目: [`.agents/progress/entries/2026/2026-04-01-3.md`](./.agents/progress/entries/2026/2026-04-01-3.md)
- 文档收口条目: [`.agents/progress/entries/2026/2026-04-01-4.md`](./.agents/progress/entries/2026/2026-04-01-4.md)

## [1.0.0] - 2026-04-01

### 版本定位

这是当前仓库第一次把“通用治理原型”正式收口为“可承接嵌入式治理项目的治理栈”的稳定版本。

这一版同时完成了两件事:

- 完成 `docs/upgrades/v1.0.0-*` 这轮治理升级闭环
- 把仓库包版本、发布清单版本和项目版本统一到同一个 `1.0.0`

### 本版完成内容

- 落地 `project_version` 机器真源, 固定格式为 `major.minor.patch`
- 实现 `init --project-type embedded` 和嵌入式默认骨架
- 扩展 `validate`, 覆盖嵌入式关键文档、关键字段、`M0 / M1 / M2 / M3` 与版本一致性检查
- 完成 `P1` 最小护栏:
  - 版本引用统一到 `project_version`
  - 环境兼容性与 UTF-8 最小护栏落盘
  - 根目录阅读顺序和目录说明收口
  - 提交消息与命名规律约束落盘
- 统一仓库版本口径:
  - `pyproject.toml`
  - `release-manifest.yaml`
  - `.agents/profile.yaml`
  - 受管输出头信息

### 发布锚点

- 正式版本号: `1.0.0`
- 展示标签: `v1.0.0`
- 发布清单: [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)
- 升级总结: [docs/upgrades/v1.0.0-summary.md](./docs/upgrades/v1.0.0-summary.md)
- 实施计划: [docs/upgrades/v1.0.0-plan.md](./docs/upgrades/v1.0.0-plan.md)

## 当前工作区说明

当前工作区的正式版本口径已经收口到 `1.3.2`。

如果你要追溯 `1.0.0 -> v1.2.0 -> 1.2.1 -> 1.3.2` 的演进链路, 建议依次查看:

1. [docs/upgrades/v1.0.0-summary.md](./docs/upgrades/v1.0.0-summary.md)
2. [docs/upgrades/v1.2.0-summary.md](./docs/upgrades/v1.2.0-summary.md)
3. [docs/upgrades/v1.3.2-summary.md](./docs/upgrades/v1.3.2-summary.md)
4. [docs/UPGRADE_SUMMARY.md](./docs/UPGRADE_SUMMARY.md)
5. [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
=======
其余深度说明下沉到了 `docs/`。

### 2. 三篇原始文章已经入仓归档

原始资料已经进入本地仓库：

- [`docs/SOURCE_MATERIALS.md`](./docs/SOURCE_MATERIALS.md)
- [`references/original-articles/`](./references/original-articles/)

### 3. 标准化为 `bootstrap`，在新 IDE 的当前目录直接落骨架

这次是当前工作区最关键的一次修正。

现在支持：

```bash
vibe-governance bootstrap --type embedded --target .
```

这更符合真实使用方式：

- 先把 `Taotaotao` 安装到本机
- 再在新的 IDE 和新的项目目录里直接调用它

### 4. 新项目入口模板已经反向指向本机 `Taotaotao`

新生成项目里的 `START_HERE.md` 和项目 `README.md`，现在会记录本机治理仓来源路径。

这样新 IDE 里的 AI 先读当前项目本地文件；如果需要理解启动器本身，再回看本机 `Taotaotao`。

## 当前工作区对应的本地记录

- `20260307-2`: 补齐根目录解释性文档
- `20260307-3`: 重构 onboarding 文档并归档原始文章
- `20260307-4`: 统一剩余人读文档并补充适配层 onboarding 规则
- `20260308-1`: 根目录人读文档瘦身为 5 个入口文件
- `20260308-3`: 新增 `smoke` 一键冒烟测试
- `20260308-5`: 修正为“新 IDE 当前目录 bootstrap”的主流程
- `20260308-6`: 删除重复旧路径，只保留 `bootstrap` 作为项目创建入口

后续如果这些变化进入正式版本，应在新的版本段落里正式归档。
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a

## [0.1.0] - 2026-03-07

### 版本定位

这是当前仓库的第一版治理内核基线版本。

它建立了：

- Python CLI
- `.agents/` 真源骨架
- 多 IDE / 多 agent 适配层生成
- `validate / render / sync / progress` 基础能力
- `PROGRESS` 滑动窗口索引
- 自举式治理仓结构

### 这个版本解决了什么

这个版本要解决的核心问题是：

- 不再依赖聊天记忆保存项目状态
- 把规则、进度、版本、迁移信息落到本地文件
- 让项目在不同 IDE、不同账号、不同 AI 之间稳定接手

### 核心内容

新增：

- `init / render / validate / sync / progress` 命令组
- [`.agents/profile.yaml`](./.agents/profile.yaml)
- [`.agents/overrides/rules.yaml`](./.agents/overrides/rules.yaml)
- [`vibe_governance/resources/rule-catalog.yaml`](./vibe_governance/resources/rule-catalog.yaml)
- 根级 AI 适配文件生成
- `generated-manifest.yaml`
- `upstream-rule-catalog.yaml`
- `PROGRESS` 生命周期基础能力

设计约束：

- 不用 LLM 做规则翻译层
- 生成文件默认不允许手工改
- immutable 规则不能被本地 override
- MCP 只预留 schema，不实现完整嵌入式协议栈

### Git 基线

- 版本号: `0.1.0`
- 基线 Commit Hash: `df203b9672d47e39fd29926e25dfe5cb2ffbaa91`
- 基线 Commit 标题: `初版_5.4生成`
- 基线提交时间: `2026-03-07T15:42:15+08:00`
