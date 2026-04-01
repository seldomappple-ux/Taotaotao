# 版本更新日志

这份文件只记录两类信息:

1. 已经发布的版本级变化
2. 当前工作区相对最近版本的解释性说明

它不负责记流水账。更细的经验和上下文, 在:

- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- `.agents/progress/entries/*`

## 维护规则

每次正式发版时, 至少要同步更新这四处:

- [`pyproject.toml`](./pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)
- [`.agents/profile.yaml`](./.agents/profile.yaml)
- 本文件

同时还要确认:

- 关联的 `PROGRESS` 条目已经写好
- 相关根目录说明文档已经更新
- 新账号接手路径没有被文档改乱

## 版本口径说明

当前仓库只维护一套正式版本号。

- 当前正式版本号: `1.2.1`
- 机器真源同步点:
  - [`pyproject.toml`](./pyproject.toml) 的 `[project].version`
  - [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml) 的 `version`
  - [`.agents/profile.yaml`](./.agents/profile.yaml) 的 `project_version`
- 展示层可以写 `v1.2.1`
- Git tag 也可以使用 `v1.2.1`

注意:

- `v1.2.1` 只是 `1.2.1` 的展示写法, 不是第二套版本号
- 默认不自动升版, 必须人工改真源后再执行 `render`

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

当前工作区的正式版本口径已经收口到 `1.2.1`。

如果你要追溯 `1.0.0 -> v1.2.0 -> 1.2.1` 的演进链路, 建议依次查看:

1. [docs/upgrades/v1.0.0-summary.md](./docs/upgrades/v1.0.0-summary.md)
2. [docs/upgrades/v1.2.0-summary.md](./docs/upgrades/v1.2.0-summary.md)
3. [docs/UPGRADE_SUMMARY.md](./docs/UPGRADE_SUMMARY.md)
4. [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)

## [0.1.0] - 2026-03-07

### 版本定位

这是当前仓库的第一版治理内核基线版本。

它建立了:

- Python CLI
- `.agents/` 真源骨架
- 多 IDE 适配层生成
- 校验、同步、`PROGRESS` 生命周期基础能力
- 自举式仓库结构

### 为什么会有这个版本

这个版本解决的核心问题是:

- 不再依赖聊天记忆保存项目状态
- 把规则、进度、版本、迁移信息全部落到本地文件
- 让项目在不同 IDE、不同账号、不同 AI 间稳定接力

### 本版本包含的核心内容

#### 新增

- `init / render / validate / sync / progress` 命令集
- [`.agents/profile.yaml`](./.agents/profile.yaml) 项目事实源
- [`.agents/overrides/rules.yaml`](./.agents/overrides/rules.yaml) override 机制
- [`vibe_governance/resources/rule-catalog.yaml`](./vibe_governance/resources/rule-catalog.yaml) canonical 规则目录
- 根级 AI 适配文件生成
- `generated-manifest.yaml` 和 `upstream-rule-catalog.yaml` 两类受管状态
- `PROGRESS` 滑动窗口索引

#### 设计约束

- 不使用 LLM 做规则分发转换
- 生成文件默认不允许手工改
- immutable 规则不能被本地 override
- MCP 只预留字段, 未实现完整嵌入式契约

### Git 信息

- 版本号: `0.1.0`
- 基线 Commit Hash: `df203b9672d47e39fd29926e25dfe5cb2ffbaa91`
- 基线 Commit 标题: `初版_5.4生成`
- 基线提交时间: `2026-03-07T15:42:15+08:00`
