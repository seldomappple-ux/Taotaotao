from __future__ import annotations

import shutil
import unittest
from pathlib import Path

import yaml

from vibe_governance.cli import main as cli_main
from vibe_governance.project import (
    GovernanceError,
    _manifest_path,
    _overrides_path,
    _profile_path,
    _snapshot_path,
    init_project,
    render_project,
    sync_project,
    validate_project,
)


class GovernanceCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_root = Path.cwd() / "tests" / ".tmp-tests"
        self.temp_root.mkdir(parents=True, exist_ok=True)
        self.root = self.temp_root / self._testMethodName
        if self.root.exists():
            shutil.rmtree(self.root)
        self.root.mkdir(parents=True)
        init_project(self.root)

    def tearDown(self) -> None:
        if self.temp_root.exists():
            shutil.rmtree(self.temp_root)

    def _read(self, relative_path: str) -> str:
        return (self.root / relative_path).read_text(encoding="utf-8")

    def _write_entry(self, index: int) -> Path:
        year_dir = self.root / ".agents" / "progress" / "entries" / "2026"
        year_dir.mkdir(parents=True, exist_ok=True)
        entry_path = year_dir / f"2026-03-{index:02d}-1.md"
        entry_path.write_text(
            "\n".join(
                [
                    "---",
                    f"page_id: 202603{index:02d}-1",
                    f"date: 2026-03-{index:02d}",
                    f"title: Entry {index}",
                    "status: draft",
                    f'related_commit_message: "chore(progress): entry {index}"',
                    'related_commit_hash: ""',
                    'upstream_reference: ""',
                    "keywords:",
                    "  - progress",
                    "---",
                    f"Body {index}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return entry_path

    def test_render_is_deterministic(self) -> None:
        render_project(self.root)
        first = self._read("AGENTS.md")
        render_project(self.root)
        second = self._read("AGENTS.md")
        self.assertEqual(first, second)
        self.assertIn("`project_version`", first)
        self.assertTrue((self.root / ".agents" / "README_中文.md").exists())
        self.assertTrue((self.root / ".agents" / "overrides" / "README_中文.md").exists())
        self.assertTrue((self.root / ".agents" / "progress" / "README_中文.md").exists())
        self.assertTrue((self.root / ".agents" / "progress" / "entries" / "README_中文.md").exists())
        self.assertEqual("Validation passed.", validate_project(self.root))

    def test_adapter_specific_override_only_changes_copilot_outputs(self) -> None:
        render_project(self.root)
        before = {
            "AGENTS.md": self._read("AGENTS.md"),
            ".github/copilot-instructions.md": self._read(".github/copilot-instructions.md"),
            ".github/instructions/project-governance.instructions.md": self._read(
                ".github/instructions/project-governance.instructions.md"
            ),
            ".cursor/rules/governance.mdc": self._read(".cursor/rules/governance.mdc"),
        }
        override_path = _overrides_path(self.root)
        override_path.write_text(
            yaml.safe_dump(
                {
                    "overrides": [
                        {
                            "rule_id": "copilot.style",
                            "adapters": ["copilot"],
                            "body": "Copilot must stay terse and prefer file-local edits only.",
                        }
                    ]
                },
                sort_keys=False,
                allow_unicode=True,
            ),
            encoding="utf-8",
        )
        render_project(self.root)
        after = {
            "AGENTS.md": self._read("AGENTS.md"),
            ".github/copilot-instructions.md": self._read(".github/copilot-instructions.md"),
            ".github/instructions/project-governance.instructions.md": self._read(
                ".github/instructions/project-governance.instructions.md"
            ),
            ".cursor/rules/governance.mdc": self._read(".cursor/rules/governance.mdc"),
        }
        changed = {path for path in before if before[path] != after[path]}
        self.assertEqual(
            changed,
            {
                ".github/copilot-instructions.md",
                ".github/instructions/project-governance.instructions.md",
            },
        )

    def test_tampered_managed_output_fails_validation(self) -> None:
        render_project(self.root)
        agents_path = self.root / "AGENTS.md"
        agents_path.write_text(agents_path.read_text(encoding="utf-8") + "\nmanual edit\n", encoding="utf-8")
        with self.assertRaises(GovernanceError):
            validate_project(self.root)

    def test_override_outside_whitelist_fails(self) -> None:
        (_overrides_path(self.root)).write_text(
            yaml.safe_dump(
                {"overrides": [{"rule_id": "git.flow", "body": "Custom git flow."}]},
                sort_keys=False,
                allow_unicode=True,
            ),
            encoding="utf-8",
        )
        with self.assertRaises(GovernanceError) as ctx:
            validate_project(self.root, check_generated=False)
        self.assertIn("override_whitelist", str(ctx.exception))

    def test_immutable_override_fails_even_when_whitelisted(self) -> None:
        profile_path = _profile_path(self.root)
        profile = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
        profile["override_whitelist"].append("git.flow")
        profile_path.write_text(yaml.safe_dump(profile, sort_keys=False, allow_unicode=True), encoding="utf-8")
        (_overrides_path(self.root)).write_text(
            yaml.safe_dump(
                {"overrides": [{"rule_id": "git.flow", "body": "Custom git flow."}]},
                sort_keys=False,
                allow_unicode=True,
            ),
            encoding="utf-8",
        )
        with self.assertRaises(GovernanceError) as ctx:
            validate_project(self.root, check_generated=False)
        self.assertIn("immutable", str(ctx.exception))

    def test_progress_sliding_window_keeps_latest_ten_entries(self) -> None:
        for index in range(1, 13):
            self._write_entry(index)
        render_project(self.root)
        progress = self._read(".agents/PROGRESS.md")
        self.assertIn("Entry 12", progress)
        self.assertIn("Entry 3", progress)
        self.assertNotIn("`20260302-1`", progress)
        self.assertNotIn("`20260301-1`", progress)

    def test_sync_dry_run_reports_changed_rule_ids(self) -> None:
        render_project(self.root)
        snapshot_path = _snapshot_path(self.root)
        snapshot = yaml.safe_load(snapshot_path.read_text(encoding="utf-8"))
        for rule in snapshot["rules"]:
            if rule["rule_id"] == "cursor.review":
                rule["body"] = "Old cursor review rule."
        snapshot_path.write_text(yaml.safe_dump(snapshot, sort_keys=False, allow_unicode=True), encoding="utf-8")
        report = sync_project(self.root, dry_run=True)
        self.assertEqual(report["status"], "changes_detected")
        self.assertIn("cursor.review", report["changed_rule_ids"])

    def test_mcp_placeholder_only_renders_when_enabled(self) -> None:
        render_project(self.root)
        self.assertNotIn("mcp.placeholder", self._read("AGENTS.md"))
        profile_path = _profile_path(self.root)
        profile = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
        profile["mcp"]["enabled"] = True
        profile_path.write_text(yaml.safe_dump(profile, sort_keys=False, allow_unicode=True), encoding="utf-8")
        render_project(self.root)
        self.assertIn("mcp.placeholder", self._read("AGENTS.md"))

    def test_render_writes_managed_manifest(self) -> None:
        render_project(self.root)
        self.assertTrue(_manifest_path(self.root).exists())

    def test_root_markdown_outputs_are_bilingual_when_doc_mode_is_bilingual(self) -> None:
        render_project(self.root)
        agents = self._read("AGENTS.md")
        claude = self._read("CLAUDE.md")
        gemini = self._read("GEMINI.md")
        self.assertIn("代理总则", agents)
        self.assertIn("`project_version`", agents)
        self.assertIn("Core Rules / 核心规则", agents)
        self.assertIn("Current project version", claude)
        self.assertIn("中文:", claude)
        self.assertIn("English:", claude)
        self.assertIn("Current project version", gemini)
        self.assertIn("中文:", gemini)
        self.assertIn("English:", gemini)

    def test_profile_requires_project_version(self) -> None:
        profile_path = _profile_path(self.root)
        profile = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
        profile.pop("project_version", None)
        profile_path.write_text(yaml.safe_dump(profile, sort_keys=False, allow_unicode=True), encoding="utf-8")
        with self.assertRaises(GovernanceError) as ctx:
            validate_project(self.root, check_generated=False)
        self.assertIn("project_version", str(ctx.exception))

    def test_invalid_project_version_format_fails(self) -> None:
        profile_path = _profile_path(self.root)
        profile = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
        profile["project_version"] = "v1.0.0"
        profile_path.write_text(yaml.safe_dump(profile, sort_keys=False, allow_unicode=True), encoding="utf-8")
        with self.assertRaises(GovernanceError) as ctx:
            validate_project(self.root, check_generated=False)
        self.assertIn("major.minor.patch", str(ctx.exception))

    def test_init_embedded_creates_embedded_scaffold_and_validates(self) -> None:
        embedded_root = self.root.parent / f"{self._testMethodName}_embedded"
        if embedded_root.exists():
            shutil.rmtree(embedded_root)
        embedded_root.mkdir(parents=True)
        init_project(embedded_root, project_type="embedded")
        profile = yaml.safe_load((embedded_root / ".agents" / "profile.yaml").read_text(encoding="utf-8"))
        self.assertEqual(profile["project_type"], "embedded")
        self.assertEqual(profile["project_version"], "1.0.0")
        self.assertTrue((embedded_root / ".agents" / "README_中文.md").exists())
        self.assertTrue((embedded_root / ".agents" / "overrides" / "README_中文.md").exists())
        self.assertTrue((embedded_root / ".agents" / "progress" / "README_中文.md").exists())
        self.assertTrue((embedded_root / ".agents" / "progress" / "entries" / "README_中文.md").exists())
        self.assertTrue((embedded_root / "docs" / "README_中文.md").exists())
        self.assertTrue((embedded_root / "docs" / "DEVELOPMENT_PLAN.md").exists())
        self.assertTrue((embedded_root / "docs" / "PROTOCOL_SPEC.md").exists())
        self.assertTrue((embedded_root / "docs" / "HARDWARE_BRINGUP.md").exists())
        self.assertTrue((embedded_root / "docs" / "VALIDATION_PLAN.md").exists())
        self.assertTrue((embedded_root / "docs" / "schema" / "README_中文.md").exists())
        self.assertTrue((embedded_root / "docs" / "schema" / "protocol.schema.json").exists())
        self.assertEqual("Validation passed.", validate_project(embedded_root))
        shutil.rmtree(embedded_root)

    def test_embedded_validate_checks_required_docs(self) -> None:
        embedded_root = self.root.parent / f"{self._testMethodName}_embedded"
        if embedded_root.exists():
            shutil.rmtree(embedded_root)
        embedded_root.mkdir(parents=True)
        init_project(embedded_root, project_type="embedded")
        (embedded_root / "docs" / "VALIDATION_PLAN.md").unlink()
        with self.assertRaises(GovernanceError) as ctx:
            validate_project(embedded_root, check_generated=False)
        self.assertIn("VALIDATION_PLAN.md", str(ctx.exception))
        shutil.rmtree(embedded_root)

    def test_invalid_project_type_is_rejected_by_cli(self) -> None:
        with self.assertRaises(SystemExit):
            cli_main(["init", "--project-type", "invalid", "--target", str(self.root / "invalid")])


if __name__ == "__main__":
    unittest.main()
