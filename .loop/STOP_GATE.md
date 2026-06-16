# STOP_GATE

## Done

All acceptance checks pass, docs are updated, forbidden paths are unchanged, and remote push succeeds.

## DoneWithRisk

Core write mode works, but a documented non-blocking edge case remains.

## Blocked

Stop if Codex cannot run, tests cannot execute, or write-mode requirements require unsafe behavior.

## HumanGate

Stop before adding autonomous execution, deleting user files, writing outside the requested target directory, or changing core protocol/template directories.
