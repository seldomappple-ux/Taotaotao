# 版本更新日志

这份文件只记录“版本级变化”和“当前工作区与版本之间的关系”。

## 维护规则

每次正式发版时, 至少要同步更新这三处:

- `pyproject.toml`
- `vibe_governance/resources/release-manifest.yaml`
- 本文件

另外还要确认:

- 关联的 `PROGRESS` 条目已经写好
- 相关的根目录说明文档已经更新

## 当前工作区说明

当前工作区已经补齐了根目录解释性文档体系, 但这些文档的职责是“解释当前版本”, 不是单独构成一个新的已发布版本。

本轮解释性文档补全对应的本地经验记录建议写入:

- `20260307-2`：根目录解释性文档补全

如果后续你要把这批文档变化算作正式版本的一部分, 应该在下一次发版时把它写进新的版本段落里。

## [0.1.0] - 2026-03-07

### 版本定位

这是当前仓库的第一版治理内核基线版本。

它完成了:

- Python CLI
- `.agents/` 真源骨架
- 多 IDE 适配层生成
- 校验、同步、`PROGRESS` 生命周期基础能力
- 自举式仓库结构

### 为什么会有这个版本

目标很明确:

- 不再依赖聊天记忆保存项目状态
- 把规则、进度、版本、迁移信息全部落到本地文件
- 让项目在不同 IDE、不同账号、不同 AI 间稳定接力

### 本版本包含的核心内容

#### 新增

- `init / render / validate / sync / progress` 命令集
- `.agents/profile.yaml` 项目事实源
- `.agents/overrides/rules.yaml` override 机制
- `rule-catalog.yaml` canonical 规则目录
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

### 关联文件

- 关联 `PROGRESS`:
  - `20260307-1` -> `.agents/progress/entries/2026/2026-03-07-1.md`
- 关联发布清单:
  - `vibe_governance/resources/release-manifest.yaml`
- 关联包版本:
  - `pyproject.toml`

### 对后续版本的要求

从这个版本开始, 后续发版必须保证:

1. `CHANGELOG` 能看懂版本为什么变
2. `PROGRESS` 能追溯经验从哪里来
3. 新账号只看本地文件就能接手
