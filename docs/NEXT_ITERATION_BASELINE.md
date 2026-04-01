# 下一轮迭代索引

这份文档是下一轮人或 AI 开始工作前的纯索引文件。

它只回答两个问题:

1. 下一轮该读哪些文件
2. 这些文件按什么顺序读

## 当前版本

- current_iteration: `v1.2.0`

## 建议阅读顺序

1. `README.md`
2. `ARCHITECTURE.md`
3. `docs/upgrades/v1.2.0-summary.md`
4. `docs/upgrades/v1.2.0-plan.md`
5. `docs/DELTA_DECISIONS.md`
6. `docs/MIGRATION_GUIDE.md`
7. `docs/CONTRIBUTING.md`

## 必读文件索引

- `README.md`
  - 项目门面和最短导航
- `ARCHITECTURE.md`
  - 长期稳定的系统边界与分层原则
- `docs/upgrades/v1.2.0-summary.md`
  - 本轮为什么做、边界是什么
- `docs/upgrades/v1.2.0-plan.md`
  - 本轮怎么做
- `docs/DELTA_DECISIONS.md`
  - 当前有效的增量决议真源
- `docs/MIGRATION_GUIDE.md`
  - 新老项目怎么接入本机制
- `docs/CONTRIBUTING.md`
  - 判定规则、人工门禁和最小验证流程

## 当前有效 delta_id

当前为空。

## 固定回归检查项

- `render` 可以正常执行
- `validate` 可以正常执行
- 目录导航仍然清晰
- `DELTA_DECISIONS.md` 仍是唯一增量真源
- 新增决议没有重复写进其他正文文件

