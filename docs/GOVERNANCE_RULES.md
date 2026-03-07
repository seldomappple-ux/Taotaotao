# 治理规则详解

这份文档不重复抄规则原文, 它只解释一件事:

这套仓库到底靠什么维持稳定, 遇到冲突时到底按什么顺序处理。

如果你只记一句话, 就记这个:

> 先看来源和边界, 再改真源; 先看同步报告, 再做升级; 先写本地经验, 再回流上游规则。

## 一、治理原则先对齐

这套治理体系不是拍脑袋写出来的, 它直接承接了最初三篇原文里的中心思想。建议先看:

- [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)

落到当前仓库里, 核心原则一共六条。

### 1. 工作流优先于单个 agent

AI 可以换, IDE 可以换, 但治理流程不能每次跟着换。

### 2. 意图对齐优先于快速动手

接手项目时, 先读解释文档和 `.agents/` 真源, 再让 agent 开始修改。

### 3. 解释层和执行层必须分开

根目录说明文档、`.agents/RULES.md`、结构化配置和生成输出不能混成一层。

### 4. 长期记忆必须本地化

经验先进 `.agents/progress/entries/*`, 再进入 `PROGRESS` 索引、`CHANGELOG` 或上游规则。

### 5. 生成层不拥有最终解释权

`AGENTS.md`、`CLAUDE.md`、`.cursor/`、`.github/` 这些都是分发结果, 不是最终拍板层。

### 6. 高风险规则必须有红线

当前代码已经用 `immutable` 规则和 override whitelist 做了第一层约束。后续嵌入式硬件红线也会继续沿这条路扩展。

## 二、这套仓库真正的治理分层

当前实现可以非常明确地分成三层。

### 第 1 层: 上游 canonical 层

位置:

- [`vibe_governance/resources/rule-catalog.yaml`](../vibe_governance/resources/rule-catalog.yaml)
- [`vibe_governance/resources/templates/`](../vibe_governance/resources/templates/)
- [`vibe_governance/resources/scaffold/`](../vibe_governance/resources/scaffold/)

这层负责:

- 定义通用 `rule_id`
- 定义模板输出结构
- 定义初始化骨架

这层的特点是:

- `immutable` 规则不能被项目本地 override
- 一旦这里变了, 往往会影响多个项目或多个适配器

### 第 2 层: 项目本地真源层

位置:

- [`.agents/profile.yaml`](../.agents/profile.yaml)
- [`.agents/overrides/rules.yaml`](../.agents/overrides/rules.yaml)
- [`.agents/architecture-decisions.yaml`](../.agents/architecture-decisions.yaml)
- [`.agents/RULES.md`](../.agents/RULES.md)
- `.agents/progress/entries/*`

这层负责:

- 记录项目事实
- 承载允许的局部 override
- 保存架构决策
- 保存项目经验

要特别记住:

- `.agents/RULES.md` 是解释层.
- 真正参与渲染和校验的核心真源, 主要是结构化文件.

### 第 3 层: 生成输出层

位置:

- [AGENTS.md](../AGENTS.md)
- [CLAUDE.md](../CLAUDE.md)
- [GEMINI.md](../GEMINI.md)
- `.cursor/`
- `.github/`
- `.opencode/`
- [`.agents/PROGRESS.md`](../.agents/PROGRESS.md)

这层负责:

- 把统一规则发给不同 IDE 和 agent
- 生成当前 `PROGRESS` 滑动索引

这层的纪律很简单:

- 原则上不直接手改
- 一旦手改, `validate` 就应该把它识别成漂移

## 三、当前仓库里的“三级优先级同步策略”到底是什么

很多人听到“三级优先级”会觉得很抽象, 但在这个仓库里它是很实在的:

1. 上游 canonical 层决定系统边界.
2. 项目本地真源层决定当前项目怎么落地.
3. 生成输出层只负责分发, 不负责重新解释规则.

翻成大白话就是:

- 第 1 层定规则天花板
- 第 2 层定项目个性和当前状态
- 第 3 层只负责把结果送到各 IDE

## 四、同步策略和当前实现边界

`profile.yaml` 的 `upstream.sync_strategy` 现在支持:

- `manual`
- `incremental`
- `full`

但必须说清楚当前代码真正做了什么:

- 默认配置仍然是 `manual`
- `sync_project()` 现在做的是“当前规则目录 vs 本地快照”的比较
- 非 dry-run 时, 它会更新 `.agents/.managed/upstream-rule-catalog.yaml` 和 `profile.yaml` 中的上游版本信息
- 当前还没有完整 overlay 合并器

所以不要把当前 `sync` 想成已经有复杂自动合并能力。

## 五、红线、权限和不可覆盖规则

### 1. override whitelist 是第一层权限边界

项目本地只有在 [`.agents/profile.yaml`](../.agents/profile.yaml) 的 `override_whitelist` 里声明过的 `rule_id`, 才能放进 [`.agents/overrides/rules.yaml`](../.agents/overrides/rules.yaml)。

### 2. immutable 规则是第二层红线

只要某条规则在 `rule-catalog.yaml` 里标记成 `immutable: true`, 项目本地就不能覆盖。

### 3. 生成输出层默认是只读层

下面这些都不应该直接改:

- [AGENTS.md](../AGENTS.md)
- [CLAUDE.md](../CLAUDE.md)
- [GEMINI.md](../GEMINI.md)
- `.cursor/rules/governance.mdc`
- `.github/copilot-instructions.md`
- [`.agents/PROGRESS.md`](../.agents/PROGRESS.md)
- `.agents/.managed/*`

## 六、冲突处理 SOP

这部分建议直接当故障手册用。

### 场景 1: 生成文件被手工改了

表现:

- `validate` 失败
- 提示 `Managed output drift detected`

处理顺序:

1. 先停, 不要继续在生成文件上补丁式修.
2. 判断这次改动本来应该落在哪一层.
3. 去改 `.agents/` 或 `vibe_governance/resources/`.
4. 重新运行 `render`.

### 场景 2: 本地 override 越权

表现:

- `validate` 报 whitelist 相关错误

处理顺序:

1. 先确认你改的 `rule_id` 是否允许项目本地覆盖.
2. 如果不允许, 说明这不该是项目局部规则.
3. 评估是否应该提升到 canonical 层.

### 场景 3: immutable 规则被尝试覆盖

表现:

- `validate` 报 immutable 相关错误

处理顺序:

1. 停止本地 override.
2. 人工确认是否真的要改治理内核.
3. 如果要改, 去改 `rule-catalog.yaml`, 不要在项目层偷改.

### 场景 4: `sync --dry-run` 报有 `changed_rule_ids`

处理顺序:

1. 先看变的是哪些 `rule_id`.
2. 再判断这些规则是否会影响当前项目.
3. 人工确认后再执行真正的 `sync`.
4. 同步后重新 `validate` 和 `render`.

## 七、版本迭代治理规范

### 版本信息现在放在哪里

当前项目至少有三处和版本直接相关:

- [`pyproject.toml`](../pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](../vibe_governance/resources/release-manifest.yaml)
- [CHANGELOG.md](../CHANGELOG.md)

### 什么情况下应该认真考虑发版

- CLI 行为变了
- 规则目录变了
- 模板输出格式变了
- 校验逻辑变了
- 同步逻辑变了

### 什么情况下通常不必马上发版

- 只补说明文档
- 只新增局部经验
- 只改还没有提升为通用规则的项目本地内容

### 发版前的标准动作

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
python -m unittest discover -s tests -v
```

然后人工确认:

- [CHANGELOG.md](../CHANGELOG.md) 是否更新
- 根目录说明文档是否需要同步更新
- [`.agents/PROGRESS.md`](../.agents/PROGRESS.md) 是否能追溯这次变化

### 当前 v1 的兼容底线

- 不轻易改 `profile.yaml` 的核心字段名
- 不轻易删除已有 `rule_id`
- 不随便改生成文件路径
- 真要改结构, 必须同步更新文档和 `CHANGELOG`

## 八、归档和经验回流怎么打通

当前体系的归档规则是:

- 活跃经验写到 `.agents/progress/entries/*`
- 已沉淀到上游的经验移到 `.agents/progress/archived/*`
- 当前索引写到 [`.agents/PROGRESS.md`](../.agents/PROGRESS.md)
- 版本级变化写到 [CHANGELOG.md](../CHANGELOG.md)

这就是“开发记录 -> 版本迭代 -> 经验回流 -> 内核升级”的闭环。

## 九、跨账号接手后的权限边界

换账号后最容易出的问题不是“读不懂”, 而是“把层级改乱了”。

### 可以直接改的

- 根目录说明文档
- [`.agents/profile.yaml`](../.agents/profile.yaml)
- [`.agents/RULES.md`](../.agents/RULES.md)
- [`.agents/overrides/rules.yaml`](../.agents/overrides/rules.yaml)
- [`.agents/architecture-decisions.yaml`](../.agents/architecture-decisions.yaml)
- `.agents/progress/entries/*`

### 不应该直接改的

- [AGENTS.md](../AGENTS.md)
- [CLAUDE.md](../CLAUDE.md)
- [GEMINI.md](../GEMINI.md)
- `.cursor/rules/governance.mdc`
- `.github/copilot-instructions.md`
- [`.agents/PROGRESS.md`](../.agents/PROGRESS.md)
- `.agents/.managed/*`

### 需要更高审查的

- [`vibe_governance/project.py`](../vibe_governance/project.py)
- [`vibe_governance/resources/rule-catalog.yaml`](../vibe_governance/resources/rule-catalog.yaml)
- [`vibe_governance/resources/templates/`](../vibe_governance/resources/templates/)
- [`pyproject.toml`](../pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](../vibe_governance/resources/release-manifest.yaml)

## 十、实际操作时的最短判断顺序

出问题时就按这个顺序来:

1. 看 [DIRECTORY_STRUCTURE.md](../DIRECTORY_STRUCTURE.md), 先判断自己碰的是哪一层.
2. 看本文件, 先判断有没有越权或踩红线.
3. 跑 `validate`.
4. 需要时跑 `render`.
5. 把经验写进 `PROGRESS`.
6. 确定它真的是通用能力后, 再考虑回流上游.

