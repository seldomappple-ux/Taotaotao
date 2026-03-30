# 治理体系迭代计划

## 目标

建立一个能够根据经验反馈不断自我迭代优化的治理体系,实现:
- 经验自动沉淀
- 规则持续优化
- 跨项目知识复用
- Skills 能力扩展

## 核心机制

### 1. 反馈收集层

**文件位置:**
- `docs/UPGRADE_FEEDBACK.md` - 原始反馈池(只保留原文)
- 外部项目 progress 条目导入

**收集来源:**
- 用户口头反馈
- 实际开发中遇到的问题
- 跨项目经验迁移
- IDE 使用痛点

**收集原则:**
- 先保留原意,不做总结
- 按时间批次记录
- 标注来源和状态
- 保持上下文完整

### 2. 经验提炼层

**文件位置:**
- `docs/UPGRADE_SUMMARY.md` - 升级总索引
- `docs/upgrades/vX.Y.Z-summary.md` - 每个版本的独立问题归纳与行动项

**提炼流程:**
```
原始反馈 → 问题识别 → 根因分析 → 优先级判断 → 行动项拆解
```

**输出结构:**
- 问题清单(编号、标题、来源、优先级、影响层级)
- 问题说明(现象、根因、风险、约束)
- 建议动作(文档层、真源层、生成器层、模板层)
- 决策状态(open/planned/in_progress/done/rejected)

### 3. 规则沉淀层

**文件位置:**
- `.agents/profile.yaml` - 项目配置事实
- `.agents/overrides/rules.yaml` - 本地规则覆盖
- `.agents/architecture-decisions.yaml` - 架构决策
- `.agents/RULES.md` - 本地规则补充

**沉淀机制:**
- 验证过的经验 → 提升为规则
- 规则变更 → 触发适配器重新渲染
- 架构决策 → 记录到 ADR
- 项目事实 → 更新 profile

### 4. 实施与沉淀层

**文件位置:**
- `.agents/progress/entries/` - 结构化进度条目
- 代码变更 - 实际实施的修改

**沉淀机制:**
- 已实施的变更 → 创建 progress entry
- Progress entry 状态流转: draft → promotable → upstreamed
- 较旧条目 → 归档到 `.agents/progress/archived/`

### 5. 适配生成层

**生成命令:**
```bash
python -m vibe_governance render --target .
```

**生成目标:**
- `CLAUDE.md` - Claude 适配
- `GEMINI.md` - Gemini 适配
- `.github/copilot-instructions.md` - Copilot 适配
- `.cursor/rules/governance.mdc` - Cursor 适配
- `.opencode/AGENTS.md` - OpenCode 适配

**生成原则:**
- 确定性生成,不依赖 LLM
- 受管输出只读
- 变更必须回流真源

## 迭代闭环

### Phase 1: 收集 (当前批次)

```
用户反馈 → UPGRADE_FEEDBACK.md
外部项目经验 → 批量导入
实际问题 → 即时记录
```

### Phase 2: 整理 (定期执行)

```
原始记录 → 问题归类
问题归类 → 优先级排序
优先级排序 → 行动项拆解
行动项拆解 → 对应版本的 summary 文档
```

### Phase 3: 决策 (评审机制)

```
行动项 → 可行性评估
可行性评估 → 影响范围分析
影响范围分析 → 决策(采纳/延后/拒绝)
决策 → 更新状态
```

### Phase 4: 实施 (分层落地)

**文档层:**
- 更新根目录入口文档
- 补充 docs/ 深度说明
- 同步 QUICKSTART

**真源层:**
- 修改 profile.yaml
- 添加 overrides/rules.yaml
- 记录 architecture-decisions.yaml

**生成器层:**
- 扩展 vibe_governance 代码
- 更新模板文件
- 增强校验逻辑

**模板层:**
- 更新上游规则目录
- 同步 canonical 模板
- 发布新版本

### Phase 5: 验证 (质量保证)

```bash
# 校验健康度
python -m vibe_governance validate --target .

# 重新生成适配器
python -m vibe_governance render --target .

# 对比上游差异
python -m vibe_governance sync --target . --dry-run --json

# 运行单元测试 (修改生成器代码或 canonical 规则/模板时必须)
python -m unittest discover -s tests -v
```

补充检查:

- 中文内容新增或修改后, 必须确认没有乱码.
- 升级总索引与版本 summary 的链接必须正确.

### Phase 6: 沉淀 (经验固化)

```
实施结果 → progress entry (draft)
验证通过 → 状态更新 (promotable)
上游合并 → 状态更新 (upstreamed)
归档处理 → 移至 archived/
```

## 参考项目位置

### 当前项目
- 主仓库: `c:\code\VScode\Taotaotao`
- 治理核心: `.agents/`
- 生成器: `vibe_governance/`

### 外部经验源
- Moss_Q 项目: `C:\code\VScode\Moss_Q`
- 其 progress 条目: `C:\code\VScode\Moss_Q\.agents\progress\entries`

### 上游资源
- 规则目录: `https://github.com/example/vibe-governance`
- 版本: `0.1.0`
- 同步策略: `manual`

## Skills 导入机制

### 当前状态
- MCP 配置入口: `.agents/mcp/config.yaml` (预留)
- MCP 启用状态: `false`
- **重要:** 当前只做了预留,尚未实现自动化能力

### Phase 2 规划方向
1. **嵌入式开发 Skills** (未实现)
   - 硬件初始化模板
   - 通信协议生成
   - 驱动代码模板
   - 调试工具集成

2. **项目初始化 Skills** (未实现)
   - 项目类型 overlay
   - 目录结构生成
   - 配置文件模板
   - Git 工作流设置

3. **代码审查 Skills** (未实现)
   - 规范检查
   - 安全扫描
   - 性能分析
   - 文档完整性

4. **测试生成 Skills** (未实现)
   - 单元测试模板
   - 集成测试框架
   - Mock 数据生成
   - 覆盖率报告

### 实现前置条件
- 完成 MCP 工具契约设计
- 实现项目类型 overlay 体系
- 建立 Skill 注册机制
- 完善生成器扩展点

## 持续改进能力

### 当前已落地能力
- 确定性适配器生成 (`render`)
- 配置和规则校验 (`validate`)
- 上游差异对比 (`sync`)
- Progress 滑动窗口索引
- 架构决策记录 (ADR)

### Phase 2 自动化方向 (未实现)
1. **新 progress entry 创建时**
   - 检查是否需要提升为规则
   - 关联相关 ADR
   - 更新 PROGRESS.md 索引

2. **规则变更时**
   - 触发适配器重新渲染
   - 运行校验
   - 生成变更日志

3. **外部经验导入时**
   - 去重
   - 分类
   - 关联现有问题

4. **版本发布时**
   - 归档旧 progress
   - 更新 CHANGELOG
   - 同步上游

### 质量度量
- 规则覆盖率: 实际问题 / 已有规则覆盖
- 经验复用率: 复用次数 / 总条目数
- 迭代周期: 反馈收集 → 规则落地的平均时长
- 适配器一致性: 跨 IDE 规则差异度

### 改进方向
1. **短期(1-2 周)**
   - 完成 UPGRADE_FEEDBACK 整理
   - 提炼前 10 个高优先级问题
   - 落地 3-5 条新规则

2. **中期(1-2 月)**
   - 实现嵌入式项目 overlay
   - 扩展 MCP Skills 体系
   - 建立自动化测试

3. **长期(3-6 月)**
   - 多项目经验库
   - 智能规则推荐
   - 社区规则市场

## 使用指南

### 日常工作流
```bash
# 1. 遇到问题时,按 Batch 模板追加到 UPGRADE_FEEDBACK.md
# 手动编辑,保持格式和编码正确

# 2. 定期整理(每周)
# 先查看 docs/UPGRADE_SUMMARY.md 确认当前版本
# 再编辑对应的 docs/upgrades/vX.Y.Z-summary.md

# 3. 决策后实施
# 修改 .agents/ 真源文件

# 4. 重新生成适配器
python -m vibe_governance render --target .

# 5. 验证变更
python -m vibe_governance validate --target .

# 6. 检查中文和链接
# 确认无乱码, 升级总索引和版本 summary 链接正确

# 7. 提交变更
git add .agents/ docs/
git commit -m "feat(governance): 新规则描述"

# 8. 对已实施的变更创建 progress entry
# 在 .agents/progress/entries/YYYY/ 下创建
```

### 跨项目经验迁移
```bash
# 1. 导出外部项目经验
# 手动复制 progress entries 到 UPGRADE_FEEDBACK.md

# 2. 在 UPGRADE_SUMMARY.md 中定位当前升级版本

# 3. 识别可复用规则
# 在对应的 docs/upgrades/vX.Y.Z-summary.md 中标记

# 4. 判断规则层级
# 项目局部覆盖 → .agents/overrides/rules.yaml
# 通用治理能力 → vibe_governance/resources/* (需上游 PR)

# 5. 测试验证
python -m vibe_governance validate --target .

# 6. 文档化
# 更新相关 docs/ 文档
```

## 下一步行动

### 立即执行
1. ✅ 创建本迭代计划文档
2. ⬜ 整理 UPGRADE_FEEDBACK.md 中的嵌入式开发反馈
3. ⬜ 在 docs/upgrades/v1.0.0-summary.md 中提炼前 10 个问题
4. ⬜ 对已决定实施的行动项创建 progress entries

### 本周完成
1. ⬜ 设计嵌入式项目 profile 扩展字段
2. ⬜ 编写嵌入式规则 overlay 初版
3. ⬜ 扩展 profile schema / scaffold / validator 以支持嵌入式项目类型
4. ⬜ 测试生成器对新字段的支持

### 本月目标
1. ⬜ 完成嵌入式 overlay 体系
2. ⬜ 实现 MCP Skills 基础框架
3. ⬜ 建立自动化测试流程
4. ⬜ 编写完整的迭代操作手册

---

**最后更新:** 2026-03-30
**维护者:** 治理体系核心团队
**状态:** 活跃迭代中
