#!/usr/bin/env python3
"""Read-only bootstrap view for a Xunhuan .loop workspace."""

from __future__ import annotations

import argparse
import json
import re
import sys
import importlib.util
from pathlib import Path

RUNNER_TITLE = "Xunhuan loop runner"
CHECK_MODULE = Path(__file__).with_name("check_loop.py")


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
        description="Render a read-only bootstrap summary for a Xunhuan .loop workspace."
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


def parse_status(content: str) -> str:
    for line in content.splitlines():
        if line.lower().startswith("status:"):
            return line.split(":", 1)[1].strip()
    return "unknown"


def parse_round(content: str) -> str:
    for line in content.splitlines():
        if line.lower().startswith("round:"):
            return line.split(":", 1)[1].strip()
    return "unknown"


def extract_next_action(content: str) -> str:
    lines = content.splitlines()
    for index, line in enumerate(lines):
        if line.strip().lower() == "## next action":
            collected: list[str] = []
            for follow in lines[index + 1 :]:
                stripped = follow.strip()
                if stripped.startswith("## ") and collected:
                    break
                if stripped.startswith("## ") and not collected:
                    break
                if stripped.startswith("<!--") and stripped.endswith("-->"):
                    continue
                if stripped:
                    collected.append(stripped)
            return " ".join(collected).strip() or "(none specified)"
    return "(none specified)"


def work_order_title(content: str) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped.lstrip("# ").strip()
    return "WORK_ORDER.md"


def build_result(target_dir: Path) -> dict[str, object]:
    base = check_loop(target_dir)
    target_dir = Path(base["target_dir"])
    loop_dir = Path(base["loop_dir"])
    issues = list(base["issues"])

    state_path = loop_dir / "STATE.md"
    work_order_path = loop_dir / "WORK_ORDER.md"
    status = "unknown"
    round_value = "unknown"
    next_action = "(none specified)"
    work_order_title_value = "WORK_ORDER.md"

    if state_path.is_file():
        state_text = read_text(state_path)
        status = parse_status(state_text)
        round_value = parse_round(state_text)
        next_action = extract_next_action(state_text)

    if work_order_path.is_file():
        work_order_title_value = work_order_title(read_text(work_order_path))

    result = {
        "ok": not issues,
        "target_dir": str(target_dir),
        "loop_dir": str(loop_dir),
        "status": status,
        "round": round_value,
        "next_action": next_action,
        "work_order_path": str(work_order_path),
        "work_order_title": work_order_title_value,
        "issues": issues,
    }
    return result


def print_human(result: dict[str, object]) -> None:
    ok = bool(result["ok"])
    headline = "READY" if ok else "NOT READY"
    print(f"{RUNNER_TITLE}: {headline}")
    print(f"Target directory: {result['target_dir']}")
    print(f"Loop directory: {result['loop_dir']}")
    print(f"Status: {result['status']}")
    print(f"Round: {result['round']}")
    print(f"Next action: {result['next_action']}")
    print(f"Work order: {result['work_order_path']}")
    print(f"Work order title: {result['work_order_title']}")
    print("Mode: read-only bootstrap; this CLI does not execute agents or mutate files.")

    issues = result["issues"]
    if not issues:
        print("Issues: none")
        return

    print("Issues:")
    for issue in issues:
        print(f"- [{issue['code']}] {issue['file']}: {issue['message']}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = build_result(Path(args.dir))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_human(result)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
