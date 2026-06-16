# WORK_ORDER - Long Theory Completion Round

## Correction

The previous execution over-focused on small CLI increments. The user has clarified the actual desired next step:

> Use the initial idea already expressed in Hermes, plus the saved AI workflow assets, and let Codex run a long task to complete the first full version of the theory/workflow. Hermes should then verify and report back.

Do not create another small standalone CLI in this round.

## Read first

- `AI_WORKFLOW_CONTROL_MODEL.md`
- `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md`
- `AI_WORKFLOW_MAP.md` if present
- `AI_WORKFLOW_ROUTER.md` if present
- `DEMAND_CONTRACT_TEMPLATE.md` if present
- `README.md`
- `INDEX.md`
- `docs/COMPILE_LOOP.md`
- `docs/INIT_RESEARCH_PACK.md`
- `.loop/HANDOFF.md`

## User's initial idea to preserve and complete

The user wants this workflow:

```text
在 Hermes 里先给出需求初步想法；
搜索外部相关信息资料来完善和填充理论框架；
把完善后的理论交给 Codex 长任务，补全具体的全部理论初步版本；
再按照全部理论使用循环代理把它做成成品；
成品完成后，根据不合适的地方继续调整修改；
外部搜索资料不能只是当时搜索使用，而要按照来源和层级保存为知识库储备；
Hermes 应该负责需求拷问、理论框架、知识库与验证；
Codex 应该负责长任务执行和具体细节完善；
人只负责关键边界、方向调整和 HumanGate。
```

## Objective

Create the first complete, coherent theory/workflow version for this AI workflow operating system. It should integrate the saved cognition into a professional artifact set that can guide future Hermes + Codex + loop-agent execution.

## Required output artifacts

Create or update documentation only. Do not create new CLI tools in this round.

Required artifacts:

1. `AI_WORKFLOW_THEORY_V0_1.md`
   - Complete theory framework.
   - Explain the control model: Human / Hermes / Codex / Loop / Verifier / Knowledge Base.
   - Explain why external research must become durable evidence assets.
   - Explain how initial ideas become theory, then Codex long tasks, then loop-built product, then iterative correction.

2. `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
   - Concrete step-by-step workflow.
   - Include exact phases from initial idea to final product.
   - Include what Hermes does, what Codex does, when HumanGate triggers, and how verifier checks results.
   - Include example Codex long-task work order shape.

3. `RESEARCH_TO_PRODUCT_LOOP.md`
   - External research → layered knowledge → theory → Codex task → loop execution → product → correction.
   - Define the durable research layers: raw, clean, reading, insights, kb, workflow.
   - Define promotion gates from source to stable knowledge and workflow patch.

4. Update `INDEX.md`
   - Add the new artifacts under Product or a new Theory / Workflow section.

5. Optionally update `README.md` only if useful for navigation.

## Allowed files

- `AI_WORKFLOW_THEORY_V0_1.md`
- `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
- `RESEARCH_TO_PRODUCT_LOOP.md`
- `INDEX.md`
- `README.md`
- `.loop/*` only if needed for status notes

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

- Avoid empty theory and vague slogans.
- Use concrete phases, gates, artifacts, and file names.
- Distinguish temporary research evidence from stable knowledge.
- Distinguish Hermes orchestration from Codex execution.
- Distinguish Codex self-report from Hermes verifier evidence.
- Include stop conditions: Done, DoneWithRisk, Blocked, HumanGate.
- Include how future external sources should be saved and promoted.
- Include how this can guide later product implementation.

## Required verification before returning

Run and report:

```bash
python - <<'PY'
from pathlib import Path
files = [
  'AI_WORKFLOW_THEORY_V0_1.md',
  'HERMES_CODEX_EXECUTION_PLAYBOOK.md',
  'RESEARCH_TO_PRODUCT_LOOP.md',
  'INDEX.md',
]
for f in files:
    p = Path(f)
    assert p.exists(), f'missing {f}'
    assert p.stat().st_size > 1000, f'too small {f}'
print('artifact existence check passed')
PY
python - <<'PY'
from pathlib import Path
required_terms = ['Hermes', 'Codex', 'HumanGate', 'Verifier', 'raw', 'clean', 'reading', 'insights', 'kb', 'workflow']
text = '\n'.join(Path(f).read_text(encoding='utf-8', errors='replace') for f in [
  'AI_WORKFLOW_THEORY_V0_1.md',
  'HERMES_CODEX_EXECUTION_PLAYBOOK.md',
  'RESEARCH_TO_PRODUCT_LOOP.md',
])
missing = [t for t in required_terms if t not in text]
assert not missing, missing
print('concept coverage check passed')
PY
git diff --name-only
```

Also verify forbidden paths are unchanged.

## Completion report

Return:

- Files created/updated.
- Summary of the completed theory/workflow version.
- Verification commands and results.
- Any risks or remaining gaps.
