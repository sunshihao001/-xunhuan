# Plan Next CLI

`scripts/plan_next.py` compiles the current Xunhuan `.loop/WORK_ORDER.md` into a structured execution and verifier checklist.

It is the v0.5 companion to the existing tool chain:

```text
Init Loop CLI   → creates .loop/
Check Loop CLI  → verifies .loop/ readiness
Run Loop CLI    → summarizes current loop state
Plan Next CLI   → structures WORK_ORDER into execution/verifier checklists
```

## Boundary

This command is intentionally safe and read-only.

It does **not**:

- execute Codex or another agent
- run shell commands from `WORK_ORDER.md`
- mutate `.loop/` files
- write git commits
- call external services

It only reads loop control files and compiles the current work order into a checklist.

## Usage

```bash
python scripts/plan_next.py --dir /path/to/project
```

Machine-readable output:

```bash
python scripts/plan_next.py --dir /path/to/project --json
```

If `--dir` is omitted, the current directory is used.

## What it parses

`plan_next.py` validates the loop using [`check_loop.py`](CHECK_LOOP.md), then parses these sections from `.loop/WORK_ORDER.md`:

- `Objective`
- `Allowed files`
- `Forbidden files/directories`
- `Requirements`
- `Required verification before returning`
- `Completion report`

Bullet lists, numbered lists, and fenced command blocks are converted into checklist items where practical.

## Human-readable example

```text
Xunhuan plan next: READY
Target directory: /tmp/demo
Loop directory: /tmp/demo/.loop
Work order: /tmp/demo/.loop/WORK_ORDER.md
Objective: Implement v0.5 planner.
Mode: read-only planner; this CLI does not execute agents or commands or mutate files.
Execution checklist:
- Parse work order sections.
Allowed files:
- scripts/plan_next.py
Forbidden files/directories:
- 00_CONCEPT/
Required verification:
- python scripts/plan_next.py --help
Completion report:
- Files changed.
Issues: none
```

If the loop is invalid, it exits non-zero and surfaces checker issues.

## JSON contract

`--json` emits parseable JSON with at least:

```json
{
  "ok": true,
  "target_dir": "/tmp/demo",
  "loop_dir": "/tmp/demo/.loop",
  "work_order_path": "/tmp/demo/.loop/WORK_ORDER.md",
  "objective": "Implement v0.5 planner.",
  "allowed_files": ["scripts/plan_next.py"],
  "forbidden_files": ["00_CONCEPT/"],
  "requirements": ["Parse work order sections."],
  "required_verification": ["python scripts/plan_next.py --help"],
  "completion_report": ["Files changed."],
  "issues": []
}
```

## Typical flow

```bash
TMPDIR=$(mktemp -d)
python scripts/init_loop.py --name demo --dir "$TMPDIR"
python scripts/check_loop.py --dir "$TMPDIR"
python scripts/run_loop.py --dir "$TMPDIR"
python scripts/plan_next.py --dir "$TMPDIR"
```

At this stage, `plan_next.py` is a planning/checklist compiler, not an executor. A future version can add guarded execution only behind explicit HumanGate approval.
