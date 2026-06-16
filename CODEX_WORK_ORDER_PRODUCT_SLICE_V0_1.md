# CODEX WORK ORDER - Productization Source-of-Truth Slice v0.1

## Objective

Create the first implementation product slice for the productization loop:

```text
Create a browsable productization source-of-truth layer that turns the current
theory stack into a concrete execution surface for future loops.
```

Do not implement automation. Do not create CLI tools. Do not add dependencies. Do not commit. Do not expand scope beyond the files named in this work order.

## Read First

Read these files before editing:

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

Use the demand contract as the controlling scope. Use the theory files as inputs, not as permission to broaden the product.

## Product slice

The selected Product slice is a documentation source-of-truth layer for future productization rounds.

It must summarize:

- which documents are source-of-truth,
- what order Hermes should read them,
- what Codex should receive,
- what Verifier should check,
- where feedback goes.

The slice should be practical and browsable. It should avoid repeating all theory. It should map the current document stack into execution decisions for future loops.

## Required Output Artifacts

1. `PRODUCTIZATION_SOURCE_OF_TRUTH.md`
   - Define the source-of-truth stack for productization.
   - Group source documents by role: theory, control, playbook, productization, knowledge, loop handoff.
   - State the read order for Hermes.
   - State the curated handoff set for Codex.
   - State Verifier evidence checks.
   - State feedback and learnback routes.
   - Include stop conditions: Done, DoneWithRisk, Blocked, HumanGate, Repair.

2. `PRODUCTIZATION_EXECUTION_INDEX.md`
   - Provide a browsable index for future productization execution.
   - Include an artifact map with document, owner, purpose, gate, and downstream use.
   - Identify the current next executable round.
   - Include HumanGate triggers and Verifier gates.
   - Make clear that this is not a CLI, not implementation automation, and not a new theory layer.

3. `INDEX.md`
   - Add links to `PRODUCTIZATION_SOURCE_OF_TRUTH.md` and `PRODUCTIZATION_EXECUTION_INDEX.md` under Product or Workflow.
   - Keep existing links intact.

## Allowed Files

The only allowed files for this implementation slice are:

- `PRODUCTIZATION_SOURCE_OF_TRUTH.md`
- `PRODUCTIZATION_EXECUTION_INDEX.md`
- `INDEX.md`

## Forbidden Files and Directories

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
- `docs/`
- `.loop/`
- any file not listed under allowed files

## Hard Constraints

- Do not create CLI tools.
- Do not add dependencies.
- Do not commit.
- Do not rewrite the accepted theory.
- Do not modify forbidden paths.
- Do not turn this into a broad product architecture pass.
- Do not add implementation code.
- Do not treat Codex self-report as verification.

## Content Requirements

The new artifacts must be concrete and executable for future loop work. They should answer:

- How does this connect to the overall workflow?
- What does Hermes read and compile?
- What does Codex receive and execute?
- What does Verifier check?
- When should HumanGate be triggered?
- Where do feedback and learnback go?

Use concise sections and tables where helpful. Avoid copying large blocks from the source theory. This slice should make the theory easier to use, not longer to read.

## Required Verification

Run and report:

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

Also verify forbidden paths are unchanged by inspecting `git diff --name-only`. The only expected changed files are:

- `PRODUCTIZATION_SOURCE_OF_TRUTH.md`
- `PRODUCTIZATION_EXECUTION_INDEX.md`
- `INDEX.md`

## Completion Report

Return:

- Files created/updated.
- Product slice advanced.
- How the new artifacts connect theory to next execution.
- Verification commands and results.
- Forbidden path check result.
- Stop state: Done, DoneWithRisk, Blocked, HumanGate, or Repair.
- Any risks or remaining gaps.

## Stop Conditions

- **Done**: All required artifacts exist, checks pass, changed files are limited to allowed files, and no material unresolved risk remains.
- **DoneWithRisk**: The source-of-truth layer is usable, but a named risk or incomplete semantic check remains.
- **Blocked**: A required read-first file is missing or unreadable, or the repository state prevents verification.
- **HumanGate**: Any next action requires scope expansion, forbidden path changes, CLI tools, dependencies, commits, or product direction judgment.
- **Repair**: Verification fails but the fix is bounded to the allowed files in this work order.
