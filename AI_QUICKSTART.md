# AI Quickstart / 给新 AI 的快速启动提示词

这份文件不是给人看的使用手册，而是给你复制到“新 IDE 里的 AI”对话框里的固定提示词。

This file is not a human-facing guide. Copy the prompt below into the AI inside the new IDE.

## 用法 / How To Use

1. 先在本机把 `Taotaotao` 安装成可调用工具。
2. 在新的 IDE 里打开新的项目目录。
3. 把下面整段提示词发给那个 IDE 里的 AI。

## 本机绝对路径 / Local Absolute Path

当前这台机器上的 `Taotaotao` 根目录绝对路径是：

```text
d:\code\VS Code\Taotaotao
```

如果以后这个工具仓移动位置，先更新这里，再继续复用这份提示词。

这里有两个关键约定：

- “当前项目根目录”指的是新 IDE 当前打开的工作区根目录，不是 `Taotaotao` 仓库根目录。
- 当前这台机器上的 `Taotaotao` 根目录已经在上面给出，AI 不应该再向用户索要这条路径，除非这个路径在本机不存在。

## 提示词 / Prompt

```text
你现在接手的是我当前 IDE 打开的本地项目。这个项目使用本机的 Taotaotao 作为本地项目启动器和治理工具。

本机 `Taotaotao` 工具仓绝对路径已经明确给出：
`d:\code\VS Code\Taotaotao`

请严格按下面的顺序工作：

1. 先确认“当前项目根目录”。
   - “当前项目根目录”就是你现在这个 IDE 打开的工作区根目录。
   - 如果你的工具能直接读取当前工作区路径，请先输出这个绝对路径。
   - 如果你无法确认当前路径，先向我确认当前项目根目录，再继续。

2. 先判断当前项目是否已经完成 Taotaotao 初始化。
   判断标准：
   - 如果根目录存在 `START_HERE.md` 和 `.agents/profile.yaml`，说明这个项目已经 bootstrap 过。
   - 如果这两个文件不存在，说明这个项目还没有完成初始化。

3. 如果项目还没有初始化，不要自己凭空创建目录、规则文件或业务骨架。
   - 先向我确认项目类型。
   - 如果我已经明确给出项目类型，并且当前终端可以直接调用 `vibe-governance`，就在“当前项目根目录”执行：
     `vibe-governance bootstrap --type <project_type> --target .`
   - 如果当前终端提示 `vibe-governance` 不存在，不要先来问我 `Taotaotao` 路径，因为路径已经给出。请直接使用下面的 fallback：
     1. 进入 `d:\code\VS Code\Taotaotao`
     2. 执行：
        `python -m vibe_governance bootstrap --type <project_type> --target "<current_project_root_absolute>"`
   - 如果上一步仍然不可用，再执行一次本机安装：
     1. 进入 `d:\code\VS Code\Taotaotao`
     2. 执行：
        `python -m pip install -e .`
     3. 回到当前项目根目录，再执行：
        `vibe-governance bootstrap --type <project_type> --target .`
   - 当前常用类型包括：
     `governance`、`software`、`backend`、`frontend`、`embedded`
   - 只有当 `d:\code\VS Code\Taotaotao` 这个路径本身不存在时，才向我确认新的 `Taotaotao` 绝对路径。

4. 初始化完成后，先阅读当前项目根目录的 `START_HERE.md`。
   不要跳过这一步，也不要一上来就递归扫描整个仓库。

5. 然后严格按 `START_HERE.md` 里规定的顺序继续读取本地文件。
   读取时优先当前项目本地文件，优先级高于生成的适配文件。

6. 如果 `START_HERE.md` 里记录了本机 `Taotaotao` 工具仓路径，只有在你需要理解生成器、模板、治理规则来源时，才回到那个路径下阅读这些文件：
   - `README.md`
   - `QUICKSTART.md`
   - `ARCHITECTURE.md`
   - `DIRECTORY_STRUCTURE.md`
   - `CHANGELOG.md`

   如果 `START_HERE.md` 里还没有这个路径，而你确实需要查看本机 `Taotaotao` 工具仓，请直接使用已经给出的绝对路径：
   `d:\code\VS Code\Taotaotao`

   只有当这个路径在本机不存在时，才向我确认新的绝对路径；在没有拿到明确路径之前，不要自己猜测本机目录。

7. 在开始修改任何文件之前，先输出下面这 5 项：
   0. 你识别到的当前项目根目录绝对路径
   1. 项目定位
   2. 当前规则和红线
   3. 当前版本和最近进展
   4. 如果继续开发，应该改哪一层
   5. 我现在最适合做的下一步

8. 如果需要调整规则，不要直接改生成的适配文件。
   包括但不限于：
   - `AGENTS.md`
   - `CLAUDE.md`
   - `GEMINI.md`
   - `.cursor/`
   - `.github/`
   - `.opencode/`
   正确做法是优先修改当前项目 `.agents/` 下的真源文件，然后按需要执行：
   `vibe-governance render --target .`

9. 除非我明确要求，否则先不要直接写代码，也不要删除文件，更不要做破坏性操作。

10. 你的目标不是自由发挥，而是先利用 Taotaotao 把当前项目带入“有规则、有骨架、有上下文”的工作状态，然后再开始后续开发。
```
