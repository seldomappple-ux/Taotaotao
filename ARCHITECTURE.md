# 架构大白话详解

这份文档不是在重复目录说明, 而是专门讲三件事:

1. 这套仓库为什么存在.
2. 它为什么要拆成“解释层 + 真源层 + 生成层 + 适配层”.
3. 它怎样把“和 AI 的对话”固化成一套可复用、可迁移、可追溯的工程框架.

## 先说结论

这个项目的目标, 不只是“让项目不依赖某一个聊天会话”。

更核心的是:

- 形成一套通行的 AI 协作框架.
- 用固定流程约束项目边界和代码质量.
- 让不同 agent、不同账号、不同 IDE 接手时, 说的是同一种“项目语言”.

换句话说, 它不是在追求“哪家 AI 更聪明”, 而是在追求“无论换哪家 AI, 工作流都不变”。

## 一、这套架构的思想从哪里来

当前仓库的设计直接承接三份原始材料, 资料已经保存在项目内:

- [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)
- [references/original-articles/01-caoxin-vibe-coding.html](./references/original-articles/01-caoxin-vibe-coding.html)
- [references/original-articles/02-caoxin-project-init.html](./references/original-articles/02-caoxin-project-init.html)
- [references/original-articles/03-zhihu-managing-10-claude-code.html](./references/original-articles/03-zhihu-managing-10-claude-code.html)

这三份材料真正影响到本仓库的, 不是表面的工具名字, 而是下面这些稳定思想:

### 1. 铁打的工作流, 流水的 agent

不管你用 Claude、Codex、Copilot、Cursor 还是别的 agent, 项目都应该有稳定入口、稳定规则和稳定记忆。

### 2. 先对齐意图, 再让 AI 动手

原文里反复强调的不是“多给点提示词”, 而是先把目标、边界、验收条件、红线对齐。这个思想在本仓库里对应:

- 根目录解释性文档
- `.agents/RULES.md`
- `.agents/architecture-decisions.yaml`

### 3. AGENTS / RULES / PROGRESS 要分层

统一入口、红线规则、长期记忆不能混成一个大文件。否则会越用越乱。

### 4. 经验必须沉淀到本地

`PROGRESS` 体系的意义不是写日报, 而是把“这次为什么这么做”“踩了什么坑”“后面怎么接”留在项目里, 而不是留在云端聊天窗口里。

### 5. Git、版本、归档、回流要形成闭环

原文的落脚点不是“完成一次对话”, 而是形成能迭代、能升级、能回流的项目治理机制。

### 6. 嵌入式和硬件协同要有单独边界

这部分在原文里被明确提出, 但当前仓库 v1 只预留了入口, 没有伪造成已经完成的能力。这也是为什么 `mcp` 相关字段已经有, 但还没有完整的硬件 overlay。

## 二、这套仓库里的“对话框架”到底是什么

这里说的“对话框架”, 不是某一段聊天模板, 而是任何人或 AI 接手项目时都要经过的固定顺序。

在当前仓库里, 这套顺序大致是:

1. 先读 [README.md](./README.md)、[SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md), 知道项目为什么存在.
2. 再读 [ARCHITECTURE.md](./ARCHITECTURE.md)、[DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md), 知道项目是怎么分层的.
3. 再读 [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md) 和 [`.agents/RULES.md`](./.agents/RULES.md), 知道边界和红线在哪里.
4. 再读 [`.agents/profile.yaml`](./.agents/profile.yaml)、[`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)、[`.agents/PROGRESS.md`](./.agents/PROGRESS.md), 知道当前项目事实和近期状态.
5. 再运行 `validate / render / sync --dry-run`, 确认当前工作区健康.
6. 最后才进入代码修改、文档更新、版本沉淀和经验回流.

这一步非常关键。

它意味着:

- AI 不是直接“看代码就干活”.
- 人也不是“靠记忆口述背景”.
- 项目先通过本地文件完成语义对齐, 再进入执行阶段。

## 三、四层结构到底在分什么

### 第一层: 根目录解释层

这一层就是现在这些给人看的文档, 比如:

- [README.md](./README.md)
- [QUICKSTART.md](./QUICKSTART.md)
- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

这一层不负责驱动程序行为, 它负责的是:

- 给维护者讲清项目到底是什么.
- 给新账号和新 AI 一个统一的入门顺序.
- 把原始设计思想、当前实现边界、迁移方式讲明白.

### 第二层: `.agents/` 真源层

这是项目真正的状态中心。

核心文件包括:

- [`.agents/profile.yaml`](./.agents/profile.yaml)
- [`.agents/RULES.md`](./.agents/RULES.md)
- [`.agents/overrides/rules.yaml`](./.agents/overrides/rules.yaml)
- [`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)
- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- `.agents/progress/entries/*`

这一层保存的是:

- 项目事实
- 可执行的 override
- 架构决策
- 项目长期记忆
- 当前同步与生成状态

### 第三层: 生成器和 canonical 资源层

这一层在:

- [`vibe_governance/cli.py`](./vibe_governance/cli.py)
- [`vibe_governance/project.py`](./vibe_governance/project.py)
- [`vibe_governance/resources/`](./vibe_governance/resources/)

它负责把“结构化真源”变成“不同 IDE 都能读的统一输出”, 并保证这个过程是确定性的。

### 第四层: IDE / Agent 适配层

这一层是最终发给不同工具的受管结果, 比如:

- [AGENTS.md](./AGENTS.md)
- [CLAUDE.md](./CLAUDE.md)
- [GEMINI.md](./GEMINI.md)
- [`.github/copilot-instructions.md`](./.github/copilot-instructions.md)
- [`.cursor/rules/governance.mdc`](./.cursor/rules/governance.mdc)
- [`.opencode/AGENTS.md`](./.opencode/AGENTS.md)

它们的职责很单纯:

- 让不同工具看到同一套治理思想.
- 不让不同工具各自偷偷长出一套新的流程定义.

## 四、为什么 `.agents/RULES.md` 不是唯一规则真源

这是最容易误解的地方。

当前实现里:

- `.agents/RULES.md` 主要负责解释项目偏好和人工规则.
- 真正参与生成和校验的是 [`.agents/profile.yaml`](./.agents/profile.yaml) 和 [`.agents/overrides/rules.yaml`](./.agents/overrides/rules.yaml).

这样拆的好处是:

- 解释和执行分开, 人容易读.
- 结构化配置和自然语言分开, 程序不容易被写坏.
- 后续你要做同步、校验、冲突拦截时, 有机器能判断的真源.

## 五、版本迭代和上下文迁移为什么能闭环

这套架构的关键能力, 不是“会生成几份 Markdown”, 而是“项目状态和经验都能在本地闭环”。

这个闭环由五部分组成:

### 1. 设计背景本地化

原始思想和来源在:

- [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)
- `references/original-articles/`

### 2. 架构决策本地化

当前决策在:

- [`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)

### 3. 经验记录本地化

近期经验和历史记录在:

- `.agents/progress/entries/*`
- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)

### 4. 版本信息本地化

版本基线和版本级历史在:

- [CHANGELOG.md](./CHANGELOG.md)
- [`pyproject.toml`](./pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)

### 5. 同步状态本地化

同步和生成快照在:

- [`.agents/.managed/upstream-rule-catalog.yaml`](./.agents/.managed/upstream-rule-catalog.yaml)
- [`.agents/.managed/generated-manifest.yaml`](./.agents/.managed/generated-manifest.yaml)

所以新账号真正接手的, 不是“某段对话”, 而是:

- 项目为什么这么做
- 项目现在是什么状态
- 项目最近做了什么
- 项目接下来应该怎么继续

## 六、数据流在仓库里怎么走

### 初始化

```text
init
-> 创建 .agents 骨架
-> 写入 profile / RULES / overrides / progress template / upstream snapshot
```

### 渲染

```text
.agents/profile.yaml
+ .agents/overrides/rules.yaml
+ .agents/architecture-decisions.yaml
+ .agents/progress/entries/*
+ vibe_governance/resources/rule-catalog.yaml
+ vibe_governance/resources/templates/*
-> render
-> 生成根目录 AI 文件和 IDE 适配层
```

### 校验

```text
真源文件 + 已生成文件 + .agents/.managed/generated-manifest.yaml
-> validate
-> 判断是否有越权 override、配置错误、生成漂移
```

### 同步

```text
当前 rule-catalog.yaml
vs
.agents/.managed/upstream-rule-catalog.yaml
-> sync --dry-run
-> 输出 changed_rule_ids
```

### 沉淀

```text
开发或文档变更
-> 新增 progress entry
-> 更新 PROGRESS 索引
-> 需要时进入 CHANGELOG / release / upstream 回流
```

## 七、当前 v1 已经做了什么, 还没做什么

### 已实现

- 确定性 CLI
- `init / render / validate / sync / progress promote / progress archive`
- canonical 规则目录和模板目录
- 根目录 AI 文件和多 IDE 适配输出
- `PROGRESS` 滑动索引
- override whitelist 校验
- immutable 规则拦截

### 已预留, 但尚未实现完整能力

- 独立项目类型 overlay 体系
- 真正的嵌入式专属规则包
- MCP 工具契约自动生成
- 完整硬件红线和联调流水线
- 真实上游地址的自动发布

所以当前文档里提到这些部分时, 只能写“已预留入口”, 不能写成“已经做完”。

## 八、读完这份架构文档后, 下一步该看什么

如果你想继续接手:

1. 看 [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md), 搞清楚每个文件能不能直接改.
2. 看 [CODE_WALKTHROUGH.md](./CODE_WALKTHROUGH.md), 理解生成器代码入口.
3. 看 [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md), 理解优先级和冲突 SOP.

如果你想继续演进这套体系:

1. 先回看 [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md), 确认没有偏离最初三篇原文的中心思想.
2. 再看 [CHANGELOG.md](./CHANGELOG.md) 和 [`.agents/PROGRESS.md`](./.agents/PROGRESS.md), 确认当前版本和近期上下文.
