# CODEX WORK ORDER - Creator Workflow Theory v1

## Objective

Expand `CREATOR_WORKFLOW_IDEA_FRAMEWORK.md` into a professional creator-first AI workflow theory and application system.

This is a theory and scenario expansion round. Do not create CLI tools. Do not implement UI code. Do not add dependencies. Do not commit.

## Read first

Read these files before writing:

- `CREATOR_WORKFLOW_IDEA_FRAMEWORK.md`
- `CORE_PRINCIPLES.md`
- `CORE_PRINCIPLES_THEORY.md`
- `CORE_PRINCIPLES_APPLICATION_MATRIX.md`
- `CREATOR_FIRST_WORKFLOW_MODEL.md`
- `ENCAPSULATED_WORKFLOW_REQUIREMENTS.md`
- `AI_WORKFLOW_THEORY_V0_1.md`
- `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
- `WORKFLOW_THEORY_AUDIT_BRIEF.md`
- `workflow_audit_research/kb/stable_conclusions.md`
- `workflow_audit_research/workflow/patch_candidates.md`

## Required output artifacts

Create:

1. `CREATOR_WORKFLOW_THEORY_V1.md`
   - Full professional theory of the creator-first AI workflow operating system.
   - Explain product philosophy, product boundary theory, user role, system role, encapsulation, and internal rigor.
   - Explain how idea/direction/satisfaction/correction maps to Hermes/Codex/Loop/Verifier/Research/Knowledge Base.
   - Explain how HumanGate protects user authority.
   - Explain how evidence and verification prevent false completion.
   - Explain how theory drives productization.

2. `CREATOR_WORKFLOW_OPERATING_MODEL.md`
   - Define the operating model from idea intake to final correction.
   - Include lifecycle stages, internal subsystem responsibilities, stop states, feedback routing, and learnback.
   - Include concise tables for user-facing state vs internal state.

3. `CREATOR_WORKFLOW_SCENARIOS.md`
   - Map the theory to practical scenarios.
   - Include at least the 20 scenarios listed in `CREATOR_WORKFLOW_IDEA_FRAMEWORK.md`.
   - For each scenario include: user sees, Hermes does, Codex does if involved, Loop preserves, Verifier checks, KB/Research receives, HumanGate trigger, acceptance signal.

4. `CREATOR_WORKFLOW_ANTI_PATTERNS.md`
   - List failure modes and anti-patterns.
   - Include: user forced to operate internals, Codex free-running, verifier skipped, research promoted too early, theory document drift, HumanGate overuse, HumanGate bypass, context overload, satisfaction ignored, implementation before demand.
   - For each anti-pattern include prevention and verifier signal.

5. Update `INDEX.md`
   - Link all new artifacts under Product.

## Allowed files

- `CREATOR_WORKFLOW_THEORY_V1.md`
- `CREATOR_WORKFLOW_OPERATING_MODEL.md`
- `CREATOR_WORKFLOW_SCENARIOS.md`
- `CREATOR_WORKFLOW_ANTI_PATTERNS.md`
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

- Preserve creator-first positioning.
- Be professional and systematic, not slogan-only.
- Use clear headings, tables, and scenario mappings.
- Make every theory section connect to productization behavior.
- Do not assume the user is technical.
- Do not weaken internal rigor.
- Do not repeat existing files verbatim; synthesize them.
- Keep candidate workflow patches as candidates unless explicitly accepted.

## Required verification

Run and report:

```bash
python - <<'PY'
from pathlib import Path
files = [
  'CREATOR_WORKFLOW_THEORY_V1.md',
  'CREATOR_WORKFLOW_OPERATING_MODEL.md',
  'CREATOR_WORKFLOW_SCENARIOS.md',
  'CREATOR_WORKFLOW_ANTI_PATTERNS.md',
  'INDEX.md',
]
for f in files:
    p = Path(f)
    assert p.exists(), f'missing {f}'
    assert p.stat().st_size > 1000, f'too small {f}'
print('creator theory v1 artifacts exist')
PY
python - <<'PY'
from pathlib import Path
terms = ['creator-first','Hermes','Codex','Loop','Verifier','Knowledge Base','HumanGate','satisfaction','scenario','anti-pattern','productization']
text = '\n'.join(Path(f).read_text(encoding='utf-8', errors='replace') for f in [
  'CREATOR_WORKFLOW_THEORY_V1.md',
  'CREATOR_WORKFLOW_OPERATING_MODEL.md',
  'CREATOR_WORKFLOW_SCENARIOS.md',
  'CREATOR_WORKFLOW_ANTI_PATTERNS.md',
])
missing = [t for t in terms if t not in text]
assert not missing, missing
print('creator theory v1 coverage passed')
PY
git diff --name-only
```

Also verify forbidden paths are unchanged.

## Completion report

Return:

- Files created/updated.
- Summary of professional theory produced.
- Scenario coverage summary.
- Anti-patterns identified.
- Verification commands and results.
- Stop state: Done / DoneWithRisk / Blocked / HumanGate / Repair.

## Stop states

- Done: all required artifacts exist, coverage passes, forbidden paths unchanged, and theory maps to scenarios.
- DoneWithRisk: artifacts are usable but a named theory/scenario gap remains.
- Blocked: required input files are missing or contradictory.
- HumanGate: scope expansion, implementation, or product-direction decision is required.
- Repair: verification fails but can be fixed inside allowed files.
