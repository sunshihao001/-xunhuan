# WORK_ORDER - Round 1

## Read first

- `README.md`
- `INDEX.md`
- `docs/RUN_LOOP.md`
- `scripts/run_loop.py`
- `scripts/check_loop.py`
- `.loop/TARGET.md`
- `.loop/ACCEPTANCE.md`

## Objective

Implement v0.5: a guarded plan/checklist compiler CLI at `scripts/plan_next.py`.

## Allowed files

- `scripts/plan_next.py`
- `tests/test_plan_next.py`
- `docs/PLAN_NEXT.md`
- `README.md`
- `INDEX.md`
- `.loop/*` for execution state and evidence only

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

Do not add dependencies.

## Requirements

Create `scripts/plan_next.py` using only Python standard library.

CLI behavior:

```bash
python scripts/plan_next.py --dir <target-project>
python scripts/plan_next.py --dir <target-project> --json
```

The planner must be read-only. It must not mutate `.loop/` files.

It should:

1. Reuse/import `scripts/check_loop.py` logic when possible.
2. Validate the target `.loop/`; if invalid, exit non-zero and surface issues.
3. Parse `WORK_ORDER.md` sections:
   - Objective
   - Allowed files
   - Forbidden files/directories
   - Requirements
   - Required verification before returning
   - Completion report
4. Convert bullet lists and fenced command blocks into structured checklist items where practical.
5. In human output, print:
   - objective
   - execution checklist
   - allowed files
   - forbidden files/directories
   - required verification checklist
   - completion report expectations
   - explicit note that the CLI does not execute agents or commands
6. In JSON output, include at least:
   - `ok`
   - `target_dir`
   - `loop_dir`
   - `work_order_path`
   - `objective`
   - `allowed_files`
   - `forbidden_files`
   - `requirements`
   - `required_verification`
   - `completion_report`
   - `issues`

Documentation:

- Add `docs/PLAN_NEXT.md` with usage, read-only boundary, examples, and how it fits after run_loop.
- Update README and INDEX to mention v0.5 planner.

## Required verification before returning

Run and report:

```bash
python scripts/plan_next.py --help
python -m py_compile scripts/plan_next.py
python tests/test_plan_next.py -v
python tests/test_run_loop.py -v
python tests/test_check_loop.py -v
TMPDIR=$(mktemp -d)
python scripts/init_loop.py --name planner-ok --dir "$TMPDIR"
python scripts/plan_next.py --dir "$TMPDIR"
python scripts/plan_next.py --dir "$TMPDIR" --json
python scripts/plan_next.py --dir "$TMPDIR" --json | python -m json.tool
```

Also verify:

- invalid `.loop` causes non-zero exit and surfaces checker issues
- running `plan_next.py` does not mutate `.loop` files
- Markdown links remain valid
- forbidden directories are unchanged

## Completion report

Return:

- Files changed.
- Commands run with pass/fail status.
- Whether read-only behavior was verified.
- Any risks or deferred work.
- Whether forbidden paths stayed unchanged.
