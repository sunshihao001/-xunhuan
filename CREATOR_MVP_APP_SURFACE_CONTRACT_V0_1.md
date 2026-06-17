# Creator MVP App Surface Contract v0.1

Version: v0.1  
Status: app-surface contract for the first real creator-facing MVP surface  
Source prototype: `prototypes/creator-mvp-loop-v0-2.html`  
Source demand: `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`

---

## 1. Purpose

This contract defines the first real app surface boundary after the static v0.2 prototype. It decides what the next implementation should build, what stays hidden, what data is safe to use, which creator-facing states and controls are required, and what verification must prove before the surface can be accepted.

The product boundary remains:

| Layer | Product rule |
| --- | --- |
| Creator-facing surface | The creator operates idea, direction, preview, satisfaction, correction, continue, stop, and HumanGate decisions. |
| Internal machinery | Demand Contract, Loop, Codex, Verifier, Research, Knowledge Base, Git, and work-order syntax remain hidden unless summarized as evidence or risk. |
| App-surface goal | Prove one complete creator-facing loop without implementing the full workflow operating system. |

This is not an implementation document. It authorizes a bounded future implementation work order only after this contract is accepted.

---

## 2. App Surface Decision

The next implementation should become a named app surface, not another open-ended static HTML prototype round.

| Decision | Contract |
| --- | --- |
| Surface name | `Creator MVP App Surface v0.1` |
| Product slice name shown in the surface | `Creator MVP Loop v0.1` |
| Implementation form | One small, browsable app surface using static HTML/CSS/JS unless a future work order explicitly names an existing app framework and exact allowed files. |
| Real automation | Out of scope for the first app surface. No real `.loop` automation, no Codex execution, no Verifier process, no Research calls, no Knowledge Base writes, and no Git operation UI. |
| Safe substitute | Read-only fixture data that represents the creator loop, state model, evidence summary, and HumanGate routes. |
| Primary value | A creator can understand and operate the product loop without seeing internal system mechanics. |

The term "app surface" means the future artifact should be treated as the first product boundary for the creator experience. It may still be technically static HTML for safety, but it should behave like a focused product surface rather than a disposable sketch.

---

## 3. v0.2 Prototype Baseline

The v0.2 prototype establishes baseline product behavior that the first app surface must preserve.

| v0.2 behavior | Baseline requirement |
| --- | --- |
| Idea intake | The surface includes a plain-language intake area for rough creator ideas. |
| Direction check | The surface summarizes inferred objective, expected output, non-goals, and material risk before work is treated as ready. |
| Status summary | The surface shows current state, decision need, preview readiness, risk, and verification result. |
| Preview | The surface includes an artifact-level preview area that a creator can judge without reading internals. |
| Evidence summary | The surface shows concise evidence and allows optional detail, without making raw internals the primary path. |
| Satisfaction controls | Approve, Adjust, Reject, Continue, and Stop are visible first-class controls. |
| HumanGate | Continue that would create a new slice routes to a HumanGate decision instead of automatic continuation. |
| Stop behavior | Stop disables automatic continuation and requires a future new demand to resume. |
| Internal route summary | Hermes, Demand Contract, Loop, Codex, Verifier, and feedback/learnback may appear only as summarized evidence, not as routine user work. |

The app surface may improve layout, labels, accessibility, and state handling, but it must not remove these baseline behaviors.

---

## 4. Visible Creator-Facing Screens and Regions

The first app surface should use one compact workflow screen with clearly separated regions. It should not become a multi-page dashboard unless a future HumanGate explicitly changes the product direction.

| Region | Required content | Required controls or behavior |
| --- | --- | --- |
| Idea intake | Original creator idea, optional correction text, and preserved wording. | Text entry for idea and correction. |
| Direction check | Inferred objective, expected output, non-goals, material risk, and readiness. | Approve direction, adjust direction, reject direction, or stop. |
| Run status | Current state, product target, what is happening, decision need, risk, and preview readiness. | Stop must remain available while the surface is not Done or Stopped. |
| Preview | Artifact name, artifact-level summary, meaningful changes, and known limitation. | PreviewReady state must be visually distinct from Running or HumanGate. |
| Evidence review | Checks performed, scope result, forbidden-scope result, assumptions, risks, and stop state. | Optional detail may expand, but raw command output must not be the default view. |
| Satisfaction feedback | Approve, Adjust, Reject, Continue, Stop. | Each action must route to a named state and explanation. |
| HumanGate | Short reason, two or three creator-owned options, and no routine technical minutiae. | Choices must include a stop path when continuation or risk acceptance is involved. |

The interface should feel like a working creator tool, not a documentation browser, internal console, or marketing page.

---

## 5. Hidden Internal Machinery

The surface must hide routine internal machinery by default while preserving accountability through summaries.

| Internal item | Default visibility | Allowed surfaced summary |
| --- | --- | --- |
| Demand Contract | Hidden | Direction, scope, non-goals, acceptance, and risk summary. |
| `.loop` state | Hidden | Current state, resumability note, stop state, and whether a handoff exists. |
| Codex | Hidden | "Work is running" or "bounded work completed" with changed artifact names. |
| Verifier | Summarized | Passed, Repair, DoneWithRisk, Blocked, or HumanGate, plus checks performed. |
| Research | Hidden unless needed | Short sourced conclusion, confidence, and conflict note. |
| Knowledge Base | Hidden unless relevant | Candidate lesson or stable context note, with no schema exposure. |
| Git | Hidden | Changed files and forbidden paths unchanged. |
| Work-order syntax | Hidden | Objective, allowed scope, forbidden scope, and verification summary. |

The surface hides mechanics, not evidence. If evidence is incomplete, the correct state is DoneWithRisk or HumanGate, not Done.

---

## 6. User Controls

The first app surface must expose creator-owned controls directly.

| Control | Creator meaning | Required route |
| --- | --- | --- |
| Idea intake | "Here is what I want." | Preserve raw wording and infer direction. |
| Approve direction | "This is the right direction." | Move to ReadyToRun or Running if a safe fixture run is already selected. |
| Adjust direction | "Mostly right, but change the framing." | Return to DirectionCheck with correction text preserved. |
| Reject direction | "This is the wrong product angle." | Reopen direction and prevent detail repair until direction is corrected. |
| Correction text | "Here is what to change." | Classify as direction, detail, evidence, depth, scope, or stop. |
| Approve result | "This satisfies the current intent." | Move to Done if evidence passes, or DoneWithRisk if named risk is accepted. |
| Adjust result | "Repair details inside the current slice." | Move to Repair, then back through ReadyToRun, Running, PreviewReady, and EvidenceReview. |
| Reject result | "The result misses value or intent." | Move to DirectionCheck or HumanGate, not blind repair. |
| Continue | "Start another slice in the same direction." | Continue only if in scope; otherwise HumanGate. |
| Stop | "Halt automatic work." | Move to Stopped and prevent automatic continuation. |
| HumanGate choice | "I own this value, risk, or scope decision." | Route to ReadyToRun, DirectionCheck, DoneWithRisk, Blocked, or Stopped depending on choice. |

No required control should ask the creator to choose file structure, command syntax, test tooling, prompt mechanics, internal state files, or git behavior.

---

## 7. State Model

The app surface must implement or clearly represent this state model.

| State | Creator-facing meaning | Valid next states | Required visible signal |
| --- | --- | --- | --- |
| Idle | No active idea is running. | DirectionCheck, Stopped | Empty or saved idea state. |
| DirectionCheck | The product direction needs confirmation or correction. | ReadyToRun, Idle, HumanGate, Stopped | Objective, output, non-goals, risk, and direction controls. |
| ReadyToRun | Direction is accepted and the fixture run can begin. | Running, HumanGate, Stopped | "Ready" status and stop control. |
| Running | The simulated work is in progress. | PreviewReady, HumanGate, Blocked, Stopped | Current step, target, and preview not ready. |
| PreviewReady | The artifact preview is available. | EvidenceReview, HumanGate, Stopped | PreviewReady label and artifact summary. |
| EvidenceReview | Evidence and risk are being judged. | Done, DoneWithRisk, Repair, HumanGate, Blocked, Stopped | Checks, scope result, risk, and stop state candidate. |
| HumanGate | A creator-owned decision is required. | DirectionCheck, ReadyToRun, DoneWithRisk, Blocked, Stopped | Short reason and creator-owned options. |
| Repair | A bounded correction is authorized. | ReadyToRun, Running, PreviewReady, HumanGate, Stopped | Correction reason and repair boundary. |
| Done | Evidence passes and no material open risk remains. | Idle, Stopped | Done status and no automatic continuation. |
| DoneWithRisk | Result is usable with a named accepted or unresolved risk. | Repair, HumanGate, Stopped, Idle | Risk name and acceptance/repair options. |
| Blocked | Missing input, tool, file, permission, or external condition prevents progress. | HumanGate, DirectionCheck, Stopped | Blocker and required change. |
| Stopped | Creator stopped automatic work. | Idle only through a new demand | Stop status and disabled continuation. |

The visible surface may use friendlier labels, but the internal model and verification terms must remain traceable to these names.

---

## 8. Data Boundary

The first app surface must use read-only fixture data by default.

| Data source | Scope decision | Reason |
| --- | --- | --- |
| Static sample data | Allowed | Safe for demonstrations, but should be labeled as sample/fixture when relevant. |
| Read-only fixture | Required default | Lets the surface represent states, evidence, and HumanGate without touching real automation. |
| Real `.loop` state | Out of scope | Connecting to `.loop` would create execution, state mutation, privacy, and verifier complexity before the surface boundary is proven. |
| Local storage | Out of scope by default | Persistence changes the product contract and must be named in a future work order. |
| Network calls | Forbidden | Adds dependency and data-risk surface not needed for the MVP. |
| Real Codex/Verifier/Research execution | Forbidden | The first app surface is a product boundary demonstration, not an automation runtime. |

Fixture data may contain example `.loop` words only as summarized evidence. It must not present `.loop` files as the creator's normal operating surface.

---

## 9. Allowed Files for the Next Implementation Work Order

The next implementation work order must name exact files before work starts. Recommended allowed surface:

| File | Permission | Constraint |
| --- | --- | --- |
| `app/creator-mvp/index.html` | Create | Static app surface only; no dependencies or build system. |
| `app/creator-mvp/styles.css` | Create | Local styles for the app surface. |
| `app/creator-mvp/app.js` | Create | Fixture state machine and UI behavior only. |
| `app/creator-mvp/fixtures.js` | Optional create | Read-only fixture data only. May be merged into `app.js` for a smaller slice. |
| `INDEX.md` | Update | Link the app surface if created. |
| `.loop/HANDOFF.md`, `.loop/STATE.md`, `.loop/LOOP_LOG.md` | Optional update | Only for round bookkeeping if the future work order requires it. |

If the repository already contains a preferred app directory by the time the future work order runs, that work order may choose it only by naming exact files and explaining why the choice keeps the slice smaller than a new static surface.

---

## 10. Forbidden Scope for the Next Implementation Work Order

The next implementation must not:

| Forbidden scope | Reason |
| --- | --- |
| Modify `prototypes/` | v0.2 is the source reference and should remain stable. |
| Add dependencies, package managers, build systems, frameworks, services, databases, auth, accounts, or network behavior | The goal is app-surface proof, not platform architecture. |
| Connect to real `.loop` state or mutate `.loop` files from the UI | Real automation is not authorized for the first app surface. |
| Expose raw Demand Contract, Loop, Codex, Verifier, Research, Knowledge Base, Git, or work-order syntax as the default UI | Violates the creator-first boundary. |
| Create CLI tools, runners, verifier tools, tests, or scripts | This round is product surface only. |
| Modify protocol, template, workflow, knowledge-base, research, trial, script, test, or docs directories | Those are internal system layers, not the app surface. |
| Commit changes | Commit behavior requires explicit user authorization. |
| Continue after Stop | Stop is a creator-owned authority signal. |
| Claim Done without verifier/browser evidence | Completion must be evidence-based. |

Any proposed exception requires HumanGate before implementation begins.

---

## 11. Browser and Verifier Checks

The next implementation round must include file checks, scope checks, and browser checks.

| Check | Required evidence |
| --- | --- |
| Artifact existence | Allowed app files exist and are substantial enough to inspect. |
| Required terms | Surface or source contains creator-facing, app surface, static HTML, read-only fixture, `.loop`, HumanGate, Verifier, Codex, allowed files, forbidden scope, browser, acceptance, stop, satisfaction, and PreviewReady where applicable. |
| State coverage | Idle, DirectionCheck, ReadyToRun, Running, PreviewReady, EvidenceReview, HumanGate, Repair, Done, DoneWithRisk, Blocked, and Stopped are represented in code, fixture, or visible state map. |
| Control coverage | Idea intake, approve, adjust, reject, continue, stop, HumanGate choices, and correction text exist and route to named states. |
| Data boundary | Read-only fixture is used; no real `.loop` automation, storage, network, or dependencies are added. |
| Hidden machinery | Internal systems are summarized as evidence/risk, not default operating UI. |
| Browser smoke | Open the local file or local server in a browser, verify nonblank render, responsive layout, visible primary controls, and no console errors. |
| Interaction smoke | Click Approve, Adjust, Reject, Continue, Stop, and HumanGate choices; verify state and route copy update. |
| Scope diff | `git diff --name-only` contains only files allowed by the future work order. |
| Forbidden paths | Forbidden directories and `prototypes/` are unchanged. |

The browser check may use a local static file URL if no server is needed.

---

## 12. HumanGate Triggers and Stop Behavior

HumanGate must appear when a user-owned decision is required.

| Trigger | Required behavior |
| --- | --- |
| Direction or value unclear | Pause in DirectionCheck or HumanGate and ask a short choice question. |
| Continue would create a new slice | Pause in HumanGate with authorize, keep current slice, or stop options. |
| Scope would touch forbidden files or add dependencies | Pause in HumanGate before any change. |
| Real `.loop` automation is proposed | Pause in HumanGate and require a new contract/work order. |
| Verification cannot prove a required outcome | Use DoneWithRisk or HumanGate for risk acceptance. |
| Creator satisfaction is unclear | Ask one classification question, not a technical interview. |
| Stop is selected | Move to Stopped, disable automatic continuation, and require a new demand to resume. |

Stop is not a soft preference. After Stop, the app surface must not run fixture progression, authorize continuation, or imply that work will continue automatically.

---

## 13. Acceptance Criteria

A creator-facing MVP app surface is accepted only when:

| Acceptance area | Required result |
| --- | --- |
| Product boundary | The creator can operate idea, direction, status, preview, satisfaction, correction, continue, stop, and HumanGate decisions without using internal mechanics. |
| App-surface decision | The implementation is a named `Creator MVP App Surface v0.1`, even if technically delivered as static HTML/CSS/JS. |
| Baseline preservation | The v0.2 baseline behaviors in this contract are preserved. |
| State model | Required states are represented and route coherently. |
| Controls | Required controls exist and update route/state/evidence meaningfully. |
| Data safety | Read-only fixture data is used; real `.loop` state is not connected. |
| Evidence | Verifier and browser checks produce concrete evidence. |
| Scope | Changed files match allowed files; forbidden scope remains unchanged. |
| HumanGate | HumanGate is a decision state, not an error or routine technical question. |
| Stop | Stop prevents automatic continuation. |

Done means all acceptance areas pass and no material risk remains. DoneWithRisk means the surface is usable but a named product, verification, or implementation choice remains open.

---

## 14. Next Codex Implementation Work Order Shape

A future implementation work order should use this shape:

| Section | Required content |
| --- | --- |
| Objective | Build `Creator MVP App Surface v0.1`, the smallest browsable creator-facing app surface for the complete MVP loop. |
| Read first | This contract, `CREATOR_INTERFACE_CONTRACT_V0_1.md`, `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`, `CREATOR_WORKFLOW_OPERATING_MODEL.md`, `CREATOR_WORKFLOW_ANTI_PATTERNS.md`, and `prototypes/creator-mvp-loop-v0-2.html`. |
| Allowed files | Exact files only, preferably `app/creator-mvp/index.html`, `styles.css`, `app.js`, optional `fixtures.js`, and `INDEX.md`. |
| Forbidden files | `prototypes/`, protocol, templates, workflows, scripts, tests, docs, research, trials, existing root files not explicitly allowed, dependencies, commits, and real automation. |
| Required behavior | Idea intake, DirectionCheck, ReadyToRun, Running, PreviewReady, EvidenceReview, HumanGate, Repair, Done, DoneWithRisk, Blocked, Stopped, satisfaction controls, correction text, and stop behavior. |
| Data rule | Use read-only fixture data; no real `.loop` state. |
| Verification | File checks, required coverage checks, browser smoke, interaction smoke, diff scope, and forbidden-path check. |
| Completion report | Files changed, baseline behavior preserved, implementation choice, verification output, risks, and stop state. |

The work order must remain a single bounded implementation round. It must not ask Codex to design a full app architecture or connect internal automation.

---

## 15. Contract Decisions Summary

| Decision | Result |
| --- | --- |
| First real app boundary | A named `Creator MVP App Surface v0.1`. |
| Technical default | Static HTML/CSS/JS remains acceptable, but as an app surface rather than another prototype-only artifact. |
| Data default | Read-only fixture data. |
| Real `.loop` automation | Explicitly out of scope. |
| v0.2 baseline | Preserve idea intake, direction check, status, preview, evidence summary, satisfaction controls, HumanGate, stop, and summarized internal route. |
| Creator controls | Idea, approve, adjust, reject, continue, stop, HumanGate choices, and correction text. |
| Hidden machinery | Demand Contract, Loop, Codex, Verifier, Research, KB, Git, and work-order syntax hidden by default. |
| Required verification | File, coverage, browser, interaction, diff-scope, and forbidden-path checks. |
| Stop state for this contract | Done when this file exists, INDEX links it, coverage passes, and forbidden paths remain unchanged. |
