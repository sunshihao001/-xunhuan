# WORK_ORDER

## Task name

Creator Interface Contract V0.1

## Read first

Codex must read these files before writing:

- `CREATOR_WORKFLOW_THEORY_V1.md`
- `CREATOR_WORKFLOW_OPERATING_MODEL.md`
- `CREATOR_WORKFLOW_SCENARIOS.md`
- `CREATOR_WORKFLOW_ANTI_PATTERNS.md`
- `CREATOR_WORKFLOW_IDEA_FRAMEWORK.md`
- `CORE_PRINCIPLES.md`
- `THEORY_TO_PRODUCT_CONNECTION.md`
- `PRODUCTIZATION_LOOP_V0_1.md`
- `INDEX.md`

## Demand cognition expression

### real_objective

Turn the completed creator-first theory into a creator-facing product interface contract that defines what the user sees, what the system hides, how intent/status/preview/feedback/HumanGate are expressed, and how creator feedback routes back into Loop/Codex/Verifier/Knowledge Base.

### problem_world

The repository now has a professional creator-first theory layer. The next risk is product drift: either exposing internal machinery to a non-technical creator, or jumping into implementation before defining the user-facing interface contract. This round must bridge theory to product without writing code or expanding theory for its own sake.

### convergence_slice

Create the first complete interface contract for the future MVP. It should be concrete enough to drive a later Codex product-slice implementation, but still remain a design/spec artifact.

## Objective

Create `CREATOR_INTERFACE_CONTRACT_V0_1.md` and update `INDEX.md` so the repository has a clear product interface contract between creator-facing surface and internal Hermes/Codex/Loop/Verifier machinery.

## Required content in `CREATOR_INTERFACE_CONTRACT_V0_1.md`

The document must include at least these sections:

1. Purpose and product boundary
2. Creator-facing principle
3. User roles / system roles
4. Input contract: what the creator can say or provide
5. Direction-check contract: how the system asks for high-level confirmation only when needed
6. Status contract: what progress/status is visible to the creator
7. Preview contract: how artifacts are shown back to the creator
8. Satisfaction feedback contract: how the creator says approve / adjust / reject / continue / stop
9. Correction routing: how feedback maps to Demand Contract, Loop, Codex rework, Verifier, Research, or KB
10. HumanGate contract: when the system must stop and ask
11. Internal-hidden contract: what details should not be exposed by default
12. Evidence contract: what verification evidence is summarized to the creator
13. Interface state model: minimal states such as Intake, DirectionCheck, Executing, Preview, Feedback, HumanGate, Done, DoneWithRisk, Blocked
14. MVP implications: what a first product slice should implement next
15. Anti-patterns: interface-level failure modes to avoid
16. Verifier checklist: how Hermes can verify this contract was respected

## Allowed files

Codex may modify only:

- `CREATOR_INTERFACE_CONTRACT_V0_1.md`
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
- existing creator theory files unless explicitly required
- `.loop/` files
- `.codex/`

## Non-goals

- Do not implement a UI.
- Do not create scripts or tests.
- Do not redesign the whole Loop OS.
- Do not change the creator-first direction.
- Do not add external research.
- Do not commit changes.

## Acceptance criteria

- `CREATOR_INTERFACE_CONTRACT_V0_1.md` exists and is substantive.
- `INDEX.md` links to the new document.
- The document clearly separates creator-facing surface from internal machinery.
- It defines input, status, preview, feedback, correction routing, HumanGate, evidence, hidden internals, state model, MVP implications, anti-patterns, and verifier checklist.
- It names the next product slice it enables.
- Only allowed files are modified.

## Required completion report from Codex

Return:

1. Files changed
2. Summary of contract design
3. How this bridges theory to MVP/product slice
4. Any risks or open questions
5. Suggested next bounded work order
