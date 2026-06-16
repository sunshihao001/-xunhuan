# STOP_GATE

## Done

All acceptance checks pass, docs are updated, and forbidden paths are unchanged.

## DoneWithRisk

Core compiler works, but a documented non-blocking parsing limitation remains.

## Blocked

Stop if requirements imply write-mode generation beyond the read-only compiler boundary.

## HumanGate

Stop before adding file writes, agent execution, shell execution, secrets, or production side effects to `compile_loop.py`.
