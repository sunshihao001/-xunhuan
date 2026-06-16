#!/usr/bin/env python3
"""Initialize a Xunhuan .loop workspace."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


LOOP_FILES = (
    "TARGET.md",
    "PATH.md",
    "ACCEPTANCE.md",
    "STATE.md",
    "LOOP_LOG.md",
    "STOP_GATE.md",
    "HANDOFF.md",
    "WORK_ORDER.md",
)

BUILTIN_TEMPLATES = {
    "TARGET.md": """# TARGET

## Target

## Value

## Human Role

## Agent Role

## Non-goals
""",
    "PATH.md": """# PATH

## Max rounds

3

## Round 1

## Round 2

## Round 3
""",
    "ACCEPTANCE.md": """# ACCEPTANCE

## Final Done Criteria

- [ ]

## Evidence Required Each Round

- Commands run and outputs
- git status / diff
- artifact checks
""",
    "STATE.md": """# STATE

status: ReadyForRound1
round: 0

## Current understanding

## Next action
""",
    "LOOP_LOG.md": """# LOOP_LOG

## Round 0 - Loop compiled

## Round 1

## Decision
""",
    "STOP_GATE.md": """# STOP_GATE

## Done

## DoneWithRisk

## Blocked

## HumanGate
""",
    "HANDOFF.md": """# HANDOFF

## Current / Final status

## What changed

## Evidence

## Risks

## Resume instructions
""",
    "WORK_ORDER.md": """# WORK_ORDER - Round N

## Read first

## Objective

## Allowed files

## Forbidden files/directories

## Requirements

## Required verification before returning

## Completion report
""",
}


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a target directory with standard Xunhuan .loop files."
    )
    parser.add_argument(
        "--name",
        default="default-loop",
        help="Loop/task name to record in generated files. Default: %(default)s.",
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Target project directory. Default: current directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing .loop files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print files that would be written without writing anything.",
    )
    return parser.parse_args(argv)


def repo_root_candidates() -> list[Path]:
    script_path = Path(__file__).resolve()
    return [
        script_path.parent.parent,
        Path.cwd(),
    ]


def find_template_dir() -> Path | None:
    for root in repo_root_candidates():
        template_dir = root / "02_TEMPLATES"
        if all(
            (template_dir / file_name.replace(".md", ".template.md")).is_file()
            for file_name in LOOP_FILES
        ):
            return template_dir
    return None


def load_templates() -> tuple[dict[str, str], str]:
    template_dir = find_template_dir()
    if template_dir is None:
        return BUILTIN_TEMPLATES, "built-in fallback templates"

    templates: dict[str, str] = {}
    for file_name in LOOP_FILES:
        template_name = file_name.replace(".md", ".template.md")
        templates[file_name] = (template_dir / template_name).read_text(encoding="utf-8")
    return templates, str(template_dir)


def with_metadata(content: str, loop_name: str) -> str:
    normalized = content.rstrip() + "\n"
    metadata = f"\n<!-- loop_name: {loop_name} -->\n"
    return normalized + metadata


def planned_writes(target_dir: Path, loop_name: str) -> tuple[dict[Path, str], str]:
    templates, source = load_templates()
    loop_dir = target_dir / ".loop"
    writes = {
        loop_dir / file_name: with_metadata(templates[file_name], loop_name)
        for file_name in LOOP_FILES
    }
    return writes, source


def fail_on_conflicts(paths: list[Path]) -> None:
    conflicts = [path for path in paths if path.exists()]
    if not conflicts:
        return

    print("Refusing to overwrite existing .loop files without --force:", file=sys.stderr)
    for path in conflicts:
        print(f"  {path}", file=sys.stderr)
    raise SystemExit(1)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    target_dir = Path(args.dir).expanduser().resolve()
    writes, source = planned_writes(target_dir, args.name)

    if args.dry_run:
        print(f"Template source: {source}")
        print(f"Target directory: {target_dir}")
        for path in writes:
            action = "overwrite" if path.exists() else "create"
            print(f"would {action}: {path}")
        return 0

    if not args.force:
        fail_on_conflicts(list(writes))

    target_dir.mkdir(parents=True, exist_ok=True)
    loop_dir = target_dir / ".loop"
    loop_dir.mkdir(exist_ok=True)

    for path, content in writes.items():
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote: {path}")

    print(f"Initialized .loop for {args.name!r} using {source}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
