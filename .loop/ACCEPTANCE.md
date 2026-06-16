# ACCEPTANCE

## Final Done Criteria

- [ ] `python scripts/compile_loop.py --help` succeeds and documents `--write`, `--dir`, and `--force`.
- [ ] `python -m py_compile scripts/compile_loop.py` succeeds.
- [ ] `python tests/test_compile_loop.py -v` passes with new write-mode coverage.
- [ ] Existing `tests/test_plan_next.py`, `tests/test_run_loop.py`, and `tests/test_check_loop.py` still pass.
- [ ] Without `--write`, compiler does not mutate files.
- [ ] With `--write --dir <target>`, compiler creates standard `.loop` files.
- [ ] Existing `.loop` files are not overwritten without `--force`.
- [ ] `--force` overwrites existing generated files.
- [ ] Written `.loop` passes `check_loop.py`.
- [ ] Markdown relative links remain valid.
- [ ] Forbidden theory/protocol/template/workflow dirs are unchanged.

## Evidence Required Each Round

- Codex completion report.
- Commands run and outputs.
- Positive and negative CLI checks.
- `git diff --name-only` and forbidden path check.
