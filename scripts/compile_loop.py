#!/usr/bin/env python3
"""Compile a high-level intent brief into a proposed Xunhuan loop package."""

from __future__ import annotations

import argparse
import json
import re
import sys
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
    return parser.parse_args(argv)


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
    print("Mode: read-only compiler; this CLI does not write files or execute agents.")
    issues = result["issues"]
    if not issues:
        print("Issues: none")
        return
    print("Issues:")
    for issue in issues:
        print(f"- [{issue['code']}] {issue['section']}: {issue['message']}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = compile_intent(Path(args.intent))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_human(result)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
