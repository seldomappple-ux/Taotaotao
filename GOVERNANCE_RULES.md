# 治理规则详解

这份文档不重复列规则原文, 只解释“这套治理体系到底怎么管项目”。

如果你只想记住一句话, 就记这个:

> 先改真源, 再生成适配层; 先看同步报告, 再决定升级; 先写本地经验, 再回流上游规则。

## 一、当前项目的真实治理分层

当前代码落地的治理层, 按优先级从高到低, 可以理解成三层。

### 第 1 层: 上游 canonical 层

位置:

- `vibe_governance/resources/rule-catalog.yaml`
- `vibe_governance/resources/templates/*`
- `vibe_governance/resources/scaffold/*`

特点:

- 这是治理内核
- 里面的 `immutable` 规则不能被项目本地 override
- 模板决定最终生成文件长什么样

### 第 2 层: 项目本地真源层

位置:

- `.agents/profile.yaml`
- `.agents/overrides/rules.yaml`
- `.agents/architecture-decisions.yaml`
- `.agents/progress/entries/*`
- `.agents/RULES.md`

特点:

- 这是项目自己的事实层
- 但不是每个文件都会直接参与生成
- 真正会影响渲染的, 主要是结构化文件

特别要注意:

- `.agents/RULES.md` 是解释层, 不是机器强制层
- 需要影响生成时, 要把可执行部分写进 `.agents/overrides/rules.yaml`

### 第 3 层: 生成输出层

位置:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.cursor/`
- `.github/`
- `.opencode/`
- `.agents/PROGRESS.md`

特点:

- 全是结果层
- 原则上不直接手改
- 如果被手改, `validate` 会把它识别成漂移

## 二、当前项目真正实现的“三级优先级同步策略”

很多人会把“三级优先级”理解成一堆抽象概念。

在这个项目里, 它是非常具体的:

1. 上游 canonical 规则和模板决定系统边界
2. 项目本地结构化真源决定当前项目怎么落地
3. 生成层负责把规则分发给各 IDE, 但自己不拥有最终解释权

简单说:

- 第 1 层定天花板
- 第 2 层定项目个性
- 第 3 层只是分发, 不负责拍板

## 三、当前代码里已经落地的同步模式

当前 `profile.yaml` 的 `upstream.sync_strategy` 支持三种值:

- `manual`
- `incremental`
- `full`

但要说清楚:

- 当前默认配置是 `manual`
- 当前 `sync_project()` 真正落地的是“先比较快照, 再决定是否更新快照和 profile 中的上游版本”
- 还没有完整实现复杂的 overlay 合并器

所以这里不要脑补成“已经有完整自动合并系统”。

## 四、冲突处理 SOP

### 场景 1: 生成文件被手工改了

表现:

- `validate` 失败
- 提示 `Managed output drift detected`

处理步骤:

1. 不要继续在生成文件上修
2. 先确认这次改动本来应该落在哪一层
3. 去改 `.agents/` 或 `vibe_governance/resources/`
4. 再跑 `render`

### 场景 2: override 越权

表现:

- `validate` 报 `override_whitelist` 相关错误

处理步骤:

1. 先确认你改的规则是不是允许项目本地覆盖
2. 如果不是, 说明这不应该是项目局部规则
3. 需要考虑把它提升到上游 canonical 层

### 场景 3: immutable 规则被尝试覆盖

表现:

- `validate` 报 immutable 相关错误

处理步骤:

1. 停止本地 override
2. 人工审查是否真的要改治理内核
3. 如果要改, 就去改 `rule-catalog.yaml`, 而不是在项目层偷改

### 场景 4: `sync --dry-run` 报有 `changed_rule_ids`

处理步骤:

1. 先看差异涉及哪些规则
2. 再判断这些规则会不会影响当前项目
3. 人工确认后再执行真正的 `sync`
4. 同步后一定重新 `validate` 和 `render`

## 五、版本迭代治理规范

### 版本号应该放哪里

当前项目至少有三处和版本相关:

- `pyproject.toml`
- `vibe_governance/resources/release-manifest.yaml`
- [CHANGELOG.md](./CHANGELOG.md)

这三处要保持一致。

### 什么情况下应该发新版本

建议发版的情况:

- CLI 行为变了
- 渲染结果格式变了
- 规则目录变了
- 模板变了
- 校验逻辑变了

不一定需要发版的情况:

- 只补说明文档
- 只改项目局部经验
- 只新增未提升为上游规则的 `PROGRESS` 条目

### 发版标准动作

1. 更新 [CHANGELOG.md](./CHANGELOG.md)
2. 更新版本号
3. 跑:

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
python -m unittest discover -s tests -v
```

4. 人工检查根目录说明文档是否需要同步更新
5. 再走 Git 提交流程

### 兼容规则

当前 v1 的兼容底线应该这样守:

- 不轻易改 `.agents/profile.yaml` 的核心字段名
- 不轻易删除已有 `rule_id`
- 生成文件路径不要随便乱换
- 真要改结构, 必须同步更新根目录说明文档和 `CHANGELOG`

## 六、归档要求

项目历史不要只堆在一个文件里。

当前体系的归档规则是:

- 活跃经验写到 `.agents/progress/entries/*`
- 已升级到上游的经验移到 `.agents/progress/archived/*`
- 版本历史写到 [CHANGELOG.md](./CHANGELOG.md)
- 当前索引写到 `.agents/PROGRESS.md`

这就是“开发记录 -> 版本迭代 -> 经验回流 -> 内核升级”的闭环。

## 七、跨账号迁移后的规则同步与权限管理

换账号后最容易出问题的不是“读不懂”, 而是“乱改了不该改的层”。

所以迁移后的权限边界要非常清楚:

### 新账号可以直接改

- 根目录说明文档
- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/overrides/rules.yaml`
- `.agents/architecture-decisions.yaml`
- `.agents/progress/entries/*`

### 新账号不应该直接改

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.cursor/rules/governance.mdc`
- `.github/copilot-instructions.md`
- `.agents/PROGRESS.md`
- `.agents/.managed/*`

### 需要更高审查再改

- `vibe_governance/project.py`
- `vibe_governance/resources/rule-catalog.yaml`
- `vibe_governance/resources/templates/*`
- `pyproject.toml`
- `vibe_governance/resources/release-manifest.yaml`

## 八、把这份文档用起来的正确方式

出问题时别慌, 先套这个顺序:

1. 看 [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md), 判断自己改的是哪一层
2. 看本文件, 判断有没有越权
3. 跑 `validate`
4. 需要时跑 `render`
5. 经验写进 `PROGRESS`
6. 如果已经变成通用规则, 再考虑升级上游

## 继续阅读

- 生命周期操作: [USAGE_GUIDE.md](./USAGE_GUIDE.md)
- 代码入口: [CODE_WALKTHROUGH.md](./CODE_WALKTHROUGH.md)
- 迁移流程: [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)
