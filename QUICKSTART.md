# 5 分钟快速上手指南

这份文档是给第一次接手仓库的人写的。

不管你是新维护者、新账号, 还是一个全新的 AI 实例, 做完这 5 分钟流程后, 你至少应该达成四件事:

1. 知道这个仓库到底在解决什么问题.
2. 能在本地跑通 `validate / render / sync --dry-run`.
3. 知道哪些文件是事实真源, 哪些文件不能直接改.
4. 知道下一步该去读哪份文档继续接手.

## 先记住一句话

这个仓库的“跑通”, 不是某个服务启动成功, 而是治理链路能闭环:

`读说明 -> 读真源 -> validate -> render -> sync -> 继续开发或接手`

## 第 1 步: 先确认环境

本机至少要有:

- Python 3.11+
- `pip`
- `git`

检查命令:

```bash
python --version
pip --version
git --version
```

如果这一步过不了, 先不要往下走。这个仓库的所有后续动作都建立在本地 Python CLI 可运行之上。

## 第 2 步: 先用 1 分钟看懂仓库是什么

不要一上来就读代码。先看这三个文件:

1. [README.md](./README.md)
2. [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)
3. [`.agents/profile.yaml`](./.agents/profile.yaml)

你要从这三处搞清楚三件事:

- 这个仓库不是业务项目, 而是治理内核和自举示例仓.
- 它的设计直接承接了最初那三篇 Vibe Coding 原文.
- 当前项目启用了哪些适配器、采用什么文档模式、认定的上游版本是什么.

## 第 3 步: 跑第一次健康检查

在项目根目录运行:

```bash
python -m vibe_governance validate --target .
```

预期结果:

- 命令成功结束.
- 输出里能看到 `Validation passed.`.

这一步的目的不是“试试看”, 而是先判断当前仓库是不是一个健康的、可继续接手的状态。

如果失败, 优先去看:

1. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
2. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
3. [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)

## 第 4 步: 重新生成一次适配层

```bash
python -m vibe_governance render --target .
```

这一步会重建当前受管输出, 包括:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.cursor/rules/governance.mdc`
- `.github/copilot-instructions.md`
- `.github/instructions/project-governance.instructions.md`
- `.opencode/AGENTS.md`
- `.agents/PROGRESS.md`

你要从这一步建立一个正确认知:

- 根目录 AI 文件、`.cursor/`、`.github/`、`.opencode/` 是生成结果.
- 真正该改的是 `.agents/` 里的源文件, 或 `vibe_governance/resources/` 里的 canonical 规则与模板.
- 如果你习惯直接改 `AGENTS.md`, 这个仓库会越来越乱。

## 第 5 步: 看当前和上游快照是否一致

```bash
python -m vibe_governance sync --target . --dry-run --json
```

这一步不会直接改文件。它只回答一个问题:

- 当前工作区认定的上游规则快照, 和现在的规则目录相比, 有没有 `rule_id` 级差异.

如果输出是 `clean`, 说明当前快照和本地规则目录一致。

如果不是 `clean`, 不要急着覆盖。先去看 [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md) 里的同步和冲突 SOP。

## 第 6 步: 进入“可接手”状态

做到前 5 步之后, 你已经不算“刚拿到仓库”了, 而是进入了“可以继续接手”的状态。接下来按这个顺序读:

1. [ARCHITECTURE.md](./ARCHITECTURE.md): 先理解这套治理框架为什么存在.
2. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md): 再理解每个目录该给谁读、能不能改.
3. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md): 再理解优先级、红线和同步方式.
4. [CHANGELOG.md](./CHANGELOG.md): 再看当前版本和最近的工作区变化.
5. [`.agents/RULES.md`](./.agents/RULES.md)、[`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)、[`.agents/PROGRESS.md`](./.agents/PROGRESS.md): 最后看当前项目偏好、架构决策和近期状态.

## 新账号 / 新 AI 的无缝接手流程

如果你换了 GPT 账号、换了 IDE 账号, 或者直接换了一台设备, 就按这个顺序做:

1. 先完整同步仓库, 不要只拷代码, 忘了 `.agents/`、`references/` 和根目录说明文档.
2. 先读 [README.md](./README.md)、[SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)、[ARCHITECTURE.md](./ARCHITECTURE.md), 不要让新 AI 一上来就猜.
3. 再让新 AI 读取 [`.agents/profile.yaml`](./.agents/profile.yaml)、[`.agents/RULES.md`](./.agents/RULES.md)、[`.agents/PROGRESS.md`](./.agents/PROGRESS.md).
4. 最后才让它看 [`AGENTS.md`](./AGENTS.md)、[`CLAUDE.md`](./CLAUDE.md)、[`GEMINI.md`](./GEMINI.md) 这些适配层结果.

这样做的原因很简单:

- 先把“项目语义”和“设计背景”对齐.
- 再把“机器执行规则”挂上去.
- 避免新 AI 只看一个适配文件, 就误判整个仓库的真实边界.

## 最容易踩的三个坑

### 坑 1: 把生成文件当真源改

不要直接改:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.cursor/rules/governance.mdc`
- `.github/copilot-instructions.md`

要改就回到:

- [`.agents/profile.yaml`](./.agents/profile.yaml)
- [`.agents/overrides/rules.yaml`](./.agents/overrides/rules.yaml)
- [`vibe_governance/resources/rule-catalog.yaml`](./vibe_governance/resources/rule-catalog.yaml)
- [`vibe_governance/resources/templates/`](./vibe_governance/resources/templates/)

### 坑 2: 只看聊天, 不看仓库里的资料

这个项目本来就是为了摆脱聊天记忆依赖才设计的。

如果你跳过 [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)、[ARCHITECTURE.md](./ARCHITECTURE.md)、[`.agents/PROGRESS.md`](./.agents/PROGRESS.md), 很容易把本项目的治理边界理解错。

### 坑 3: 以为 `RULES.md` 一改就自动生效

`.agents/RULES.md` 主要是解释层。

真正影响生成和校验的, 还是 [`.agents/profile.yaml`](./.agents/profile.yaml) 和 [`.agents/overrides/rules.yaml`](./.agents/overrides/rules.yaml)。

## 5 分钟之后该看哪里

- 想理解为什么这套东西要这样拆: [ARCHITECTURE.md](./ARCHITECTURE.md)
- 想理解每个目录能不能改: [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
- 想按完整生命周期操作: [USAGE_GUIDE.md](./USAGE_GUIDE.md)
- 想处理迁移和换账号: [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)
