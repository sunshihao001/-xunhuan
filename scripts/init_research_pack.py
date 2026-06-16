#!/usr/bin/env python3
"""Initialize a layered research evidence pack."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


PACK_DIRS = (
    "raw",
    "raw/source_captures",
    "clean",
    "reading",
    "insights",
    "kb",
    "workflow",
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a layered research evidence pack for Xunhuan workflows."
    )
    parser.add_argument("--name", required=True, help="Research pack directory name.")
    parser.add_argument("--dir", required=True, help="Parent directory for the research pack.")
    parser.add_argument("--question", required=True, help="Cognition question this pack investigates.")
    parser.add_argument("--force", action="store_true", help="Overwrite generated starter files.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned directories and files without writing anything.",
    )
    return parser.parse_args(argv)


def readme_content(pack_name: str, question: str) -> str:
    return f"""# {pack_name}

## Cognition Question

{question}

## Layer Roles

- `raw/`: original evidence, links, captures, transcripts, repository notes, and source snapshots.
- `raw/source_captures/`: copied or exported source material that should remain traceable.
- `clean/`: deduplicated source inventory, quality notes, relevance ratings, and source boundaries.
- `reading/`: AI reading cards for important sources, including claims, evidence strength, risks, and transfer value.
- `insights/`: cross-source synthesis, disagreements, risks, and open verification questions.
- `kb/`: stable conclusions that are sourced, bounded, and useful beyond one run.
- `workflow/`: candidate patches that can change Hermes, Codex, Loop, or Verifier behavior.

## Promotion Gate

Evidence can become a workflow patch only after it passes the promotion gate:

1. It has a traceable source in `raw/` or `clean/sources.json`.
2. It has been interpreted in `reading/` or synthesized in `insights/`.
3. It maps to a concrete Hermes, Codex, Loop, or Verifier behavior.
4. It names the expected executable or reviewable output.
5. It records source limits so candidate ideas are not treated as stable knowledge.

## Hermes / Codex / Verifier Usage

- Hermes uses this pack to preserve research context, synthesize evidence, and decide what can enter `kb/` or `workflow/`.
- Codex receives curated `insights/`, `kb/`, and `workflow/` handoff material rather than unfiltered raw evidence.
- Verifier checks whether a proposed workflow patch is sourced, bounded, and aligned with the promotion gate before it becomes durable process knowledge.
"""


def starter_files(pack_name: str, question: str) -> dict[str, str]:
    return {
        "README.md": readme_content(pack_name, question),
        "clean/sources.json": "[]\n",
        "clean/source_quality.md": """# Source Quality

Track source type, authority, relevance, evidence strength, and known limits.
""",
        "insights/synthesis.md": """# Synthesis

## Consensus

## Disagreements

## Risks

## Open Questions
""",
        "kb/stable_conclusions.md": """# Stable Conclusions

Only promote sourced, bounded conclusions that should guide future workflow decisions.
""",
        "workflow/patches.md": """# Workflow Patches

Record candidate and accepted changes to Hermes, Codex, Loop, or Verifier behavior.
""",
        "workflow/next_execution_plan.md": """# Next Execution Plan

Convert accepted research findings into bounded implementation or verification steps.
""",
    }


def planned_paths(pack_dir: Path, pack_name: str, question: str) -> tuple[list[Path], dict[Path, str]]:
    directories = [pack_dir / relative for relative in PACK_DIRS]
    files = {
        pack_dir / relative: content
        for relative, content in starter_files(pack_name, question).items()
    }
    return directories, files


def fail_on_conflicts(paths: list[Path]) -> None:
    conflicts = [path for path in paths if path.exists()]
    if not conflicts:
        return

    print("Refusing to overwrite existing research pack files without --force:", file=sys.stderr)
    for path in conflicts:
        print(f"  {path}", file=sys.stderr)
    raise SystemExit(1)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    target_dir = Path(args.dir).expanduser().resolve()
    pack_dir = target_dir / args.name
    directories, files = planned_paths(pack_dir, args.name, args.question)

    if args.dry_run:
        print(f"Research pack: {pack_dir}")
        for path in directories:
            action = "exists" if path.exists() else "create"
            print(f"would {action}: {path}")
        for path in files:
            action = "overwrite" if path.exists() else "create"
            print(f"would {action}: {path}")
        return 0

    if not args.force:
        fail_on_conflicts(list(files))

    for path in directories:
        path.mkdir(parents=True, exist_ok=True)
        print(f"created: {path}")

    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote: {path}")

    print(f"Initialized research pack {args.name!r} at {pack_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
