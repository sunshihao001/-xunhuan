# WORK_ORDER - Theory to Product Connection Round

## User feedback to address

The user approved continued progress but raised a concern:

> After completing the theory, does this feel disconnected from the overall workflow?

Demand interrogation conclusion:

Yes, it can become disconnected if the theory remains only as documentation. The next action must connect the theory artifacts back into an executable productization loop.

## Objective

Create the connection layer that turns the completed theory into an explicit next product-building loop. Do not create CLI tools. Create documentation that answers: how does the new theory drive the next Codex/loop execution round?

## Read first

- `AI_WORKFLOW_THEORY_V0_1.md`
- `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
- `RESEARCH_TO_PRODUCT_LOOP.md`
- `AI_WORKFLOW_CONTROL_MODEL.md`
- `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md`
- `INDEX.md`
- `.loop/HANDOFF.md`

## Required output artifacts

1. `THEORY_TO_PRODUCT_CONNECTION.md`
   - Explain why theory can become disconnected.
   - Explain how to prevent that with explicit artifacts and gates.
   - Map each theory artifact to its role in the next productization loop.
   - Define the connection contract from theory → demand contract → loop → Codex → verifier → feedback.

2. `PRODUCTIZATION_LOOP_V0_1.md`
   - Define the next executable loop to turn the theory into a usable product/system.
   - Include phases, deliverables, allowed owners, verifier gates, and HumanGate triggers.
   - Define a concrete next Codex long-task objective.
   - Include stop states: Done, DoneWithRisk, Blocked, HumanGate, Repair.

3. Update `INDEX.md`
   - Link both new documents under Product or Workflow.

## Allowed files

- `THEORY_TO_PRODUCT_CONNECTION.md`
- `PRODUCTIZATION_LOOP_V0_1.md`
- `INDEX.md`
- `.loop/*` only if needed for state notes

## Forbidden files/directories

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

Do not create CLI tools. Do not add dependencies.

## Content quality requirements

- Do not just repeat the theory.
- Focus on connection: what is the next executable loop and what artifacts carry context.
- Make it clear that theory is not the end state; it is input to productization.
- Include exact next Codex work order direction, but not the full implementation yet.
- Explain when Hermes should ask the user vs continue automatically.

## Required verification before returning

Run and report:

```bash
python - <<'PY'
from pathlib import Path
files = [
  'THEORY_TO_PRODUCT_CONNECTION.md',
  'PRODUCTIZATION_LOOP_V0_1.md',
  'INDEX.md',
]
for f in files:
    p = Path(f)
    assert p.exists(), f'missing {f}'
    assert p.stat().st_size > 1000, f'too small {f}'
print('connection artifacts exist')
PY
python - <<'PY'
from pathlib import Path
terms = ['theory', 'Demand Contract', '.loop', 'Codex', 'Verifier', 'HumanGate', 'productization', 'feedback']
text = '\n'.join(Path(f).read_text(encoding='utf-8', errors='replace') for f in [
  'THEORY_TO_PRODUCT_CONNECTION.md',
  'PRODUCTIZATION_LOOP_V0_1.md',
])
missing = [t for t in terms if t not in text]
assert not missing, missing
print('connection concept coverage passed')
PY
git diff --name-only
```

Also verify forbidden paths are unchanged.

## Completion report

Return:

- Files created/updated.
- How this fixes the user's concern.
- Verification commands and results.
- Any risks or remaining gaps.
