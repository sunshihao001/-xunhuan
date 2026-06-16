# TARGET

## Target

v0.7 adds guarded write mode to `scripts/compile_loop.py`.

## Value

Xunhuan moves from read-only proposal to controlled loop materialization: a high-level intent can become real `.loop/` files only when an explicit write flag is provided.

## Human Role

Approve guarded write-mode semantics and ensure future destructive writes remain behind explicit flags.

## Agent Role

Hermes compiles this v0.7 bounded loop, Codex executes implementation, Hermes verifies independently, commits, pushes, and updates loop state.

## Non-goals

- Do not add autonomous agent execution.
- Do not run shell commands from intent briefs.
- Do not overwrite existing `.loop` files without `--force`.
- Do not introduce external dependencies.
