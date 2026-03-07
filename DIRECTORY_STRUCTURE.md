# 目录结构全解

这份文档按“谁在读、能不能改、改了有什么后果”的方式讲目录。

## 根目录总览

| 路径 | 主要给谁看 | 能不能直接改 | 作用 |
| --- | --- | --- | --- |
| `README.md` | 人、新账号、新 AI | 可以 | 项目门面和导航 |
| `QUICKSTART.md` | 人、新账号、新 AI | 可以 | 5 分钟接手 |
| `USAGE_GUIDE.md` | 人 | 可以 | 生命周期操作手册 |
| `ARCHITECTURE.md` | 人、新 AI | 可以 | 架构解释 |
| `DIRECTORY_STRUCTURE.md` | 人、新 AI | 可以 | 目录说明 |
| `CODE_WALKTHROUGH.md` | 人、新 AI | 可以 | 代码走读 |
| `GOVERNANCE_RULES.md` | 人、新 AI | 可以 | 治理原则和 SOP |
| `CONTRIBUTING.md` | 人 | 可以 | 迭代流程 |
| `CHANGELOG.md` | 人、新账号 | 可以 | 版本历史 |
| `CONTEXT_MIGRATION.md` | 人、新账号、新 AI | 可以 | 迁移说明 |
| `EMBEDDED_GUIDE.md` | 人 | 可以 | 嵌入式接入说明 |
| `AGENTS.md` | AI / agent | 不建议直接改 | 根级 AI 入口, 生成文件 |
| `CLAUDE.md` | Claude 类 agent | 不建议直接改 | Claude 适配层, 生成文件 |
| `GEMINI.md` | Gemini 类 agent | 不建议直接改 | Gemini 适配层, 生成文件 |
| `pyproject.toml` | Python / 人 | 可以 | 包配置和脚本入口 |
| `.gitignore` | Git / 人 | 可以 | 忽略规则 |

## 重点目录详解

### 1. `.agents/`

这是项目本地真源目录, 也是跨账号迁移时必须完整同步的核心目录。

#### `.agents/profile.yaml`

- 作用: 当前项目事实配置
- 里面有什么: `project_type`、语言、适配器、上游信息、override 白名单、MCP 预留字段
- 能不能改: 可以
- 改完要做什么: `validate` + `render`

#### `.agents/RULES.md`

- 作用: 人类维护的项目偏好和解释说明
- 能不能改: 可以
- 注意: 改这里本身不会自动改变生成结果

#### `.agents/overrides/rules.yaml`

- 作用: 对允许覆盖的规则做结构化 override
- 能不能改: 可以
- 注意: 只有在 `override_whitelist` 里的规则才允许在这里改

#### `.agents/architecture-decisions.yaml`

- 作用: 保存当前项目已经定下来的架构决策
- 能不能改: 可以
- 影响: 会进入生成后的 `.agents/PROGRESS.md`

#### `.agents/PROGRESS.md`

- 作用: 当前项目经验索引
- 能不能改: 不建议直接改
- 原因: 它是生成文件

#### `.agents/progress/entries/YYYY/*.md`

- 作用: 真实经验记录
- 能不能改: 可以
- 什么时候改: 每次有值得保留的经验、坑、决策、版本上下文时

#### `.agents/progress/archived/YYYY/*.md`

- 作用: 已归档的历史经验
- 能不能改: 一般不主动改

#### `.agents/.managed/upstream-rule-catalog.yaml`

- 作用: 记录当前项目认定的上游规则快照
- 能不能改: 不建议手工改
- 通常由谁改: `sync`

#### `.agents/.managed/generated-manifest.yaml`

- 作用: 记录生成文件的清单和 checksum
- 能不能改: 不建议手工改
- 通常由谁改: `render`

### 2. `vibe_governance/`

这是生成器代码和 canonical 资源目录。

#### `vibe_governance/cli.py`

- 作用: 命令行入口
- 负责命令: `init`、`render`、`validate`、`sync`、`progress`

#### `vibe_governance/project.py`

- 作用: 核心逻辑实现
- 这里面负责:
  - 读取 profile 和 override
  - 校验规则
  - 渲染模板
  - 维护 `PROGRESS`
  - 管理同步快照

#### `vibe_governance/resources/rule-catalog.yaml`

- 作用: 上游 canonical 规则目录
- 注意: 这里才是规则本体

#### `vibe_governance/resources/templates/`

- 作用: 各个适配层的模板

#### `vibe_governance/resources/scaffold/`

- 作用: `init` 时使用的初始化骨架

### 3. `tests/`

- 作用: 核心行为测试
- 当前主要验证:
  - 渲染确定性
  - override 合法性
  - immutable 规则拦截
  - `PROGRESS` 滑动窗口
  - 同步报告

### 4. `.github/`

#### `.github/copilot-instructions.md`

- 作用: GitHub Copilot 适配文件
- 来源: `render`

#### `.github/instructions/project-governance.instructions.md`

- 作用: GitHub instructions 适配文件
- 来源: `render`

#### `.github/workflows/release-governance.yml`

- 作用: 校验、渲染、测试、打包发布
- 能不能改: 可以, 但这属于治理引擎层改动

### 5. `.cursor/`

- 作用: Cursor 规则适配目录
- 当前核心文件: `.cursor/rules/governance.mdc`
- 来源: `render`

### 6. `.opencode/`

- 作用: opencode 适配目录
- 当前核心文件: `.opencode/AGENTS.md`
- 来源: `render`

### 7. `.tmp-tests/`

- 作用: 本地测试临时目录
- 需要同步吗: 不需要
- 需要提交吗: 不需要
- 为什么有它: 当前测试在工作区内创建临时项目目录, 避免系统临时目录权限问题

## 哪些文件是跨账号迁移必须同步的

必须同步:

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

可以不同步:

- `.tmp-tests/`
- `__pycache__/`

## 哪些文件最容易改错

### 容易误改 1: `AGENTS.md` / `CLAUDE.md` / `GEMINI.md`

这些都是生成文件。

真正该改的是:

- `.agents/profile.yaml`
- `.agents/overrides/rules.yaml`
- `vibe_governance/resources/templates/*`
- `vibe_governance/resources/rule-catalog.yaml`

### 容易误改 2: `.agents/RULES.md`

这份文件可以改, 但它主要是解释层。

如果你希望规则真的影响生成结果, 还要把可执行部分写到:

- `.agents/overrides/rules.yaml`

## 最后给新接手的人一句话

看目录时只记住这条:

- 根目录说明文档负责“讲清楚”
- `.agents/` 负责“保存事实”
- `vibe_governance/` 负责“驱动生成”
- 各 IDE 目录负责“接收结果”

接下来建议读:

- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [CODE_WALKTHROUGH.md](./CODE_WALKTHROUGH.md)
- [CONTEXT_MIGRATION.md](./CONTEXT_MIGRATION.md)
