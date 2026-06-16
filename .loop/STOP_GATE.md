# STOP_GATE

## Done

All acceptance checks pass, docs are updated, and forbidden paths are unchanged.

## DoneWithRisk

Core runner works, but a documented non-blocking limitation remains.

## Blocked

Stop if repository auth fails or requirements imply autonomous execution beyond the safe bootstrap boundary.

## HumanGate

Stop before adding real agent execution, shell command execution, git writes, secrets, or production side effects to `run_loop.py`.
