# 完整全流程使用手册

这份手册讲的是一条完整闭环:

从第一次接手仓库, 到日常修改, 再到版本发布、经验沉淀和规则回流, 每一步到底怎么做。

如果你刚接这个项目, 建议先读:

1. [QUICKSTART.md](../QUICKSTART.md)
2. [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)
3. [ARCHITECTURE.md](../ARCHITECTURE.md)

然后再回来看这份手册。

## 一、先把真实工作流记住

这套仓库真正的工作流不是“开个会话, 让 AI 猜着写”, 而是:

1. 先用根目录说明文档和原始资料对齐语义.
2. 再从 `.agents/` 读取项目事实、规则和长期记忆.
3. 再让 `vibe_governance` 读取真源并生成适配层.
4. 每次变更都回写到本地文件, 形成版本、经验和迁移闭环.

所以这份手册也按这个顺序来讲。

## 二、场景 1: 接手一个已经存在的仓库

这是当前仓库最常见的使用方式。

### 第 1 步: 先读, 不要先改

建议顺序:

1. [README.md](../README.md)
2. [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)
3. [ARCHITECTURE.md](../ARCHITECTURE.md)
4. [DIRECTORY_STRUCTURE.md](../DIRECTORY_STRUCTURE.md)
5. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

然后再看:

- [`.agents/profile.yaml`](../.agents/profile.yaml)
- [`.agents/RULES.md`](../.agents/RULES.md)
- [`.agents/architecture-decisions.yaml`](../.agents/architecture-decisions.yaml)
- [`.agents/PROGRESS.md`](../.agents/PROGRESS.md)

### 第 2 步: 跑三条标准命令

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

这三条命令的职责分别是:

- `validate`: 检查配置、override、progress 和受管输出是否健康.
- `render`: 按当前真源重建适配层和 `PROGRESS` 索引.
- `sync --dry-run`: 查看本地快照和当前规则目录有没有差异.

### 第 3 步: 判断这次接手要改哪一层

最常见的四层是:

1. 根目录解释层
2. `.agents/` 真源层
3. `vibe_governance/` 生成器代码层
4. `vibe_governance/resources/` canonical 规则和模板层

如果这一步判断错了, 后面基本都会乱。

## 三、场景 2: 用这套治理体系初始化一个新仓库

当前仓库已经是初始化完成的状态, 但你以后复用时应该按下面做。

### 第 1 步: 把治理内核带进新项目

最少需要:

- `vibe_governance/`
- `pyproject.toml`

### 第 2 步: 初始化 `.agents/` 骨架

```bash
python -m vibe_governance init --target .
```

当前代码会创建这些核心文件:

- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/overrides/rules.yaml`
- `.agents/architecture-decisions.yaml`
- `.agents/progress/ENTRY_TEMPLATE.md`
- `.agents/.managed/upstream-rule-catalog.yaml`

### 第 3 步: 补项目事实和项目边界

优先改:

- [`.agents/profile.yaml`](../.agents/profile.yaml)
- [`.agents/RULES.md`](../.agents/RULES.md)
- [`.agents/architecture-decisions.yaml`](../.agents/architecture-decisions.yaml)

这一步要做的不是“赶紧开始写代码”, 而是先把:

- 项目类型
- 文档模式
- 注释语言
- 启用的适配器
- 项目红线
- 关键架构边界

写清楚。

### 第 4 步: 立刻校验和生成

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
```

不要跳过这一步。很多初始化问题, 在第一轮 `validate` 就能暴露出来。

## 四、日常迭代到底怎么做

日常迭代可以按一个固定循环来做。

### 第 1 步: 先判断改动类型

常见改动类型有三类:

#### 类型 A: 只改解释文档

例如:

- [README.md](../README.md)
- [ARCHITECTURE.md](../ARCHITECTURE.md)
- [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)

这类改动通常不影响生成逻辑, 但如果对接手方式、版本理解或治理边界有影响, 仍然建议补 `PROGRESS`。

#### 类型 B: 改项目真源

例如:

- [`.agents/profile.yaml`](../.agents/profile.yaml)
- [`.agents/overrides/rules.yaml`](../.agents/overrides/rules.yaml)
- [`.agents/architecture-decisions.yaml`](../.agents/architecture-decisions.yaml)
- `.agents/progress/entries/*`

这类改动通常要走:

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
```

#### 类型 C: 改治理内核

例如:

- [`vibe_governance/project.py`](../vibe_governance/project.py)
- [`vibe_governance/cli.py`](../vibe_governance/cli.py)
- [`vibe_governance/resources/rule-catalog.yaml`](../vibe_governance/resources/rule-catalog.yaml)
- [`vibe_governance/resources/templates/`](../vibe_governance/resources/templates/)

这类改动通常要走:

```bash
python -m vibe_governance render --target .
python -m vibe_governance validate --target .
python -m unittest discover -s tests -v
```

### 第 2 步: 先写 `PROGRESS`, 再继续改

只要这次改动具有以下任一特征, 建议先写一条 entry:

- 会影响后续接手
- 会影响规则理解
- 会影响版本历史
- 会影响多个文件或多个阶段

entry 位置在:

- `.agents/progress/entries/YYYY/YYYY-MM-DD-N.md`

### 第 3 步: 修改正确层级

最重要的纪律只有两条:

- 不要直接改受管生成文件.
- 不要把项目局部经验直接写成通用规则.

## 五、同步、升级和规则调整怎么做

这部分最容易出事故, 必须单独讲清楚。

### 第 1 步: 先看同步报告

```bash
python -m vibe_governance sync --target . --dry-run --json
```

重点看:

- `status`
- `changed_rule_ids`

### 第 2 步: 再判断变化属于哪一类

- 只是快照和当前规则目录不同
- 还是你真的想升级上游基线
- 还是你其实只想做项目局部 override

### 第 3 步: 真要同步时再执行

```bash
python -m vibe_governance sync --target .
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
```

当前代码里的 `sync_project()` 做的是真正的“快照更新和上游版本信息回写”, 不是复杂的 overlay 自动合并器。不要把它理解成已经有完整自动合并系统。

## 六、版本迭代怎么形成闭环

这套项目最重要的不是“能改文件”, 而是“每次改动能被后人看懂”。

### 第 1 步: 先决定这次改动要不要升到版本级

一般建议认真考虑发版的情况:

- CLI 行为变了
- 规则目录变了
- 模板输出格式变了
- 校验逻辑变了
- 同步策略或 `PROGRESS` 生命周期变了

一般不一定需要马上发版的情况:

- 只补解释文档
- 只新增项目局部经验
- 只调整还未提升为通用规则的局部内容

### 第 2 步: 版本相关文件一起看

当前版本信息至少分布在:

- [`pyproject.toml`](../pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](../vibe_governance/resources/release-manifest.yaml)
- [CHANGELOG.md](../CHANGELOG.md)

### 第 3 步: 发版前跑标准动作

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
python -m unittest discover -s tests -v
```

然后人工确认:

- [CHANGELOG.md](../CHANGELOG.md) 是否更新
- [`.agents/PROGRESS.md`](../.agents/PROGRESS.md) 是否能追到最近变化
- 根目录说明文档是否需要同步更新

## 七、经验回流到治理内核怎么做

经验回流不是“看着不错就往上塞”, 而是一个升级动作。

### 哪些经验值得回流

- 多个项目重复出现的规则
- 可以减少高频事故的校验逻辑
- 应该统一的模板表达
- 已经被验证为通用的跨 IDE / 嵌入式坑点

### 回流到哪里

- 通用规则: [`vibe_governance/resources/rule-catalog.yaml`](../vibe_governance/resources/rule-catalog.yaml)
- 通用模板: [`vibe_governance/resources/templates/`](../vibe_governance/resources/templates/)
- 初始化骨架: [`vibe_governance/resources/scaffold/`](../vibe_governance/resources/scaffold/)
- 解释层说明: 根目录说明文档

### 回流前必须先满足什么

1. 先有 `.agents/progress/entries/*` 里的原始经验记录.
2. 先确认这不是一次性项目噪音.
3. 先判断它应该提升到哪一层.

## 八、常见场景的最短路径

### 我只想改某条适配文案

先看它是否允许项目本地覆盖:

- [`.agents/profile.yaml`](../.agents/profile.yaml) 里的 `override_whitelist`

如果允许, 去改:

- [`.agents/overrides/rules.yaml`](../.agents/overrides/rules.yaml)

不要直接改:

- `.github/copilot-instructions.md`
- `.cursor/rules/governance.mdc`
- `CLAUDE.md`

### 我想加一个新的规则种类

去改:

- [`vibe_governance/resources/rule-catalog.yaml`](../vibe_governance/resources/rule-catalog.yaml)

必要时再改:

- [`vibe_governance/resources/templates/`](../vibe_governance/resources/templates/)
- [`vibe_governance/project.py`](../vibe_governance/project.py)

### 我换账号了, 还想继续做

直接看:

- [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)

## 九、最后记住这四条

- 真源优先, 生成层靠后.
- 经验先写 `PROGRESS`, 再谈升级规则和发版本.
- 新账号接手靠文件闭环, 不靠聊天历史.
- 当前 v1 只预留了嵌入式 / MCP 的入口, 不要把预留能力写成现成功能.

