from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .project import (
    PROJECT_TYPES,
    bootstrap_project,
    GovernanceError,
    archive_progress_entry,
    init_project,
    promote_progress_entry,
    render_project,
    smoke_test,
    sync_project,
    validate_project,
)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vibe-governance",
        description="Deterministic governance bootstrapper and adapter renderer.",
    )

    target_parent = argparse.ArgumentParser(add_help=False)
    target_parent.add_argument(
        "--target",
        default=".",
        help="Target project directory. Defaults to the current working directory.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    bootstrap_parser = subparsers.add_parser(
        "bootstrap",
        parents=[target_parent],
        help="Bootstrap the current target directory as a project root.",
    )
    bootstrap_parser.add_argument(
        "--type",
        dest="project_type",
        required=True,
        choices=sorted(PROJECT_TYPES),
        help="Project type template to bootstrap into the target directory.",
    )
    bootstrap_parser.add_argument(
        "--name",
        default=None,
        help="Optional project name written into generated entry files. Defaults to the target directory name.",
    )
    bootstrap_parser.add_argument(
        "--project-lang",
        default=None,
        help="Optional project language override written into .agents/profile.yaml.",
    )
    bootstrap_parser.add_argument(
        "--comment-lang",
        default=None,
        help="Optional comment language override written into .agents/profile.yaml.",
    )
    bootstrap_parser.add_argument(
        "--doc-mode",
        default=None,
        help="Optional doc mode override: zh, en, or bilingual.",
    )
    subparsers.add_parser("init", parents=[target_parent], help="Initialize the .agents source tree.")
    subparsers.add_parser("render", parents=[target_parent], help="Render all managed outputs.")
    subparsers.add_parser(
        "validate",
        parents=[target_parent],
        help="Validate source files and managed outputs.",
    )
    smoke_parser = subparsers.add_parser(
        "smoke",
        parents=[target_parent],
        help="Run a one-command smoke test against the current repo and a generated sample project.",
    )
    smoke_parser.add_argument(
        "--type",
        dest="project_type",
        default="embedded",
        choices=sorted(PROJECT_TYPES),
        help="Project type used for the generated smoke project. Defaults to embedded.",
    )
    smoke_parser.add_argument(
        "--name",
        default=None,
        help="Optional name for the generated smoke project directory.",
    )

    sync_parser = subparsers.add_parser("sync", parents=[target_parent], help="Compare or apply upstream updates.")
    sync_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report rule-level changes without mutating the project.",
    )
    sync_parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the sync report as JSON.",
    )

    progress_parser = subparsers.add_parser(
        "progress",
        parents=[target_parent],
        help="Promote or archive progress entries and refresh PROGRESS.md.",
    )
    progress_subparsers = progress_parser.add_subparsers(dest="progress_command", required=True)

    promote_parser = progress_subparsers.add_parser(
        "promote",
        parents=[target_parent],
        help="Mark an entry as promotable.",
    )
    promote_parser.add_argument("entry", help="Path to the entry file, relative or absolute.")

    archive_parser = progress_subparsers.add_parser(
        "archive",
        parents=[target_parent],
        help="Archive an entry as upstreamed.",
    )
    archive_parser.add_argument("entry", help="Path to the entry file, relative or absolute.")
    archive_parser.add_argument(
        "--upstream-ref",
        default="",
        help="Optional upstream PR or commit reference to attach before archiving.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    target = Path(args.target).resolve()

    try:
        if args.command == "bootstrap":
            created = bootstrap_project(
                target,
                args.project_type,
                project_name=args.name,
                project_lang=args.project_lang,
                comment_lang=args.comment_lang,
                doc_mode=args.doc_mode,
            )
            for item in created:
                print(item)
            return 0

        if args.command == "init":
            created = init_project(target)
            for item in created:
                print(item)
            return 0

        if args.command == "render":
            rendered = render_project(target)
            for item in rendered:
                print(item)
            return 0

        if args.command == "validate":
            report = validate_project(target)
            print(report)
            return 0

        if args.command == "smoke":
            report = smoke_test(target, project_type=args.project_type, project_name=args.name)
            print("Smoke test passed.")
            print(f"Current project: {report['current_validation']}")
            print(f"Generated project: {report['generated_project']}")
            print(f"Generated START_HERE: {report['generated_start_here']}")
            print(f"Generated project validation: {report['generated_validation']}")
            print(f"Generated project sync: {report['sync_status']}")
            return 0

        if args.command == "sync":
            report = sync_project(target, dry_run=args.dry_run)
            if args.json:
                print(json.dumps(report, indent=2, ensure_ascii=False))
            else:
                if report["status"] == "clean":
                    print("No upstream rule changes detected.")
                else:
                    print(f"status: {report['status']}")
                    for rule_id in report["changed_rule_ids"]:
                        print(rule_id)
            return 0

        if args.command == "progress":
            if args.progress_command == "promote":
                entry_path = promote_progress_entry(target, args.entry)
                print(entry_path)
                return 0
            if args.progress_command == "archive":
                entry_path = archive_progress_entry(target, args.entry, args.upstream_ref)
                print(entry_path)
                return 0

        parser.error("Unsupported command.")
        return 2
    except GovernanceError as exc:
        print(str(exc), file=sys.stderr)
        return 1
