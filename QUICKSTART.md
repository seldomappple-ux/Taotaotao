# 5 分钟快速上手指南

这份文档只做一件事: 让你在最短时间内把当前仓库看懂、校验通过、接手成功。

## 第 0 步: 先知道“跑通”是什么意思

这个项目不是一个 Web 服务, 也不是一个桌面程序。

对它来说, “跑通” 的标准是:

1. 你能在本地成功运行治理 CLI.
2. `validate` 能通过.
3. `render` 能重新生成适配文件.
4. 你知道该去哪里看规则、历史和上下文.

## 第 1 步: 准备环境

确认本机有这些东西:

- Python 3.11+
- `pip`
- `git`

检查命令:

```bash
python --version
pip --version
git --version
```

## 第 2 步: 打开项目根目录

进入当前仓库根目录后, 先看一眼核心入口:

- [README.md](./README.md)
- [AGENTS.md](./AGENTS.md)
- [`.agents/profile.yaml`](./.agents/profile.yaml)

这三处能让你很快知道:

- 这个仓库是什么
- 当前启用了哪些 IDE 适配器
- 当前版本是怎么组织的

## 第 3 步: 跑第一次校验

```bash
python -m vibe_governance validate --target .
```

预期结果:

- 看到 `Validation passed.`

如果失败, 先去看:

- [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
- [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
- [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)

## 第 4 步: 重新生成一次适配层

```bash
python -m vibe_governance render --target .
```

这一步会重新生成这些文件:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.cursor/rules/governance.mdc`
- `.github/copilot-instructions.md`
- `.github/instructions/project-governance.instructions.md`
- `.opencode/AGENTS.md`
- `.agents/PROGRESS.md`

注意:

- 这些文件是“受管生成文件”.
- 不要直接改.
- 真正应该改的是 `.agents/` 里的源文件, 或 `vibe_governance/resources/` 里的 canonical 模板和规则目录.

## 第 5 步: 看一次同步报告

```bash
python -m vibe_governance sync --target . --dry-run --json
```

这一步不会改东西, 只是告诉你:

- 当前工作区保存的上游规则快照
- 和当前代码里的规则目录相比, 有没有 `rule_id` 级别的差异

如果输出是 `clean`, 说明当前快照和规则目录一致。

## 第 6 步: 搞清楚文档分工

你只要记住这一句:

- 根目录说明文档是给人和新接手的 AI 看的.
- `.agents/` 是本地真源.
- 根目录 AI 适配文件和 `.cursor/`、`.github/`、`.opencode/` 是生成结果.
- `vibe_governance/` 是生成器代码和上游资源.

推荐阅读顺序:

1. [ARCHITECTURE.md](./ARCHITECTURE.md)
2. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
3. [USAGE_GUIDE.md](./USAGE_GUIDE.md)
4. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

## 专属章节: 新账号 / 新 AI 无缝接手流程

这是最重要的一段。如果你换了 GPT 账号、换了 Cursor 账号、换了设备, 就按下面做。

### 1. 先把仓库完整同步下来

必须同步这些内容:

- 根目录全部说明文档
- `.agents/`
- `vibe_governance/`
- `tests/`
- `.github/`
- `.cursor/`
- `.opencode/`
- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `pyproject.toml`

### 2. 先读人类说明, 不要一上来就让 AI 猜

按顺序读:

1. [README.md](./README.md)
2. [CHANGELOG.md](./CHANGELOG.md)
3. [ARCHITECTURE.md](./ARCHITECTURE.md)
4. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
5. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

### 3. 再读本地真源

按顺序打开:

1. [`.agents/profile.yaml`](./.agents/profile.yaml)
2. [`.agents/RULES.md`](./.agents/RULES.md)
3. [`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)
4. [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)

### 4. 跑三条命令确认状态

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

### 5. 再让新 AI 读取适配文件

最后再给 AI 看:

- [AGENTS.md](./AGENTS.md)
- [CLAUDE.md](./CLAUDE.md)
- [GEMINI.md](./GEMINI.md)

这样做的原因很简单:

- 先把“人类理解层”补齐
- 再把“机器执行层”挂上去
- 避免新 AI 只盯着一个适配文件, 误判整个仓库的真实状态

## 常见误区

- 误区 1: 直接改 `AGENTS.md`
  实际上应该改 `.agents/` 或 `vibe_governance/resources/`
- 误区 2: 只看聊天记录不看文件
  这个项目就是为“脱离聊天记忆”设计的
- 误区 3: 看到 `RULES.md` 就以为改完自动生效
  `RULES.md` 是人类说明文件, 真正会影响生成结果的是 `.agents/overrides/rules.yaml`

## 接下来去哪里

- 想学完整流程: [USAGE_GUIDE.md](./USAGE_GUIDE.md)
- 想理解项目结构: [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
- 想处理迁移和换账号: [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)
