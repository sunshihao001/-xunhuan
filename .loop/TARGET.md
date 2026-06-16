# TARGET

## Target

v0.5 adds a guarded plan/checklist compiler CLI: `scripts/plan_next.py`.

## Value

Xunhuan can now convert a bounded `WORK_ORDER.md` from plain Markdown into a structured execution and verifier checklist consumable by humans, Hermes, Codex, or future tools.

## Human Role

Approve only if the scope expands into actual agent execution, shell execution, secrets, or production side effects.

## Agent Role

Hermes compiles this v0.5 bounded loop, attempts Codex execution, verifies independently, commits, pushes, and updates loop state.

## Non-goals

- Do not execute agents.
- Do not execute shell commands from `WORK_ORDER.md`.
- Do not mutate `.loop/` from `plan_next.py`.
- Do not introduce external dependencies.
- Do not build a full runner yet.
