# 5 分钟快速上手

这份文档只回答一个问题：

我在新的 IDE 里开一个新项目后，应该怎么调用 `Taotaotao`，让 AI 进入正确工作状态？

## 第 1 步：先把 `Taotaotao` 装成你本机的工具

这一步通常只做一次。

在 `Taotaotao` 根目录执行：

```bash
cd "d:\code\VS Code\Taotaotao"
python -m pip install -e .
```

安装完成后，你在任意终端里都可以直接用：

```bash
vibe-governance
```

## 第 2 步：在新的 IDE 里创建空项目目录

例如你在新的 IDE 里新建并打开：

```text
D:\work\my-esp32-project
```

注意，这里应该是一个新的、基本空白的项目目录。  
允许已经存在 `.git`、`.vscode`、`.idea` 这类元数据目录，但不要先放业务文件进去。

## 第 3 步：在新的 IDE 终端里直接落骨架

进入那个新项目目录后，执行：

```bash
vibe-governance bootstrap --type embedded --target .
```

如果是纯软件项目：

```bash
vibe-governance bootstrap --type software --target .
```

如果是后端项目：

```bash
vibe-governance bootstrap --type backend --target .
```

这一步会直接在“当前新项目根目录”生成：

- `START_HERE.md`
- `README.md`
- `.agents/`
- `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`
- 对应项目类型的业务目录骨架
- 本地 `skills`

## 第 4 步：让新 IDE 里的 AI 先读本地入口

不要让 AI 自己扫仓库。

直接把这段话发给 AI：

```text
请先阅读 START_HERE.md，然后严格按里面的本地读取顺序读取文件，再开始工作。先不要修改任何文件，先输出：
1. 项目定位
2. 当前规则和红线
3. 当前版本和最近进展
4. 如果继续开发，应该改哪一层
5. 我现在最适合做的下一步
```

如果你不想每次手工组织这段话，直接复制根目录的 [`AI_QUICKSTART.md`](./AI_QUICKSTART.md) 给 AI 即可。

## 第 5 步：如果 AI 需要理解启动器本身

新项目生成出来的 `START_HERE.md` 里，会记录本机 `Taotaotao` 工具仓路径。

如果 AI 需要理解“这套生成器本身为什么这样设计”，再让它去读那个路径下的：

1. `README.md`
2. `QUICKSTART.md`
3. `ARCHITECTURE.md`

但日常业务开发，仍然以“当前新项目根目录”和“当前新项目 `.agents/` 真源”为主。

## 第 6 步：开始写代码前先补两件事

建议先补：

- `.agents/RULES.md`
- `.agents/architecture-decisions.yaml`

尤其是嵌入式项目，第一批就该补：

- 硬件红线
- 烧录边界
- 串口参数
- 联调纪律

## 第 7 步：之后最常用的命令

在新项目里，最常用的是：

```bash
vibe-governance validate --target .
vibe-governance render --target .
vibe-governance sync --target . --dry-run
```

## 你只要记住这一条线

正确顺序是：

`先安装 Taotaotao -> 新 IDE 打开空项目目录 -> bootstrap 到当前目录 -> AI 先读 START_HERE -> 再开始写代码`
