#!/usr/bin/env python3
"""Compile a Xunhuan WORK_ORDER into a read-only execution/verifier checklist."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

CHECK_MODULE = Path(__file__).with_name("check_loop.py")

SECTION_KEYS = {
    "objective": "Objective",
    "allowed_files": "Allowed files",
    "forbidden_files": "Forbidden files/directories",
    "requirements": "Requirements",
    "required_verification": "Required verification before returning",
    "completion_report": "Completion report",
}


class MarkdownSections:
    def __init__(self, text: str):
        self.sections = parse_sections(text)

    def section(self, heading: str) -> str:
        wanted = normalize_heading(heading)
        return self.sections.get(wanted, "").strip()


def load_check_module():
    spec = importlib.util.spec_from_file_location("check_loop", CHECK_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load checker module at {CHECK_MODULE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


check_loop = load_check_module().check_loop


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compile WORK_ORDER.md into a read-only Xunhuan execution/verifier checklist."
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Target project directory containing .loop/. Default: current directory.",
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


def clean_line(line: str) -> str:
    stripped = line.strip()
    stripped = re.sub(r"^[-*+]\s+", "", stripped)
    stripped = re.sub(r"^\d+[.)]\s+", "", stripped)
    return stripped.strip()


def lines_and_commands(section_text: str) -> list[str]:
    items: list[str] = []
    in_fence = False
    fence_lang = ""
    command_lines: list[str] = []

    for raw_line in section_text.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_lang = stripped[3:].strip()
                command_lines = []
            else:
                in_fence = False
                for command in command_lines:
                    command = command.strip()
                    if command:
                        items.append(command)
                fence_lang = ""
                command_lines = []
            continue

        if in_fence:
            command_lines.append(raw_line)
            continue

        cleaned = clean_line(raw_line)
        if not cleaned:
            continue
        if cleaned.lower() in {"do not modify:", "run:", "return:"}:
            continue
        if cleaned.startswith("<!--") and cleaned.endswith("-->"):
            continue
        items.append(cleaned)

    for command in command_lines:
        command = command.strip()
        if command:
            items.append(command)
    return items


def paragraph(section_text: str) -> str:
    parts = []
    for line in section_text.splitlines():
        cleaned = clean_line(line)
        if cleaned and not (cleaned.startswith("<!--") and cleaned.endswith("-->")):
            parts.append(cleaned)
    return " ".join(parts).strip()


def compile_plan(target_dir: Path) -> dict[str, object]:
    check = check_loop(target_dir)
    target = Path(check["target_dir"])
    loop_dir = Path(check["loop_dir"])
    issues = list(check["issues"])
    work_order_path = loop_dir / "WORK_ORDER.md"

    objective = ""
    allowed_files: list[str] = []
    forbidden_files: list[str] = []
    requirements: list[str] = []
    required_verification: list[str] = []
    completion_report: list[str] = []

    if work_order_path.is_file():
        sections = MarkdownSections(work_order_path.read_text(encoding="utf-8", errors="replace"))
        objective = paragraph(sections.section(SECTION_KEYS["objective"]))
        allowed_files = lines_and_commands(sections.section(SECTION_KEYS["allowed_files"]))
        forbidden_files = lines_and_commands(sections.section(SECTION_KEYS["forbidden_files"]))
        requirements = lines_and_commands(sections.section(SECTION_KEYS["requirements"]))
        required_verification = lines_and_commands(sections.section(SECTION_KEYS["required_verification"]))
        completion_report = lines_and_commands(sections.section(SECTION_KEYS["completion_report"]))

    return {
        "ok": not issues,
        "target_dir": str(target),
        "loop_dir": str(loop_dir),
        "work_order_path": str(work_order_path),
        "objective": objective,
        "allowed_files": allowed_files,
        "forbidden_files": forbidden_files,
        "requirements": requirements,
        "required_verification": required_verification,
        "completion_report": completion_report,
        "issues": issues,
    }


def print_list(title: str, values: list[str]) -> None:
    print(f"{title}:")
    if not values:
        print("- (none found)")
        return
    for value in values:
        print(f"- {value}")


def print_human(result: dict[str, object]) -> None:
    headline = "READY" if result["ok"] else "NOT READY"
    print(f"Xunhuan plan next: {headline}")
    print(f"Target directory: {result['target_dir']}")
    print(f"Loop directory: {result['loop_dir']}")
    print(f"Work order: {result['work_order_path']}")
    print(f"Objective: {result['objective'] or '(none found)'}")
    print("Mode: read-only planner; this CLI does not execute agents or commands or mutate files.")
    print_list("Execution checklist", result["requirements"])  # type: ignore[arg-type]
    print_list("Allowed files", result["allowed_files"])  # type: ignore[arg-type]
    print_list("Forbidden files/directories", result["forbidden_files"])  # type: ignore[arg-type]
    print_list("Required verification", result["required_verification"])  # type: ignore[arg-type]
    print_list("Completion report", result["completion_report"])  # type: ignore[arg-type]

    issues = result["issues"]
    if not issues:
        print("Issues: none")
        return
    print("Issues:")
    for issue in issues:
        print(f"- [{issue['code']}] {issue['file']}: {issue['message']}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = compile_plan(Path(args.dir))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_human(result)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
