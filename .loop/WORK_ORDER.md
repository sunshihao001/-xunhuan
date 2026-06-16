# WORK_ORDER - Round 1

## Read first

- `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md`
- `README.md`
- `INDEX.md`
- `scripts/compile_loop.py`
- `tests/test_compile_loop.py`
- `.loop/TARGET.md`
- `.loop/ACCEPTANCE.md`

## Objective

Implement v0.8: a research evidence pack initializer at `scripts/init_research_pack.py`.

## Allowed files

- `scripts/init_research_pack.py`
- `tests/test_init_research_pack.py`
- `docs/INIT_RESEARCH_PACK.md`
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

Create `scripts/init_research_pack.py` using only Python standard library.

CLI behavior:

```bash
python scripts/init_research_pack.py --name <pack-name> --dir <target-dir> --question <cognition-question>
python scripts/init_research_pack.py --name <pack-name> --dir <target-dir> --question <cognition-question> --dry-run
python scripts/init_research_pack.py --name <pack-name> --dir <target-dir> --question <cognition-question> --force
```

Required behavior:

1. Create a research evidence pack directory under `<target-dir>/<pack-name>/`.
2. Create these directories:
   - `raw/`
   - `raw/source_captures/`
   - `clean/`
   - `reading/`
   - `insights/`
   - `kb/`
   - `workflow/`
3. Write root `README.md` explaining:
   - cognition question
   - layer roles
   - promotion gate from evidence to workflow patch
   - Hermes / Codex / Verifier usage
4. Write starter files:
   - `clean/sources.json`
   - `clean/source_quality.md`
   - `insights/synthesis.md`
   - `kb/stable_conclusions.md`
   - `workflow/patches.md`
   - `workflow/next_execution_plan.md`
5. Default behavior must refuse to overwrite existing files.
6. `--force` may overwrite generated files.
7. `--dry-run` previews planned directories/files without writing.
8. Human output should list created or planned paths.
9. JSON output is optional; do not implement unless simple.

Documentation:

- Add `docs/INIT_RESEARCH_PACK.md` with usage, layer meanings, examples, and how it feeds Hermes/Codex/Loop.
- Update README / INDEX to mention the research pack initializer.

## Required verification before returning

Run and report:

```bash
python scripts/init_research_pack.py --help
python -m py_compile scripts/init_research_pack.py
python tests/test_init_research_pack.py -v
python tests/test_compile_loop.py -v
python tests/test_plan_next.py -v
python tests/test_run_loop.py -v
python tests/test_check_loop.py -v
TMPDIR=$(mktemp -d)
python scripts/init_research_pack.py --name ai-workflow-research --dir "$TMPDIR" --question "How should external research become durable AI workflow knowledge?"
python scripts/init_research_pack.py --name ai-workflow-research --dir "$TMPDIR" --question "x" ; test $? -ne 0
python scripts/init_research_pack.py --name ai-workflow-research --dir "$TMPDIR" --question "x" --force
python scripts/init_research_pack.py --name dry --dir "$TMPDIR" --question "x" --dry-run
```

Also verify:

- dry-run does not write files
- Markdown links remain valid
- forbidden directories are unchanged

## Completion report

Return:

- Files changed.
- Commands run with pass/fail status.
- Whether Codex encountered blockers.
- Whether research pack behavior was verified.
- Whether forbidden paths stayed unchanged.
