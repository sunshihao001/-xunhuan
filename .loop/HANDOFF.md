# HANDOFF

## Final status

Done.

## What changed

v0.8 adds a research evidence pack initializer:

```bash
python scripts/init_research_pack.py --name <pack-name> --dir <target-dir> --question <cognition-question>
python scripts/init_research_pack.py --name <pack-name> --dir <target-dir> --question <cognition-question> --dry-run
python scripts/init_research_pack.py --name <pack-name> --dir <target-dir> --question <cognition-question> --force
```

It creates a layered pack:

```text
raw/
raw/source_captures/
clean/
reading/
insights/
kb/
workflow/
```

and starter files:

```text
README.md
clean/sources.json
clean/source_quality.md
insights/synthesis.md
kb/stable_conclusions.md
workflow/patches.md
workflow/next_execution_plan.md
```

## Evidence

Verifier evidence passed:

- `python scripts/init_research_pack.py --help`
- `python -m py_compile scripts/init_research_pack.py`
- `python tests/test_init_research_pack.py -v`
- `python tests/test_compile_loop.py -v`
- `python tests/test_plan_next.py -v`
- `python tests/test_run_loop.py -v`
- `python tests/test_check_loop.py -v`
- positive init path
- overwrite refusal path
- `--force` path
- `--dry-run` non-write path
- Markdown link check
- forbidden path diff check

## Risks

This initializes evidence packs only. It does not crawl the web, build a RAG/vector store, or automatically promote evidence into stable knowledge.

## Resume instructions

Recommended next loop: v0.9 research pack checker. After that, add source capture/import and promotion-gate tooling.
