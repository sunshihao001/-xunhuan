# ACCEPTANCE

## Final Done Criteria

- [ ] `python scripts/init_research_pack.py --help` succeeds.
- [ ] `python -m py_compile scripts/init_research_pack.py` succeeds.
- [ ] `python tests/test_init_research_pack.py -v` passes.
- [ ] Existing compile/check/run/plan tests still pass.
- [ ] Initializer creates `raw/`, `clean/`, `reading/`, `insights/`, `kb/`, and `workflow/` under a target pack directory.
- [ ] Initializer writes a root `README.md` explaining the cognition question, layer meanings, and promotion gate.
- [ ] Initializer writes starter files for source inventory and workflow patches.
- [ ] Existing files are not overwritten without `--force`.
- [ ] `--dry-run` previews without writing.
- [ ] Markdown links remain valid.
- [ ] Forbidden core theory/protocol/template/workflow dirs are unchanged.

## Evidence Required Each Round

- Codex completion report.
- Commands run and outputs.
- Positive and negative CLI checks.
- `git diff --name-only` and forbidden path check.
