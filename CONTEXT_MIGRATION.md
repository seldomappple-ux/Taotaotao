# 上下文迁移专属指南

这份文档就是专门解决一个问题:

换账号、换 AI 实例、换设备之后, 怎么保证项目上下文 0 丢失。

## 一、先说原则

这个项目默认假设:

- 任何云端聊天历史都可能丢
- 任何账号都可能切换
- 任何 IDE 都可能换

所以项目上下文必须 100% 固化在本地文件。

## 二、迁移时必须同步的文件清单

### 必须同步

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
- `.gitignore`

### 不需要同步

- `.tmp-tests/`
- `__pycache__/`

## 三、完整迁移流程

### 第 1 步: 把仓库完整拿到新环境

推荐方式:

- 直接 `git clone`
- 或者完整拷贝整个仓库目录

最忌讳的做法:

- 只拷贝代码文件, 不拷贝 `.agents/`
- 只拷贝根目录文档, 不拷贝生成器

这样会直接断上下文。

### 第 2 步: 新环境先装基础依赖

```bash
python --version
pip --version
git --version
```

### 第 3 步: 先读文档, 不要先问 AI

推荐阅读顺序:

1. [README.md](./README.md)
2. [CHANGELOG.md](./CHANGELOG.md)
3. [ARCHITECTURE.md](./ARCHITECTURE.md)
4. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
5. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

### 第 4 步: 再读本地真源

按这个顺序打开:

1. [`.agents/profile.yaml`](./.agents/profile.yaml)
2. [`.agents/RULES.md`](./.agents/RULES.md)
3. [`.agents/architecture-decisions.yaml`](./.agents/architecture-decisions.yaml)
4. [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)

### 第 5 步: 跑接手校验

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

### 第 6 步: 最后再把 AI 接进来

给新 AI 或新账号看的顺序建议是:

1. 先喂根目录说明文档
2. 再喂 `.agents/` 真源
3. 最后才看 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`

原因很简单:

- 先把项目语义对齐
- 再把机器规则对齐

## 四、新账号接手后的验证步骤

你可以按这个检查清单一条条过:

- [ ] `validate` 通过
- [ ] `render` 成功执行
- [ ] `sync --dry-run` 能输出 JSON 报告
- [ ] 能看懂 `README` 到 `GOVERNANCE_RULES` 这组文档
- [ ] 能从 `.agents/profile.yaml` 看懂当前项目配置
- [ ] 能从 `.agents/PROGRESS.md` 找到最近的项目状态
- [ ] 能知道哪些文件能改, 哪些不能直接改

## 五、常见问题和解决方案

### 问题 1: 新 AI 一上来就去改 `AGENTS.md`

解决:

- 告诉它先读 [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)
- 再读 [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

### 问题 2: 新账号不知道当前版本是什么

解决:

- 看 [CHANGELOG.md](./CHANGELOG.md)
- 看 `pyproject.toml`
- 看 `vibe_governance/resources/release-manifest.yaml`

### 问题 3: 新设备上看到的生成文件和旧设备不一样

解决:

1. 先跑 `validate`
2. 再跑 `render`
3. 再检查 `.agents/.managed/generated-manifest.yaml`

### 问题 4: 只拷了代码没拷 `.agents/`

解决:

- 这不算接手成功
- 必须重新同步完整仓库

### 问题 5: 新账号没有任何对话历史

解决:

- 这本来就是设计目标
- 只要本地文件完整, 就不应该依赖聊天上下文

## 六、迁移后如果继续开发, 应该先做什么

1. 新增一条 `PROGRESS` 记录, 说明是谁在什么环境接手
2. 如果只是继续当前版本工作, 不用急着改版本号
3. 真正有通用价值的变化, 再考虑补 `CHANGELOG`

## 七、这份文档的真正用途

把它当成“断线重连手册”。

只要你发现:

- 账号换了
- IDE 换了
- 设备换了
- AI 换了

就回来按这份文档走一遍。
