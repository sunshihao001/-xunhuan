# WORK_ORDER

## Task name

Creator MVP Loop Demand Contract V0.1

## Read first

Codex must read these files before writing:

- `CREATOR_INTERFACE_CONTRACT_V0_1.md`
- `CREATOR_WORKFLOW_THEORY_V1.md`
- `CREATOR_WORKFLOW_OPERATING_MODEL.md`
- `CREATOR_WORKFLOW_SCENARIOS.md`
- `CREATOR_WORKFLOW_ANTI_PATTERNS.md`
- `CORE_PRINCIPLES.md`
- `DEMAND_CONTRACT_TEMPLATE.md`
- `CODEX_WORK_ORDER_PRODUCT_SLICE_V0_1.md`
- `PRODUCTIZATION_LOOP_V0_1.md`
- `INDEX.md`

## Demand cognition expression

### real_objective

Compile the creator-facing interface contract into an implementation-ready MVP demand contract, without implementing the UI yet. The contract must define the first minimal product slice that Codex can later build while preserving creator-first boundaries and hiding internal machinery.

### problem_world

The repository now has theory, scenarios, anti-patterns, operating model, and an interface contract. The next risk is premature implementation: Codex could build a UI/prototype before the MVP slice, file scope, acceptance checks, HumanGate triggers, state model, and verifier gates are explicit. This round must produce the final demand contract before implementation.

### convergence_slice

Create one implementation-ready demand contract that turns `CREATOR_INTERFACE_CONTRACT_V0_1.md` into a bounded MVP slice. It should be specific enough for a future Codex implementation work order, but must not itself implement UI/code.

## Objective

Create `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md` and update `INDEX.md` so the next stage can safely move from docs/spec into a bounded MVP implementation work order.

## Required content in `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`

The document must include at least these sections:

1. Purpose and source contract
2. MVP product slice name and thesis
3. Real objective / problem world / convergence slice
4. User-facing flow: idea intake → direction check → executing/status → preview → satisfaction feedback → correction/stop
5. Internal routing flow: Hermes → Demand Contract → Loop → Codex → Verifier → feedback/learnback
6. Explicit user role and system role boundaries
7. Allowed future implementation surface, expressed as categories rather than exact files if the codebase does not exist yet
8. Forbidden future implementation scope
9. MVP states and transitions
10. Required creator-facing controls: approve / adjust / reject / continue / stop
11. HumanGate triggers
12. Evidence and verifier requirements
13. Acceptance criteria for future implementation
14. Failure modes / anti-patterns to prevent
15. Open decisions before implementation
16. Suggested next Codex implementation work order

## Important requirements

- Keep this as a demand contract, not an implementation.
- Do not create UI/code/scripts/tests.
- Use the interface contract as the source of truth.
- Keep creator-facing simplicity and internal rigor separated.
- Make the next implementation stage concrete enough to run as a bounded Codex task.
- If exact implementation files are not yet known, define an allowed implementation surface by artifact categories, for example: prototype doc, single HTML mockup, local web prototype, or future app surface. Do not invent a large app architecture.

## Allowed files

Codex may modify only:

- `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`
- `INDEX.md`

## Forbidden files and paths

Do not modify:

- `00_CONCEPT/`
- `01_PROTOCOL/`
- `02_TEMPLATES/`
- `03_RUNNERS/`
- `04_VERIFIERS/`
- `05_WORKFLOWS/`
- `06_KNOWLEDGE_BASE/`
- `07_TRIALS/`
- `scripts/`
- `tests/`
- `README.md`
- existing creator theory/interface files unless explicitly required
- `.loop/` files
- `.codex/`

## Non-goals

- Do not implement UI.
- Do not write code.
- Do not create scripts or tests.
- Do not redesign the full Loop OS.
- Do not add external research.
- Do not commit changes.

## Acceptance criteria

- `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md` exists and is substantive.
- `INDEX.md` links to the new document.
- The document explicitly names the next product slice.
- It includes user-facing flow, internal routing flow, roles, states, controls, HumanGate triggers, verifier requirements, future implementation acceptance criteria, anti-patterns, open decisions, and next Codex work order.
- It does not implement UI/code.
- Only allowed files are modified.

## Required completion report from Codex

Return:

1. Files changed
2. Summary of demand contract design
3. How this makes the next implementation round safe and bounded
4. Any risks or open questions
5. Suggested next bounded work order
