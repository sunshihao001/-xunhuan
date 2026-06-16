# Check Loop CLI

`scripts/check_loop.py` verifies that a target project has a structurally complete Xunhuan `.loop/` workspace.

It is the v0.3 companion to [`scripts/init_loop.py`](INIT_LOOP.md):

```text
Init Loop CLI  → creates .loop/
Check Loop CLI → verifies .loop/ readiness
```

## Usage

```bash
python scripts/check_loop.py --dir /path/to/project
```

Machine-readable output:

```bash
python scripts/check_loop.py --dir /path/to/project --json
```

If `--dir` is omitted, the current directory is checked.

## What it checks

The checker verifies that `/path/to/project/.loop/` exists and contains exactly the required control files:

- `TARGET.md`
- `PATH.md`
- `ACCEPTANCE.md`
- `STATE.md`
- `LOOP_LOG.md`
- `STOP_GATE.md`
- `HANDOFF.md`
- `WORK_ORDER.md`

It also verifies required readiness markers:

- `STATE.md` contains `status:` and `round:`
- `STOP_GATE.md` contains `Done`, `DoneWithRisk`, `Blocked`, and `HumanGate`
- `WORK_ORDER.md` contains `Objective`, `Allowed files`, and `Required verification`

## Exit codes

- `0`: all checks passed
- `1`: one or more structural checks failed

## Human-readable example

```text
Xunhuan loop check: PASS
Target directory: /tmp/demo
Loop directory: /tmp/demo/.loop
Issues: none
```

Failure output lists each issue with a stable code, file, and message:

```text
Xunhuan loop check: FAIL
Target directory: /tmp/demo
Loop directory: /tmp/demo/.loop
Issues:
- [missing_required_file] STATE.md: Missing required .loop file: STATE.md
```

## JSON example

```json
{
  "ok": true,
  "target_dir": "/tmp/demo",
  "loop_dir": "/tmp/demo/.loop",
  "issues": []
}
```

On failure, `issues` contains objects with:

- `code`
- `file`
- `message`

## Typical flow

```bash
TMPDIR=$(mktemp -d)
python scripts/init_loop.py --name demo --dir "$TMPDIR"
python scripts/check_loop.py --dir "$TMPDIR"
python scripts/check_loop.py --dir "$TMPDIR" --json
```
