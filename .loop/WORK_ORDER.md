# WORK_ORDER - Workflow External Audit Research Pack Round

## Context

The user approved the workflow theory audit direction. The next correct step is to turn the audit brief and external source candidates into a layered research evidence pack.

This is a research cognition update round, not product implementation and not CLI tooling.

## Objective

Create a durable `workflow_audit_research/` evidence pack that audits the current Hermes + Codex + Loop + Knowledge Base workflow against external literature and practice.

The pack must preserve candidate evidence separately from reading cards, synthesis, stable conclusions, and workflow patch candidates.

## Read first

- `WORKFLOW_THEORY_AUDIT_BRIEF.md`
- `WORKFLOW_EXTERNAL_AUDIT_SOURCES.md`
- `AI_WORKFLOW_THEORY_V0_1.md`
- `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
- `RESEARCH_TO_PRODUCT_LOOP.md`
- `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md`
- `THEORY_TO_PRODUCT_CONNECTION.md`
- `PRODUCTIZATION_LOOP_V0_1.md`

## Required output tree

Create:

```text
workflow_audit_research/
  README.md
  raw/
    source_urls.md
  clean/
    source_candidates.md
  reading/
    S1_loop_engineering.md
    S2_context_engineering.md
    S3_spec_driven_development.md
    S4_human_in_loop_audit_trail.md
  insights/
    workflow_audit_synthesis.md
    risk_register.md
  kb/
    stable_conclusions.md
  workflow/
    patch_candidates.md
    next_research_plan.md
```

Update `INDEX.md` with a link to `workflow_audit_research/README.md`.

## Content requirements

### README.md

- Explain the purpose of the audit pack.
- State that it is not final kb yet.
- Define the reading order.
- Explain raw / clean / reading / insights / kb / workflow promotion gates.

### raw/source_urls.md

- List source URLs, titles, source type, and audit dimension.
- Clearly label as raw/candidate evidence.

### clean/source_candidates.md

- Summarize each candidate source.
- Include relevance, quality, limitations, and use_for.

### reading cards

For each source card include:

- source metadata
- core thesis
- useful claims
- evidence strength
- limits / risks
- relation to current workflow
- audit implications
- candidate workflow patch

### insights/workflow_audit_synthesis.md

Synthesize across sources by audit dimension:

- Loop Engineering
- Context Engineering
- Spec-driven Development
- Human-in-the-loop
- Verifier / maker-checker
- Audit trail / provenance
- Knowledge pipeline

For each dimension include:

- support evidence
- challenge / risk evidence
- current workflow assessment
- improvement direction

### insights/risk_register.md

List current workflow risks:

- risk
- why it matters
- evidence source
- severity
- mitigation
- target artifact to improve

### kb/stable_conclusions.md

Only include cautiously promoted conclusions. It must explicitly state which conclusions are stable enough and which are still candidates.

### workflow/patch_candidates.md

Include workflow patch candidates, not final patches. Each candidate must have:

- patch id
- source evidence
- target artifact / behavior
- proposed change
- verifier gate
- status: candidate

### workflow/next_research_plan.md

Define next research/search steps, including missing source types such as official docs, GitHub repos, academic/industry frameworks, and examples of audit trail schema.

## Allowed files

- `workflow_audit_research/**`
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
- any root theory/contract/work order file except `INDEX.md`

Do not create CLI tools. Do not add dependencies. Do not commit.

## Required verification before returning

Run and report:

```bash
python - <<'PY'
from pathlib import Path
required = [
  'workflow_audit_research/README.md',
  'workflow_audit_research/raw/source_urls.md',
  'workflow_audit_research/clean/source_candidates.md',
  'workflow_audit_research/reading/S1_loop_engineering.md',
  'workflow_audit_research/reading/S2_context_engineering.md',
  'workflow_audit_research/reading/S3_spec_driven_development.md',
  'workflow_audit_research/reading/S4_human_in_loop_audit_trail.md',
  'workflow_audit_research/insights/workflow_audit_synthesis.md',
  'workflow_audit_research/insights/risk_register.md',
  'workflow_audit_research/kb/stable_conclusions.md',
  'workflow_audit_research/workflow/patch_candidates.md',
  'workflow_audit_research/workflow/next_research_plan.md',
]
for f in required:
    p = Path(f)
    assert p.exists(), f'missing {f}'
    assert p.stat().st_size > 500, f'too small {f}'
print('workflow audit research pack exists')
PY
python - <<'PY'
from pathlib import Path
terms = ['Loop Engineering','Context Engineering','Spec-driven','HumanGate','Verifier','audit trail','provenance','raw','clean','reading','insights','kb','workflow patch']
text = '\n'.join(p.read_text(encoding='utf-8', errors='replace') for p in Path('workflow_audit_research').rglob('*.md'))
missing = [t for t in terms if t not in text]
assert not missing, missing
print('workflow audit coverage passed')
PY
git diff --name-only
```

Also verify forbidden paths are unchanged.

## Completion report

Return:

- Files created/updated.
- Main audit findings.
- Patch candidates created.
- Verification commands and results.
- Stop state: Done / DoneWithRisk / Blocked / HumanGate / Repair.
