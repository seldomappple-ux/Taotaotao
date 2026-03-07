# 5 分钟快速上手

这份文档只回答两个问题:

1. 我怎么快速看懂当前仓库
2. 我怎么把这套东西用到一个新项目里

## 一、先看懂当前仓库

先做这 3 件事:

### 1. 读 3 个文件

按顺序读:

1. [README.md](./README.md)
2. [ARCHITECTURE.md](./ARCHITECTURE.md)
3. [DIRECTORY_STRUCTURE.md](./DIRECTORY_STRUCTURE.md)

读完后你至少要知道:

- 这个仓库是治理内核, 不是业务项目
- `.agents/` 是真源
- 根目录的 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 是生成结果

### 2. 跑 3 条命令

```bash
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
```

如果这 3 条命令都正常, 说明当前仓库可以继续接手。

### 3. 知道深度资料在哪里

如果你还要继续深挖, 再去看 [`docs/`](./docs/) 里的文档, 不要一开始就被十几份根目录文件淹没。

## 二、如果你要在新 IDE 里开一个新项目

当前版本能帮你搭的是“治理骨架”, 不是“完整业务目录骨架”。

最短路径是:

### 1. 把治理内核带进新项目

最少带这两样:

- `vibe_governance/`
- `pyproject.toml`

### 2. 初始化治理骨架

在新项目根目录运行:

```bash
python -m vibe_governance init --target .
```

### 3. 补 3 个核心真源

优先改:

- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/architecture-decisions.yaml`

### 4. 重新生成适配层

```bash
python -m vibe_governance render --target .
python -m vibe_governance validate --target .
```

### 5. 再开始建业务目录

比如你自己再建:

- `src/`
- `firmware/`
- `backend/`
- `frontend/`

当前 v1 还没有把“业务目录模板化”做完, 所以这一步仍然需要你自己定。

## 三、现在先别纠结的事

当前阶段你先不要试图一口气理解所有深度文档。先只记住:

- 根目录 5 个文件是入口
- `docs/` 是深度资料
- `.agents/` 是真源
- `vibe_governance/` 是程序本体

做到这一步, 你的阅读路径就不会乱。
