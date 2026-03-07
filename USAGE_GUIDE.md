# 完整全流程使用手册

这份手册讲的是“从一个治理仓库开始, 一直到版本发布、经验回流”为止, 每一步怎么做。

## 一句话先说清

当前仓库的真实工作流是:

1. 人在根目录说明文档里理解项目.
2. 真正的项目事实落在 `.agents/`.
3. 生成器从 `.agents/` 和 `vibe_governance/resources/` 出发, 生成多 IDE 适配层.
4. 变更、验证、版本、经验全部回写到本地文件, 不依赖聊天上下文.

## 一、初始化阶段

> 当前仓库已经初始化完成。下面这段主要是给你在新仓库复用这套体系时参考。

### 1. 准备代码

最少需要这些内容:

- `vibe_governance/`
- `pyproject.toml`

### 2. 初始化治理骨架

```bash
python -m vibe_governance init --target .
```

这一步会创建:

- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/overrides/rules.yaml`
- `.agents/architecture-decisions.yaml`
- `.agents/progress/ENTRY_TEMPLATE.md`
- `.agents/.managed/upstream-rule-catalog.yaml`

### 3. 立即做第一次校验和渲染

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
```

## 二、日常开发阶段

日常开发分三类, 处理方式不一样。

### 类别 1: 只改人类说明文档

例如:

- 修改 [README.md](./README.md)
- 补充 [ARCHITECTURE.md](./ARCHITECTURE.md)
- 更新 [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)

这种情况:

- 不需要重跑 `render`
- 但建议补 `PROGRESS` 记录
- 如果影响使用方式或版本说明, 要同步改 [CHANGELOG.md](./CHANGELOG.md)

### 类别 2: 改项目真源

例如:

- 改 `.agents/profile.yaml`
- 改 `.agents/overrides/rules.yaml`
- 改 `.agents/architecture-decisions.yaml`
- 新增或修改 `.agents/progress/entries/*`

这种情况:

1. 先改真源文件
2. 跑 `validate`
3. 跑 `render`
4. 再检查生成结果是否符合预期

### 类别 3: 改治理引擎和上游规则

例如:

- 改 `vibe_governance/project.py`
- 改 `vibe_governance/cli.py`
- 改 `vibe_governance/resources/rule-catalog.yaml`
- 改 `vibe_governance/resources/templates/*`

这种情况:

1. 先改代码或 canonical 资源
2. 运行 `render`
3. 运行 `validate`
4. 跑测试:

```bash
python -m unittest discover -s tests -v
```

5. 检查根目录生成文件有没有跟着正确变化

## 三、版本迭代管理全流程

这里是这套项目最重要的一部分。

### 第 1 步: 确认这次改动属于哪个层级

先判断:

- 是文档解释层变化
- 是项目真源变化
- 还是治理引擎变化

不同层级会决定你要不要更新:

- `.agents/progress/entries/*`
- [CHANGELOG.md](./CHANGELOG.md)
- `vibe_governance/resources/release-manifest.yaml`
- `pyproject.toml`

### 第 2 步: 先写 `PROGRESS`, 再谈发版

任何值得保留的经验, 先落到:

- `.agents/progress/entries/YYYY/YYYY-MM-DD-N.md`

推荐写法:

- 这次为什么改
- 改了什么
- 哪些坑以后别再踩
- 相关 commit message 应该写什么

如果这条经验只是项目局部经验, 停在 `draft` 或 `promotable` 就够了。

如果这条经验已经值得提升到通用规则, 再走回流。

### 第 3 步: 再决定要不要发版本

当前仓库已经有一个版本基线:

- `0.1.0`

版本信息现在分散在三个地方:

- [`pyproject.toml`](./pyproject.toml): Python 包版本
- [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml): 上游发布清单
- [CHANGELOG.md](./CHANGELOG.md): 人类可读版本历史

如果你只是补局部说明文档, 不一定要马上发版。

如果你改了以下内容, 就应该认真考虑发版:

- CLI 行为
- 规则目录
- 模板输出格式
- 同步策略
- 进度管理逻辑

### 第 4 步: 发版前的标准动作

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
python -m unittest discover -s tests -v
```

然后人工确认:

- [CHANGELOG.md](./CHANGELOG.md) 是否更新
- `.agents/PROGRESS.md` 是否包含新记录
- 根目录说明文档是否需要同步更新

### 第 5 步: 发布和归档

当前仓库里已经有 GitHub Actions 工作流:

- [`.github/workflows/release-governance.yml`](./.github/workflows/release-governance.yml)

它现在做的事情很明确:

1. 校验治理源文件
2. 重新渲染生成文件
3. 跑单元测试
4. 打包发布产物

发版完成后:

- 相关 `PROGRESS` 可以从 `draft` 提升为 `promotable`
- 真正被上游吸收后, 再转 `upstreamed` 并归档

## 四、经验回流流程

“经验回流”不是一句空话, 在这个项目里它对应明确动作。

### 什么时候该回流

当你发现下面这类内容时, 应该考虑回流:

- 某条规则在多个项目重复出现
- 某个模板的表达方式应该统一
- 某个校验逻辑能防止高频事故
- 某个嵌入式/跨 IDE 的坑已经被证明是通用坑

### 回流到哪里

按实际情况回:

- 通用规则: `vibe_governance/resources/rule-catalog.yaml`
- 通用模板: `vibe_governance/resources/templates/*`
- 初始化骨架: `vibe_governance/resources/scaffold/*`
- 解释性文档: 根目录这套说明文档

### 回流前必须先做什么

1. 在 `.agents/progress/entries/*` 留下原始经验
2. 人工确认这不是一次性项目噪音
3. 明确它要升级到哪一层

## 五、同步上游规则

当前实现里的同步不是自动覆盖, 而是“先看报告, 再决定”.

### 先看报告

```bash
python -m vibe_governance sync --target . --dry-run --json
```

### 报告看什么

- `status`
- `changed_rule_ids`

如果为空, 当前快照和规则目录一致。

如果有变化, 先去看:

- [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
- [CODE_WALKTHROUGH.md](./CODE_WALKTHROUGH.md)

### 真正执行同步

```bash
python -m vibe_governance sync --target .
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
```

## 六、常见场景怎么做

### 场景 1: 我只想改某条 Copilot 文案

去改:

- `.agents/overrides/rules.yaml`

前提:

- 这条规则必须在 `.agents/profile.yaml -> override_whitelist` 里

不要去改:

- `.github/copilot-instructions.md`

### 场景 2: 我想加一个新的规则种类

去改:

- `vibe_governance/resources/rule-catalog.yaml`
- 必要时改模板

然后:

```bash
python -m vibe_governance render --target .
python -m unittest discover -s tests -v
```

### 场景 3: 我想换账号继续做

直接看:

- [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)

## 七、手册结尾的硬原则

- 真源优先, 生成文件靠后
- 经验先落 `PROGRESS`, 再谈升规则和发版
- 新账号接手靠文件, 不靠聊天上下文
- 当前 v1 已经有 MCP 配置入口, 但还没有完整嵌入式 overlay, 不要把“预留能力”当成“现成能力”

## 继续阅读

- 规则和冲突处理: [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
- 架构设计: [ARCHITECTURE.md](./ARCHITECTURE.md)
- 代码入口: [CODE_WALKTHROUGH.md](./CODE_WALKTHROUGH.md)
