# 迁移指南

本文档说明如何将使用旧版本 vibe-governance 的项目升级到新版本。

## 从 v0.1.0 升级到 v1.0.0

### 破坏性变更

v1.0.0 引入了以下必填字段和结构要求：

1. `.agents/profile.yaml` 必须包含 `project_version` 字段
2. 嵌入式项目必须包含特定文档结构

### 升级步骤

#### 第 1 步：备份当前项目

```bash
git commit -am "chore: backup before upgrade to v1.0.0"
git tag pre-v1.0.0-upgrade
```

#### 第 2 步：更新 vibe-governance 工具

```bash
pip install --upgrade vibe-governance
```

#### 第 3 步：添加 `project_version` 字段

编辑 `.agents/profile.yaml`，添加：

```yaml
project_version: 1.0.0
```

版本号格式必须是 `major.minor.patch`，例如 `1.0.0`、`2.1.3`。

#### 第 4 步：如果是嵌入式项目，补充必需文档

嵌入式项目（`project_type: embedded`）需要以下文档：

- `docs/DEVELOPMENT_PLAN.md` - 开发计划
- `docs/PROTOCOL_SPEC.md` - 协议规范
- `docs/HARDWARE_BRINGUP.md` - 硬件启动清单
- `docs/VALIDATION_PLAN.md` - 验证计划（需包含 M0/M1/M2/M3 结构）
- `docs/schema/protocol.schema.json` - 协议 Schema

可以使用以下命令生成默认骨架：

```bash
# 在新目录初始化嵌入式骨架作为参考
mkdir /tmp/embedded-ref
cd /tmp/embedded-ref
vibe-governance init --project-type embedded
# 复制需要的文档模板到你的项目
```

#### 第 5 步：重新生成适配文件

```bash
vibe-governance render
```

#### 第 6 步：验证升级结果

```bash
vibe-governance validate
```

如果验证通过，说明升级成功。

#### 第 7 步：提交升级变更

```bash
git add .
git commit -m "chore: upgrade to vibe-governance v1.0.0"
```

### 常见问题

**Q: 我的项目是通用治理项目（`project_type: governance`），需要补充嵌入式文档吗？**

A: 不需要。嵌入式文档要求仅适用于 `project_type: embedded` 的项目。

**Q: `project_version` 应该设置为多少？**

A: 建议设置为你项目当前的实际版本号。如果项目刚开始，可以使用 `0.1.0` 或 `1.0.0`。

**Q: 升级后 CLAUDE.md 等文件被修改了怎么办？**

A: 这些是受管生成文件，应该通过 `vibe-governance render` 重新生成，不要手动编辑。

**Q: 验证失败怎么办？**

A: 查看错误信息，通常是缺少必填字段或文档。根据提示补充后重新运行 `validate`。

### 回退方案

如果升级后遇到问题，可以回退到升级前的状态：

```bash
git reset --hard pre-v1.0.0-upgrade
pip install vibe-governance==0.1.0
```

## 未来版本升级

后续版本升级说明将在此文档中持续更新。

## 从 v1.0.0 升级到 v1.2.0

### 这次升级新增什么

`v1.2.0` 不新增第二套文档体系, 但会新增两份治理文件:

1. `docs/DELTA_DECISIONS.md`
2. `docs/NEXT_ITERATION_BASELINE.md`

它们的职责分别是:

- `DELTA_DECISIONS.md`: 唯一增量真源
- `NEXT_ITERATION_BASELINE.md`: 下一轮必读索引

### 升级步骤

#### 第 1 步：确认当前项目已稳定在 v1.0.0

至少确认:

- `project_version` 已存在
- `render` 和 `validate` 能正常运行

#### 第 2 步：补齐 v1.2.0 文档

创建或同步以下文件:

- `docs/DELTA_DECISIONS.md`
- `docs/NEXT_ITERATION_BASELINE.md`
- `docs/upgrades/v1.2.0-summary.md`
- `docs/upgrades/v1.2.0-plan.md`

#### 第 3 步：更新规则与迁移说明

同步更新:

- `docs/CONTRIBUTING.md`
- `docs/MIGRATION_GUIDE.md`
- `docs/UPGRADE_SUMMARY.md`

#### 第 4 步：重新生成受管输出

```bash
vibe-governance render
```

#### 第 5 步：验证结果

```bash
vibe-governance validate
```

#### 第 6 步：提交升级结果

```bash
git add .
git commit -m "docs(governance): land v1.2.0 delta and iteration baseline workflow"
```

### 新项目初始化

如果是新建嵌入式项目:

```bash
vibe-governance init --project-type embedded
```

当前 `v1.2.0` 已支持在嵌入式脚手架中直接带出:

- `docs/DELTA_DECISIONS.md`
- `docs/NEXT_ITERATION_BASELINE.md`

### 现有项目首次接入

如果项目已经运行中, 但此前没有使用这套机制:

1. 先在临时目录执行:

```bash
vibe-governance init --project-type embedded
```

2. 从参考骨架中复制:
   - `docs/DELTA_DECISIONS.md`
   - `docs/NEXT_ITERATION_BASELINE.md`
3. 根据当前项目状态补初始内容
4. 从下一次修复开始按 `L0 / L1 / L2` 规则分流

### 回退建议

如果接入 `v1.2.0` 后发现方向不对, 建议:

1. 在升级前先打回退锚点
2. 保留原有 `v1.0.0` 文档
3. 需要时回退到升级前 tag 或 commit
