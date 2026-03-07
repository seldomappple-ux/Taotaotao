# 核心代码走读

这份文档是给准备改生成器的人看的。

它不会逐行解释代码, 只讲三件事:

1. 真实执行链路是什么
2. 关键函数各管什么
3. 如果你想扩展功能, 应该从哪一层下手

## 一、先用一句话看懂代码结构

当前实现可以直接理解成:

- [`vibe_governance/cli.py`](../vibe_governance/cli.py) 负责接命令
- [`vibe_governance/project.py`](../vibe_governance/project.py) 负责真正干活

所以读代码时, 最简单的顺序就是:

1. 先看 `cli.py`
2. 再看 `project.py`
3. 最后看 `tests/test_governance.py`

## 二、CLI 到底在做什么

`cli.py` 本身很薄, 它的职责主要有两个:

1. 用 `argparse` 定义命令和参数
2. 把子命令分发给 `project.py` 里的公开函数

当前公开出来的动作只有这些:

- `bootstrap`
- `init`
- `render`
- `validate`
- `smoke`
- `sync`
- `progress promote`
- `progress archive`

其中要特别分清:

- `bootstrap` 是当前推荐给使用者的项目创建入口
- `init` 是更底层的骨架初始化动作, 现在主要给内部流程和维护者理解用

也就是说, 这个文件本身几乎不承载业务逻辑。它更像是一个稳定入口。

## 三、真实执行链路怎么走

如果把整个生成器压缩成一条线, 当前代码的核心流程是:

```text
CLI 参数
-> 读取 `.agents/` 真源和 canonical 资源
-> 校验 profile / overrides / progress
-> 按 adapter 解析有效规则
-> 用模板生成受管输出
-> 写 manifest 和 PROGRESS 索引
-> 需要时比较上游快照
```

这条线非常重要, 因为它解释了为什么这个仓库能做到:

- 先有真源
- 再有生成结果
- 最后才有适配层分发

## 四、`project.py` 应该怎么读

`project.py` 虽然比 `cli.py` 大很多, 但你可以按下面几个区块去理解。

### 1. 常量和基础数据结构

这里最先出现的是:

- `KNOWN_ADAPTERS`
- `SYNC_STRATEGIES`
- `DOC_MODES`
- `ACTIVE_PROGRESS_STATUSES`
- `ALL_PROGRESS_STATUSES`

以及三个 dataclass:

- `ReleaseManifest`
- `ProgressEntry`
- `ArchitectureDecision`

这部分的作用很直接:

- 把允许值集中定义
- 把 YAML / Markdown 解析结果变成更明确的结构

### 2. 路径和资源读取函数

这部分是 `_profile_path()`、`_rules_path()`、`_overrides_path()`、`_managed_dir()` 这一类函数, 再加上 `_resource_text()`、`_load_resource_yaml()`、`_read_scaffold()`。

它们负责做两件事:

- 统一定位本地真源和受管文件的位置
- 统一读取 `resources/` 里的规则、模板和 scaffold

这层虽然看起来朴素, 但它决定了整个项目的目录约定。

### 3. 真源读取和校验

这部分核心函数是:

- `_load_profile()`
- `_load_overrides()`
- `_load_decisions()`
- `_validate_profile()`
- `_validate_overrides()`

这里的关键约束有两个:

1. `override_whitelist` 之外的规则不能乱 override
2. `immutable` 规则不能被项目层覆盖

这部分就是治理红线在代码里的第一道落点。

### 4. `PROGRESS` 读取、序列化和索引生成

这部分核心函数是:

- `_load_entry()`
- `_serialize_entry()`
- `_load_entries()`
- `_render_progress_markdown()`

它解决的是:

- 如何把零散的 entry 文件变成结构化对象
- 如何只把最近 10 条活跃 entry 放进 [`.agents/PROGRESS.md`](../.agents/PROGRESS.md)
- 如何把更早或已沉淀的记录继续留在磁盘上可检索

这部分代码直接对应了“长期记忆本地化”和“滑动窗口索引”的设计。

### 5. 规则选择和模板渲染

这部分核心函数是:

- `_effective_rule_for_adapter()`
- `_rules_for_adapter()`
- `_render_template()`
- `_expected_managed_outputs()`

它的真实工作顺序可以理解成:

1. 从 `rule-catalog.yaml` 里找出当前 adapter 相关的规则
2. 把允许的项目级 override 合并进去
3. 根据 `doc_mode`、`mcp.enabled` 等条件筛选规则
4. 把结果喂给模板
5. 得到每个受管输出的预期内容和 checksum

### 6. 受管输出包装和漂移检测

这部分关键函数是:

- `_metadata_comment()`
- `_wrap_managed_content()`
- `validate_project()`

它负责把这些信息写进每个受管文件头部:

- 工具版本
- 上游仓地址
- 上游版本
- 发布时间
- checksum

然后在 `validate_project()` 里, 再用这些预期输出来检查当前磁盘内容是否漂移。

### 7. 公开动作函数

这部分是你在 `cli.py` 里最终会调到的函数:

- `bootstrap_project()`
- `init_project()`
- `render_project()`
- `validate_project()`
- `smoke_test()`
- `sync_project()`
- `promote_progress_entry()`
- `archive_progress_entry()`

它们分别对应仓库的生命周期动作:

- 当前目录 bootstrap
- 低层初始化
- 生成
- 校验
- 冒烟测试
- 同步
- 经验提升
- 经验归档

## 五、几个最关键的执行细节

### 1. `render_project()` 先校验, 再生成

当前实现里, `render_project()` 会先调用:

- `validate_project(target, check_generated=False)`

这意味着:

- 真源本身如果有问题, 根本不会进入渲染阶段
- 但渲染前不会因为“当前生成文件已经漂移”而卡死

### 2. `validate_project()` 会检查两类问题

第一类是源文件问题:

- profile 字段缺失
- override 越权
- progress entry 格式错误

第二类是生成层问题:

- manifest 与预期输出集合不一致
- 受管文件内容和当前应生成内容不一致

### 3. `sync_project()` 现在做的是快照同步, 不是复杂合并

当前 `sync_project()` 的工作重点是:

- 比较当前 `rule-catalog.yaml` 和 `.agents/.managed/upstream-rule-catalog.yaml`
- 输出 `changed_rule_ids`
- 非 dry-run 时更新快照和 `profile.yaml` 里的上游版本信息

它还没有实现复杂 overlay 合并器。写文档或扩展功能时要守住这个边界。

### 4. `progress promote` 和 `progress archive` 都会触发重新渲染

这是因为:

- [`.agents/PROGRESS.md`](../.agents/PROGRESS.md) 是生成文件
- entry 状态一变, 滑动索引也必须跟着变

### 5. `bootstrap_project()` 才是当前真实的项目启动入口

当前最新流程里, 新项目应该这样启动:

1. 先把 `Taotaotao` 安装到本机
2. 在新的 IDE 里打开一个空项目目录
3. 在那个目录里运行 `vibe-governance bootstrap --type ... --target .`

代码上, `bootstrap_project()` 现在会负责:

- 检查目标目录是否足够干净
- 调用 `init_project()` 建立 `.agents/` 基础骨架
- 写入项目类型配置
- 追加项目类型规则和架构决策
- 创建业务目录骨架
- 创建本地 `skills`
- 生成项目级 `START_HERE.md` 和 `README.md`
- 最后触发 `render_project()`

## 六、如果你想扩展功能, 应该从哪下手

### 场景 1: 新增一个 CLI 子命令

先改:

- [`vibe_governance/cli.py`](../vibe_governance/cli.py)

再改:

- [`vibe_governance/project.py`](../vibe_governance/project.py)

最后补:

- [tests/test_governance.py](../tests/test_governance.py)
- 根目录说明文档

### 场景 2: 新增一个规则字段或新 `rule_id`

先改:

- [`vibe_governance/resources/rule-catalog.yaml`](../vibe_governance/resources/rule-catalog.yaml)

如有需要, 再改:

- [`vibe_governance/resources/templates/`](../vibe_governance/resources/templates/)
- [`vibe_governance/project.py`](../vibe_governance/project.py)

### 场景 3: 新增一个 IDE 适配器

当前最少要同时改这些地方:

1. `KNOWN_ADAPTERS`
2. `_managed_targets()`
3. 对应模板文件
4. 测试
5. 说明文档

### 场景 4: 推进嵌入式 / MCP 到下一阶段

当前 v1 还没有独立 overlay 体系。

更稳的切入顺序是:

1. 先把设计和边界写进文档
2. 再补结构化 schema 或目录
3. 再决定是扩 `profile.yaml`, 还是新增 overlay 层
4. 最后再改渲染和校验逻辑

不要直接在模板里堆大量嵌入式判断。

## 七、版本、经验和快照相关代码在哪里

### 与版本号直接相关

- [`pyproject.toml`](../pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](../vibe_governance/resources/release-manifest.yaml)

### 与经验记录相关

- `.agents/progress/entries/*`
- [`.agents/PROGRESS.md`](../.agents/PROGRESS.md)
- [CHANGELOG.md](../CHANGELOG.md)

### 与同步基线相关

- [`.agents/.managed/upstream-rule-catalog.yaml`](../.agents/.managed/upstream-rule-catalog.yaml)

### 与当前生成状态相关

- [`.agents/.managed/generated-manifest.yaml`](../.agents/.managed/generated-manifest.yaml)

也就是说, 版本和状态并不是只放在一个文件里, 而是由发布清单、经验索引、版本说明和同步快照一起组成。

## 八、新账号接手代码时, 推荐怎么读

推荐顺序:

1. [ARCHITECTURE.md](../ARCHITECTURE.md)
2. [`vibe_governance/cli.py`](../vibe_governance/cli.py)
3. [`vibe_governance/project.py`](../vibe_governance/project.py)
4. [tests/test_governance.py](../tests/test_governance.py)
5. [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

## 九、最后的底线提醒

- 这个项目已经把解释层和执行层分开了, 不要再把它们混回去
- 当前项目还没有真正的项目类型 overlay, 文档里提到的方向不等于现成功能
- 想改行为时, 先确认自己在改真源、canonical 资源, 还是生成结果

