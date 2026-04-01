# 增量决议

这份文档是当前仓库的唯一增量真源。

它只负责记录:

- 当前仍生效的增量决议
- 已升格决议的状态
- 已废弃决议的状态

它不负责:

- 复写协议正文
- 复写架构正文
- 复写下一轮索引

## 文件头

- current_iteration: `v1.2.0`
- current_repo_version: `1.2.1`
- last_cleanup_version: `v1.2.0`
- next_cleanup_due: `v1.4.0`

说明:

- `current_iteration` 表示最近一次已完成的治理迭代标签
- `current_repo_version` 表示当前正式版本号

## 字段说明

- `delta_id`: 决议编号
- `status`: `active | promoted | deprecated`
- `level`: `L0 | L1 | L2`
- `created`: 创建版本
- `expires`: 到期版本, `L1` 必填
- `promotion_target`: `L2` 的回写真源目标
- `source_entries`: 对应的 progress 条目

## 分级规则

- `L0`: 不影响跨层契约, 只影响实现层
- `L1`: 不影响正式跨层契约, 但会影响下一轮 AI 对行为的理解
- `L2`: 已影响跨层契约, 必须回写真源

## 活跃决议

当前为空。

首条决议将在 `v1.2.0` 发布后的第一次 `L1` 或 `L2` 修复时写入。

### 模板

```yaml
- delta_id: DELTA-2026-04-001
  status: active
  level: L1
  created: v1.2.0
  expires: v1.4.0
  promotion_target: ""
  source_entries:
    - .agents/progress/entries/2026/2026-04-01-1.md
```

## 已升格决议

当前为空。

## 已废弃决议

当前为空。

## 清理规则

- 每个 `L1` 最多存活 2 个迭代周期
- 到 `expires` 时必须:
  - 升格为 `L2`
  - 或标记为 `deprecated`
  - 或从活跃区移除
- 如果同一模块连续出现 3 次 `L0`, 必须人工复核是否应补 `L1` 或直接升格 `L2`
