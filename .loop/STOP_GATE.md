# STOP_GATE

## Done

All acceptance checks pass, docs are updated, and forbidden paths are unchanged.

## DoneWithRisk

Core planner works, but a documented non-blocking parsing limitation remains.

## Blocked

Stop if requirements imply autonomous execution beyond the read-only planning boundary.

## HumanGate

Stop before adding real agent execution, shell command execution, git writes, secrets, or production side effects to `plan_next.py`.
