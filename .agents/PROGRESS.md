<!--
managed-by: vibe-governance 1.0.0
upstream-repo: https://github.com/example/vibe-governance
upstream-version: 1.2.1
upstream-published-at: 2026-04-01T00:00:00Z
checksum-sha256: 60b60133cf103d3ac21332297c4cb62b57d33d55284dd0135e4f58b831016b88
managed-note-en: DO NOT EDIT DIRECTLY. Regenerate with `vibe-governance render`.
managed-note-zh: 请勿直接编辑此文件, 请运行 `vibe-governance render` 重新生成.
-->
# PROGRESS

## Project Version

- Current project version: `1.2.1`

## Purpose

Use this file as a sliding index, not a long-form journal. Detailed history lives under `.agents/progress/entries/` and `.agents/progress/archived/`.

## Active Architecture Decisions

| ID | Status | Title | Summary |
| --- | --- | --- | --- |
| `ADR-0001` | `active` | Deterministic adapter generation | Adapter files are rendered by the Python CLI from structured sources. LLM output is never used as a translation layer. |
| `ADR-0002` | `active` | Managed outputs stay read-only | Durable policy changes must flow through .agents source files and the canonical rule catalog, not direct edits to generated adapters. |
| `ADR-0003` | `active` | Sliding-window progress index | PROGRESS.md only tracks current architecture decisions and the latest active entries, while older or upstreamed records stay searchable on disk. |

## Active Entries

| Page ID | Date | Title | Status | Path | Related Commit Message |
| --- | --- | --- | --- | --- | --- |
| `20260401-3` | `2026-04-01` | Unify version numbering strategy and bump to 1.2.1 | `draft` | `.agents/progress/entries/2026/2026-04-01-3.md` | v1.2.1 统一版本号策略，明确工具版本与项目版本保持一致，补充版本递增规则 |
| `20260401-2` | `2026-04-01` | Land v1.2.0 delta decision and next-iteration baseline workflow | `promotable` | `.agents/progress/entries/2026/2026-04-01-2.md` | docs(governance): land v1.2.0 delta and iteration baseline workflow |
| `20260401-1` | `2026-04-01` | Unify repository package and project version to 1.0.0 | `draft` | `.agents/progress/entries/2026/2026-04-01-1.md` | chore(release): unify repository version to 1.0.0 |
| `20260331-4` | `2026-03-31` | Add canonical Chinese directory explainer rule for current and future projects | `draft` | `.agents/progress/entries/2026/2026-03-31-4.md` | docs(governance): require Chinese explainer files for stable directories |
| `20260331-3` | `2026-03-31` | Add root physical governance checklist and move test temp directories off-root | `draft` | `.agents/progress/entries/2026/2026-03-31-3.md` | docs(governance): add root physical governance checklist and isolate test temp directories |
| `20260331-2` | `2026-03-31` | Complete v1.0.0 P1 closure and Phase 5 validation | `promotable` | `.agents/progress/entries/2026/2026-03-31-2.md` | feat(governance): complete v1.0.0 P1 closure with environment rules, UTF-8 validation, and commit message templates |
| `20260331-1` | `2026-03-31` | v1.0.0 落地 project_version、embedded init 与最小嵌入式校验闭环 | `draft` | `.agents/progress/entries/2026/2026-03-31-1.md` | feat(governance): implement v1.0.0 embedded scaffold and version guards |
| `20260330-5` | `2026-03-30` | Align iteration plan with the three-layer upgrade document structure | `draft` | `.agents/progress/entries/2026/2026-03-30-5.md` | docs(governance): align iteration plan with versioned upgrade docs |
| `20260330-4` | `2026-03-30` | Restructure upgrade documentation into three-layer system | `draft` | `.agents/progress/entries/2026/2026-03-30-4.md` | docs(governance): restructure upgrade docs into feedback/index/versioned-summary |
| `20260330-3` | `2026-03-30` | Derive v1.0.0 root problems from upgrade raw records | `draft` | `.agents/progress/entries/2026/2026-03-30-3.md` | docs(governance): summarize v1.0.0 root problems from raw feedback |

## Archive

- Active entries older than the latest 10 should remain in `.agents/progress/entries/` and be located by search or tooling.
- Entries that have already been promoted upstream belong in `.agents/progress/archived/`.
- Upstream promotion must go through human-reviewed pull requests.
