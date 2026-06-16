# Codex Work Order: Creator MVP Loop Prototype Refinement v0.2

Status: ready for Codex execution  
Owner: Hermes  
Executor: Codex  
Verifier: Hermes  
Source baseline: `prototypes/creator-mvp-loop-v0-1.html`  
Source contract: `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`

---

## 1. Objective

Create a refined v0.2 static prototype that improves the product feel, creator-facing clarity, and interaction quality of the first `Creator MVP Loop v0.1` prototype without expanding into full app architecture.

This is a refinement stage, not a new system build.

The v0.2 prototype must still demonstrate the same complete creator-facing loop:

```text
idea intake -> direction check -> executing/status -> preview -> evidence summary -> satisfaction feedback -> correction/stop
```

and must still keep internal machinery summarized rather than exposed:

```text
Hermes -> Demand Contract -> Loop -> Codex -> Verifier -> feedback/learnback
```

---

## 2. Read First

Read these files before editing:

- `prototypes/creator-mvp-loop-v0-1.html`
- `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`
- `CREATOR_INTERFACE_CONTRACT_V0_1.md`
- `CREATOR_WORKFLOW_OPERATING_MODEL.md`
- `CREATOR_WORKFLOW_ANTI_PATTERNS.md`
- `CODEX_WORK_ORDER_CREATOR_MVP_PROTOTYPE_V0_1.md`
- `INDEX.md`

---

## 3. Allowed Files

Codex may create or update only:

```text
prototypes/creator-mvp-loop-v0-2.html
INDEX.md
```

Codex must not modify `prototypes/creator-mvp-loop-v0-1.html`. Preserve v0.1 as the baseline artifact.

Hermes may update `.loop/*` after verification.

---

## 4. Forbidden Scope

Do not:

- add dependencies, package files, build systems, frameworks, services, databases, auth, accounts, integrations, or network behavior;
- create CLI tools;
- connect to real `.loop` automation;
- create a full product architecture;
- expose raw `.loop`, work order syntax, verifier transcript, git, research layers, or KB schemas as the default creator interface;
- modify protocol/template/runner/verifier/workflow/knowledge-base/trial/script/test directories;
- modify README;
- commit changes.

---

## 5. Required v0.2 Improvements

Build a single self-contained static HTML/CSS/JS file at:

```text
prototypes/creator-mvp-loop-v0-2.html
```

The v0.2 prototype must improve v0.1 in these ways:

1. **Sharper creator-facing hierarchy**
   - Make the primary path obvious within 5 seconds.
   - Separate creator controls from internal evidence.
   - Reduce the feeling of a document dashboard.

2. **More product-like interaction**
   - Provide a clear primary path from idea -> direction -> work status -> preview -> feedback.
   - Feedback controls must visibly update state, route copy, evidence, and stop state.
   - Stop must disable continuation controls.
   - Continue must route to HumanGate if it would create a new slice.

3. **Better status/evidence design**
   - Show current state, decision need, preview readiness, risk, and verification result.
   - Evidence must be summarized for a creator, with optional internal detail hidden behind a `details`/disclosure element or equivalent.

4. **HumanGate clarity**
   - HumanGate must read as a creator-owned decision, not an error.
   - It should show a short reason and 2-3 meaningful options.

5. **Professional visual system**
   - Use a restrained, original product UI style.
   - Avoid generic SaaS filler, fake metrics, emoji, decorative dashboards, aggressive gradients, and unnecessary icons.
   - Preserve accessibility basics: semantic sections, keyboard-focusable controls, responsive layout, 44px touch targets, readable contrast.

6. **Review affordance**
   - Include a small visible note that this is `v0.2 refinement` and v0.1 remains preserved.
   - Include an artifact/version label so the creator can distinguish prototype versions.

---

## 6. Required Content and Controls

The prototype must include these exact or semantically equivalent labels/concepts:

- `Creator MVP Loop v0.1`
- `v0.2 refinement`
- `Idea Intake`
- `Direction Check`
- `Status`
- `Preview`
- `Evidence Summary`
- `Satisfaction Feedback`
- `Approve`
- `Adjust`
- `Reject`
- `Continue`
- `Stop`
- `HumanGate`
- `Correction Routing`
- `Hermes`
- `Demand Contract`
- `Loop`
- `Codex`
- `Verifier`
- `feedback/learnback`
- `scope expansion`
- `automatic continuation`

---

## 7. INDEX Update

Update `INDEX.md` under the Product section with a link to:

```text
prototypes/creator-mvp-loop-v0-2.html
```

Keep the existing v0.1 links.

---

## 8. Acceptance Criteria

Hermes verifier will check:

- v0.2 HTML exists and is substantive;
- v0.1 HTML remains unchanged;
- required content and controls are present;
- feedback actions are wired in JavaScript;
- Stop disables continuation controls;
- Continue routes to HumanGate / scope expansion decision;
- evidence includes a summarized view and optional details/disclosure;
- no network/dependency patterns are present;
- `INDEX.md` links v0.2 while preserving v0.1 links;
- changed files are limited to the allowed files plus this work order and Hermes-owned `.loop` state updates;
- forbidden directories are not changed;
- extracted inline JavaScript passes `node --check`;
- HTML parses with Python stdlib `html.parser`.

---

## 9. Completion Report Required

When done, report:

- files changed;
- how v0.2 improves v0.1;
- checks run;
- any risks or remaining open decisions;
- recommended stop state: Done, DoneWithRisk, Blocked, HumanGate, or Repair.
