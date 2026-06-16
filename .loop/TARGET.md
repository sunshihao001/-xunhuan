# TARGET

## Target

v0.4 adds a safe Loop Bootstrap Runner CLI: `scripts/run_loop.py`.

## Value

Xunhuan can initialize a loop, check a loop, and now summarize the current loop execution state without launching autonomous agents. This creates a safe bridge from static loop files to an executable loop lifecycle.

## Human Role

Approve only scope expansions such as fully autonomous execution, secrets, or production side effects.

## Agent Role

Hermes compiles this v0.4 bounded loop, attempts Codex execution, verifies independently, commits, pushes, and updates loop state.

## Non-goals

- Do not build a fully autonomous runner.
- Do not invoke Codex, Hermes, shell commands, git, or external tools from `run_loop.py`.
- Do not mutate `.loop/` files from `run_loop.py`.
- Do not introduce external dependencies.
