# 目录结构

这份文档只做一件事:

让你一眼看懂“哪里是入口, 哪里是真源, 哪里是程序本体, 哪里是生成结果”。

## 一、根目录现在只保留 5 个给人看的入口文件

| 文件 | 作用 |
| --- | --- |
| `README.md` | 项目门面和最短导航 |
| `QUICKSTART.md` | 5 分钟看懂仓库和启动新项目 |
| `ARCHITECTURE.md` | 解释它为什么这样设计 |
| `DIRECTORY_STRUCTURE.md` | 解释目录和文件分工 |
| `CHANGELOG.md` | 看版本和最近工作区变化 |

除了这 5 个, 根目录不再放太多给人看的解释文档。

## 二、还有 3 个根目录文件是给 AI / IDE 读的

| 文件 | 作用 | 能不能直接改 |
| --- | --- | --- |
| `AGENTS.md` | 根级 AI 入口 | 不建议直接改 |
| `CLAUDE.md` | Claude 适配层 | 不建议直接改 |
| `GEMINI.md` | Gemini 适配层 | 不建议直接改 |

它们都是受管生成文件。

## 三、真正要记住的 5 个目录

### 1. `.agents/`

这是项目真源。

最重要的文件在这里:

- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/overrides/rules.yaml`
- `.agents/architecture-decisions.yaml`
- `.agents/progress/entries/*`

### 2. `vibe_governance/`

这是程序本体。

核心入口:

- `vibe_governance/cli.py`
- `vibe_governance/project.py`

### 3. `docs/`

这是深度资料区。

根目录之外的说明文档都下沉到这里了, 包括:

- `docs/SOURCE_MATERIALS.md`
- `docs/UPGRADE_FEEDBACK.md`
- `docs/UPGRADE_SUMMARY.md`
- `docs/USAGE_GUIDE.md`
- `docs/GOVERNANCE_RULES.md`
- `docs/CODE_WALKTHROUGH.md`
- `docs/CONTEXT_MIGRATION.md`
- `docs/CONTRIBUTING.md`
- `docs/EMBEDDED_GUIDE.md`

### 4. `references/`

这是原始资料区。

目前放的是最初三篇文章的网页快照。

### 5. `.cursor/` / `.github/` / `.opencode/`

这些是 IDE / agent 适配结果目录。

它们不是规则真源, 而是生成层的输出目标。

## 四、哪些能直接改, 哪些不要直接改

### 可以直接改

- 根目录 5 个入口文档
- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/overrides/rules.yaml`
- `.agents/architecture-decisions.yaml`
- `.agents/progress/entries/*`
- `vibe_governance/` 里的程序代码和资源

### 不建议直接改

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.cursor/rules/*`
- `.github/copilot-instructions.md`
- `.agents/PROGRESS.md`
- `.agents/.managed/*`

## 五、如果你第一次接手, 只记住这句话

阅读顺序是:

`README -> QUICKSTART -> ARCHITECTURE -> DIRECTORY_STRUCTURE -> CHANGELOG`

动手顺序是:

`根目录入口 -> .agents 真源 -> vibe_governance -> 生成结果`
