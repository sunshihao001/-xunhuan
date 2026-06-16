#!/usr/bin/env python3
"""Compile a high-level intent brief into a proposed Xunhuan loop package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REQUIRED_SECTIONS = (
    "Goal",
    "Scope",
    "Non-goals",
    "Inputs",
    "Outputs",
    "Constraints",
    "Acceptance",
    "Risks",
    "HumanGate",
)

STANDARD_LOOP_FILES = (
    "TARGET.md",
    "PATH.md",
    "ACCEPTANCE.md",
    "STATE.md",
    "LOOP_LOG.md",
    "STOP_GATE.md",
    "HANDOFF.md",
    "WORK_ORDER.md",
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compile a compact intent brief into a read-only proposed Xunhuan loop package."
    )
    parser.add_argument(
        "--intent",
        required=True,
        help="Path to a markdown intent brief / demand contract.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON instead of human-readable text.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Materialize standard .loop files under --dir/.loop.",
    )
    parser.add_argument(
        "--dir",
        help="Target project directory for guarded write mode. Required with --write.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing generated .loop files in write mode.",
    )
    args = parser.parse_args(argv)
    if args.write and not args.dir:
        parser.error("--write requires --dir; refusing to silently write to cwd")
    return args


def normalize_heading(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def parse_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            current = normalize_heading(match.group(1))
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)
    return {key: "\n".join(lines).strip() for key, lines in sections.items()}


def clean_item(line: str) -> str:
    stripped = line.strip()
    stripped = re.sub(r"^[-*+]\s+", "", stripped)
    stripped = re.sub(r"^\d+[.)]\s+", "", stripped)
    return stripped.strip()


def split_items(section_text: str) -> list[str]:
    items: list[str] = []
    in_fence = False
    fence_lines: list[str] = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_lines = []
            else:
                in_fence = False
                for cmd in fence_lines:
                    cmd = cmd.strip()
                    if cmd:
                        items.append(cmd)
                fence_lines = []
            continue
        if in_fence:
            fence_lines.append(line)
            continue
        cleaned = clean_item(line)
        if cleaned:
            items.append(cleaned)
    return items


def section_text(sections: dict[str, str], heading: str) -> str:
    return sections.get(normalize_heading(heading), "").strip()


def first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return text


def build_proposed_loop(intent_path: Path, sections: dict[str, str]) -> dict[str, object]:
    goal = first_sentence(section_text(sections, "Goal"))
    scope = first_sentence(section_text(sections, "Scope"))
    non_goals = split_items(section_text(sections, "Non-goals"))
    inputs = split_items(section_text(sections, "Inputs"))
    outputs = split_items(section_text(sections, "Outputs"))
    constraints = split_items(section_text(sections, "Constraints"))
    acceptance = split_items(section_text(sections, "Acceptance"))
    risks = split_items(section_text(sections, "Risks"))
    human_gate = split_items(section_text(sections, "HumanGate"))

    return {
        "TARGET.md": {
            "Target": goal,
            "Value": scope,
            "Human Role": "Provide intent and approve any future write-mode expansion.",
            "Agent Role": "Compile intent into a bounded loop package draft.",
            "Non-goals": non_goals,
        },
        "PATH.md": {
            "Max rounds": 1,
            "Round 1": "Use the proposed loop draft to create a concrete WORK_ORDER in a later step.",
        },
        "ACCEPTANCE.md": {
            "Final Done Criteria": acceptance,
            "Evidence Required Each Round": [
                "Intent sections parsed successfully",
                "JSON output parses",
                "No files are written",
            ],
        },
        "WORK_ORDER.md": {
            "Objective": goal,
            "Inputs": inputs,
            "Outputs": outputs,
            "Constraints": constraints,
            "Risks": risks,
            "HumanGate": human_gate,
        },
        "source_intent": str(intent_path),
    }


def markdown_list(items: list[str], fallback: str = "None.") -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)


def render_loop_files(result: dict[str, object]) -> dict[str, str]:
    proposed = result["proposed_loop"]
    target = proposed["TARGET.md"]  # type: ignore[index]
    path = proposed["PATH.md"]  # type: ignore[index]
    acceptance = proposed["ACCEPTANCE.md"]  # type: ignore[index]
    work_order = proposed["WORK_ORDER.md"]  # type: ignore[index]
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    return {
        "TARGET.md": f"""# TARGET

## Target

{target["Target"] or "No target provided."}

## Value

{target["Value"] or "No scope provided."}

## Human Role

{target["Human Role"]}

## Agent Role

{target["Agent Role"]}

## Non-goals

{markdown_list(target["Non-goals"])}
""",
        "PATH.md": f"""# PATH

## Max rounds

{path["Max rounds"]}

## Round 1

{path["Round 1"]}
""",
        "ACCEPTANCE.md": f"""# ACCEPTANCE

## Final Done Criteria

{markdown_list(acceptance["Final Done Criteria"])}

## Evidence Required Each Round

{markdown_list(acceptance["Evidence Required Each Round"])}
""",
        "STATE.md": f"""# STATE

status: Ready
round: 1

## Current Focus

Loop package generated from intent brief.

## Updated

{generated_at}
""",
        "LOOP_LOG.md": f"""# LOOP_LOG

## Round 1

- {generated_at}: Loop package generated by scripts/compile_loop.py guarded write mode.
""",
        "STOP_GATE.md": """# STOP_GATE

## Allowed Outcomes

- Done
- DoneWithRisk
- Blocked
- HumanGate

## Current Gate

HumanGate before execution or destructive changes.
""",
        "HANDOFF.md": f"""# HANDOFF

## Summary

Loop package generated from `{result["intent_path"]}`.

## Next Action

Review `.loop/WORK_ORDER.md` before assigning bounded execution.
""",
        "WORK_ORDER.md": f"""# WORK_ORDER

## Objective

{work_order["Objective"] or "No objective provided."}

## Inputs

{markdown_list(work_order["Inputs"])}

## Outputs

{markdown_list(work_order["Outputs"])}

## Constraints

{markdown_list(work_order["Constraints"])}

## Risks

{markdown_list(work_order["Risks"])}

## HumanGate

{markdown_list(work_order["HumanGate"])}

## Allowed files

- `.loop/*`

## Required verification

- `python scripts/check_loop.py --dir <target-project>`
""",
    }


def write_loop_files(result: dict[str, object], target_dir: Path, force: bool) -> tuple[list[str], list[dict[str, str]]]:
    target_dir = target_dir.expanduser().resolve()
    loop_dir = target_dir / ".loop"
    rendered = render_loop_files(result)
    paths = {file_name: loop_dir / file_name for file_name in STANDARD_LOOP_FILES}
    existing = [path for path in paths.values() if path.exists()]
    if existing and not force:
        return [], [
            {
                "code": "target_exists",
                "file": str(path),
                "message": f"refusing to overwrite existing target file without --force: {path}",
            }
            for path in existing
        ]

    loop_dir.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    for file_name in STANDARD_LOOP_FILES:
        path = paths[file_name]
        path.write_text(rendered[file_name], encoding="utf-8", newline="\n")
        written.append(str(path))
    return written, []


def compile_intent(intent_path: Path) -> dict[str, object]:
    intent_path = intent_path.expanduser().resolve()
    text = intent_path.read_text(encoding="utf-8", errors="replace")
    sections = parse_sections(text)
    issues = []
    for heading in REQUIRED_SECTIONS:
        if not section_text(sections, heading):
            issues.append({
                "code": "missing_section",
                "section": heading,
                "message": f"Missing required section: {heading}",
            })

    proposed_loop = build_proposed_loop(intent_path, sections)
    return {
        "ok": not issues,
        "intent_path": str(intent_path),
        "write": False,
        "target_dir": None,
        "written_files": [],
        "goal": first_sentence(section_text(sections, "Goal")),
        "scope": first_sentence(section_text(sections, "Scope")),
        "non_goals": split_items(section_text(sections, "Non-goals")),
        "inputs": split_items(section_text(sections, "Inputs")),
        "outputs": split_items(section_text(sections, "Outputs")),
        "constraints": split_items(section_text(sections, "Constraints")),
        "acceptance": split_items(section_text(sections, "Acceptance")),
        "risks": split_items(section_text(sections, "Risks")),
        "human_gate": split_items(section_text(sections, "HumanGate")),
        "proposed_loop": proposed_loop,
        "issues": issues,
    }


def print_human(result: dict[str, object]) -> None:
    status = "READY" if result["ok"] else "NOT READY"
    print(f"Xunhuan compile loop: {status}")
    print(f"Intent: {result['intent_path']}")
    print(f"Goal: {result['goal'] or '(none found)'}")
    print(f"Scope: {result['scope'] or '(none found)'}")
    print("Non-goals:")
    for item in result["non_goals"]:
        print(f"- {item}")
    print("Proposed loop:")
    proposed = result["proposed_loop"]
    for file_name, data in proposed.items():
        if file_name == "source_intent":
            continue
        print(f"- {file_name}: {list(data.keys())}")
    if result["write"]:
        print(f"Mode: guarded write; target directory: {result['target_dir']}")
        if result["written_files"]:
            print("Files written:")
            for path in result["written_files"]:
                print(f"- {path}")
    else:
        print("Mode: read-only compiler; this CLI does not write files or execute agents.")
    issues = result["issues"]
    if not issues:
        print("Issues: none")
        return
    print("Issues:")
    for issue in issues:
        location = issue.get("section") or issue.get("file") or "general"
        print(f"- [{issue['code']}] {location}: {issue['message']}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = compile_intent(Path(args.intent))
    if args.write:
        target_dir = Path(args.dir).expanduser().resolve()
        result["write"] = True
        result["target_dir"] = str(target_dir)
        if result["ok"]:
            written_files, write_issues = write_loop_files(result, target_dir, args.force)
            result["written_files"] = written_files
            if write_issues:
                result["issues"].extend(write_issues)
                result["ok"] = False
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_human(result)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
