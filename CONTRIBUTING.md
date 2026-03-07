# 迭代修改指南

这份文档讲的是:

如果你要继续迭代这个仓库, 应该按什么顺序做, 才不会把治理层、文档层、生成层搅乱。

## 一、先判断自己在改什么

改动大体分四类:

1. 根目录解释性文档
2. `.agents/` 项目真源
3. 生成器代码
4. canonical 规则 / 模板

你先把这件事判断清楚, 后面的动作才不会错。

## 二、标准修改流程

### 第 1 步: 先读当前上下文

每次开始前, 至少看这些文件:

- [README.md](./README.md)
- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
- [CHANGELOG.md](./CHANGELOG.md)
- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)

### 第 2 步: 明确这次改动的落点

如果你是:

- 改文档 -> 改根目录说明文档
- 改项目个性 -> 改 `.agents/*`
- 改生成行为 -> 改 `vibe_governance/*`
- 改通用规则 -> 改 `vibe_governance/resources/*`

### 第 3 步: 写或补 `PROGRESS`

有实际价值的改动, 先补一条 entry:

- `.agents/progress/entries/YYYY/YYYY-MM-DD-N.md`

推荐 commit message 也一起写进去, 方便后续提交。

### 第 4 步: 按层修改

关键原则:

- 不要直接改生成文件
- 不要把只属于一个项目的经验直接塞进通用规则目录
- 不要把解释性内容只留在聊天里

### 第 5 步: 本地验证

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m unittest discover -s tests -v
```

如果只是改根目录说明文档, 可以不一定跑全量测试, 但至少建议跑一次 `validate`。

### 第 6 步: 更新文档和版本说明

视情况更新:

- [CHANGELOG.md](./CHANGELOG.md)
- [README.md](./README.md)
- [USAGE_GUIDE.md](./USAGE_GUIDE.md)
- [ARCHITECTURE.md](./ARCHITECTURE.md)

## 三、跨账号提交迭代内容的标准流程

这个项目很强调“换账号也不断线”, 所以跨账号提交流程要比一般仓库更严格。

### 账号 A 做了改动, 账号 B 要接着做

账号 B 的动作必须是:

1. 拉最新仓库
2. 先读 [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)
3. 跑:

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

4. 读 `.agents/PROGRESS.md`
5. 再开始改

这样做的目的就是:

- 先把文件里的上下文对齐
- 再开始新的迭代
- 避免新账号凭空猜测旧账号的设计意图

## 四、什么改动一定要补文档

下面这些改动, 不能只改代码不改文档:

- 新增 CLI 命令
- 修改 `profile.yaml` 字段语义
- 新增或删除 `rule_id`
- 改模板输出路径
- 改同步逻辑
- 改 `PROGRESS` 生命周期
- 增加嵌入式/MCP 相关能力

## 五、什么改动一定要补 `CHANGELOG`

建议补 `CHANGELOG` 的情况:

- 对外使用方式变了
- 根目录文档导航变了
- 规则目录有通用变更
- 生成文件格式变了
- 版本号变了

## 六、提交流程建议

当前项目没有在代码里强制 Git 钩子, 但治理规则已经很明确:

- 提交信息尽量用 Conventional Commit
- 提交前先确认生成结果正确
- 提交后能从 `CHANGELOG` 和 `PROGRESS` 找到上下文

推荐顺序:

1. 写或补 `PROGRESS`
2. 修改文件
3. `validate`
4. `render`
5. `unittest`
6. 更新 `CHANGELOG`
7. 准备 commit

## 七、Pull Request 或合并前的检查清单

- [ ] 我改的是正确层级, 不是直接手改生成文件
- [ ] 我补了需要的 `PROGRESS`
- [ ] 我更新了需要的说明文档
- [ ] `validate` 通过
- [ ] `render` 已执行
- [ ] 测试通过
- [ ] 变更原因、影响范围、迁移方式能从本地文件看明白

## 八、给未来维护者的提醒

这套仓库不是“代码写完就完了”, 它本质上是一个治理产品。

所以每次迭代都要问自己:

- 这次改动会不会影响后续项目初始化
- 会不会影响新账号接手
- 会不会影响版本追溯
- 会不会让规则边界变得更模糊

如果答案是会, 那就必须补文档。
