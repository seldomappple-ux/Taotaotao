# 目录结构全解

这份文档只讲两件事：

1. 当前 `Taotaotao` 工具仓里，哪些目录是干什么的。
2. 你在新 IDE 里 `bootstrap` 出来的项目，应该先看哪里、先改哪里。

<<<<<<< HEAD
## 一、根目录稳定保留的 6 个给人看的入口文件

| 文件 | 作用 |
| --- | --- |
| `README.md` | 项目门面和最短导航 |
| `QUICKSTART.md` | 5 分钟看懂仓库和启动新项目 |
| `ARCHITECTURE.md` | 解释它为什么这样设计 |
| `DIRECTORY_STRUCTURE.md` | 解释目录和文件分工 |
| `CHANGELOG.md` | 看版本和最近工作区变化 |
| `TEMPLATES.md` | 模板库入口列表 |

除了这 6 个, 根目录不再继续增加更多给人看的解释文档。
=======
## 1. 当前 `Taotaotao` 工具仓的关键结构

### 根目录 5 个人类入口文件 + 1 个 AI 启动提示词

| 文件 | 作用 |
| --- | --- |
| `README.md` | 项目定位和正确使用方式 |
| `QUICKSTART.md` | 在新 IDE 里如何调用它 |
| `ARCHITECTURE.md` | 为什么用这种分层结构 |
| `DIRECTORY_STRUCTURE.md` | 当前目录职责 |
| `CHANGELOG.md` | 版本与当前工作区变化 |
| `AI_QUICKSTART.md` | 复制给新 IDE 里 AI 的固定启动提示词 |

### 4 个最关键的目录
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a

| 路径 | 作用 | 能不能直接改 |
| --- | --- | --- |
| `.agents/` | 当前治理仓自己的真源 | 可以 |
| `vibe_governance/` | 生成器代码、规则目录、模板 | 可以 |
| `docs/` | 深度资料 | 可以 |
| `references/` | 原始文章和资料快照 | 一般只读 |

### 3 类不要当真源的路径

<<<<<<< HEAD
## 三、根目录里还有 2 个技术清单文件

| 文件 | 作用 |
| --- | --- |
| `.gitignore` | 忽略临时文件和本机噪音 |
| `pyproject.toml` | Python 包和 CLI 的技术清单 |

它们不是入口文档, 但属于仓库稳定组成部分。

## 四、根目录里还可能出现的本机 / 临时目录

这些目录不是治理真源, 也不是人类入口, 但在实际工作区里可能出现:

| 目录 | 性质 | 说明 |
| --- | --- | --- |
| `.claude/` | 本机工具目录 | 当前本机的 Claude 本地设置目录 |
| `.tmp-tests/` | 临时目录 | 测试过程生成的临时目录, 已被 `.gitignore` 忽略 |

其中 `.tmp-tests/` 不应被当成稳定项目结构的一部分; 如果存在, 说明当前工作区残留了本地测试痕迹。

## 五、真正要记住的 6 个目录
=======
| 路径 | 真实定位 | 建议 |
| --- | --- | --- |
| `AGENTS.md` | 根级受管适配文件 | 不直接改 |
| `CLAUDE.md` / `GEMINI.md` | agent 适配文件 | 不直接改 |
| `.cursor/` / `.github/` / `.opencode/` | 适配层输出目录 | 不直接改 |
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a

## 2. 当前工具仓里真正重要的代码和资源

### `vibe_governance/`

这里是程序本体。

重点文件：

- `vibe_governance/cli.py`
- `vibe_governance/project.py`
- `vibe_governance/resources/rule-catalog.yaml`
- `vibe_governance/resources/project-types.yaml`
- `vibe_governance/resources/templates/`

如果你要改命令、改模板、改项目类型、改生成逻辑，主要改这里。

### `.agents/`

这里是当前治理仓自己的本地真源。

<<<<<<< HEAD
- `docs/SOURCE_MATERIALS.md`
- `docs/UPGRADE_FEEDBACK.md` (原始记录池)
- `docs/UPGRADE_SUMMARY.md` (升级总索引)
- `docs/upgrades/vX.Y.Z-summary.md` (每版本独立总结)
- `docs/upgrades/vX.Y.Z-plan.md` (每版本独立实施计划)
- `docs/USAGE_GUIDE.md`
- `docs/GOVERNANCE_RULES.md`
- `docs/CODE_WALKTHROUGH.md`
- `docs/CONTEXT_MIGRATION.md`
- `docs/CONTRIBUTING.md`
- `docs/EMBEDDED_GUIDE.md`
- `docs/DELTA_DECISIONS.md`
- `docs/NEXT_ITERATION_BASELINE.md`
- `docs/ROOT_DIRECTORY_PHYSICAL_GOVERNANCE_CHECKLIST.md`

### 4. `templates/`

这是项目模板库。

当前用于放可复用项目模板的正文内容, 例如:

- `templates/lightweight-comparison-test/`

要特别区分:

- 根目录 `templates/` 是给人读的项目模板库
- `vibe_governance/resources/templates/` 是给生成器读的适配器模板资源

### 5. `references/`

这是原始资料区。

目前放的是最初三篇文章的网页快照。

### 6. `.cursor/` / `.github/` / `.opencode/`

这些是 IDE / agent 适配结果目录。

它们不是规则真源, 而是生成层的输出目标。

## 六、哪些能直接改, 哪些不要直接改

### 可以直接改

- 根目录 6 个入口文档
=======
重点文件：

>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a
- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/overrides/rules.yaml`
- `.agents/architecture-decisions.yaml`
<<<<<<< HEAD
- `.agents/progress/entries/*`
- `templates/*`
- `vibe_governance/` 里的程序代码和资源
=======
- `.agents/progress/entries/`
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a

如果你要改治理仓自己的规则、架构边界或经验沉淀，改这里。

## 3. 新项目 `bootstrap` 后的核心结构

当你在新的 IDE 里进入一个空项目目录后运行：

```bash
vibe-governance bootstrap --type embedded --target .
```

当前目录会直接变成一个可工作的项目骨架。

核心会包括：

```text
当前项目/
├─ START_HERE.md
├─ README.md
├─ AGENTS.md
├─ CLAUDE.md
├─ GEMINI.md
├─ .agents/
├─ .cursor/
├─ .github/
├─ .opencode/
└─ 业务目录骨架...
```

## 4. 新项目里应该先看哪里

在新的 IDE 里，正确顺序是：

1. `START_HERE.md`
2. `README.md`
3. `.agents/profile.yaml`
4. `.agents/RULES.md`
5. `.agents/architecture-decisions.yaml`
6. `.agents/skills/*/SKILL.md`
7. `.agents/PROGRESS.md`
8. 最后才是 `AGENTS.md`、`CLAUDE.md`、`.cursor/`、`.github/`

如果 AI 需要理解“这套工具仓本身”，再去读本机 `Taotaotao` 根目录文档。

## 5. 新项目里哪些能改，哪些别直接改

### 建议直接改的

- `START_HERE.md`
- `README.md`
- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/overrides/rules.yaml`
- `.agents/architecture-decisions.yaml`
- `.agents/skills/*/SKILL.md`
- `.agents/progress/entries/*`
- 业务目录里的代码和文档

### 不建议直接改的

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.cursor/rules/*`
- `.github/copilot-instructions.md`
- `.github/instructions/*`
- `.agents/PROGRESS.md`
- `.agents/.managed/*`

<<<<<<< HEAD
## 七、如果你第一次接手, 只记住这句话
=======
原因只有一条：
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a

- 前者是人工入口、真源和业务内容
- 后者是受管输出

<<<<<<< HEAD
`README -> QUICKSTART -> ARCHITECTURE -> DIRECTORY_STRUCTURE -> CHANGELOG -> TEMPLATES`
=======
## 6. 一句话记住现在的关系
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a

`Taotaotao` 负责当本机工具仓。  
新项目负责当当前工作仓。  
AI 在新 IDE 里先读新项目本地文件，必要时再回看 `Taotaotao`。
