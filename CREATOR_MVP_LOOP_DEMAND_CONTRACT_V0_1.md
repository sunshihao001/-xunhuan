# Creator MVP Loop Demand Contract v0.1

Version: v0.1  
Status: implementation-ready demand contract  
Creator: Hermes  
Future executor: Codex, inside a bounded implementation work order  
Source contract: `CREATOR_INTERFACE_CONTRACT_V0_1.md`

---

## 1. Purpose and Source Contract

This document compiles `CREATOR_INTERFACE_CONTRACT_V0_1.md` into the first implementation-ready MVP demand contract.

The purpose is to define one small product slice that a future Codex round can implement without redesigning the full workflow operating system, exposing internal machinery to the creator, or starting UI work before scope and verification are explicit.

Source-of-truth inputs:

- `CREATOR_INTERFACE_CONTRACT_V0_1.md`
- `CREATOR_WORKFLOW_THEORY_V1.md`
- `CREATOR_WORKFLOW_OPERATING_MODEL.md`
- `CREATOR_WORKFLOW_SCENARIOS.md`
- `CREATOR_WORKFLOW_ANTI_PATTERNS.md`
- `CORE_PRINCIPLES.md`
- `DEMAND_CONTRACT_TEMPLATE.md`
- `PRODUCTIZATION_LOOP_V0_1.md`

This is a demand contract, not an implementation. It does not create UI, code, scripts, tests, dependencies, or runtime automation.

---

## 2. MVP Product Slice Name and Thesis

Product slice name:

```text
Creator MVP Loop v0.1
```

Slice thesis:

```text
A creator can move one rough idea through direction confirmation, bounded work status,
artifact preview, evidence summary, satisfaction feedback, and correction routing,
while Hermes, Demand Contract, Loop, Codex, Verifier, Research, Knowledge Base,
and HumanGate remain internal system roles.
```

The first implementation must prove the complete creator-facing loop, not every internal subsystem. It should be the smallest usable surface that demonstrates the boundary:

```text
creator surface: idea -> direction check -> status -> preview -> feedback -> correction/stop
internal route: Hermes -> Demand Contract -> Loop -> Codex -> Verifier -> feedback/learnback
```

---

## 3. Real Objective / Problem World / Convergence Slice

### Real Objective

Create a bounded MVP contract that lets a future implementation round build one creator-facing loop without asking Codex to invent product scope, architecture, verification, or role boundaries.

### Problem World

The repository already contains theory, scenarios, anti-patterns, operating model, and interface contract. The current risk is premature implementation: a UI or prototype could be built before the MVP slice, states, controls, verifier gates, HumanGate triggers, and future file surface are explicit.

The product risk is two-sided:

- exposing internal workflow mechanics makes the creator operate the system instead of creating;
- hiding too much evidence makes the surface vague, self-certifying, and unsafe.

### Convergence Slice

The convergence slice is one implementation-ready demand contract for `Creator MVP Loop v0.1`. It must be concrete enough for the next Codex implementation work order and narrow enough to prevent a broad app architecture pass.

---

## 4. User-Facing Flow

The future MVP must expose this sequence as the primary creator experience:

| Step | Creator sees | Creator can do | System response |
| --- | --- | --- | --- |
| Idea intake | A simple place to state a rough idea, attach notes, or describe desired outcome. | Enter raw intent in natural language. | Hermes preserves wording and infers objective, output, and risk. |
| Direction check | A concise summary of intended direction, output, non-goals, and material risk. | Approve direction, adjust direction, reject direction, or stop. | Hermes confirms or reopens the Demand Contract. |
| Executing/status | Current state, product target, what is happening, decision need, risk, and preview readiness. | Wait, stop, or respond to a HumanGate prompt. | Loop and Codex progress remain internal; state is summarized. |
| Preview | Artifact-level result, changed artifact name, meaningful summary, evidence, and known risks. | Inspect the result without reading internals. | Hermes translates internal work into product language. |
| Satisfaction feedback | Controls for approve, adjust, reject, continue, and stop. | Judge satisfaction or request correction. | Feedback is classified and routed. |
| Correction/stop | A repair, revised direction, continuation, HumanGate, Done, DoneWithRisk, Blocked, or stopped state. | Continue only when desired and authorized. | No feedback disappears into chat memory only. |

The creator must not be required to operate `.loop` files, work order syntax, prompt engineering, verifier commands, raw research layers, git diffs, or Knowledge Base schemas.

---

## 5. Internal Routing Flow

The future implementation must keep this route internally visible to the system, even if hidden from the creator by default:

```text
Hermes intake
-> Demand Contract formation
-> Loop state and authorization
-> Codex bounded execution
-> Verifier evidence gate
-> feedback route
-> learnback candidate or stop state
```

Internal routing responsibilities:

| Internal role | Required responsibility |
| --- | --- |
| Hermes | Preserve creator wording, infer objective, ask only necessary direction questions, compile Demand Contract, summarize status, route feedback, create HumanGate prompts. |
| Demand Contract | Hold objective, scope, non-goals, allowed surface, forbidden scope, acceptance criteria, verifier needs, risks, stop states, and HumanGate triggers. |
| Loop | Preserve durable state, current step, authorization, evidence, stop gate, and handoff when work spans rounds. |
| Codex | Execute only the bounded task defined by the future work order. |
| Verifier | Check artifact existence, scope, forbidden paths, required concepts, semantic fit, evidence, and stop-state classification. |
| Feedback/learnback | Route creator satisfaction or dissatisfaction to Done, DoneWithRisk, Repair, revised Demand Contract, HumanGate, continuation, stop, or candidate knowledge/workflow update. |

---

## 6. Explicit User Role and System Role Boundaries

| Boundary | Creator owns | System owns |
| --- | --- | --- |
| Idea | Desired outcome, raw language, examples, constraints. | Preservation, interpretation, route selection. |
| Direction | Value judgment, audience, purpose, priority, major non-goals. | Summary, ambiguity detection, demand formation. |
| Execution | Continue/stop authority and risk acceptance when needed. | Bounded work, state, evidence, checks, repair routing. |
| Preview | Satisfaction judgment and correction signal. | Artifact-level summary, changed artifacts, evidence, risks. |
| Feedback | Approve, adjust, reject, continue, or stop. | Classification and routing to contract, Loop, Codex, Verifier, Research, KB, or HumanGate. |
| Risk | Accept, reject, or ask to repair user-owned risk. | Name risk, avoid hidden defaults, block unauthorized continuation. |

Codex must never own product direction, scope expansion, HumanGate decisions, risk acceptance, or final completion judgment.

---

## 7. Allowed Future Implementation Surface

Because the final codebase surface is not defined yet, the next work order must express implementation scope by category unless it names exact files.

Allowed categories for the first implementation round:

- a prototype document that defines screen/state behavior;
- a single static HTML/CSS/JS mockup with no build system;
- a local web prototype inside a clearly named prototype surface;
- a future app surface only if the work order names exact files and keeps the slice minimal;
- fixture or sample content embedded directly in the prototype, if needed to demonstrate states;
- lightweight verification notes or commands specific to the prototype.

The allowed surface must remain focused on the complete MVP loop, not platform architecture.

---

## 8. Forbidden Future Implementation Scope

The first implementation round must not:

- implement the full Loop OS;
- create CLI tools;
- add dependencies, packages, framework migrations, services, databases, auth, accounts, integrations, or network behavior;
- create broad app architecture;
- expose `.loop`, work order syntax, raw verifier output, research layers, git mechanics, or KB schemas as the default creator interface;
- implement automatic Knowledge Base promotion;
- modify protocol, template, runner, verifier, workflow, knowledge base, trial, script, or test directories unless a future HumanGate explicitly authorizes it;
- commit changes;
- claim Done from Codex self-report without verifier evidence;
- continue after stop feedback.

---

## 9. MVP States and Transitions

| State | Creator-facing meaning | Internal owner | Valid next states |
| --- | --- | --- | --- |
| Intake | The creator's idea is being captured. | Hermes | DirectionCheck, HumanGate, Stop |
| DirectionCheck | The system needs confirmation of direction, output, non-goals, or risk. | Hermes / HumanGate | Preparing, Intake, Stop |
| Preparing | The system is forming executable demand. | Hermes | Executing, HumanGate, Blocked |
| Executing | Work is running inside approved bounds. | Codex / Loop | Checking, Blocked, HumanGate |
| Checking | Evidence and scope are being verified. | Verifier | Preview, Repair, DoneWithRisk, Blocked, HumanGate |
| Preview | Artifact-level result is ready for judgment. | Hermes | Feedback, DoneWithRisk, Done |
| Feedback | The creator is deciding approve, adjust, reject, continue, or stop. | Creator / Hermes | Done, Repair, DirectionCheck, Preparing, HumanGate, Stop |
| Repair | A bounded correction is authorized. | Hermes / Codex / Verifier | Preparing, Executing, Checking, Preview |
| HumanGate | A user-owned decision is required before continuing. | Creator / Hermes | DirectionCheck, Preparing, DoneWithRisk, Stop |
| Done | Contract and evidence pass with no material open risk. | Verifier / Hermes | Stop or future new demand |
| DoneWithRisk | Usable result exists with named risk or unverified assumption. | Verifier / Hermes | Feedback, Repair, Stop |
| Blocked | Progress requires missing input, file, tool, permission, or external condition. | Hermes / Loop | HumanGate, Preparing, Stop |
| Stop | Automatic execution is halted. | Creator / Hermes | Future new demand only |

Repair may be an internal route when the correction is already authorized. It should appear to the creator as an adjustment in progress.

---

## 10. Required Creator-Facing Controls

The MVP must include these controls as first-class feedback options:

| Control | Creator meaning | Required route |
| --- | --- | --- |
| Approve | This satisfies the current intent. | Mark Done if verifier evidence passes, or DoneWithRisk if creator accepts named risk. |
| Adjust | Direction is close, but details, tone, depth, structure, or quality need repair. | Create bounded Repair inside authorized scope. |
| Reject | The output misses intent or value. | Reopen DirectionCheck or Demand Contract; do not patch details blindly. |
| Continue | The creator wants another slice in the same direction. | Continue only if already in scope; otherwise HumanGate. |
| Stop | The creator wants work to halt. | Stop automatic execution and preserve state or handoff if needed. |

If feedback is ambiguous, Hermes may ask one classification question about whether the issue is direction, detail, evidence, depth, scope, or stop.

---

## 11. HumanGate Triggers

The MVP must stop and ask the creator when:

- direction, value, audience, priority, or satisfaction is unclear;
- user feedback contradicts the active Demand Contract;
- the next step expands scope beyond the authorized slice;
- implementation would move from contract/prototype into product code without authorization;
- work would touch forbidden paths or add dependencies, integrations, network behavior, commits, or durable data storage;
- verification cannot prove a required outcome and risk acceptance is needed;
- the result is usable but has a named risk that the creator must accept;
- a stop request has been received;
- the next action is irreversible, costly, or changes the Human/Hermes/Codex/Verifier responsibility model.

HumanGate prompts must be short, choice-oriented, and about creator-owned decisions. They must not ask the creator to choose routine mechanics such as file structure, command syntax, or verifier implementation unless those choices change value, risk, or scope.

---

## 12. Evidence and Verifier Requirements

Creator-facing evidence summary must include:

- artifact created or changed;
- current state and stop state;
- checks performed and pass/fail result;
- scope boundary result;
- forbidden-path result when relevant;
- known risks, assumptions, or gaps;
- whether a creator decision is needed.

Internal verifier requirements for the future implementation:

- required artifact exists and is substantial enough for the selected implementation category;
- the user-facing flow includes idea intake, direction check, status, preview, satisfaction feedback, and correction/stop;
- the internal route includes Hermes, Demand Contract, Loop, Codex, Verifier, and feedback/learnback concepts;
- creator controls include approve, adjust, reject, continue, and stop;
- MVP states and transitions are represented;
- HumanGate triggers are visible in the model;
- internal machinery is not the default creator interface;
- forbidden scope is not implemented;
- changed files match the future work order's allowed surface;
- Done is supported by evidence, not by Codex self-report.

DoneWithRisk is required when the artifact is usable but any material verification, semantic, scope, or assumption gap remains.

---

## 13. Acceptance Criteria for Future Implementation

A future implementation of `Creator MVP Loop v0.1` is acceptable only if:

- it implements one complete creator-facing loop from idea intake through feedback routing;
- it names the product slice as `Creator MVP Loop v0.1`;
- it keeps creator-facing simplicity separate from internal routing rigor;
- it includes all required controls: approve, adjust, reject, continue, stop;
- it represents the states listed in this contract or a documented strict subset that still supports the complete loop;
- it exposes artifact preview and evidence summary without requiring raw internals;
- it includes HumanGate as a decision state, not an error state;
- it prevents continuation after stop;
- it makes scope expansion require HumanGate;
- it avoids full app architecture, CLI tooling, dependencies, commits, or unauthorized directories;
- it provides verifier evidence and changed-file scope evidence;
- it can be reviewed against this contract without relying on chat memory.

Minimum viable completion:

```text
One browsable or inspectable prototype surface that demonstrates the full creator loop,
with visible states, controls, preview/evidence areas, HumanGate behavior, and correction routes.
```

Unacceptable completion:

- a marketing page instead of the usable loop;
- a raw internal console;
- a theory-only document with no implementable surface decision;
- a full architecture pass that skips the MVP loop;
- a prototype that has no evidence summary, no HumanGate, or no correction routing.

---

## 14. Failure Modes / Anti-Patterns to Prevent

| Failure mode | Prevention |
| --- | --- |
| Implementation before demand | Future work order must cite this contract and keep scope bounded. |
| Internal console as product | Default surface must use creator actions, not `.loop`, git, verifier, or work order mechanics. |
| Chat-only simplification | Surface must show state, preview, evidence, risk, and stop state. |
| Codex free-running | Future work order must define allowed files, forbidden files, checks, and stop states. |
| Direction bypass | DirectionCheck or HumanGate is required when value, scope, or risk is unclear. |
| HumanGate spam | Ask only for creator-owned decisions. |
| HumanGate bypass | Scope, risk, dependency, integration, forbidden path, or commit changes require user authorization. |
| Satisfaction ignored | Every feedback option must route to Done, Repair, revised Demand Contract, HumanGate, continuation, stop, or learnback. |
| Verification theater | Checks must be named and tied to evidence. |
| Preview absent | Creator must be able to judge the artifact-level result. |
| Scope drift through continue | Continue must remain in scope or trigger HumanGate. |
| DoneWithRisk hidden | Usable but unverified results must name risk. |
| Learnback dump | Only stable lessons become durable knowledge; other lessons remain candidates. |

---

## 15. Open Decisions Before Implementation

These decisions should be resolved by the next implementation work order or a short HumanGate prompt:

1. Select the implementation category: prototype document, single static HTML mockup, local web prototype, or named future app surface.
2. Decide whether the MVP uses static sample data only or connects to any real Loop artifacts. The recommended first slice is static sample data.
3. Name the exact allowed implementation files if the work order chooses a real repo surface.
4. Decide the verifier commands appropriate to the selected surface.
5. Decide whether browser verification is required for a web prototype.
6. Decide how much optional evidence detail is inspectable beyond the default creator summary.

Recommended defaults for the next round:

- use a single static HTML/CSS/JS mockup or a narrowly scoped local prototype;
- use static sample data;
- do not connect to real `.loop` state;
- do not add dependencies;
- verify by file checks, required text/state coverage, changed-file scope, and browser screenshot if applicable.

---

## 16. Suggested Next Codex Implementation Work Order

Task name:

```text
Implement Creator MVP Loop v0.1 Prototype
```

Objective:

```text
Build the smallest browsable prototype that demonstrates the Creator MVP Loop v0.1:
idea intake -> direction check -> executing/status -> preview -> satisfaction feedback
-> correction/stop, while showing internal routing and evidence only as summarized,
creator-facing information.
```

Read first:

- `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`
- `CREATOR_INTERFACE_CONTRACT_V0_1.md`
- `CREATOR_WORKFLOW_OPERATING_MODEL.md`
- `CREATOR_WORKFLOW_ANTI_PATTERNS.md`
- `CORE_PRINCIPLES.md`
- `INDEX.md`

Allowed implementation surface:

```text
To be selected before execution. Recommended: one static prototype artifact
or one narrowly scoped local web prototype surface named explicitly in the work order.
```

Forbidden scope:

```text
No full app architecture, no CLI tools, no dependencies, no commits, no real Loop
automation, no protocol/template/runner/verifier/workflow/knowledge-base/test/script
directory changes, and no default exposure of raw internals.
```

Required output:

- one creator-facing prototype surface for the complete MVP loop;
- visible states and transitions;
- controls for approve, adjust, reject, continue, and stop;
- artifact preview area;
- evidence summary area;
- HumanGate decision state;
- correction routing behavior or clearly inspectable static demonstration;
- verification evidence and changed-file scope report.

Acceptance checks:

- required flow steps are present;
- required controls are present;
- MVP states or strict subset are present;
- HumanGate triggers are represented;
- preview and evidence summary are visible;
- internal machinery is summarized, not exposed as required user work;
- changed files are limited to the future allowed surface;
- no dependencies, CLI, commits, or forbidden paths are added.

Completion report:

- files changed;
- product slice implemented;
- verification commands and results;
- forbidden path check;
- stop state: Done, DoneWithRisk, Blocked, HumanGate, or Repair;
- risks and remaining open decisions.
