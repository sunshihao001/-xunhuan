# TARGET

## Target

v0.3 adds a minimal runnable Loop Verifier CLI: `scripts/check_loop.py`.

## Value

Xunhuan can not only initialize `.loop/` workspaces, but also verify whether an existing `.loop/` workspace is structurally complete and ready for a bounded agent round.

## Human Role

Define product direction and approve broad scope changes only if required.

## Agent Role

Hermes compiles this bounded loop, delegates implementation to Codex, independently verifies behavior, commits, pushes, and updates loop state.

## Non-goals

- Do not build a full loop runner.
- Do not execute agent work orders automatically.
- Do not alter core theory/protocol/template/workflow directories unless documentation links require it.
- Do not introduce external dependencies.
