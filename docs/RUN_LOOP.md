# Run Loop CLI

`scripts/run_loop.py` renders a read-only bootstrap briefing for a Xunhuan `.loop/` workspace.

It is the v0.4 companion to the existing tool chain:

```text
Init Loop CLI  → creates .loop/
Check Loop CLI → verifies .loop/ readiness
Run Loop CLI   → summarizes current loop state and next work order
```

## Boundary

This command is intentionally safe and read-only.

It does **not**:

- execute Codex or another agent
- run shell commands from `WORK_ORDER.md`
- mutate `.loop/` files
- write git commits
- call external services

It only reads loop control files and prints a bootstrap briefing.

## Usage

```bash
python scripts/run_loop.py --dir /path/to/project
```

Machine-readable output:

```bash
python scripts/run_loop.py --dir /path/to/project --json
```

If `--dir` is omitted, the current directory is used.

## What it does

1. Reuses the structural checks from [`check_loop.py`](CHECK_LOOP.md).
2. Reads `.loop/STATE.md`.
3. Extracts:
   - `status:`
   - `round:`
   - `## Next action`
4. Reads `.loop/WORK_ORDER.md` and reports its path/title.
5. Prints whether the loop is ready for a human or agent executor to pick up.

## Human-readable example

```text
Xunhuan loop runner: READY
Target directory: /tmp/demo
Loop directory: /tmp/demo/.loop
Status: ReadyForRound1
Round: 0
Next action: Run verifier and decide stop gate.
Work order: /tmp/demo/.loop/WORK_ORDER.md
Work order title: WORK_ORDER - Round N
Mode: read-only bootstrap; this CLI does not execute agents or mutate files.
Issues: none
```

If the loop is invalid, it exits non-zero and surfaces checker issues:

```text
Xunhuan loop runner: NOT READY
...
Issues:
- [missing_required_file] STATE.md: Missing required .loop file: STATE.md
```

## JSON contract

`--json` emits parseable JSON with at least:

```json
{
  "ok": true,
  "target_dir": "/tmp/demo",
  "loop_dir": "/tmp/demo/.loop",
  "status": "ReadyForRound1",
  "round": "0",
  "next_action": "Run verifier and decide stop gate.",
  "work_order_path": "/tmp/demo/.loop/WORK_ORDER.md",
  "work_order_title": "WORK_ORDER - Round N",
  "issues": []
}
```

## Typical flow

```bash
TMPDIR=$(mktemp -d)
python scripts/init_loop.py --name demo --dir "$TMPDIR"
python scripts/check_loop.py --dir "$TMPDIR"
python scripts/run_loop.py --dir "$TMPDIR"
```

At this stage, `run_loop.py` is a bootstrap/status command, not a full autonomous loop runner. A future version can add guarded execution only behind explicit HumanGate approval.
