# WORK_ORDER - Round 1

## Read first

- `README.md`
- `INDEX.md`
- `docs/CHECK_LOOP.md`
- `scripts/check_loop.py`
- `scripts/init_loop.py`
- `.loop/TARGET.md`
- `.loop/ACCEPTANCE.md`

## Objective

Implement v0.4: a safe Loop Bootstrap Runner CLI at `scripts/run_loop.py`.

## Allowed files

- `scripts/run_loop.py`
- `tests/test_run_loop.py`
- `docs/RUN_LOOP.md`
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

Create `scripts/run_loop.py` using only Python standard library.

CLI behavior:

```bash
python scripts/run_loop.py --dir <target-project>
python scripts/run_loop.py --dir <target-project> --json
```

The runner must be read-only. It must not mutate `.loop/` files.

It should:

1. Reuse/import `scripts/check_loop.py` logic when possible.
2. Validate the target `.loop/`; if invalid, exit non-zero and surface issues.
3. Parse `STATE.md` for:
   - `status:` value
   - `round:` value
4. Extract a concise `next_action` from the `## Next action` section when present.
5. Report the `WORK_ORDER.md` path and a short work-order preview/heading.
6. In human output, print a safe execution briefing:
   - check result
   - status
   - round
   - next action
   - work order path
   - explicit note that the CLI does not execute agents
7. In JSON output, include at least:
   - `ok`
   - `target_dir`
   - `loop_dir`
   - `status`
   - `round`
   - `next_action`
   - `work_order_path`
   - `work_order_title`
   - `issues`

Documentation:

- Add `docs/RUN_LOOP.md` with usage, read-only boundary, examples, and how it fits after init/check.
- Update README and INDEX to mention v0.4 runner.

## Required verification before returning

Run and report:

```bash
python scripts/run_loop.py --help
python -m py_compile scripts/run_loop.py
python tests/test_run_loop.py -v
TMPDIR=$(mktemp -d)
python scripts/init_loop.py --name runner-ok --dir "$TMPDIR"
python scripts/run_loop.py --dir "$TMPDIR"
python scripts/run_loop.py --dir "$TMPDIR" --json
python scripts/run_loop.py --dir "$TMPDIR" --json | python -m json.tool
```

Also verify:

- invalid `.loop` causes non-zero exit and surfaces checker issues
- running `run_loop.py` does not mutate `.loop` files
- Markdown links remain valid
- forbidden directories are unchanged

## Completion report

Return:

- Files changed.
- Commands run with pass/fail status.
- Whether read-only behavior was verified.
- Any risks or deferred work.
- Whether forbidden paths stayed unchanged.
