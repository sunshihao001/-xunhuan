# Demand Contract - Productization v0.1

Version: v0.1  
Status: first productization contract  
Owner model: Human direction, Hermes compilation, Codex bounded execution, Verifier evidence gate

---

## Goal

Compile the accepted AI workflow theory into the first narrow productization slice. The contract exists to move the repository from theory documents toward an executable source-of-truth layer that future Hermes, Codex, and Verifier rounds can use without reinterpreting the whole theory stack.

The immediate product goal is:

```text
Create a browsable productization source-of-truth layer that turns the current
theory stack into a concrete execution surface for future loops.
```

## Real Objective

The real objective is not to add another explanatory essay or another CLI. The objective is to make future productization work easier to route, execute, and verify by giving each role a clear navigation surface:

- Hermes can identify which documents control the next contract and work order.
- Codex can receive a narrow read-first set and bounded allowed files.
- Verifier can check whether a future implementation follows the theory and source-of-truth map.
- Human can intervene only at value, boundary, risk, or scope gates.
- Feedback has an explicit destination instead of remaining only in chat.

## Problem World

The repository already contains accepted theory and connection documents:

- `AI_WORKFLOW_THEORY_V0_1.md`
- `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
- `RESEARCH_TO_PRODUCT_LOOP.md`
- `THEORY_TO_PRODUCT_CONNECTION.md`
- `PRODUCTIZATION_LOOP_V0_1.md`
- `AI_WORKFLOW_CONTROL_MODEL.md`
- `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md`

These documents define a coherent operating model, but they are still spread across several files. A future executor could read too much, miss the controlling order, treat theory as implementation, or expand into tools before the product surface is defined. The first product slice must therefore be a source-of-truth layer that organizes the current documents into an execution-facing route.

## Scope

This contract covers one documentation product slice only:

- Create `PRODUCTIZATION_SOURCE_OF_TRUTH.md`.
- Create `PRODUCTIZATION_EXECUTION_INDEX.md`.
- Optionally update `INDEX.md` so future actors can find the new productization surface.
- Preserve the no-CLI, no-dependency, no-commit boundary.
- Keep all changes in explicitly allowed files for the next round.

## Non-Goals

This contract does not authorize:

- creating CLI tools,
- adding scripts,
- adding dependencies,
- changing protocol, template, runner, verifier, workflow, knowledge base, trial, script, test, or docs directories,
- implementing guarded writer behavior,
- reorganizing the repository,
- rewriting the accepted theory,
- making product architecture decisions outside the selected source-of-truth slice,
- committing changes.

## Product slice Definition

The selected Product slice is a browsable productization source-of-truth layer.

It should answer five execution questions in concrete form:

1. Which documents are source-of-truth for productization?
2. What order should Hermes read them in when compiling the next contract or work order?
3. What should Codex receive for a bounded implementation round?
4. What should Verifier check before accepting a round?
5. Where should feedback, risks, and learnback candidates go?

The slice is intentionally narrow. It does not build automation. It creates the execution surface that later automation or implementation rounds can rely on.

## Inputs

Read-first inputs for the implementation slice:

- `AI_WORKFLOW_THEORY_V0_1.md`
- `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
- `RESEARCH_TO_PRODUCT_LOOP.md`
- `THEORY_TO_PRODUCT_CONNECTION.md`
- `PRODUCTIZATION_LOOP_V0_1.md`
- `AI_WORKFLOW_CONTROL_MODEL.md`
- `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md`
- `DEMAND_CONTRACT_PRODUCTIZATION_V0_1.md`
- `CODEX_WORK_ORDER_PRODUCT_SLICE_V0_1.md`
- `INDEX.md`

## Outputs

Required outputs for the implementation slice:

- `PRODUCTIZATION_SOURCE_OF_TRUTH.md`
  - Names the controlling source-of-truth documents.
  - Separates theory, control model, execution playbook, productization contract, and loop state roles.
  - States the order Hermes should read them.
  - States which subset Codex should receive for bounded future work.
  - States what Verifier should check.
  - States where feedback and learnback go.

- `PRODUCTIZATION_EXECUTION_INDEX.md`
  - Provides a concise browsable index for future productization rounds.
  - Maps artifacts to role, owner, gate, and downstream use.
  - Identifies the current next executable round.
  - Includes stop-state and HumanGate routing guidance.

- `INDEX.md`
  - Links the two new productization documents under Product or Workflow.

## Responsibilities

### Human

The Human owns direction, value judgment, hard boundaries, and HumanGate decisions. The Human decides whether the selected product slice is worth continuing and whether any future scope expansion into tools, dependencies, forbidden paths, or irreversible actions is acceptable.

### Hermes

Hermes owns contract compilation, work order drafting, verification review, feedback routing, and learnback selection. Hermes should use this contract to keep the next round narrow and should not ask the Human for mechanical repairs that are already authorized and verifiable.

### Codex

Codex owns bounded execution of the next work order. Codex must read the specified files, create or update only allowed files, avoid forbidden paths, run required verification, and return evidence. Codex must not redefine the product, create CLI tools, add dependencies, or decide HumanGate outcomes.

### Verifier

Verifier owns evidence checks. Verifier checks file existence, content coverage, diff scope, forbidden path stability, semantic fit with this contract, and whether the completion report names real risks. Verifier treats Codex self-report as evidence to inspect, not as acceptance.

## Acceptance Criteria

The implementation slice is accepted when:

- `PRODUCTIZATION_SOURCE_OF_TRUTH.md` exists and is substantial enough to guide future Hermes, Codex, and Verifier rounds.
- `PRODUCTIZATION_EXECUTION_INDEX.md` exists and provides a browsable execution index rather than repeating all theory.
- `INDEX.md` links the new productization documents.
- The new documents identify source-of-truth documents, read order, Codex handoff, Verifier checks, and feedback destination.
- The new documents include the stop states Done, DoneWithRisk, Blocked, HumanGate, and Repair.
- The diff touches only allowed files.
- Forbidden files and directories are unchanged.
- No CLI tools, dependencies, scripts, tests, docs, or commits are created.

## Verification Plan

The next round must run and report:

```bash
python - <<'PY'
from pathlib import Path
files = [
  'PRODUCTIZATION_SOURCE_OF_TRUTH.md',
  'PRODUCTIZATION_EXECUTION_INDEX.md',
  'INDEX.md',
]
for f in files:
    p = Path(f)
    assert p.exists(), f'missing {f}'
    assert p.stat().st_size > 1000, f'too small {f}'
print('productization source-of-truth artifacts exist')
PY
python - <<'PY'
from pathlib import Path
terms = [
  'source-of-truth',
  'Hermes',
  'Codex',
  'Verifier',
  'HumanGate',
  'DoneWithRisk',
  'Blocked',
  'Repair',
  'feedback',
  'learnback',
]
text = '\n'.join(Path(f).read_text(encoding='utf-8', errors='replace') for f in [
  'PRODUCTIZATION_SOURCE_OF_TRUTH.md',
  'PRODUCTIZATION_EXECUTION_INDEX.md',
])
missing = [t for t in terms if t not in text]
assert not missing, missing
print('productization source-of-truth coverage passed')
PY
git diff --name-only
```

The Verifier must also inspect `git diff --name-only` and confirm that only allowed files changed.

## Stop Conditions

- **Done**: Required artifacts exist, verification passes, `INDEX.md` links the new docs, no forbidden paths changed, and no material unresolved risk remains.
- **DoneWithRisk**: The artifacts are usable, but a named semantic risk, incomplete check, or downstream ambiguity remains.
- **Blocked**: Required source files are missing, unreadable, or contradictory in a way that prevents honest compilation.
- **HumanGate**: The next step would expand scope, modify forbidden paths, create CLI tools, add dependencies, commit, or decide product value beyond this contract.
- **Repair**: Verification fails, but the fix is bounded to the allowed files and does not require a HumanGate decision.

## Learnback Target

Learnback from the implementation slice should target future workflow behavior, not broad theory. Candidate learnback destinations:

- update future work order structure when the source-of-truth map reveals missing fields,
- add Verifier checks if future rounds miss the read order or feedback route,
- create a workflow patch candidate if the source-of-truth layer materially improves future productization execution,
- record DoneWithRisk causes when a source document remains ambiguous or poorly connected.

This contract is complete when it enables the next Codex work order to implement the selected source-of-truth layer without needing to infer product strategy from the whole repository.
