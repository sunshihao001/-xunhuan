# Hermes Codex Execution Playbook

Version: v0.1  
Status: operational playbook for theory-to-product execution  
Audience: Human Owner, Hermes, Codex, Loop Verifier

---

## 1. Purpose

This playbook defines how a rough idea becomes a verified product through Hermes, Codex, loop-agent execution, and durable knowledge management.

The default path is:

```text
Human idea
-> Hermes intake and interrogation
-> research evidence pack if needed
-> theory and Demand Contract
-> Codex long-task work order
-> Loop execution
-> Verifier evidence check
-> HumanGate only when needed
-> product correction and learnback
```

Hermes is responsible for orchestration and verification. Codex is responsible for bounded execution. The Human is responsible for direction, boundaries, and HumanGate decisions.

---

## 2. Phase 0: Intake

Trigger: the Human gives an initial idea in Hermes.

Hermes records:

```yaml
surface_ask: <user's original words>
real_objective_guess: <what the user is probably trying to achieve>
domain: <project, product, research, workflow, codebase>
expected_product: <document, code, tool, workflow, knowledge base, product>
known_boundaries:
  - <forbidden action or path>
research_needed: yes | no
codex_needed: yes | no
loop_needed: yes | no
risk_of_wrong_execution: low | medium | high | critical
```

Verifier check:

- The intake preserves the human idea.
- The suspected objective does not erase user constraints.
- Any obvious HumanGate is identified early.

HumanGate triggers:

- The idea has multiple incompatible directions.
- The cost, scope, or risk is not bounded.
- The output product is unclear.

---

## 3. Phase 1: Demand Interrogation

Hermes asks only the questions needed to make the task executable. It should not trap the Human in endless clarification.

Hermes must define:

- Goal.
- Non-goals.
- Target user or use case.
- Current repository or asset context.
- Allowed and forbidden areas.
- Verification expectations.
- Stop conditions.

Output artifact:

```text
Demand Contract or Demand Contract Lite
```

Verifier check:

- The contract has a clear goal, scope, output, acceptance criteria, and stop conditions.
- The contract separates Human, Hermes, Codex, Verifier, and Knowledge Base responsibilities.

---

## 4. Phase 2: Research Capture and Promotion

Trigger: the theory or product depends on external information, best practices, examples, docs, market references, or prior art.

Hermes creates or uses layered research assets:

```text
raw/
clean/
reading/
insights/
kb/
workflow/
```

Hermes responsibilities:

- Save raw source identity and capture context.
- Clean and classify useful sources.
- Produce reading cards for important sources.
- Synthesize cross-source insights.
- Promote only stable, scoped conclusions into kb.
- Promote only behavior-changing conclusions into workflow.

Codex responsibilities:

- Do not consume random raw research unless explicitly instructed.
- Use curated reading, insights, kb, or workflow material supplied in the work order.

Verifier check:

- A promoted conclusion has source traceability.
- raw evidence is not treated as stable knowledge.
- workflow patches describe concrete behavior changes.

HumanGate triggers:

- Research reveals a direction change.
- Sources conflict on a value or strategy decision.
- A workflow patch would meaningfully alter how future agents operate.

---

## 5. Phase 3: Theory Draft

Hermes integrates:

- The Human's initial idea.
- Existing repository docs.
- Promoted research.
- Current control model.
- Current product constraints.

The theory must answer:

- What is the system trying to accomplish?
- Which role owns which decision?
- How does an idea become a Codex task?
- How does external research become durable knowledge?
- How does loop execution become a product?
- How are unsuitable parts corrected?

Output artifact examples:

```text
AI_WORKFLOW_THEORY_V0_1.md
RESEARCH_TO_PRODUCT_LOOP.md
HERMES_CODEX_EXECUTION_PLAYBOOK.md
```

Verifier check:

- The theory is concrete enough to guide a future work order.
- It names gates, artifacts, role boundaries, and stop states.
- It distinguishes Codex self-report from Verifier evidence.

---

## 6. Phase 4: Codex Long-Task Work Order

Hermes converts the theory and contract into a bounded Codex work order.

Minimum work order shape:

```markdown
# WORK_ORDER - <round name>

## Objective

<one concrete outcome>

## Read first

- <file>
- <file>

## Required output artifacts

1. `<path>`
   - <requirements>

## Allowed files

- `<path>`
- `<directory pattern if allowed>`

## Forbidden files/directories

- `<path>`
- `<directory>`

## Requirements

- <content, behavior, or implementation requirement>

## Required verification

```bash
<command>
<command>
```

Also verify forbidden paths are unchanged.

## Completion report

Return:

- Files created/updated.
- Summary.
- Verification commands and results.
- Risks or gaps.
```
```

Codex should receive enough context to execute without reinterpreting the whole product strategy. The work order must explicitly say whether CLI tools, dependencies, commits, network calls, or forbidden paths are allowed.

Verifier check:

- The work order is bounded.
- Allowed and forbidden paths are unambiguous.
- Required output artifacts are named.
- Verification commands are executable.

---

## 7. Phase 5: Codex Execution

Codex procedure:

1. Read the work order and required context.
2. Inspect existing files before editing.
3. Modify only allowed files.
4. Do not create tools, dependencies, or commits unless allowed.
5. Run required verification.
6. Check forbidden paths remain unchanged.
7. Return the required completion report.

Codex completion report must include:

- Files created or updated.
- Summary of what changed.
- Verification commands and results.
- Risks, gaps, or blocked items.

Codex report is not final verification. It is evidence for Hermes and Verifier.

---

## 8. Phase 6: Verifier Gate

Hermes or a dedicated Verifier checks:

- Required files exist and are large enough or complete enough.
- Required terms or sections are present.
- The diff touches only allowed files.
- Forbidden paths are unchanged.
- Verification commands actually passed.
- The output matches the theory and contract.
- The report names real risks instead of hiding them.

Decision states:

- Done: all required checks pass.
- DoneWithRisk: usable output with explicit residual risk.
- Blocked: cannot proceed because of missing prerequisites.
- HumanGate: human decision needed.
- Repair: Codex should fix within scope.

---

## 9. Phase 7: Loop Product Build

If the target is a product, not only a document, Hermes creates loop rounds:

```text
Round 1: theory and contract
Round 2: minimal product skeleton
Round 3: core behavior
Round 4: verifier checks
Round 5: usability correction
Round 6: learnback and workflow patch
```

Each round gets a separate `WORK_ORDER.md`. Each round has its own allowed files, forbidden files, required checks, and stop conditions.

The Loop updates:

- `STATE.md`: current status, round, assumptions, next action.
- `LOOP_LOG.md`: what happened and what evidence exists.
- `HANDOFF.md`: what the next executor must know.
- `STOP_GATE.md`: when to continue, stop, block, or ask the Human.

---

## 10. Phase 8: Correction and Learnback

After a product exists, Hermes reviews user feedback, verifier results, and execution friction.

Correction sources:

- The Human says a behavior or direction is unsuitable.
- The Verifier finds a mismatch with acceptance criteria.
- Codex reports a risk.
- Usage exposes a missing workflow rule.
- Research produces a better stable conclusion.

Learnback targets:

- `kb`: stable conclusions.
- `workflow`: behavior-changing patches.
- templates: repeated work order or contract structure.
- verifier rules: new checks.
- stop gates: new DoneWithRisk, Blocked, or HumanGate conditions.

The system improves when corrections become durable operating knowledge, not just one-off fixes.
