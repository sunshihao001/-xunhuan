# ACCEPTANCE

## Final Done Criteria

- [ ] `python scripts/compile_loop.py --help` succeeds.
- [ ] `python -m py_compile scripts/compile_loop.py` succeeds.
- [ ] `python tests/test_compile_loop.py -v` passes.
- [ ] Existing `tests/test_plan_next.py`, `tests/test_run_loop.py`, and `tests/test_check_loop.py` still pass.
- [ ] On a sample intent brief, `compile_loop.py --intent <file>` exits 0 and prints a structured loop draft.
- [ ] `compile_loop.py --json` emits parseable JSON containing `ok`, `intent_path`, `goal`, `scope`, `non_goals`, `proposed_loop`, and `issues`.
- [ ] If the intent brief is missing required sections, the compiler exits non-zero and reports issues.
- [ ] The compiler does not mutate files.
- [ ] Markdown relative links remain valid.
- [ ] Forbidden theory/protocol/template/workflow dirs are unchanged.

## Evidence Required Each Round

- Commands run and outputs.
- Positive and negative CLI checks.
- Read-only hash check.
- `git status --short` and forbidden path check.
