#!/usr/bin/env python3
"""Verify the structural readiness of a Xunhuan .loop workspace."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


REQUIRED_FILES = (
    "TARGET.md",
    "PATH.md",
    "ACCEPTANCE.md",
    "STATE.md",
    "LOOP_LOG.md",
    "STOP_GATE.md",
    "HANDOFF.md",
    "WORK_ORDER.md",
)

STATE_MARKERS = ("status:", "round:")
STOP_GATES = ("Done", "DoneWithRisk", "Blocked", "HumanGate")
WORK_ORDER_MARKERS = ("Objective", "Allowed files", "Required verification")


@dataclass(frozen=True)
class Issue:
    code: str
    file: str
    message: str


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check whether a target directory contains a valid Xunhuan .loop workspace."
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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def contains_marker(content: str, marker: str) -> bool:
    return marker.lower() in content.lower()


def check_required_files(loop_dir: Path) -> list[Issue]:
    issues: list[Issue] = []
    if not loop_dir.is_dir():
        return [
            Issue(
                code="missing_loop_dir",
                file=".loop/",
                message=f"Missing .loop directory: {loop_dir}",
            )
        ]

    for file_name in REQUIRED_FILES:
        path = loop_dir / file_name
        if not path.is_file():
            issues.append(
                Issue(
                    code="missing_required_file",
                    file=file_name,
                    message=f"Missing required .loop file: {file_name}",
                )
            )
    return issues


def check_markers(loop_dir: Path) -> list[Issue]:
    issues: list[Issue] = []

    marker_specs = (
        ("STATE.md", STATE_MARKERS, "missing_state_marker"),
        ("STOP_GATE.md", STOP_GATES, "missing_stop_gate"),
        ("WORK_ORDER.md", WORK_ORDER_MARKERS, "missing_work_order_marker"),
    )

    for file_name, markers, code in marker_specs:
        path = loop_dir / file_name
        if not path.is_file():
            continue
        content = read_text(path)
        for marker in markers:
            if not contains_marker(content, marker):
                issues.append(
                    Issue(
                        code=code,
                        file=file_name,
                        message=f"{file_name} is missing required marker: {marker}",
                    )
                )

    return issues


def check_loop(target_dir: Path) -> dict[str, object]:
    target_dir = target_dir.expanduser().resolve()
    loop_dir = target_dir / ".loop"
    issues = check_required_files(loop_dir)
    issues.extend(check_markers(loop_dir))
    return {
        "ok": not issues,
        "target_dir": str(target_dir),
        "loop_dir": str(loop_dir),
        "issues": [asdict(issue) for issue in issues],
    }


def print_human(result: dict[str, object]) -> None:
    ok = bool(result["ok"])
    status = "PASS" if ok else "FAIL"
    print(f"Xunhuan loop check: {status}")
    print(f"Target directory: {result['target_dir']}")
    print(f"Loop directory: {result['loop_dir']}")

    issues = result["issues"]
    if not issues:
        print("Issues: none")
        return

    print("Issues:")
    for issue in issues:  # type: ignore[assignment]
        print(f"- [{issue['code']}] {issue['file']}: {issue['message']}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = check_loop(Path(args.dir))

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_human(result)

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
