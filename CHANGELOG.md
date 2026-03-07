# 版本更新日志

这份文件只记录两类信息:

1. 已经发布的版本级变化
2. 当前工作区相对最近版本的解释性说明

它不负责记流水账。更细的经验和上下文, 在:

- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- `.agents/progress/entries/*`

## 维护规则

每次正式发版时, 至少要同步更新这三处:

- [`pyproject.toml`](./pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)
- 本文件

同时还要确认:

- 关联的 `PROGRESS` 条目已经写好
- 相关根目录说明文档已经更新
- 新账号接手路径没有被文档改乱

## 当前工作区说明

当前工作区相对 `0.1.0` 基线, 已经完成两类解释层增强:

1. 把根目录入门文档重构为更清晰的接手顺序
2. 把最初三篇原文纳入仓库内资料归档, 并把其中心思想映射到当前实现

这部分变化目前仍然是“当前工作区说明”, 不是单独的已发布版本段落。

当前工作区可对应的本地经验记录包括:

- `20260307-2`: 根目录解释性文档补全
- `20260307-3`: 重构 onboarding 文档并补齐原始资料归档
- `20260307-4`: 统一剩余人读文档并补充适配层 onboarding 规则

如果后续要把这些变化并入正式版本, 应在下一个版本段落里明确写入。

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

### 关联上下文

- 关联 `PROGRESS`:
  - `20260307-1` -> `.agents/progress/entries/2026/2026-03-07-1.md`
- 关联发布清单:
  - [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)
- 关联包版本:
  - [`pyproject.toml`](./pyproject.toml)

### 对后续版本的要求

从这个版本开始, 后续发版至少要保证:

1. `CHANGELOG` 能解释版本为什么变
2. `PROGRESS` 能追溯经验从哪里来
3. 新账号只看本地文件就能接手
