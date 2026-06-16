# WORK_ORDER - Round 1

## Read first

- `README.md`
- `INDEX.md`
- `docs/PLAN_NEXT.md`
- `scripts/plan_next.py`
- `scripts/run_loop.py`
- `scripts/check_loop.py`
- `.loop/TARGET.md`
- `.loop/ACCEPTANCE.md`

## Objective

Implement v0.6: a read-only higher-level intent compiler CLI at `scripts/compile_loop.py`.

## Allowed files

- `scripts/compile_loop.py`
- `tests/test_compile_loop.py`
- `docs/COMPILE_LOOP.md`
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

Create `scripts/compile_loop.py` using only Python standard library.

CLI behavior:

```bash
python scripts/compile_loop.py --intent <intent-file>
python scripts/compile_loop.py --intent <intent-file> --json
```

The compiler must be read-only. It must not mutate files.

It should:

1. Parse a compact intent brief / demand contract Markdown file.
2. Recognize at least these sections:
   - Goal
   - Scope
   - Non-goals
   - Inputs
   - Outputs
   - Constraints
   - Acceptance
   - Risks
   - HumanGate
3. Build a `proposed_loop` structure containing at least:
   - `TARGET.md` draft data
   - `PATH.md` draft data
   - `ACCEPTANCE.md` draft data
   - `WORK_ORDER.md` draft data
4. In human output, print:
   - goal
   - scope
   - non-goals
   - proposed loop summary
   - explicit note that the CLI does not write files or execute agents
5. In JSON output, include at least:
   - `ok`
   - `intent_path`
   - `goal`
   - `scope`
   - `non_goals`
   - `inputs`
   - `outputs`
   - `constraints`
   - `acceptance`
   - `risks`
   - `human_gate`
   - `proposed_loop`
   - `issues`

Documentation:

- Add `docs/COMPILE_LOOP.md` with usage, read-only boundary, examples, and how it fits before plan_next.
- Update README and INDEX to mention v0.6 compiler.

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
python scripts/compile_loop.py --intent <sample-intent>
python scripts/compile_loop.py --intent <sample-intent> --json
python scripts/compile_loop.py --intent <sample-intent> --json | python -m json.tool
```

Also verify:

- missing required sections causes non-zero exit and issues
- running `compile_loop.py` does not mutate files
- Markdown links remain valid
- forbidden directories are unchanged

## Completion report

Return:

- Files changed.
- Commands run with pass/fail status.
- Whether read-only behavior was verified.
- Any risks or deferred work.
- Whether forbidden paths stayed unchanged.
