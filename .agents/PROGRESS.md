<!--
managed-by: vibe-governance 1.3.2
upstream-repo: https://github.com/example/vibe-governance
upstream-version: 1.3.2
upstream-published-at: 2026-06-02T00:00:00Z
checksum-sha256: ff4e37dd97014d5ce874457866882059895116f9601f01d94720592357223136
managed-note-en: DO NOT EDIT DIRECTLY. Regenerate with `vibe-governance render`.
managed-note-zh: 请勿直接编辑此文件, 请运行 `vibe-governance render` 重新生成.
-->
# PROGRESS

## Project Version

- Current project version: `1.3.2`

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
| `20260702-1` | `2026-07-02` | Resolve committed merge conflicts and restore bootstrap workflow | `draft` | `.agents/progress/entries/2026/2026-07-02-1.md` | fix(governance): resolve committed merge conflicts and restore bootstrap |
| `20260602-1` | `2026-06-02` | Promote 1.3.2 as the current governance mainline | `draft` | `.agents/progress/entries/2026/2026-06-02-1.md` | chore(release): bump version to 1.3.2 |
| `20260422-7` | `2026-04-22` | Add trigger-based recording rules and minimum multi-agent entry layer to lightweight templates | `draft` | `.agents/progress/entries/2026/2026-04-22-7.md` | docs(governance): add trigger-based recording and multi-agent layer to lightweight templates |
| `20260422-6` | `2026-04-22` | Strengthen lightweight templates with the minimum .agents governance skeleton | `draft` | `.agents/progress/entries/2026/2026-04-22-6.md` | docs(governance): clarify minimum .agents skeleton in lightweight templates |
| `20260422-5` | `2026-04-22` | Add the lightweight general template as the second template-library entry | `draft` | `.agents/progress/entries/2026/2026-04-22-5.md` | docs(governance): add lightweight general template as second template-library entry |
| `20260422-4` | `2026-04-22` | Abstract the lightweight comparison test template away from image-specific language | `draft` | `.agents/progress/entries/2026/2026-04-22-4.md` | docs(governance): abstract lightweight comparison test template away from image-specific language |
| `20260422-3` | `2026-04-22` | Strengthen the lightweight comparison test template around minimal structure | `draft` | `.agents/progress/entries/2026/2026-04-22-3.md` | docs(governance): strengthen lightweight comparison test template around minimal structure |
| `20260422-2` | `2026-04-22` | Land the template library entry and the first lightweight comparison test template | `draft` | `.agents/progress/entries/2026/2026-04-22-2.md` | docs(governance): add template library entry and first lightweight comparison test template |
| `20260422-1` | `2026-04-22` | Read the migration brief before starting the next governance upgrade round | `draft` | `.agents/progress/entries/2026/2026-04-22-1.md` | docs(governance): record upgrade kickoff from migration brief |
| `20260420-1` | `2026-04-20` | Capture governance lessons from the image-generation derivative project | `draft` | `.agents/progress/entries/2026/2026-04-20-生图测试衍生项目经验回流.md` | docs(governance): capture lessons from image-generation derivative project |

## Archive

- Active entries older than the latest 10 should remain in `.agents/progress/entries/` and be located by search or tooling.
- Entries that have already been promoted upstream belong in `.agents/progress/archived/`.
- Upstream promotion must go through human-reviewed pull requests.
