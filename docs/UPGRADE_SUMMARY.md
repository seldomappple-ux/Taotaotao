# 升级总索引

这份文档是升级工作的总入口, 不承载具体问题细节。

它的职责是:
- 列出当前进行中的版本
- 列出已完成的版本
- 提供每个版本 summary 的链接
- 记录每轮升级的状态

## 文档分工

### UPGRADE_FEEDBACK.md
- 职责: 原始记录池
- 维护方式: 持续累计, 按时间批次追加
- 不按版本拆分
- 保留原话、上下文、历史证据

### UPGRADE_SUMMARY.md (本文件)
- 职责: 升级总索引
- 维护方式: 只列版本和状态, 不写细节
- 提供导航和概览

### docs/upgrades/vX.Y.Z-summary.md
- 职责: 每个版本的独立总结文档
- 维护方式: 一个版本一份
- 包含: 问题清单、决策、实施范围、结果

### docs/upgrades/vX.Y.Z-plan.md
- 职责: 每个版本的独立实施计划
- 维护方式: 一个版本一份
- 包含: 阶段目标、接口约束、实施步骤、验收方式

## 当前进行中的版本

当前无进行中的升级版本。

## 当前仓库版本

- 当前正式版本号: `1.2.1`
- 机器真源:
  - `pyproject.toml`
  - `.agents/profile.yaml`
  - `vibe_governance/resources/release-manifest.yaml`
- 说明:
  - `v1.2.0` 是最近一次已完成的治理迭代文档标签
  - `1.2.1` 是随后完成的统一版本号收口结果, 不是另一轮独立的升级计划

## 已完成的版本

### v1.2.0

- 状态: `completed`
- 启动日期: `2026-04-01`
- 完成日期: `2026-04-01`
- 目标: 建立单体系真源、增量分流、纯索引基线与人读友好的迭代治理机制
- 详细文档: [v1.2.0-summary.md](./upgrades/v1.2.0-summary.md)
- 实施计划: [v1.2.0-plan.md](./upgrades/v1.2.0-plan.md)
- 收口锚点:
  - `v1.2.0` 收口当日正式版本号为: `1.0.0`
  - 当前仓库正式版本号已在后续版本策略收口中更新为: `1.2.1`
  - Progress entry: `.agents/progress/entries/2026/2026-04-01-2.md`
  - 验证命令: `python -m vibe_governance render --target .`、`python -m vibe_governance validate --target .`、`python -m unittest discover -s tests -v`
- 输入来源:
  - `v1.0.0` 实施后的使用反馈
  - 对“上游稳定 + 增量分流 + 下一轮基线包”的进一步治理要求

### v1.0.0

- 状态: `completed`
- 启动日期: `2026-03-30`
- 完成日期: `2026-03-31`
- 目标: 从通用治理原型升级到能够正式承接嵌入式治理的第一版
- 详细文档: [v1.0.0-summary.md](./upgrades/v1.0.0-summary.md)
- 实施计划: [v1.0.0-plan.md](./upgrades/v1.0.0-plan.md)
- 发布锚点:
  - Commit: `532d1545bad666aa52305e66a9adbece1c733b9b`
  - Tag: `v1.0.0`
  - Progress entry: `.agents/progress/entries/2026/2026-03-31-2.md`
- 输入来源:
  - UPGRADE_FEEDBACK.md 中的用户口述嵌入式反馈
  - 导入的 Moss_Q progress 原始记录 (153 条)

## 版本状态说明

- `planned`: 已规划, 未开始
- `in_progress`: 进行中
- `completed`: 已完成
- `cancelled`: 已取消

## 使用指南

### 启动新版本升级时

1. 在 UPGRADE_FEEDBACK.md 中按批次追加原始记录
2. 创建 `docs/upgrades/vX.Y.Z-summary.md`
3. 创建 `docs/upgrades/vX.Y.Z-plan.md`
4. 在本文件的"当前进行中的版本"中添加条目
5. 在版本 summary 中进行问题整理和决策

### 完成版本升级时

1. 更新版本 summary 的实施结果
2. 将版本从"进行中"移到"已完成"
3. 更新 CHANGELOG.md
4. 创建对应的 progress entry
5. 发布版本

### 查找历史问题时

1. 先看本索引, 定位到具体版本
2. 查看该版本的 summary 文档
3. 如需原始记录, 回到 UPGRADE_FEEDBACK.md 按日期查找
