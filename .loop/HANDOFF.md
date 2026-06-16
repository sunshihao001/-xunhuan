# HANDOFF

## Final status

Done.

## What changed

v0.4 adds a safe read-only Loop Bootstrap Runner CLI:

```bash
python scripts/run_loop.py --dir <target-project>
python scripts/run_loop.py --dir <target-project> --json
```

It reuses `check_loop.py`, reads `.loop/STATE.md`, extracts `status`, `round`, and `## Next action`, and points to `.loop/WORK_ORDER.md` with a short work-order title.

It explicitly does not execute agents or mutate files.

## Evidence

Verifier evidence passed:

- `python scripts/run_loop.py --help`
- `python -m py_compile scripts/run_loop.py`
- `python scripts/check_loop.py --dir .`
- `python scripts/run_loop.py --dir .`
- `python tests/test_run_loop.py -v`
- `python tests/test_check_loop.py -v`
- fresh `init_loop.py` + `run_loop.py` positive path
- `run_loop.py --json | python -m json.tool`
- invalid `.loop` negative path
- `.loop` read-only hash check
- Markdown relative link check
- forbidden path diff check

## Risks

Codex CLI could not run because of usage limits, so Hermes executed implementation directly with TDD-style verifier evidence. This is recorded in `LOOP_LOG.md`.

There are untracked top-level files (`AI_WORKFLOW_MAP.md`, `AI_WORKFLOW_ROUTER.md`) in the working tree that were not part of this loop and were intentionally not staged for the v0.4 commit.

## Resume instructions

Recommended next loop: v0.5 guarded planner/checklist mode. Keep it read-only by default: convert `WORK_ORDER.md` into a verifier/execution checklist, but do not launch Codex or shell commands without explicit HumanGate approval.
