<!--
managed-by: vibe-governance 0.1.0
upstream-repo: https://github.com/example/vibe-governance
upstream-version: 0.1.0
upstream-published-at: 2026-03-07T00:00:00Z
checksum-sha256: 6faf9e7abcc0202e752566c9854b9ad45b343a8c0302530192963cd77cc347e5
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
| `20260307-4` | `2026-03-07` | Unify remaining human docs and add onboarding rule for generated adapters | `draft` | `.agents/progress/entries/2026/2026-03-07-4.md` | docs(governance): unify human docs and add onboarding adapter rule |
| `20260307-3` | `2026-03-07` | Restructure onboarding docs and archive source articles in-repo | `draft` | `.agents/progress/entries/2026/2026-03-07-3.md` | docs(governance): restructure onboarding docs and archive source articles |
| `20260307-2` | `2026-03-07` | Add root explanatory documentation set for human and cross-account handoff | `draft` | `.agents/progress/entries/2026/2026-03-07-2.md` | docs(governance): add root explanatory documentation set |
| `20260307-1` | `2026-03-07` | Bootstrap deterministic governance core | `draft` | `.agents/progress/entries/2026/2026-03-07-1.md` | chore(governance): bootstrap deterministic cross-IDE governance core |

## Archive

- Active entries older than the latest 10 should remain in `.agents/progress/entries/` and be located by search or tooling.
- Entries that have already been promoted upstream belong in `.agents/progress/archived/`.
- Upstream promotion must go through human-reviewed pull requests.
