# 轻量通用模板

这个模板用于搭建“根目录干净、治理轻量、不预设阶段目录”的通用轻量项目。

它适合:

- 需要一个可快速起步的轻量项目骨架
- 业务目录尚未稳定, 不希望一开始就预设阶段结构
- 希望保留最小治理和最小 AI 入口层, 但不想引入多 IDE 扩展层

## 我该用哪个模板

- 如果项目需要多阶段、多方案、横向对比和统一测试记录规则:
  - 使用 [`lightweight-comparison-test`](../lightweight-comparison-test/README.md)
- 如果项目只是想要一个根目录干净、轻量治理、不预设阶段目录的通用骨架:
  - 使用当前“轻量通用模板”

## 轻量特征

这里的“轻量”指的是:

- 根目录尽量保持简洁
- 只保留少量稳定入口和必要目录
- 治理信息集中到 `.agents/`
- 业务目录按项目实际需要逐步长出来

它追求的是先把项目落稳, 再决定是否继续加层, 而不是一开始就铺满适配输出和复杂规则。

## 推荐目录骨架

### 最小人工根结构

推荐把根目录收敛到这类最小人工结构:

```text
.
|-- .agents/
|-- docs/
|-- <业务目录, 按项目自定>
`-- README.md
```

业务目录可以按项目需要逐步补充, 例如:

- `data/`
- `materials/`
- `notes/`
- `prompts/`
- `assets/`
- `workflows/`

### 主体结构

推荐至少保留这 3 层:

1. 业务内容层
2. 说明与索引层
3. 轻量治理层

说明:

- 业务内容层承接项目自己的资料、流程文件或资产目录
- `docs/` 用于放结构说明、索引和长期说明文档
- `.agents/` 用于放规则、接手信息和过程记录

## 最小治理骨架

这个模板虽然不预设阶段目录, 但如果你要引入“轻量治理”, 也不应该把 `.agents/` 写成只有目录名的空壳。

推荐至少补齐下面这组最小治理骨架:

```text
.agents/
|-- README_中文.md
|-- profile.yaml
|-- RULES.md
|-- architecture-decisions.yaml
|-- overrides/
|   |-- README_中文.md
|   `-- rules.yaml
|-- PROGRESS.md
`-- progress/
    |-- README_中文.md
    |-- ENTRY_TEMPLATE.md
    `-- entries/
        |-- README_中文.md
        `-- YYYY/
```

它们分别承担:

- `profile.yaml`: 项目画像与治理配置真源
- `RULES.md`: 稳定规则与接手约束
- `architecture-decisions.yaml`: 稳定架构决策沉淀
- `overrides/rules.yaml`: 本地规则补丁
- `PROGRESS.md`: 当前活跃事项的滑动索引
- `progress/ENTRY_TEMPLATE.md`: 新增条目的统一写法
- `progress/entries/YYYY/`: 按年份沉淀原始记录

如果项目声称已经接入治理体系, 但没有 `profile.yaml`、`overrides/rules.yaml` 或 `progress/entries/` 这些关键层, 往往说明它只带入了“目录概念”, 还没有真正带入治理闭环。

## 治理触发记录规则

模板里的“自动记录”默认按“触发即记”理解, 即事件一发生就必须落到稳定位置, 即便当前还是人工执行。

- 用户提出 bug、回归、行为异常、规则冲突时, 至少补一条 `.agents/progress/entries/YYYY/` 条目
- 运行 `render`、`validate`、结构迁移、批量改名或规则调整时, 也应补一条 progress entry
- `.agents/PROGRESS.md` 只是滑动索引, 真正的原始记录应写在 `.agents/progress/entries/YYYY/`
- 新增 entry 后应运行 `render`, 让索引自动收进 `.agents/PROGRESS.md`

## 可选的最小多 agent 入口层

纯轻量默认结构下, 不预设任何生成式 agent 文件。

如果项目后续引入 `vibe-governance` 或其他治理生成工具, 可以只保留最小多 agent 入口层:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`

要特别说明:

- 在 `Taotaotao` 仓里, `AGENTS.md` 是受管生成文件
- 在一般轻量项目里, 如果没有引入生成式治理工具, 就不应默认把这些文件理解为现成生成物
- 即便不引入 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`, 只要选择保留 `.agents/` 作为治理层, 也应把 `progress/entries/` 这一组最小骨架补齐
- 这组文件属于“多 agent 最小适配层”, 不等于多 IDE 扩展层

## 默认不带的扩展层

下面这些目录默认不是轻量通用模板的组成部分:

- `.cursor/`
- `.github/`
- `.opencode/`
- 其他多 IDE 统一适配输出目录

它们不是错误项, 也不是禁止项, 但默认不带。

如果项目只需要最小多 agent 入口层, 优先单独引入 `AGENTS.md` / `CLAUDE.md` / `GEMINI.md`, 不要把它和“默认不带的多 IDE 扩展层”混为一类。

## 何时保持轻量, 何时加层

判断时只问一个问题:

- 是否真的需要更多 IDE / agent 的统一分发?
  - 否: 保持当前轻量结构
  - 是: 再考虑引入更重的适配层或治理层

## 不迁移的内容边界

这个模板默认不预设:

- `01/02/03` 阶段目录
- 多方案对比结构
- 统一测试记录规则
- 特定业务术语
- 特定行业案例

换句话说, 它保留的是“轻量起步方法”, 不是某一类业务项目的专用骨架。
