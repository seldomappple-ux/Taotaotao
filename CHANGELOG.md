# 版本更新日志

这份文件只记录两类信息:

1. 已经发布的版本级变化
2. 当前工作区相对最近版本的解释性说明

它不负责记流水账。更细的经验和上下文, 在:

- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- `.agents/progress/entries/*`

## 维护规则

每次正式发版时, 至少要同步更新这四处:

- [`pyproject.toml`](./pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)
- [`.agents/profile.yaml`](./.agents/profile.yaml)
- 本文件

同时还要确认:

- 关联的 `PROGRESS` 条目已经写好
- 相关根目录说明文档已经更新
- 新账号接手路径没有被文档改乱

## 版本口径说明

当前仓库只维护一套正式版本号。

- 正式版本号: `1.0.0`
- 机器真源同步点:
  - [`pyproject.toml`](./pyproject.toml) 的 `[project].version`
  - [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml) 的 `version`
  - [`.agents/profile.yaml`](./.agents/profile.yaml) 的 `project_version`
- 展示层可以写 `v1.0.0`
- Git tag 也可以使用 `v1.0.0`

注意:

- `v1.0.0` 只是 `1.0.0` 的展示写法, 不是第二套版本号
- 默认不自动升版, 必须人工改真源后再执行 `render`

## [1.0.0] - 2026-04-01

### 版本定位

这是当前仓库第一次把“通用治理原型”正式收口为“可承接嵌入式治理项目的治理栈”的稳定版本。

这一版同时完成了两件事:

- 完成 `docs/upgrades/v1.0.0-*` 这轮治理升级闭环
- 把仓库包版本、发布清单版本和项目版本统一到同一个 `1.0.0`

### 本版完成内容

- 落地 `project_version` 机器真源, 固定格式为 `major.minor.patch`
- 实现 `init --project-type embedded` 和嵌入式默认骨架
- 扩展 `validate`, 覆盖嵌入式关键文档、关键字段、`M0 / M1 / M2 / M3` 与版本一致性检查
- 完成 `P1` 最小护栏:
  - 版本引用统一到 `project_version`
  - 环境兼容性与 UTF-8 最小护栏落盘
  - 根目录阅读顺序和目录说明收口
  - 提交消息与命名规律约束落盘
- 统一仓库版本口径:
  - `pyproject.toml`
  - `release-manifest.yaml`
  - `.agents/profile.yaml`
  - 受管输出头信息

### 发布锚点

- 正式版本号: `1.0.0`
- 展示标签: `v1.0.0`
- 发布清单: [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)
- 升级总结: [docs/upgrades/v1.0.0-summary.md](./docs/upgrades/v1.0.0-summary.md)
- 实施计划: [docs/upgrades/v1.0.0-plan.md](./docs/upgrades/v1.0.0-plan.md)

## 当前工作区说明

当前工作区相对 `1.0.0` 基线, 已经完成的解释层和治理层增强包括:

1. 完成 `v1.2.0` 治理迭代收口, 建立 `DELTA_DECISIONS.md` 与 `NEXT_ITERATION_BASELINE.md` 两个新入口
2. 补了一轮根目录“物理治理清单”, 明确哪些目录可迁、必须留、应清理
3. 把“每个稳定目录都要有中文说明文件”写进 canonical 规则和初始化骨架
4. 让测试临时目录下沉到 `tests/.tmp-tests/`, 减少根目录噪音
5. 让嵌入式初始化骨架直接生成增量决议与下一轮基线模板

这部分变化属于已完成的治理迭代结果, 但尚未触发新的正式包版本发布, 因此正式版本号仍是 `1.0.0`。

## [0.1.0] - 2026-03-07

### 版本定位

这是当前仓库的第一版治理内核基线版本。

它建立了:

- Python CLI
- `.agents/` 真源骨架
- 多 IDE 适配层生成
- 校验、同步、`PROGRESS` 生命周期基础能力
- 自举式仓库结构

### 为什么会有这个版本

这个版本解决的核心问题是:

- 不再依赖聊天记忆保存项目状态
- 把规则、进度、版本、迁移信息全部落到本地文件
- 让项目在不同 IDE、不同账号、不同 AI 间稳定接力

### 本版本包含的核心内容

#### 新增

- `init / render / validate / sync / progress` 命令集
- [`.agents/profile.yaml`](./.agents/profile.yaml) 项目事实源
- [`.agents/overrides/rules.yaml`](./.agents/overrides/rules.yaml) override 机制
- [`vibe_governance/resources/rule-catalog.yaml`](./vibe_governance/resources/rule-catalog.yaml) canonical 规则目录
- 根级 AI 适配文件生成
- `generated-manifest.yaml` 和 `upstream-rule-catalog.yaml` 两类受管状态
- `PROGRESS` 滑动窗口索引

#### 设计约束

- 不使用 LLM 做规则分发转换
- 生成文件默认不允许手工改
- immutable 规则不能被本地 override
- MCP 只预留字段, 未实现完整嵌入式契约

### Git 信息

- 版本号: `0.1.0`
- 基线 Commit Hash: `df203b9672d47e39fd29926e25dfe5cb2ffbaa91`
- 基线 Commit 标题: `初版_5.4生成`
- 基线提交时间: `2026-03-07T15:42:15+08:00`
