# 架构大白话详解

这份文档专门解释一件事:

为什么这个项目要拆成“根目录说明文档 + `.agents/` 真源 + 生成器 + IDE 适配层”四层。

## 先说结论

这套架构的目标不是“让 AI 更聪明”, 而是“让项目不依赖某一个聊天会话”。

也就是说:

- 换 GPT 账号没关系
- 换 Cursor 账号没关系
- 换设备没关系
- 甚至换一个新的 AI 也没关系

因为项目状态不在聊天里, 而在本地文件里。

## 一、四层结构到底是什么

### 第一层: 根目录解释性文档

这一层就是你现在看到的这些文件, 例如:

- [README.md](./README.md)
- [QUICKSTART.md](./QUICKSTART.md)
- [USAGE_GUIDE.md](./USAGE_GUIDE.md)
- [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

这一层是给人看的。

它的作用不是“驱动生成器”, 而是:

- 让项目维护者看得懂
- 让新账号接手时能快速进入状态
- 让新 AI 先用自然语言理解整个项目, 再去读规则文件

### 第二层: `.agents/` 本地真源层

这是整个项目真正的状态中心。

核心文件有:

- [`.agents/profile.yaml`](./.agents/profile.yaml)
- [`.agents/RULES.md`](./.agents/RULES.md)
- [`.agents/overrides/rules.yaml`](./.agents/overrides/rules.yaml)
- [`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)
- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- `.agents/progress/entries/*`

这层负责保存:

- 项目当前配置
- 项目允许的 override
- 架构决策
- 项目经验和历史上下文

### 第三层: 生成器和 canonical 资源层

这一层在:

- [`vibe_governance/cli.py`](./vibe_governance/cli.py)
- [`vibe_governance/project.py`](./vibe_governance/project.py)
- [`vibe_governance/resources/`](./vibe_governance/resources/)

它的工作是:

1. 读取 `.agents/` 真源
2. 读取上游规则目录和模板
3. 按确定性规则生成适配文件
4. 校验漂移、同步快照、维护进度索引

### 第四层: IDE / Agent 适配层

这一层是生成结果, 例如:

- [AGENTS.md](./AGENTS.md)
- [CLAUDE.md](./CLAUDE.md)
- [GEMINI.md](./GEMINI.md)
- [`.github/copilot-instructions.md`](./.github/copilot-instructions.md)
- [`.cursor/rules/governance.mdc`](./.cursor/rules/governance.mdc)
- [`.opencode/AGENTS.md`](./.opencode/AGENTS.md)

这一层的目标是:

- 让不同 IDE 读到同一套治理思想
- 但不让每个 IDE 都各自维护一份独立规则

## 二、数据流是怎么走的

### 初始化数据流

```text
init
-> 创建 .agents 骨架
-> 写入 profile / RULES / overrides / progress template / upstream snapshot
```

### 渲染数据流

```text
.agents/profile.yaml
+ .agents/overrides/rules.yaml
+ .agents/architecture-decisions.yaml
+ .agents/progress/entries/*
+ vibe_governance/resources/rule-catalog.yaml
+ vibe_governance/resources/templates/*
-> render
-> 根目录和 IDE 适配文件
```

### 校验数据流

```text
真源文件 + 已生成文件 + .agents/.managed/generated-manifest.yaml
-> validate
-> 判断是否有越权 override、无效配置、生成漂移
```

### 同步数据流

```text
当前 rule-catalog.yaml
vs
.agents/.managed/upstream-rule-catalog.yaml
-> sync --dry-run
-> 输出 changed_rule_ids
```

## 三、为什么 `.agents/RULES.md` 不是唯一规则真源

这是很多人第一次接手时最容易误解的地方。

当前实现里:

- `.agents/RULES.md` 是给人看的项目偏好说明
- 真正参与生成和校验的是 `.agents/profile.yaml` 与 `.agents/overrides/rules.yaml`

所以:

- `RULES.md` 负责讲清“为什么”
- `profile.yaml` 和 `overrides/rules.yaml` 负责落地“怎么执行”

这样拆开有个很大的好处:

- 解释不会污染机器结构
- 机器结构不会被自然语言随便写坏

## 四、版本迭代和上下文迁移为什么能闭环

这套设计最关键的能力不是“会生成 Markdown”, 而是“项目状态全在本地”。

它靠下面几样东西闭环:

### 1. 架构决策本地化

架构决策在:

- [`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)

这让新接手的人不用去翻很长的聊天记录找“当时为什么这么设计”。

### 2. 经验记录本地化

经验在:

- `.agents/progress/entries/*`
- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)

这让项目历史不是散在聊天里, 而是变成可搜索、可提升、可归档的文档资产。

### 3. 版本记录本地化

版本现在至少落在:

- [CHANGELOG.md](./CHANGELOG.md)
- [`pyproject.toml`](./pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)

### 4. 同步快照本地化

同步相关的受管状态在:

- [`.agents/.managed/upstream-rule-catalog.yaml`](./.agents/.managed/upstream-rule-catalog.yaml)
- [`.agents/.managed/generated-manifest.yaml`](./.agents/.managed/generated-manifest.yaml)

这两个文件分别解决:

- “我现在认的上游规则基线是什么”
- “我当前生成结果应该长什么样”

## 五、当前 v1 已实现什么, 没实现什么

### 已实现

- 确定性 CLI
- `init / render / validate / sync / progress promote / progress archive`
- 规则目录
- 模板目录
- 根目录和多 IDE 适配输出
- `PROGRESS` 滑动索引
- override whitelist 校验
- immutable 规则拦截

### 还没实现

- 独立的项目类型 overlay 体系
- 真正的嵌入式专属规则包
- MCP 工具契约自动生成
- 自动发布到真实上游地址

所以文档里凡是提到这部分, 都只能写“已预留入口”, 不能写成“已经做完”。

## 六、从架构角度看换账号接手

换账号接手时, 新账号真正要恢复的是这三样:

1. 项目事实
2. 项目历史
3. 项目规则

在这个仓库里, 它们分别落在:

- 项目事实: `.agents/profile.yaml`
- 项目历史: `.agents/progress/*` + [CHANGELOG.md](./CHANGELOG.md)
- 项目规则: `rule-catalog.yaml` + `.agents/overrides/rules.yaml` + 根目录解释文档

所以新账号不需要“继承某段聊天”, 只需要读文件。

## 七、你应该把这份架构文档当成什么

把它当成“总说明书”, 不要当成规则文件。

如果你要真正改行为:

- 改 `.agents/`
- 改 `vibe_governance/`

如果你只是想搞清楚为什么这样设计:

- 先看本文件
- 再看 [CODE_WALKTHROUGH.md](./CODE_WALKTHROUGH.md)
- 再看 [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
