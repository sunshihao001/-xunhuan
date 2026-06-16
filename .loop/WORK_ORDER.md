# WORK_ORDER - Core Principles Theory and Application Round

## Context

The user clarified the next required move:

> 抓住重点，把需要立为核心的原则确定好；根据现在积累的知识，使用需求拷问端深入研究给出需要立为核心的；根据 Hermes 确认初步想法，由 Codex 完善到专业理论，并根据专业理论落实到具体全部实际应用场景。

This is a theory-to-application round. The purpose is to identify the non-negotiable core principles of the current AI workflow, formalize them into professional theory, and map them to actual usage scenarios.

Do not implement code or CLI tools. Do not add dependencies. Do not modify forbidden paths.

## Objective

Create a core-principles layer for the creator-first AI workflow operating system, then map those principles to concrete practical scenarios.

## Read first

- `CREATOR_FIRST_WORKFLOW_MODEL.md`
- `ENCAPSULATED_WORKFLOW_REQUIREMENTS.md`
- `AI_WORKFLOW_THEORY_V0_1.md`
- `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
- `WORKFLOW_THEORY_AUDIT_BRIEF.md`
- `workflow_audit_research/kb/stable_conclusions.md`
- `workflow_audit_research/workflow/patch_candidates.md`
- `PRODUCTIZATION_LOOP_V0_1.md`
- `DEMAND_CONTRACT_PRODUCTIZATION_V0_1.md`

## Hermes-confirmed initial idea

Use this as the initial frame:

```text
The system must be creator-first. The user is not a professional AI programming operator. The product must encapsulate scattered AI workflow capabilities so the user only needs to provide ideas, adjust direction, judge satisfaction, and request correction. Internally, Hermes, Codex, Loop, Verifier, Research, Knowledge Base, and Git/GitHub can remain professional and rigorous. Externally, the workflow must be simple, creator-facing, and satisfaction-driven.

The key output now is not more scattered documents. It is a set of core principles that can govern all future design, implementation, verification, and productization scenarios.
```

## Required output artifacts

1. `CORE_PRINCIPLES.md`
   - List the core principles that must govern the project.
   - Each principle must include:
     - principle statement
     - why it exists
     - what it forbids
     - what it requires
     - related internal subsystem
     - verifier signal
   - Principles should be concise and memorable.

2. `CORE_PRINCIPLES_THEORY.md`
   - Turn the principles into professional theory.
   - Explain the system as a creator-first AI operating system.
   - Explain how idea/direction/satisfaction maps to Hermes/Codex/Loop/Verifier/KB internals.
   - Explain why encapsulation is not simplification; it is product boundary design.
   - Explain how theory must drive productization, not become document drift.

3. `CORE_PRINCIPLES_APPLICATION_MATRIX.md`
   - Map the principles to real application scenarios.
   - Include at least these scenarios:
     - idea intake
     - demand interrogation
     - external research
     - knowledge-base update
     - Codex long task
     - loop execution
     - verifier review
     - product preview
     - satisfaction feedback
     - correction / repair
     - HumanGate
     - stop / handoff
     - workflow patch promotion
     - future UI / interface
   - For each scenario include:
     - user sees
     - system does internally
     - core principles applied
     - acceptance / verifier signal

4. Update `INDEX.md`
   - Link the three new artifacts under Product.

5. Optional: update `.loop/STATE.md`, `.loop/LOOP_LOG.md`, `.loop/HANDOFF.md`.

## Allowed files

- `CORE_PRINCIPLES.md`
- `CORE_PRINCIPLES_THEORY.md`
- `CORE_PRINCIPLES_APPLICATION_MATRIX.md`
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
- root files not explicitly listed in allowed files

Do not create CLI tools. Do not add dependencies. Do not commit.

## Content requirements

- Be professional, not slogan-only.
- Keep principles few enough to govern: around 8-12 is appropriate.
- Make principles actionable and verifiable.
- Make the user's role simple: idea / direction / satisfaction / correction.
- Make internal responsibilities clear: Hermes / Codex / Loop / Verifier / KB / Research.
- Include actual practical application scenarios, not abstract theory only.
- Tie every principle to later productization.

## Required verification before returning

Run and report:

```bash
python - <<'PY'
from pathlib import Path
files = ['CORE_PRINCIPLES.md','CORE_PRINCIPLES_THEORY.md','CORE_PRINCIPLES_APPLICATION_MATRIX.md','INDEX.md']
for f in files:
    p = Path(f)
    assert p.exists(), f'missing {f}'
    assert p.stat().st_size > 1000, f'too small {f}'
print('core principle artifacts exist')
PY
python - <<'PY'
from pathlib import Path
terms = ['creator-first','Hermes','Codex','Loop','Verifier','Knowledge Base','HumanGate','satisfaction','principle','scenario']
text = '\n'.join(Path(f).read_text(encoding='utf-8', errors='replace') for f in ['CORE_PRINCIPLES.md','CORE_PRINCIPLES_THEORY.md','CORE_PRINCIPLES_APPLICATION_MATRIX.md'])
missing = [t for t in terms if t not in text]
assert not missing, missing
print('core principle coverage passed')
PY
git diff --name-only
```

Also verify forbidden paths are unchanged.

## Completion report

Return:

- Files created/updated.
- List of core principles created.
- How theory maps to practical scenarios.
- Verification results.
- Stop state.
