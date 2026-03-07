<!--
managed-by: vibe-governance 0.1.0
upstream-repo: https://github.com/example/vibe-governance
upstream-version: 0.1.0
upstream-published-at: 2026-03-07T00:00:00Z
checksum-sha256: e9c39fd283efab1d0b038093b72b52db6608b15426525c34a11d7cdc31742742
managed-note-en: DO NOT EDIT DIRECTLY. Regenerate with `vibe-governance render`.
managed-note-zh: 请勿直接编辑此文件, 请运行 `vibe-governance render` 重新生成.
-->
# PROGRESS

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

## Archive

- Active entries older than the latest 10 should remain in `.agents/progress/entries/` and be located by search or tooling.
- Entries that have already been promoted upstream belong in `.agents/progress/archived/`.
- Upstream promotion must go through human-reviewed pull requests.
