<!--
managed-by: vibe-governance 1.3.2
upstream-repo: https://github.com/example/vibe-governance
<<<<<<< HEAD
upstream-version: 1.3.2
upstream-published-at: 2026-06-02T00:00:00Z
checksum-sha256: a5fc816bb4dd4662251c8fe82f745af460ef83dafaeb57b6f2e7ff74b8d6f5ae
=======
upstream-version: 0.1.0
upstream-published-at: 2026-03-07T00:00:00Z
checksum-sha256: e9c39fd283efab1d0b038093b72b52db6608b15426525c34a11d7cdc31742742
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a
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
<<<<<<< HEAD
| `20260602-1` | `2026-06-02` | Promote 1.3.2 as the current governance mainline | `draft` | `.agents/progress/entries/2026/2026-06-02-1.md` | chore(release): bump version to 1.3.2 |
| `20260422-7` | `2026-04-22` | Add trigger-based recording rules and minimum multi-agent entry layer to lightweight templates | `draft` | `.agents/progress/entries/2026/2026-04-22-7.md` | docs(governance): add trigger-based recording and multi-agent layer to lightweight templates |
| `20260422-6` | `2026-04-22` | Strengthen lightweight templates with the minimum .agents governance skeleton | `draft` | `.agents/progress/entries/2026/2026-04-22-6.md` | docs(governance): clarify minimum .agents skeleton in lightweight templates |
| `20260422-5` | `2026-04-22` | Add the lightweight general template as the second template-library entry | `draft` | `.agents/progress/entries/2026/2026-04-22-5.md` | docs(governance): add lightweight general template as second template-library entry |
| `20260422-4` | `2026-04-22` | Abstract the lightweight comparison test template away from image-specific language | `draft` | `.agents/progress/entries/2026/2026-04-22-4.md` | docs(governance): abstract lightweight comparison test template away from image-specific language |
| `20260422-3` | `2026-04-22` | Strengthen the lightweight comparison test template around minimal structure | `draft` | `.agents/progress/entries/2026/2026-04-22-3.md` | docs(governance): strengthen lightweight comparison test template around minimal structure |
| `20260422-2` | `2026-04-22` | Land the template library entry and the first lightweight comparison test template | `draft` | `.agents/progress/entries/2026/2026-04-22-2.md` | docs(governance): add template library entry and first lightweight comparison test template |
| `20260422-1` | `2026-04-22` | Read the migration brief before starting the next governance upgrade round | `draft` | `.agents/progress/entries/2026/2026-04-22-1.md` | docs(governance): record upgrade kickoff from migration brief |
| `20260420-1` | `2026-04-20` | Capture governance lessons from the image-generation derivative project | `draft` | `.agents/progress/entries/2026/2026-04-20-生图测试衍生项目经验回流.md` | docs(governance): capture lessons from image-generation derivative project |
| `20260401-5` | `2026-04-01` | Close migration gaps for projects adopting the v1.2 governance system | `draft` | `.agents/progress/entries/2026/2026-04-01-5.md` | fix(governance): close v1.0 to v1.2 migration gaps |
=======
| `20260308-9` | `2026-03-08` | Clarify path resolution in AI quickstart prompt | `draft` | `.agents/progress/entries/2026/2026-03-08-9.md` | docs(governance): clarify local path handling in AI quickstart |
| `20260308-8` | `2026-03-08` | Add dedicated root AI quickstart prompt | `draft` | `.agents/progress/entries/2026/2026-03-08-8.md` | docs(governance): add dedicated AI quickstart prompt |
| `20260308-7` | `2026-03-08` | Align deep docs with bootstrap-first workflow | `draft` | `.agents/progress/entries/2026/2026-03-08-7.md` | docs(governance): align deep docs with bootstrap workflow |
| `20260308-6` | `2026-03-08` | Keep bootstrap as the single project creation path | `draft` | `.agents/progress/entries/2026/2026-03-08-6.md` | refactor(governance): keep bootstrap as sole project creation path |
| `20260308-5` | `2026-03-08` | Add in-place bootstrap flow for new IDE project directories | `draft` | `.agents/progress/entries/2026/2026-03-08-5.md` | feat(governance): add in-place bootstrap workflow |
| `20260308-4` | `2026-03-08` | Rewrite root entry docs around bootstrap and START_HERE workflow | `draft` | `.agents/progress/entries/2026/2026-03-08-4.md` | docs(governance): rewrite root entry docs around bootstrap usage |
| `20260308-3` | `2026-03-08` | Add one-command smoke test for repo validation and sample project bootstrap | `draft` | `.agents/progress/entries/2026/2026-03-08-3.md` | feat(governance): add one-command smoke test |
| `20260308-10` | `2026-03-08` | Write explicit Taotaotao absolute path into AI quickstart | `draft` | `.agents/progress/entries/2026/2026-03-08-10.md` | docs(governance): add explicit Taotaotao path to AI quickstart |
| `20260308-1` | `2026-03-08` | Slim root human docs to five entry files and move deep guides into docs | `draft` | `.agents/progress/entries/2026/2026-03-08-1.md` | docs(governance): slim root human docs and move deep guides to docs |
| `20260307-4` | `2026-03-07` | Unify remaining human docs and add onboarding rule for generated adapters | `draft` | `.agents/progress/entries/2026/2026-03-07-4.md` | docs(governance): unify human docs and add onboarding adapter rule |
>>>>>>> 3a5b8e46de24dad832a8aeeed26e633f5707838a

## Archive

- Active entries older than the latest 10 should remain in `.agents/progress/entries/` and be located by search or tooling.
- Entries that have already been promoted upstream belong in `.agents/progress/archived/`.
- Upstream promotion must go through human-reviewed pull requests.
