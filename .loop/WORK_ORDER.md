# WORK_ORDER - Round 1

## Read first

- `README.md`
- `INDEX.md`
- `docs/COMPILE_LOOP.md`
- `scripts/compile_loop.py`
- `scripts/check_loop.py`
- `tests/test_compile_loop.py`
- `.loop/TARGET.md`
- `.loop/ACCEPTANCE.md`

## Objective

Implement v0.7: guarded write mode for `scripts/compile_loop.py`.

## Allowed files

- `scripts/compile_loop.py`
- `tests/test_compile_loop.py`
- `docs/COMPILE_LOOP.md`
- `README.md`
- `INDEX.md`
- `.loop/*` only for execution notes if needed

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

Enhance `scripts/compile_loop.py` using only Python standard library.

CLI behavior:

```bash
python scripts/compile_loop.py --intent <intent-file>
python scripts/compile_loop.py --intent <intent-file> --json
python scripts/compile_loop.py --intent <intent-file> --write --dir <target-project>
python scripts/compile_loop.py --intent <intent-file> --write --dir <target-project> --force
```

Required behavior:

1. Default mode remains read-only and must not mutate files.
2. `--write` materializes standard `.loop/` files under `<target-project>/.loop/`.
3. Write mode must require `--dir`; do not silently write to cwd.
4. Standard files written:
   - `TARGET.md`
   - `PATH.md`
   - `ACCEPTANCE.md`
   - `STATE.md`
   - `LOOP_LOG.md`
   - `STOP_GATE.md`
   - `HANDOFF.md`
   - `WORK_ORDER.md`
5. Without `--force`, refuse to overwrite existing target files and exit non-zero.
6. With `--force`, overwrite generated target files.
7. Written files must be structurally valid enough for `scripts/check_loop.py --dir <target-project>` to pass.
8. Human output should clearly say when files were written.
9. JSON output should include at least:
   - `ok`
   - `intent_path`
   - `write`
   - `target_dir`
   - `written_files`
   - `issues`

Documentation:

- Update `docs/COMPILE_LOOP.md` with guarded write mode examples and safety boundary.
- Update README / INDEX if needed.

## Required verification before returning

Run and report:

```bash
python scripts/compile_loop.py --help
python -m py_compile scripts/compile_loop.py
python tests/test_compile_loop.py -v
python tests/test_plan_next.py -v
python tests/test_run_loop.py -v
python tests/test_check_loop.py -v
TMPDIR=$(mktemp -d)
# create sample intent file
python scripts/compile_loop.py --intent <sample-intent>
python scripts/compile_loop.py --intent <sample-intent> --json | python -m json.tool
python scripts/compile_loop.py --intent <sample-intent> --write --dir "$TMPDIR"
python scripts/check_loop.py --dir "$TMPDIR"
python scripts/compile_loop.py --intent <sample-intent> --write --dir "$TMPDIR" ; test $? -ne 0
python scripts/compile_loop.py --intent <sample-intent> --write --dir "$TMPDIR" --force
```

Also verify:

- default read-only mode does not mutate files
- forbidden directories are unchanged
- Markdown links remain valid

## Completion report

Return:

- Files changed.
- Commands run with pass/fail status.
- Whether Codex encountered blockers.
- Whether guarded write behavior was verified.
- Whether forbidden paths stayed unchanged.
