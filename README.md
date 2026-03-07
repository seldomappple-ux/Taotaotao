# Vibe Governance / 跨 IDE 治理生成器

Deterministic cross-IDE governance tooling for AI-assisted repositories.

面向 AI 协作仓库的确定性跨 IDE 治理工具.

## Overview / 概览

This repository implements a v1 governance core that keeps human-owned project sources under `.agents/` and renders read-only adapter files for IDE-specific instruction systems.

本仓库实现了一套 v1 治理内核: 人工维护的项目源文件集中放在 `.agents/` 下, IDE 专属指令文件通过生成器输出为只读适配层.

## Design Goals / 设计目标

- No LLM in the render or sync path.
- Stable structured sources: `profile.yaml`, `rule-catalog.yaml`, local override YAML, and progress entry front matter.
- Read-only generated adapters with checksum metadata.
- Sliding-window `PROGRESS.md` backed by searchable entry files.
- Sync reports aggregated by `rule_id`.

- 渲染与同步链路完全不依赖 LLM.
- 使用稳定的结构化真源: `profile.yaml`、`rule-catalog.yaml`、本地 override YAML 与 progress entry front matter.
- 生成的适配文件只读, 并带有 checksum 元信息.
- `PROGRESS.md` 采用滑动窗口索引, 详细记录保存在可检索 entry 文件中.
- `sync` 报告按 `rule_id` 聚合, 便于人工审查.

## Repository Layout / 仓库结构

- `vibe_governance/`: Python CLI and bundled canonical resources.
- `.agents/`: project-local source files and managed state.
- `.github/`, `.cursor/`, `.opencode/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`: generated adapter outputs.

- `vibe_governance/`: Python CLI 与内置 canonical 资源.
- `.agents/`: 项目本地治理源文件与受管状态目录.
- `.github/`、`.cursor/`、`.opencode/`、`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`: 生成出的适配层文件.

## Commands / 命令

```bash
python -m vibe_governance init --target .
python -m vibe_governance validate --target .
python -m vibe_governance render --target .
python -m vibe_governance sync --target . --dry-run --json
python -m vibe_governance progress promote --target . .agents/progress/entries/2026/2026-03-07-1.md
```

## Local Override Flow / 本地覆盖流程

1. Record repository-specific rationale in `.agents/RULES.md`.
2. Add enforceable overrides to `.agents/overrides/rules.yaml`.
3. Keep overrides inside `override_whitelist`.
4. Run `validate` and `render`.

1. 在 `.agents/RULES.md` 记录仓库特有的说明与约束背景.
2. 将可执行的覆盖规则写入 `.agents/overrides/rules.yaml`.
3. 所有 override 必须位于 `override_whitelist` 内.
4. 修改后执行 `validate` 与 `render`.

## Root Markdown Policy / 根目录 Markdown 规则

All root-level Markdown files should be bilingual Chinese and English by default.

根目录下的 Markdown 文件默认应为中英双语.

In special cases, Chinese may appear as comments or explanatory annotations as long as the English structure remains clear.

特殊情况下, 中文可以作为注释或说明性补充出现, 但英文结构仍需保持清晰.

## Progress Lifecycle / Progress 生命周期

- `draft`: local record, not yet reviewed for upstream reuse.
- `promotable`: human-reviewed and suitable for a governance PR.
- `upstreamed`: already merged upstream and archived locally.

- `draft`: 项目本地临时记录, 尚未审核为通用经验.
- `promotable`: 已人工审核, 可以回流治理仓.
- `upstreamed`: 已沉淀到上游治理仓, 本地进入归档.

Use `.agents/progress/ENTRY_TEMPLATE.md` for new entries. `PROGRESS.md` is regenerated from architecture decisions plus the latest 10 active entries.

新增 entry 时请使用 `.agents/progress/ENTRY_TEMPLATE.md`. `PROGRESS.md` 会根据架构决策和最近 10 条活跃 entry 自动重建.
