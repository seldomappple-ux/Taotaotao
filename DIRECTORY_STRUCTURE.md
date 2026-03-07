# 目录结构全解

这份文档只讲两件事：

1. 当前 `Taotaotao` 工具仓里，哪些目录是干什么的。
2. 你在新 IDE 里 `bootstrap` 出来的项目，应该先看哪里、先改哪里。

## 1. 当前 `Taotaotao` 工具仓的关键结构

### 根目录 5 个入口文件

| 文件 | 作用 |
| --- | --- |
| `README.md` | 项目定位和正确使用方式 |
| `QUICKSTART.md` | 在新 IDE 里如何调用它 |
| `ARCHITECTURE.md` | 为什么用这种分层结构 |
| `DIRECTORY_STRUCTURE.md` | 当前目录职责 |
| `CHANGELOG.md` | 版本与当前工作区变化 |

### 4 个最关键的目录

| 路径 | 作用 | 能不能直接改 |
| --- | --- | --- |
| `.agents/` | 当前治理仓自己的真源 | 可以 |
| `vibe_governance/` | 生成器代码、规则目录、模板 | 可以 |
| `docs/` | 深度资料 | 可以 |
| `references/` | 原始文章和资料快照 | 一般只读 |

### 3 类不要当真源的路径

| 路径 | 真实定位 | 建议 |
| --- | --- | --- |
| `AGENTS.md` | 根级受管适配文件 | 不直接改 |
| `CLAUDE.md` / `GEMINI.md` | agent 适配文件 | 不直接改 |
| `.cursor/` / `.github/` / `.opencode/` | 适配层输出目录 | 不直接改 |

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

重点文件：

- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/overrides/rules.yaml`
- `.agents/architecture-decisions.yaml`
- `.agents/progress/entries/`

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

原因只有一条：

- 前者是人工入口、真源和业务内容
- 后者是受管输出

## 6. 一句话记住现在的关系

`Taotaotao` 负责当本机工具仓。  
新项目负责当当前工作仓。  
AI 在新 IDE 里先读新项目本地文件，必要时再回看 `Taotaotao`。
