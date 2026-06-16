# Codex Work Order: Creator MVP Loop v0.1 Prototype

Status: ready for Codex execution  
Owner: Hermes  
Executor: Codex  
Verifier: Hermes  
Source contract: `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`

---

## 1. Objective

Implement the smallest browsable prototype for `Creator MVP Loop v0.1`.

The prototype must demonstrate this creator-facing flow:

```text
idea intake -> direction check -> executing/status -> preview -> satisfaction feedback -> correction/stop
```

It must keep creator-facing simplicity separate from the internal route:

```text
Hermes -> Demand Contract -> Loop -> Codex -> Verifier -> feedback/learnback
```

This round is an implementation prototype only. It must not become a full app architecture pass.

---

## 2. Read First

Read these files before editing:

- `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`
- `CREATOR_INTERFACE_CONTRACT_V0_1.md`
- `CREATOR_WORKFLOW_OPERATING_MODEL.md`
- `CREATOR_WORKFLOW_ANTI_PATTERNS.md`
- `CORE_PRINCIPLES.md`
- `INDEX.md`

---

## 3. Allowed Files

Codex may create or update only:

```text
prototypes/creator-mvp-loop-v0-1.html
INDEX.md
```

Do not edit `.loop/*`. Hermes will update loop state after verification.

---

## 4. Forbidden Scope

Do not:

- add dependencies, package files, build systems, frameworks, services, databases, auth, accounts, integrations, or network behavior;
- create CLI tools;
- connect to real `.loop` automation;
- expose raw `.loop`, work order, verifier transcript, git, research layers, or KB schemas as the default creator interface;
- modify protocol/template/runner/verifier/workflow/knowledge-base/trial/script/test directories;
- modify README unless explicitly necessary;
- commit changes.

---

## 5. Required Prototype Behavior

Create a single self-contained static HTML/CSS/JS file at:

```text
prototypes/creator-mvp-loop-v0-1.html
```

The prototype must be openable directly in a browser and must include:

1. Product name: `Creator MVP Loop v0.1`.
2. Idea intake area with a rough creator idea sample and editable input.
3. Direction check card with inferred objective, expected output, non-goals, and risk.
4. Status/state area showing the loop progression.
5. Preview area showing artifact-level result, not raw internals.
6. Evidence summary area showing checks, scope, known risk, and decision need.
7. Feedback controls: `Approve`, `Adjust`, `Reject`, `Continue`, `Stop`.
8. HumanGate decision state as a normal decision state, not an error.
9. Correction routing display explaining where feedback goes.
10. Stop behavior: after Stop, the prototype must visibly prevent automatic continuation.
11. Continue behavior: if continuation expands scope, route to HumanGate instead of silently continuing.
12. Internal route summary that names Hermes, Demand Contract, Loop, Codex, Verifier, and feedback/learnback, but does not make the creator operate those internals.

Use static sample data only. No network calls.

---

## 6. UX Direction

This is a product workflow prototype, not a marketing page.

Design priorities:

- clear creator-facing hierarchy;
- professional workflow-product feel;
- compact but readable information density;
- state and evidence must be understandable without reading repository docs;
- avoid generic SaaS filler, fake metrics, decorative dashboards, and arbitrary icons.

The prototype may use inline JS to switch states and update route/evidence copy.

---

## 7. INDEX Update

Update `INDEX.md` under the Product section with links to:

- `CODEX_WORK_ORDER_CREATOR_MVP_PROTOTYPE_V0_1.md`
- `prototypes/creator-mvp-loop-v0-1.html`

Keep the hierarchy clean.

---

## 8. Acceptance Criteria

Hermes verifier will check:

- the HTML file exists and is substantial;
- the prototype contains the required flow steps;
- approve / adjust / reject / continue / stop controls are present;
- HumanGate is visible;
- preview and evidence summary are visible;
- internal route is summarized, not exposed as required creator work;
- static-only / no dependencies / no network behavior;
- `INDEX.md` links the new work order and prototype;
- changed files are limited to the allowed files plus this work order;
- forbidden directories are not changed.

---

## 9. Completion Report Required

When done, report:

- files changed;
- how the prototype implements the creator-facing loop;
- verification you performed;
- any risks or remaining open decisions;
- stop state recommendation: Done, DoneWithRisk, Blocked, HumanGate, or Repair.
