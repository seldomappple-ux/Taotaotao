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

另外, 当前仓库也开始承载可复用项目模板索引, 可以从根目录的 [`TEMPLATES.md`](./TEMPLATES.md) 进入模板库。

## 二、如果你要在新 IDE 里开一个新项目

当前推荐路径是: 先把 `Taotaotao` 安装成一次性的本机工具, 再在新 IDE 打开的空项目目录里运行 `bootstrap`。

最短路径是:

### 1. 先安装本机工具

这一步通常只做一次:

```bash
cd "d:\code\VS Code\Taotaotao"
python -m pip install -e .
```

### 2. 在新 IDE 里打开空项目目录

例如:

```text
D:\work\my-project
```

这个目录可以已经有 `.git`、`.vscode`、`.idea` 这类元数据, 但不要先放业务文件。

### 3. 在当前目录直接 bootstrap

```bash
vibe-governance bootstrap --type software --target .
```

嵌入式项目用:

```bash
vibe-governance bootstrap --type embedded --target .
```

如果 `vibe-governance` 还不在 PATH, 可以从本仓库路径直接调用:

```bash
cd "d:\code\VS Code\Taotaotao"
python -m vibe_governance bootstrap --type embedded --target "D:\work\my-project"
```

### 4. 先读生成的 START_HERE

`bootstrap` 会生成:

- `START_HERE.md`
- `README.md`
- `.agents/`
- `AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 等适配层
- 对应项目类型的初始目录
- `.agents/skills/` 本地技能文件

新项目里的 AI 应该先读 `START_HERE.md`, 再按它指定的顺序读取 `.agents/` 真源。

### 5. 补 3 个核心真源

优先改:

- `.agents/profile.yaml`
- `.agents/RULES.md`
- `.agents/architecture-decisions.yaml`

### 6. 重新生成适配层

```bash
vibe-governance render --target .
vibe-governance validate --target .
```

`init` 命令仍然保留, 但它是底层兼容入口。新项目默认不要从 `init` 开始, 除非你明确只需要 `.agents` 治理骨架。

## 三、现在先别纠结的事

当前阶段你先不要试图一口气理解所有深度文档。先只记住:

- 根目录 6 个文件是入口
- `docs/` 是深度资料
- `templates/` 是项目模板库
- `.agents/` 是真源
- `vibe_governance/` 是程序本体

做到这一步, 你的阅读路径就不会乱。
