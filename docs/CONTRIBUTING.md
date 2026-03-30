# 迭代修改指南

这份文档是写给准备继续维护这个仓库的人看的。

它要解决的不是“怎么写代码”, 而是“怎么改这个仓库, 才不会把治理层、文档层和生成层搅乱”。

如果你是第一次接手, 先读:

1. [README.md](../README.md)
2. [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)
3. [ARCHITECTURE.md](../ARCHITECTURE.md)
4. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

## 一、开始改之前, 先判断自己碰的是哪一层

绝大多数改动都落在下面四类之一:

1. 根目录解释性文档
2. `.agents/` 项目真源
3. `vibe_governance/` 生成器代码
4. `vibe_governance/resources/` canonical 规则 / 模板 / scaffold

这一步是整个贡献流程的起点。层级判断错了, 后面几乎一定会出漂移或文档失真。

## 二、标准贡献流程

### 第 1 步: 先对齐当前上下文

每次开始前, 至少看这些文件:

- [README.md](../README.md)
- [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)
- [ARCHITECTURE.md](../ARCHITECTURE.md)
- [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
- [CHANGELOG.md](../CHANGELOG.md)
- [`.agents/PROGRESS.md`](../.agents/PROGRESS.md)

### 第 2 步: 明确这次改动应该落哪一层

- 改文档解释 -> 根目录说明文档
- 改项目事实或项目个性 -> `.agents/*`
- 改生成行为 -> `vibe_governance/*`
- 改通用治理能力 -> `vibe_governance/resources/*`

### 第 3 步: 先写或补 `PROGRESS`

只要改动对后续接手、版本理解、治理边界或实现方式有价值, 就建议先补一条 entry:

- `.agents/progress/entries/YYYY/YYYY-MM-DD-N.md`

entry 里至少要写清:

- 为什么改
- 改了什么
- 有哪些后续人需要知道的点
- 推荐的 `related_commit_message`

如果这次工作是一次升级整理, 先不要急着拆任务。应先把用户给出的零散材料统一归并到 [UPGRADE_FEEDBACK.md](./UPGRADE_FEEDBACK.md), 只保存原始记录; 后续再把总结、归类和行动项写到 [UPGRADE_SUMMARY.md](./UPGRADE_SUMMARY.md)。

### 第 4 步: 按层修改, 不要跨层乱改

这一步只有三条硬纪律:

- 不直接改受管生成文件
- 不把项目局部经验直接塞进通用规则目录
- 不把关键解释只留在聊天里而不写回仓库

### 第 5 步: 做最小必要验证

最基础的验证动作是:

```bash
python -m vibe_governance validate --target .
```

如果你改了 `.agents/`、规则目录、模板或生成器, 还要继续跑:

```bash
python -m vibe_governance render --target .
```

如果你改了 Python 代码或 canonical 规则 / 模板, 再跑:

```bash
python -m unittest discover -s tests -v
```

### 第 6 步: 补文档和版本说明

只要这次改动会影响下面任一方面, 就不能只改代码:

- 接手顺序
- 使用方式
- 版本理解
- 规则边界
- 迁移方式

常见需要一起更新的文件有:

- [README.md](../README.md)
- [USAGE_GUIDE.md](./USAGE_GUIDE.md)
- [ARCHITECTURE.md](../ARCHITECTURE.md)
- [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
- [CHANGELOG.md](../CHANGELOG.md)

## 三、不同类型改动的标准动作

### 类型 A: 只改根目录说明文档

常见动作:

- 改说明结构
- 补迁移说明
- 重写入门文档

建议动作:

1. 补 `PROGRESS`
2. 修改文档
3. 跑 `validate`
4. 如果文档提到了新行为, 同步检查 [CHANGELOG.md](../CHANGELOG.md)

### 类型 B: 改 `.agents/` 真源

常见动作:

- 改 `profile.yaml`
- 改项目级 override
- 改架构决策
- 新增经验记录

建议动作:

1. 改真源
2. `validate`
3. `render`
4. 检查受管输出是否符合预期

### 类型 C: 改生成器代码

常见动作:

- 改 CLI 子命令
- 改校验逻辑
- 改同步逻辑
- 改 `PROGRESS` 处理流程

建议动作:

1. 补 `PROGRESS`
2. 修改代码
3. `render`
4. `validate`
5. `unittest`
6. 补说明文档和 `CHANGELOG`

### 类型 D: 改 canonical 规则或模板

常见动作:

- 新增 `rule_id`
- 调整模板输出
- 补初始化 scaffold

建议动作:

1. 先确认这真的是通用能力, 不是项目局部需求
2. 修改 `vibe_governance/resources/*`
3. `render`
4. `validate`
5. `unittest`
6. 更新文档和版本说明

## 四、跨账号继续迭代的标准流程

这个项目强调“换账号也不断线”, 所以跨账号继续开发时必须先做接手动作, 再做新改动。

### 账号 B 接着账号 A 的工作时

账号 B 至少应该:

1. 拉取最新仓库
2. 阅读 [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)
3. 阅读 [`.agents/PROGRESS.md`](../.agents/PROGRESS.md) 和最近的 entry
4. 运行:

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

5. 再开始自己的修改

这样做的目的很明确:

- 先把文件里的上下文重新对齐
- 再启动新的迭代
- 避免新账号靠猜测续写旧账号的设计意图

## 五、哪些改动一定要补文档

下面这些改动, 不允许只改代码不改文档:

- 新增 CLI 命令
- 修改 `profile.yaml` 字段语义
- 新增或删除 `rule_id`
- 改模板输出路径
- 改同步逻辑
- 改 `PROGRESS` 生命周期
- 增加嵌入式 / MCP 相关能力
- 改新账号的接手顺序

## 六、哪些改动应该进 `CHANGELOG`

建议进入 [CHANGELOG.md](../CHANGELOG.md) 的情况:

- 对外使用方式变了
- 根目录文档导航变了
- 通用规则或模板变了
- 生成文件结构变了
- 版本号变了

## 七、提交和评审前的最小清单

- [ ] 我确认了改动层级, 没有直接手改生成文件
- [ ] 我补了需要的 `PROGRESS`
- [ ] 我更新了需要的说明文档
- [ ] `validate` 通过
- [ ] 需要时我已经执行了 `render`
- [ ] 需要时我已经跑了测试
- [ ] 变更原因、影响范围、迁移方式能从本地文件看明白

## 八、给后续维护者的一句提醒

这个仓库本质上是一个治理产品, 不是一堆脚本文件。

所以每次改动前都问自己:

- 这次改动会不会影响后续项目初始化
- 会不会影响新账号或新 AI 接手
- 会不会影响版本追溯
- 会不会让规则边界更模糊

如果答案是会, 那就必须把解释写回仓库。

