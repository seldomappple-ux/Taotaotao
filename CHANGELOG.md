# 版本更新日志

这份文件只做两件事：

1. 记录正式版本。
2. 解释当前工作区相对最近版本的关键变化。

更细的上下文不写在这里，而是在：

- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- `.agents/progress/entries/`

## 当前工作区相对 `0.1.0` 的关键变化

当前工作区相对 `0.1.0`，最重要的变化有 5 类。

### 1. 根目录人读入口文档被收敛到 5 个

根目录现在只保留：

- `README.md`
- `QUICKSTART.md`
- `ARCHITECTURE.md`
- `DIRECTORY_STRUCTURE.md`
- `CHANGELOG.md`

其余深度说明下沉到了 `docs/`。

### 2. 三篇原始文章已经入仓归档

原始资料已经进入本地仓库：

- [`docs/SOURCE_MATERIALS.md`](./docs/SOURCE_MATERIALS.md)
- [`references/original-articles/`](./references/original-articles/)

### 3. 标准化为 `bootstrap`，在新 IDE 的当前目录直接落骨架

这次是当前工作区最关键的一次修正。

现在支持：

```bash
vibe-governance bootstrap --type embedded --target .
```

这更符合真实使用方式：

- 先把 `Taotaotao` 安装到本机
- 再在新的 IDE 和新的项目目录里直接调用它

### 4. 新项目入口模板已经反向指向本机 `Taotaotao`

新生成项目里的 `START_HERE.md` 和项目 `README.md`，现在会记录本机治理仓来源路径。

这样新 IDE 里的 AI 先读当前项目本地文件；如果需要理解启动器本身，再回看本机 `Taotaotao`。

## 当前工作区对应的本地记录

- `20260307-2`: 补齐根目录解释性文档
- `20260307-3`: 重构 onboarding 文档并归档原始文章
- `20260307-4`: 统一剩余人读文档并补充适配层 onboarding 规则
- `20260308-1`: 根目录人读文档瘦身为 5 个入口文件
- `20260308-3`: 新增 `smoke` 一键冒烟测试
- `20260308-5`: 修正为“新 IDE 当前目录 bootstrap”的主流程
- `20260308-6`: 删除重复旧路径，只保留 `bootstrap` 作为项目创建入口

后续如果这些变化进入正式版本，应在新的版本段落里正式归档。

## [0.1.0] - 2026-03-07

### 版本定位

这是当前仓库的第一版治理内核基线版本。

它建立了：

- Python CLI
- `.agents/` 真源骨架
- 多 IDE / 多 agent 适配层生成
- `validate / render / sync / progress` 基础能力
- `PROGRESS` 滑动窗口索引
- 自举式治理仓结构

### 这个版本解决了什么

这个版本要解决的核心问题是：

- 不再依赖聊天记忆保存项目状态
- 把规则、进度、版本、迁移信息落到本地文件
- 让项目在不同 IDE、不同账号、不同 AI 之间稳定接手

### 核心内容

新增：

- `init / render / validate / sync / progress` 命令组
- [`.agents/profile.yaml`](./.agents/profile.yaml)
- [`.agents/overrides/rules.yaml`](./.agents/overrides/rules.yaml)
- [`vibe_governance/resources/rule-catalog.yaml`](./vibe_governance/resources/rule-catalog.yaml)
- 根级 AI 适配文件生成
- `generated-manifest.yaml`
- `upstream-rule-catalog.yaml`
- `PROGRESS` 生命周期基础能力

设计约束：

- 不用 LLM 做规则翻译层
- 生成文件默认不允许手工改
- immutable 规则不能被本地 override
- MCP 只预留 schema，不实现完整嵌入式协议栈

### Git 基线

- 版本号: `0.1.0`
- 基线 Commit Hash: `df203b9672d47e39fd29926e25dfe5cb2ffbaa91`
- 基线 Commit 标题: `初版_5.4生成`
- 基线提交时间: `2026-03-07T15:42:15+08:00`
