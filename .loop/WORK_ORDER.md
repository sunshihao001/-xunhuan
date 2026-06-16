# WORK_ORDER - Non-Expert Creator Workflow Encapsulation Round

## Context

The user clarified an important product principle:

> The user is not a professional AI programming person and may not understand many technical parts. The workflow should encapsulate scattered capabilities so the user only needs to create ideas, adjust the broad direction, and judge satisfaction with the finished product before requesting changes.

This changes the product model. The current repo contains many powerful but scattered assets: demand interrogation, external research, knowledge pipeline, Codex work orders, loop state, verifier gates, audit packs, and productization contracts. These must be wrapped into a creator-facing operating model.

## Objective

Create a creator-facing encapsulation model for the AI workflow. The model should define what the user should and should not need to operate, and how Hermes should hide internal complexity behind simple stages and feedback loops.

This is documentation/product-model work. Do not create CLI tools. Do not add dependencies. Do not implement UI.

## Read first

- `AI_WORKFLOW_THEORY_V0_1.md`
- `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
- `THEORY_TO_PRODUCT_CONNECTION.md`
- `PRODUCTIZATION_LOOP_V0_1.md`
- `DEMAND_CONTRACT_PRODUCTIZATION_V0_1.md`
- `workflow_audit_research/workflow/patch_candidates.md`
- `workflow_audit_research/kb/stable_conclusions.md`
- `WORKFLOW_THEORY_AUDIT_BRIEF.md`

## Required output artifacts

1. `CREATOR_FIRST_WORKFLOW_MODEL.md`
   - Define the user's role as creator / direction owner / satisfaction judge.
   - Define what the user should not need to understand: prompt engineering, Codex, loop files, verifier implementation, research pack internals, git details.
   - Define what the system should encapsulate.
   - Explain the difference between internal engineering workflow and user-facing workflow.
   - Include a simple user-facing loop: idea → direction check → system execution → artifact preview → satisfaction feedback → correction.

2. `ENCAPSULATED_WORKFLOW_REQUIREMENTS.md`
   - Convert the principle into product requirements.
   - Include functional requirements for Hermes, Codex, Loop, Verifier, Knowledge Base, and Research.
   - Include non-goals.
   - Include acceptance criteria.
   - Include HumanGate rules from a non-technical user perspective.
   - Include what feedback should look like: “满意 / 不满意 / 方向错 / 细节错 / 继续深化 / 停止”.

3. Update `INDEX.md`
   - Link both new artifacts under Product.

4. Optional: update `.loop/STATE.md`, `.loop/LOOP_LOG.md`, `.loop/HANDOFF.md` with this round's state.

## Allowed files

- `CREATOR_FIRST_WORKFLOW_MODEL.md`
- `ENCAPSULATED_WORKFLOW_REQUIREMENTS.md`
- `INDEX.md`
- `.loop/STATE.md`
- `.loop/LOOP_LOG.md`
- `.loop/HANDOFF.md`

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
- `workflow_audit_research/`
- root theory/contract files not listed in allowed files

## Content requirements

- Write in clear language suitable for a non-professional AI programming user.
- Do not reduce the system's internal rigor; hide complexity behind product boundaries.
- Make it clear that the user should not have to manually operate demand interrogation, research collection, Codex, `.loop`, verifier, or git.
- Preserve HumanGate: the user still decides direction, risk, value, scope, satisfaction, and major corrections.
- Define how the system should report back: concise product status, evidence summary, what changed, what needs feedback.
- Include a warning that the current repo is still building this encapsulation and not yet a finished UI/product.

## Required verification before returning

Run and report:

```bash
python - <<'PY'
from pathlib import Path
files = ['CREATOR_FIRST_WORKFLOW_MODEL.md','ENCAPSULATED_WORKFLOW_REQUIREMENTS.md','INDEX.md']
for f in files:
    p = Path(f)
    assert p.exists(), f'missing {f}'
    assert p.stat().st_size > 1000, f'too small {f}'
print('creator workflow artifacts exist')
PY
python - <<'PY'
from pathlib import Path
terms = ['creator','direction','satisfaction','Hermes','Codex','Loop','Verifier','Knowledge Base','HumanGate','encapsulate']
text = '\n'.join(Path(f).read_text(encoding='utf-8', errors='replace') for f in ['CREATOR_FIRST_WORKFLOW_MODEL.md','ENCAPSULATED_WORKFLOW_REQUIREMENTS.md'])
missing = [t for t in terms if t not in text]
assert not missing, missing
print('creator workflow coverage passed')
PY
git diff --name-only
```

Also verify forbidden paths are unchanged.

## Completion report

Return:

- Files created/updated.
- How the user's role changed in the model.
- What complexity is now marked for encapsulation.
- Verification results.
- Stop state.
