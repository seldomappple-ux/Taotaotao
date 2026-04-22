<!--
managed-by: vibe-governance 1.2.1
upstream-repo: https://github.com/example/vibe-governance
upstream-version: 1.2.1
upstream-published-at: 2026-04-01T00:00:00Z
checksum-sha256: 94ee0171ab032cc6ce406205106c84d12402764b3629f3306133bbf08f0e7525
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
| `20260422-4` | `2026-04-22` | Abstract the lightweight comparison test template away from image-specific language | `draft` | `.agents/progress/entries/2026/2026-04-22-4.md` | docs(governance): abstract lightweight comparison test template away from image-specific language |
| `20260422-3` | `2026-04-22` | Strengthen the lightweight comparison test template around minimal structure | `draft` | `.agents/progress/entries/2026/2026-04-22-3.md` | docs(governance): strengthen lightweight comparison test template around minimal structure |
| `20260422-2` | `2026-04-22` | Land the template library entry and the first lightweight comparison test template | `draft` | `.agents/progress/entries/2026/2026-04-22-2.md` | docs(governance): add template library entry and first lightweight comparison test template |
| `20260422-1` | `2026-04-22` | Read the migration brief before starting the next governance upgrade round | `draft` | `.agents/progress/entries/2026/2026-04-22-1.md` | docs(governance): record upgrade kickoff from migration brief |
| `20260420-1` | `2026-04-20` | Capture governance lessons from the image-generation derivative project | `draft` | `.agents/progress/entries/2026/2026-04-20-生图测试衍生项目经验回流.md` | docs(governance): capture lessons from image-generation derivative project |
| `20260401-5` | `2026-04-01` | Close migration gaps for projects adopting the v1.2 governance system | `draft` | `.agents/progress/entries/2026/2026-04-01-5.md` | fix(governance): close v1.0 to v1.2 migration gaps |
| `20260401-4` | `2026-04-01` | Close v1.2 documentation wording around the 1.2.1 official version | `draft` | `.agents/progress/entries/2026/2026-04-01-4.md` | docs(governance): close v1.2 version wording around 1.2.1 |
| `20260401-3` | `2026-04-01` | Unify version numbering strategy and bump to 1.2.1 | `draft` | `.agents/progress/entries/2026/2026-04-01-3.md` | v1.2.1 统一版本号策略，明确工具版本与项目版本保持一致，补充版本递增规则 |
| `20260401-2` | `2026-04-01` | Land v1.2.0 delta decision and next-iteration baseline workflow | `promotable` | `.agents/progress/entries/2026/2026-04-01-2.md` | docs(governance): land v1.2.0 delta and iteration baseline workflow |
| `20260401-1` | `2026-04-01` | Unify repository package and project version to 1.0.0 | `draft` | `.agents/progress/entries/2026/2026-04-01-1.md` | chore(release): unify repository version to 1.0.0 |

## Archive

- Active entries older than the latest 10 should remain in `.agents/progress/entries/` and be located by search or tooling.
- Entries that have already been promoted upstream belong in `.agents/progress/archived/`.
- Upstream promotion must go through human-reviewed pull requests.
