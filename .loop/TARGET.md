# TARGET

## Target

v0.6 adds a read-only higher-level intent compiler CLI: `scripts/compile_loop.py`.

## Value

Xunhuan can now take a compact loop brief / demand contract and compile it into a proposed `.loop/` package shape without mutating files. This is the first step toward a true loop brief compiler instead of only per-file CLIs.

## Human Role

Provide a concise intent brief and approve any future write-mode expansion explicitly.

## Agent Role

Hermes compiles this v0.6 bounded loop, attempts Codex execution, verifies independently, commits, pushes, and updates loop state.

## Non-goals

- Do not write files from the compiler.
- Do not execute agents.
- Do not run shell commands from the compiler.
- Do not introduce external dependencies.
