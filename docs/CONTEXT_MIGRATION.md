# 上下文迁移专属指南

这份文档就是专门解决一个问题:

换账号、换 AI 实例、换设备之后, 怎么保证项目上下文不丢、接手不断线。

## 一、先把迁移目标说清楚

这个项目从设计上就假设:

- 云端聊天历史可能随时丢
- 账号可能随时换
- IDE 和设备也可能随时换

所以“迁移成功”的标准不是你记住了上一段对话, 而是:

1. 新环境拿到了完整仓库
2. 新账号能从本地文件恢复设计背景、当前状态和最近历史
3. 新 AI 能按同一套顺序接手项目

## 二、迁移时必须同步哪些文件

### 必须同步

- 根目录全部说明文档
- `references/`
- `.agents/`
- `vibe_governance/`
- `tests/`
- `.github/`
- `.cursor/`
- `.opencode/`
- [AGENTS.md](../AGENTS.md)
- [CLAUDE.md](../CLAUDE.md)
- [GEMINI.md](../GEMINI.md)
- [`pyproject.toml`](../pyproject.toml)
- `.gitignore`

### 不需要同步

- `.tmp-tests/`
- `__pycache__/`

## 三、完整迁移流程

### 第 1 步: 把仓库完整带到新环境

推荐方式:

- 直接 `git clone`
- 或完整拷贝整个仓库目录

最忌讳的做法:

- 只拷代码, 不拷 `.agents/`
- 只拷根目录文档, 不拷 `references/`
- 只拷业务文件, 不拷生成器

这样做会直接把项目语义和长期记忆切断。

### 第 2 步: 先确认新环境可运行

```bash
python --version
pip --version
git --version
```

### 第 3 步: 先读本地资料, 不要先让 AI 猜

建议顺序:

1. [README.md](../README.md)
2. [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)
3. [CHANGELOG.md](../CHANGELOG.md)
4. [ARCHITECTURE.md](../ARCHITECTURE.md)
5. [DIRECTORY_STRUCTURE.md](../DIRECTORY_STRUCTURE.md)
6. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

这一步的目的不是“补知识”, 而是先把项目为什么存在、当前边界在哪里、现在到了哪个版本阶段对齐。

### 第 4 步: 再读本地真源

按这个顺序打开:

1. [`.agents/profile.yaml`](../.agents/profile.yaml)
2. [`.agents/RULES.md`](../.agents/RULES.md)
3. [`.agents/architecture-decisions.yaml`](../.agents/architecture-decisions.yaml)
4. [`.agents/PROGRESS.md`](../.agents/PROGRESS.md)

如果要继续接手最近工作, 还应继续看最近的 `.agents/progress/entries/*`。

### 第 5 步: 跑标准接手校验

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

这一步是迁移的“验收动作”。如果这三条命令都过了, 才能算真正进入可接手状态。

### 第 6 步: 最后再让新 AI 读取适配层

给新 AI 或新账号看的顺序建议是:

1. 先读根目录说明文档
2. 再读 `.agents/` 真源
3. 最后再看 [AGENTS.md](../AGENTS.md)、[CLAUDE.md](../CLAUDE.md)、[GEMINI.md](../GEMINI.md)

原因很简单:

- 先对齐项目语义和设计背景
- 再对齐机器执行规则

## 四、迁移成功后的自检清单

- [ ] `validate` 通过
- [ ] `render` 成功执行
- [ ] `sync --dry-run --json` 能正常输出
- [ ] 能从 [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md) 说清项目最初来源
- [ ] 能从 [`.agents/profile.yaml`](../.agents/profile.yaml) 看懂当前项目事实
- [ ] 能从 [`.agents/PROGRESS.md`](../.agents/PROGRESS.md) 找到最近状态
- [ ] 能说清哪些文件能改, 哪些不能直接改

## 五、常见问题和处理方式

### 问题 1: 新 AI 一上来就去改 `AGENTS.md`

处理方式:

1. 先让它读 [DIRECTORY_STRUCTURE.md](../DIRECTORY_STRUCTURE.md)
2. 再让它读 [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)
3. 明确告诉它先改 `.agents/` 或 canonical 资源, 不直接改生成文件

### 问题 2: 新账号不知道项目为什么会长成这样

处理方式:

1. 先读 [SOURCE_MATERIALS.md](./SOURCE_MATERIALS.md)
2. 再读 [ARCHITECTURE.md](../ARCHITECTURE.md)
3. 再看 `references/original-articles/`

### 问题 3: 新账号不知道当前版本是什么

处理方式:

- 看 [CHANGELOG.md](../CHANGELOG.md)
- 看 [`pyproject.toml`](../pyproject.toml)
- 看 [`vibe_governance/resources/release-manifest.yaml`](../vibe_governance/resources/release-manifest.yaml)

### 问题 4: 新设备看到的生成文件和旧设备不一样

处理方式:

1. 先跑 `validate`
2. 再跑 `render`
3. 再检查 [`.agents/.managed/generated-manifest.yaml`](../.agents/.managed/generated-manifest.yaml)

### 问题 5: 只拷了代码, 没拷 `.agents/` 或 `references/`

处理方式:

- 这不算迁移成功
- 必须重新同步完整仓库

### 问题 6: 新账号没有任何对话历史

处理方式:

- 这本来就是设计目标
- 只要仓库内文件完整, 接手就不应依赖聊天上下文

## 六、迁移后如果继续开发, 第一步该做什么

1. 先确认最近的 `PROGRESS` 和 `CHANGELOG` 已读完
2. 必要时新增一条 `PROGRESS` 记录, 说明是谁在什么环境接手
3. 如果只是继续当前版本工作, 不用急着改版本号
4. 真正有通用价值的变化, 再考虑补 `CHANGELOG` 或升级上游规则

## 七、把这份文档当成什么用

把它当成“断线重连手册”。

只要你发现:

- 账号换了
- IDE 换了
- 设备换了
- AI 换了

就回来按这份文档走一遍。

