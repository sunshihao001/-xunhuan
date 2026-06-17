# CODEX WORK ORDER - Creator MVP App Surface Contract v0.1

## Objective

Create `CREATOR_MVP_APP_SURFACE_CONTRACT_V0_1.md`: a product/app-surface contract that decides the first real app boundary after the static v0.2 prototype, before any framework/app implementation begins.

This is a contract/specification round. Do not implement an app. Do not create UI code. Do not add dependencies. Do not modify prototypes. Do not commit.

## Read first

Read these files before writing:

- `.loop/HANDOFF.md`
- `CREATOR_INTERFACE_CONTRACT_V0_1.md`
- `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`
- `CREATOR_WORKFLOW_THEORY_V1.md`
- `CREATOR_WORKFLOW_OPERATING_MODEL.md`
- `CREATOR_WORKFLOW_SCENARIOS.md`
- `CREATOR_WORKFLOW_ANTI_PATTERNS.md`
- `prototypes/creator-mvp-loop-v0-2.html`
- `INDEX.md`

## Required output artifacts

Create:

1. `CREATOR_MVP_APP_SURFACE_CONTRACT_V0_1.md`
   - Define the first real app surface boundary after the static prototype.
   - Decide what parts of v0.2 become baseline product behavior.
   - Define whether the next implementation remains static HTML or becomes a named app surface.
   - Define visible creator-facing screens/regions/states.
   - Define hidden internal machinery and what evidence summaries are allowed to surface.
   - Define user controls: idea intake, approve, adjust, reject, continue, stop, HumanGate choices, correction text.
   - Define state model: Idle, DirectionCheck, ReadyToRun, Running, PreviewReady, EvidenceReview, HumanGate, Repair, Done, DoneWithRisk, Blocked, Stopped.
   - Define data boundary: static sample data vs read-only fixtures vs real `.loop` state; default should be safe and explicit.
   - Define allowed files for the next implementation work order.
   - Define forbidden scope for the next implementation work order.
   - Define verifier/browser checks required for the next implementation round.
   - Define HumanGate triggers and stop behavior.
   - Define what constitutes acceptance for a creator-facing MVP app surface.
   - Define next-step work order shape for Codex implementation.

2. Update `INDEX.md`
   - Link `CREATOR_MVP_APP_SURFACE_CONTRACT_V0_1.md` under Product.
   - Link this work order near related Codex work orders if appropriate.

## Allowed files

- `CREATOR_MVP_APP_SURFACE_CONTRACT_V0_1.md`
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
- `prototypes/`
- existing root files not explicitly listed in allowed files

Do not create implementation files. Do not create CLI tools. Do not add dependencies. Do not commit.

## Content requirements

- Preserve creator-first positioning.
- Do not expose internal machinery as routine user work.
- Keep the next implementation bounded and verifiable.
- Prefer a safe first real app surface boundary over broad app architecture.
- Explicitly decide whether real `.loop` automation is in scope; if not, state the safe substitute.
- Make every contract section actionable for a future Codex implementation work order.
- Use clear headings and tables.

## Required verification

Run and report:

```bash
python - <<'PY'
from pathlib import Path
files = [
  'CREATOR_MVP_APP_SURFACE_CONTRACT_V0_1.md',
  'INDEX.md',
]
for f in files:
    p = Path(f)
    assert p.exists(), f'missing {f}'
    assert p.stat().st_size > 1000, f'too small {f}'
print('app surface contract artifacts exist')
PY
python - <<'PY'
from pathlib import Path
terms = [
  'creator-facing', 'app surface', 'static HTML', 'read-only fixture', '.loop',
  'HumanGate', 'Verifier', 'Codex', 'allowed files', 'forbidden scope',
  'browser', 'acceptance', 'stop', 'satisfaction', 'PreviewReady'
]
text = Path('CREATOR_MVP_APP_SURFACE_CONTRACT_V0_1.md').read_text(encoding='utf-8', errors='replace')
missing = [t for t in terms if t not in text]
assert not missing, missing
print('app surface contract coverage passed')
PY
git diff --name-only
```

Also verify forbidden paths are unchanged.

## Completion report

Return:

- Files created/updated.
- Summary of app surface contract decisions.
- What v0.2 prototype behavior becomes baseline.
- What remains explicitly out of scope.
- Verification commands and results.
- Stop state: Done / DoneWithRisk / Blocked / HumanGate / Repair.

## Stop states

- Done: contract exists, INDEX links it, coverage passes, and forbidden paths unchanged.
- DoneWithRisk: contract is usable but a named implementation choice remains open.
- Blocked: required source files are missing or contradictory.
- HumanGate: a product-direction decision is required before this contract can be completed.
- Repair: verification fails but can be fixed inside allowed files.
