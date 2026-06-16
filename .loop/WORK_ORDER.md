# WORK_ORDER - Round 1

## Read first

- `README.md`
- `INDEX.md`
- `docs/INIT_LOOP.md`
- `scripts/init_loop.py`
- `.loop/TARGET.md`
- `.loop/ACCEPTANCE.md`

## Objective

Implement v0.3: a minimal Loop Verifier CLI at `scripts/check_loop.py`.

## Allowed files

- `scripts/check_loop.py`
- `docs/CHECK_LOOP.md`
- `README.md`
- `INDEX.md`
- Optional lightweight test/helper files if useful, but prefer no dependencies.
- `.loop/*` only for execution notes if necessary.

## Forbidden files/directories

Do not modify:

- `00_CONCEPT/`
- `01_PROTOCOL/`
- `02_TEMPLATES/`
- `03_RUNNERS/`
- `04_VERIFIERS/`
- `05_WORKFLOWS/`
- `06_KNOWLEDGE_BASE/`
- `07_TRIALS/`

## Requirements

Create `scripts/check_loop.py` using only Python standard library.

CLI behavior:

```bash
python scripts/check_loop.py --dir <target-project>
python scripts/check_loop.py --dir <target-project> --json
```

The checker must inspect `<target-project>/.loop/` and verify:

1. Required files exist:
   - `TARGET.md`
   - `PATH.md`
   - `ACCEPTANCE.md`
   - `STATE.md`
   - `LOOP_LOG.md`
   - `STOP_GATE.md`
   - `HANDOFF.md`
   - `WORK_ORDER.md`
2. `STATE.md` contains `status:` and `round:` markers.
3. `STOP_GATE.md` contains the four gates:
   - Done
   - DoneWithRisk
   - Blocked
   - HumanGate
4. `WORK_ORDER.md` contains at least these sections/markers:
   - Objective
   - Allowed files
   - Required verification
5. Exit code 0 if all checks pass; non-zero if any check fails.
6. Human-readable default output summarizing PASS/FAIL and issues.
7. `--json` output with parseable JSON containing at least:
   - `ok`: boolean
   - `target_dir`
   - `loop_dir`
   - `issues`: list

Documentation:

- Add `docs/CHECK_LOOP.md` with usage, checks, exit codes, and examples.
- Update README and INDEX to mention v0.3 checker.

## Required verification before returning

Run and report:

```bash
python scripts/check_loop.py --help
python -m py_compile scripts/check_loop.py
TMPDIR=$(mktemp -d)
python scripts/init_loop.py --name verifier-ok --dir "$TMPDIR"
python scripts/check_loop.py --dir "$TMPDIR"
python scripts/check_loop.py --dir "$TMPDIR" --json
rm "$TMPDIR/.loop/STATE.md"
python scripts/check_loop.py --dir "$TMPDIR" ; test $? -ne 0
```

Also test these negative cases in any robust way:

- missing STOP_GATE gate fails
- missing WORK_ORDER Required verification marker fails
- `--json` output parses as JSON

Finally run:

```bash
git diff --name-only
```

Confirm forbidden paths were not modified.

## Completion report

Return:

- Files changed.
- Commands run with pass/fail status.
- Any risks or deferred work.
- Whether forbidden paths stayed unchanged.
