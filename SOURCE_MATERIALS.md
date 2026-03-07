# 原始资料与思想来源

这份文档只解决一件事:

告诉后来接手的人, 这套仓库最初是从哪三篇文章长出来的, 当前实现到底吸收了哪些思想, 又刻意没有越界到哪些地方。

如果你后续要继续改根目录说明文档、治理规则、项目初始化方式, 建议先读这份文件, 避免越改越偏。

## 一、原文已经保存到项目里了吗

已经保存了。

当前仓库内的归档位置在:

- [references/original-articles/01-caoxin-vibe-coding.html](./references/original-articles/01-caoxin-vibe-coding.html)
- [references/original-articles/02-caoxin-project-init.html](./references/original-articles/02-caoxin-project-init.html)
- [references/original-articles/03-zhihu-managing-10-claude-code.html](./references/original-articles/03-zhihu-managing-10-claude-code.html)

这里保存的是网页快照 HTML 文件, 重点是把原文内容和上下文留在仓库里, 方便后续接手时本地查阅。它们不是生成器的输入, 但属于项目的重要背景资料。

## 二、这三篇原文分别提供了什么

### 1. 《关于 Vibe Coding 的思考与探索》

它给本项目带来的核心点是:

- Vibe Coding 的问题本质上不是模型不够强, 而是缺少工程约束.
- 重点问题包括: 意图对齐、代码一致性、上下文衰减、工程链路复杂度.
- 解决方向是固定工作流: 需求对齐、开发约束、调试验证、上线、复盘沉淀.
- `AGENTS.md`、`RULES.md`、`PROGRESS.md` 应该各司其职.
- 嵌入式 / 软硬件协同场景需要额外 red line、MCP 和 skill 预留。

### 2. 《项目初始化 Prompt》

它给本项目带来的核心点是:

- 项目初始化不能只靠随手一句 Prompt, 要有一套固定骨架.
- Git、文档、代码风格、测试、打包、agent 工作目录都应该在初始化时说清楚.
- 用户文档和开发文档要分离.
- 注释语言、文档语言、项目语言、是否测试、是否打包等项目事实要结构化.

### 3. 《如何有效地给 10 个 Claude Code 打工》

它给本项目带来的核心点是:

- AI 编码效率提升, 靠的是工作流和吞吐量设计, 不是只靠一次对话.
- `CLAUDE.md` 和 `PROGRESS.md` 的价值在于统一入口和长期记忆.
- Plan Mode、任务拆分、统一入口、长期记忆这些机制, 才是多 agent 协作可持续的基础.

## 三、当前仓库真正吸收了哪些中心思想

下面这些是已经落地到当前实现里的部分:

### 1. 固定工作流, 不绑定单一 agent

当前仓库用的是:

- `.agents/` 保存真源
- `vibe_governance` 做确定性生成
- `AGENTS.md / CLAUDE.md / GEMINI.md / .cursor / .github / .opencode` 做薄适配

这正对应“铁打的工作流, 流水的 agent”。

### 2. 先把项目事实和边界结构化

当前仓库把这些事实放进了 [`.agents/profile.yaml`](./.agents/profile.yaml):

- 项目类型
- 文档模式
- 注释语言
- 启用的适配器
- 上游信息
- override 白名单
- MCP 预留配置

这正对应初始化 Prompt 里“项目初始化时就把规则和配置说清楚”的思路。

### 3. 用 `PROGRESS` 做长期记忆, 不是靠聊天记忆

当前仓库有:

- `.agents/progress/entries/*`
- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- `progress promote / archive`

这正对应原文里对长期记忆、上下文压缩、经验沉淀的强调。

### 4. 让规则治理可校验、可同步、可追溯

当前仓库已经落地:

- `render`
- `validate`
- `sync`
- override whitelist
- immutable 规则拦截
- generated manifest
- upstream snapshot

这正对应“不要让 AI 自己长出一堆不可控规则变体”的治理要求。

### 5. 让版本和经验形成闭环

当前仓库把版本相关信息拆到了:

- [CHANGELOG.md](./CHANGELOG.md)
- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- [`pyproject.toml`](./pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)

这正对应“开发记录 -> 版本迭代 -> 经验回流 -> 内核升级”的闭环方向。

## 四、当前仓库刻意没有假装实现的部分

下面这些方向是原文明确提到、但当前 v1 只做了预留没有做满的:

- 独立的项目类型 overlay 体系
- 嵌入式专属规则包
- MCP 工具契约的自动生成
- 完整的硬件协同 red line
- 多 worktree 并行 agent 工作中心

所以后续你在写文档或扩展代码时, 要坚持一个原则:

- 已经做了的, 才写成“已实现”.
- 只是预留了入口的, 只能写成“已预留”.

## 五、后续什么时候必须回来看这份资料

下面这些场景, 建议先回看本文件和三篇原文快照:

1. 你准备重写项目初始化方式.
2. 你准备调整根目录解释文档的整体结构.
3. 你准备把嵌入式 / MCP 能力推进到 Phase 2.
4. 你准备引入新的 IDE 适配器或新的工作流约束.
5. 你发现仓库开始重新依赖“聊天口述背景”了.

## 六、读完这份文件后建议怎么继续

推荐顺序:

1. [ARCHITECTURE.md](./ARCHITECTURE.md)
2. [QUICKSTART.md](./QUICKSTART.md)
3. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
4. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
