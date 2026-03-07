# 核心代码走读

这份文档是给“想改代码的人”看的。

它不会把每一行代码抄一遍, 只讲最关键的执行路线、函数职责和扩展入口。

## 一、先看入口

当前 CLI 入口在:

- [`vibe_governance/cli.py`](./vibe_governance/cli.py)

你只要记住一个事实:

- `cli.py` 负责接命令
- `project.py` 负责干活

## 二、CLI 支持哪些命令

### `init`

作用:

- 创建 `.agents/` 基础目录
- 写入 profile、RULES、override 骨架、架构决策骨架、progress 模板
- 写入上游规则快照

对应实现:

- `init_project()`

### `render`

作用:

- 读取项目真源
- 渲染根目录和 IDE 适配层
- 生成 manifest

对应实现:

- `render_project()`

### `validate`

作用:

- 校验 profile
- 校验 override
- 校验 progress entry
- 校验生成结果有没有漂移

对应实现:

- `validate_project()`

### `sync`

作用:

- 把当前 `rule-catalog.yaml` 和项目保存的快照做比较
- 输出按 `rule_id` 聚合的差异
- 非 dry-run 时更新快照和 profile 中的上游版本信息

对应实现:

- `sync_project()`

### `progress promote`

作用:

- 把 entry 状态改成 `promotable`
- 顺手重建 `.agents/PROGRESS.md`

对应实现:

- `promote_progress_entry()`

### `progress archive`

作用:

- 把 entry 移到 `archived/`
- 状态改成 `upstreamed`
- 重建 `.agents/PROGRESS.md`

对应实现:

- `archive_progress_entry()`

## 三、`project.py` 的关键模块怎么理解

### 1. 常量区

这里定义了:

- 支持的适配器
- 支持的同步策略
- 支持的文档模式
- `PROGRESS` 状态集合

它的意义是:

- 把“允许什么”放到一处统一管理
- 避免散落在代码里的魔法字符串

### 2. 数据结构区

当前主要用了几个 dataclass:

- `ReleaseManifest`
- `ProgressEntry`
- `ArchitectureDecision`

这些结构的作用是把 YAML / Markdown 解析后的数据变成明确对象, 后续渲染和校验都围绕它们走。

### 3. 文件定位函数

例如:

- `_profile_path()`
- `_rules_path()`
- `_overrides_path()`
- `_progress_entries_dir()`
- `_manifest_path()`

这些函数的价值很朴素:

- 以后目录如果要调整, 改一处比改十几处安全

### 4. 配置读取与校验函数

核心是:

- `_load_profile()`
- `_load_overrides()`
- `_load_decisions()`
- `_validate_profile()`
- `_validate_overrides()`

它们负责把“人写的配置”变成“程序能判断对错的结构”。

最重要的两个约束:

1. `override_whitelist` 之外不允许乱 override
2. `immutable` 规则就算进了 whitelist 也不能改

### 5. `PROGRESS` 处理函数

核心是:

- `_load_entry()`
- `_serialize_entry()`
- `_load_entries()`
- `_render_progress_markdown()`

这部分代码解决的是:

- 经验记录怎么从“零散 Markdown”变成“结构化索引”
- 为什么 `.agents/PROGRESS.md` 可以只保留最近 10 条活跃 entry

这就是版本迭代和上下文迁移能落地的关键之一。

### 6. 规则选择和渲染函数

核心是:

- `_effective_rule_for_adapter()`
- `_rules_for_adapter()`
- `_render_template()`
- `_expected_managed_outputs()`

可以这样理解:

1. 先找出当前 adapter 应该看到哪些规则
2. 再把允许的 override 覆盖进去
3. 最后把规则喂给模板, 生成目标文件

### 7. Manifest 和漂移校验

核心是:

- `_metadata_comment()`
- `_wrap_managed_content()`
- `validate_project()`

它解决的是:

- 生成文件如何带上 checksum
- 怎么知道有人是不是手工改过生成文件

这也是跨账号接手很重要的一层保险:

- 新 AI 拿到仓库后可以先 `validate`
- 一眼判断当前生成层是不是被人手工动过

## 四、如果你想扩展功能, 应该从哪下手

### 场景 1: 新增一个 CLI 子命令

先改:

- [`vibe_governance/cli.py`](./vibe_governance/cli.py)

再改:

- [`vibe_governance/project.py`](./vibe_governance/project.py)

最后补:

- [tests/test_governance.py](./tests/test_governance.py)
- 根目录说明文档

### 场景 2: 新增一个新的规则字段

先改:

- `vibe_governance/resources/rule-catalog.yaml`

如果模板也要显示它, 再改:

- `vibe_governance/resources/templates/*`

如果校验也要管它, 再改:

- `project.py` 里的校验逻辑

### 场景 3: 新增一个新的 IDE 适配器

最少要动这些地方:

1. `KNOWN_ADAPTERS`
2. `_managed_targets()`
3. 新增模板文件
4. 测试
5. 文档

### 场景 4: 补真正的嵌入式 overlay

当前 v1 还没有独立 overlay 系统。

如果你要做, 推荐的切入顺序是:

1. 先在文档里补设计
2. 再设计新的结构化目录
3. 再决定是扩 `profile.yaml`, 还是新增 overlay 目录
4. 最后再改生成器

不要一上来就在模板里硬塞大量嵌入式判断。

## 五、版本迭代相关代码逻辑在哪

### 与版本号直接相关

- [`pyproject.toml`](./pyproject.toml)
- [`vibe_governance/resources/release-manifest.yaml`](./vibe_governance/resources/release-manifest.yaml)

### 与版本历史和经验相关

- `.agents/progress/entries/*`
- [`.agents/PROGRESS.md`](./.agents/PROGRESS.md)
- [CHANGELOG.md](./CHANGELOG.md)

### 与同步基线相关

- [`.agents/.managed/upstream-rule-catalog.yaml`](./.agents/.managed/upstream-rule-catalog.yaml)

### 与当前生成状态相关

- [`.agents/.managed/generated-manifest.yaml`](./.agents/.managed/generated-manifest.yaml)

也就是说:

- 版本本身不是只存在一个文件里
- 它是“发布清单 + 变更历史 + 经验索引 + 当前快照”一起组成的

## 六、新账号接手代码时建议怎么读

推荐顺序:

1. 先看 [ARCHITECTURE.md](./ARCHITECTURE.md)
2. 再看 [`vibe_governance/cli.py`](./vibe_governance/cli.py)
3. 再看 [`vibe_governance/project.py`](./vibe_governance/project.py)
4. 再看 [tests/test_governance.py](./tests/test_governance.py)
5. 最后回来看 [GOVERNANCE_RULES.md](./GOVERNANCE_RULES.md)

这样读不会乱。

## 七、这份代码走读的底线提醒

- 当前项目已经把“解释层”和“执行层”分开了, 改代码时不要再把它们混回去
- 当前项目还没有项目类型 overlay, 文档里提到的扩展方向不等于现成功能
- 想改行为, 一定先确认自己是在改“真源”, 还是在改“生成结果”
