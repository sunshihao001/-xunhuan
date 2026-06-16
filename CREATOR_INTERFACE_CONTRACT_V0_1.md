# Creator Interface Contract v0.1

Version: v0.1  
Status: creator-facing product interface contract  
Scope: future MVP surface between a non-technical creator and internal Hermes, Codex, Loop, Verifier, Research, and Knowledge Base machinery

---

## 1. Purpose and Product Boundary

This contract defines what the creator sees, what the system hides, and how creator feedback routes back into the internal operating system.

The boundary is:

```text
creator-facing surface:
idea -> direction check -> status -> preview -> satisfaction feedback -> correction

internal operating system:
Hermes intake -> Demand Contract -> Research if needed -> Loop state
-> Codex bounded execution -> Verifier evidence gate
-> feedback route -> Knowledge Base / workflow learnback
```

The future MVP must let the creator operate through natural product actions, not through work orders, verifier commands, git mechanics, prompt engineering, research-pack layers, or `.loop` files. The internal system must still preserve contracts, allowed scope, forbidden scope, evidence, state, stop states, and learnback.

This document is not a UI implementation. It is the interface contract that a later product slice should implement.

---

## 2. Creator-Facing Principle

The creator owns creative authority. The system owns translation, execution, evidence, and routing.

The creator-facing product should support these actions:

- state an idea;
- confirm or adjust high-level direction;
- inspect progress status;
- preview the resulting artifact;
- say approve, adjust, reject, continue, or stop;
- give corrections in natural language.

The creator should not be asked to choose routine implementation mechanics when the demand is already bounded and verifiable. Simplicity at the surface must not remove internal rigor.

---

## 3. User Roles / System Roles

| Role | Creator-facing responsibility | Internal responsibility |
| --- | --- | --- |
| Creator | Idea, direction, value judgment, satisfaction, risk boundary, continue/stop decision, major correction. | Provides authority signals that Hermes converts into contract changes or routes. |
| Hermes | Product-facing guide that asks only necessary questions and summarizes result, risk, and evidence. | Translates intent into Demand Contract, work order, HumanGate prompt, feedback route, and learnback candidate. |
| Codex | Appears only as "work is being performed" unless details are useful evidence. | Executes bounded tasks inside allowed files, avoids forbidden scope, runs checks, and reports evidence. |
| Loop | Appears as resumable status and handoff when needed. | Preserves objective, path, state, log, acceptance, stop gate, and work order context. |
| Verifier | Appears as evidence status: passed, risk, repair needed, blocked, or decision needed. | Independently checks artifacts, commands, diff scope, forbidden paths, required concepts, and semantic fit. |
| Research | Appears as concise sourced context, confidence, and conflict notes. | Separates raw, clean, reading, insight, candidate, and stable knowledge layers. |
| Knowledge Base | Appears as stable reusable context or a note that a lesson was captured as candidate. | Stores durable conclusions only with source trail, confidence, boundaries, and promotion status. |
| HumanGate | Appears as a short decision prompt. | Stops automatic progress when direction, value, risk, scope, authorization, or satisfaction belongs to the creator. |

---

## 4. Input Contract: What the Creator Can Say or Provide

The interface must accept rough, incomplete, and non-technical input. Valid creator input includes:

- a raw idea or desired outcome;
- existing text, files, links, notes, screenshots, or examples;
- target audience, purpose, tone, constraints, or quality bar;
- boundary statements such as "do not change this", "keep it simple", or "avoid implementation";
- direction feedback such as "this is the wrong product angle";
- detail feedback such as "this section is too shallow";
- satisfaction feedback such as "approve", "adjust", "reject", "continue", or "stop";
- risk preference such as "ship with this gap" or "do not proceed until verified".

Hermes must preserve the creator's original wording while converting it into executable demand. If input is enough to proceed safely, the system should not over-question. If input contains incompatible directions, missing authority, or material risk, the system enters DirectionCheck or HumanGate.

---

## 5. Direction-Check Contract

Direction checks are high-level confirmations, not implementation interviews.

The system asks for confirmation only when:

- multiple plausible product directions would lead to different outcomes;
- the intended artifact, audience, or value is unclear;
- the next step would change scope, risk, dependency, integration, commit behavior, or forbidden paths;
- feedback contradicts the active Demand Contract;
- verification cannot prove a required outcome without user risk acceptance.

A direction check should show:

- the inferred objective;
- the expected output;
- major non-goals;
- the material risk or choice;
- two or three meaningful options when possible.

Example:

```text
I can treat this as a first MVP interface contract, or as a broader product strategy document. Which direction should govern this round?
```

The system must not ask the creator to choose file structure, command syntax, prompt format, verifier implementation, or other routine mechanics unless those choices change user-owned value, risk, or scope.

---

## 6. Status Contract

Status visible to the creator must be short, stateful, and product-oriented.

Required visible status fields:

- current state;
- current product target;
- what is happening now;
- whether a decision is needed;
- whether risk is known;
- whether a preview is ready.

Recommended user-facing states:

| Visible status | Meaning |
| --- | --- |
| Intake | The creator's idea is being captured and interpreted. |
| DirectionCheck | The system needs a high-level confirmation or correction. |
| Preparing | Hermes is forming the executable demand or selecting context. |
| Executing | Internal work is running inside authorized bounds. |
| Checking | Verifier is checking evidence and scope. |
| Preview | A result is ready for creator judgment. |
| Feedback | The system is waiting for approve, adjust, reject, continue, or stop. |
| HumanGate | A user-owned decision is required before continuing. |
| Done | The required result is complete with no material open risk. |
| DoneWithRisk | The result is usable, but a named risk remains. |
| Blocked | Progress cannot continue until a missing input, tool, file, permission, or external condition changes. |

The creator should not see raw Loop logs by default. The interface may expose "details" or "evidence" as an optional expansion.

---

## 7. Preview Contract

Preview is the artifact-level view the creator uses to judge satisfaction.

The preview must include:

- the created or changed artifact name;
- the product-level result, not just an internal summary;
- the meaningful change summary;
- any known limitation or risk;
- a clear feedback prompt.

For document artifacts, preview can show the title, section list, key claims, and changed-file link. For UI artifacts, preview can show the running surface, screenshots, or interaction path. For code artifacts, preview should describe user-visible behavior and verification evidence without requiring the creator to inspect diffs.

The preview should not be replaced by:

- raw git diff as the primary interface;
- Codex execution transcript;
- verifier command output without interpretation;
- internal work order text;
- research dumps.

---

## 8. Satisfaction Feedback Contract

The interface must treat satisfaction as product evidence, not casual chat.

Supported creator feedback:

| Feedback | Creator meaning | Required system route |
| --- | --- | --- |
| Approve | The result satisfies the current intent. | Mark Done if verification supports it, or DoneWithRisk if accepted risk remains. |
| Adjust | Direction is mostly right, but detail, depth, tone, structure, or quality needs repair. | Create bounded repair or continuation inside allowed scope. |
| Reject | The result misses intent or value. | Reopen direction, Demand Contract, or HumanGate depending on cause. |
| Continue | The creator wants another slice in the same direction. | Continue only if scope is authorized; otherwise HumanGate. |
| Stop | The creator wants work to halt. | Stop automatic execution, preserve state and handoff if needed. |

If feedback is ambiguous, Hermes should ask one classification question:

```text
Is the issue the overall direction, a specific detail, missing evidence, or the amount of depth?
```

---

## 9. Correction Routing

Feedback must map to a concrete internal destination.

| Creator signal | Demand Contract | Loop | Codex | Verifier | Research / KB |
| --- | --- | --- | --- | --- | --- |
| Direction wrong | Reopen objective, scope, non-goals, and acceptance. | Preserve revised direction and reason. | Pause detail repair until new work order exists. | Flag semantic mismatch. | Candidate workflow warning if repeated. |
| Detail wrong | Keep objective; add bounded repair criteria. | Record repair state and handoff. | Repair allowed artifact details. | Recheck corrected output and diff scope. | Candidate defect lesson if repeated. |
| Not enough evidence | Add evidence requirement or risk condition. | Record DoneWithRisk or Repair path. | Run allowed checks or gather authorized evidence. | Check evidence gap. | Research route if external evidence is needed. |
| Scope too broad | Narrow objective and non-goals. | Preserve scope reduction. | Stop broad execution; repair only inside reduced scope. | Check output against narrowed scope. | No KB promotion unless stable. |
| Continue/deepen | Add next-slice objective if in scope. | Create next state or handoff. | Execute next bounded round. | Verify new acceptance criteria. | Capture productization path candidate. |
| Stop | Close or pause contract. | Preserve stop state. | Stop. | Confirm no unauthorized continuation. | Record reusable reason only if useful. |
| Stable lesson | Add future contract rule only after approval. | Preserve learnback candidate. | None unless future work order uses it. | Check promotion status. | Candidate or stable KB entry depending on gates. |

No feedback should disappear into conversation memory only.

---

## 10. HumanGate Contract

HumanGate is a decision state, not an error state.

The system must stop and ask when:

- direction, value, priority, or satisfaction is unclear;
- the creator must accept known risk;
- work would expand scope or touch forbidden paths;
- work would add dependencies, integrations, network behavior, or commits not already authorized;
- external research changes the product direction or confidence;
- implementation would begin after a documentation-only contract;
- feedback contradicts the current Demand Contract;
- the next step is irreversible or costly.

HumanGate prompt requirements:

- one short statement of why the decision is needed;
- two or three clear options when possible;
- no routine technical minutiae;
- no hidden default that changes risk, scope, or direction.

Example:

```text
The contract is ready to drive an MVP implementation slice, but implementation would move from design docs into product files. Continue to an implementation work order, or keep refining the contract?
```

---

## 11. Internal-Hidden Contract

The following details should not be exposed by default:

- `.loop` file structure and raw state content;
- work order syntax;
- prompt engineering details;
- raw verifier command output;
- internal Codex execution transcript;
- raw research-pack layers;
- git diff mechanics and commit workflow;
- Knowledge Base schemas and promotion internals;
- forbidden-path enforcement mechanics;
- implementation file choices that do not affect creator-owned value.

The following must remain visible in summarized form:

- current state;
- artifact preview;
- changed artifact names;
- evidence summary;
- risk and residual gaps;
- decision prompts;
- feedback options;
- stop state.

The interface hides machinery, not accountability.

---

## 12. Evidence Contract

The creator sees evidence summaries, while Verifier retains detailed checks.

Creator-facing evidence summary should include:

- artifacts created or changed;
- checks performed and whether they passed;
- scope boundary result, including forbidden paths unchanged when relevant;
- known risks or unverified assumptions;
- stop state: Done, DoneWithRisk, Repair, HumanGate, Blocked, or stopped by user.

Internal evidence may include:

- file existence and size checks;
- required section or term coverage;
- command output;
- `git diff --name-only`;
- semantic fit against Demand Contract;
- research source trail and confidence;
- KB promotion status.

The system must not claim Done from Codex self-report alone. If evidence is incomplete but the artifact is usable, the correct state is DoneWithRisk.

---

## 13. Interface State Model

The minimal state model for the MVP is:

| State | Creator sees | Internal owner | Exit condition |
| --- | --- | --- | --- |
| Intake | A place to state or attach the idea. | Hermes | Objective is inferred or ambiguity is found. |
| DirectionCheck | A concise direction summary and confirmation options. | Hermes / HumanGate | Creator confirms, corrects, or stops. |
| Preparing | The system is converting direction into executable work. | Hermes / Research | Demand is ready, research is routed, or HumanGate appears. |
| Executing | Work is running inside approved bounds. | Codex / Loop | Artifact exists or execution hits a blocker. |
| Checking | Result is being verified. | Verifier | Done, DoneWithRisk, Repair, HumanGate, or Blocked is selected. |
| Preview | Artifact and summary are ready to inspect. | Hermes | Creator gives satisfaction feedback. |
| Feedback | Approve, adjust, reject, continue, or stop. | Creator / Hermes | Feedback is routed. |
| HumanGate | A user-owned decision is required. | Creator / Hermes | Creator chooses a direction or stop. |
| Done | Work satisfies contract and checks. | Verifier / Hermes | No automatic continuation unless requested. |
| DoneWithRisk | Work is usable with named risk. | Verifier / Hermes | Creator accepts risk, requests repair, or stops. |
| Blocked | Missing condition prevents progress. | Hermes / Loop | Missing input, tool, permission, file, or external state changes. |

Repair is an internal route from Checking or Feedback back to Preparing or Executing. It may appear to the creator as "adjustment in progress" when the repair is already authorized.

---

## 14. MVP Implications

This contract enables the next product slice:

```text
Creator MVP Loop v0.1: a single creator-facing flow from idea intake to direction confirmation, bounded execution status, artifact preview, evidence summary, satisfaction feedback, and correction routing.
```

The first implementation slice should implement only the smallest complete loop:

- intake field for rough creator intent;
- direction confirmation surface;
- status display for Preparing, Executing, Checking, Preview, HumanGate, DoneWithRisk, Done, and Blocked;
- artifact preview area;
- evidence summary area;
- feedback controls for approve, adjust, reject, continue, and stop;
- routing model that maps feedback to Demand Contract revision, bounded Codex rework, Verifier check, Research request, KB candidate, HumanGate, or stop state.

Non-goals for the first slice:

- full visual design system;
- full `.loop` editor;
- raw verifier console;
- research-pack browser;
- git UI;
- automatic Knowledge Base promotion;
- open-ended agent control panel.

---

## 15. Anti-Patterns

Interface-level failure modes to avoid:

| Anti-pattern | Failure | Required prevention |
| --- | --- | --- |
| Internal console as product | The creator must operate work orders, `.loop`, verifier output, git diffs, or research layers. | Keep those as optional evidence details, not the default path. |
| Chat-only simplification | The product hides contracts, state, evidence, and risks. | Show concise status, preview, evidence summary, risk, and stop state. |
| Direction bypass | The system proceeds despite unclear value, scope, or risk. | Enter DirectionCheck or HumanGate. |
| HumanGate spam | The creator is asked routine implementation questions. | Ask only for user-owned decisions. |
| Satisfaction ignored | Feedback does not change the route. | Every feedback item must map to repair, revision, continuation, stop, HumanGate, or learnback. |
| Verification theater | The system says "checked" without evidence. | Summarize actual checks and keep detailed verifier evidence internally inspectable. |
| Preview absent | The creator cannot judge the artifact itself. | Show the product artifact or a concrete artifact-level summary. |
| Scope drift through continue | Continue becomes unbounded expansion. | Require next-slice scope or HumanGate when direction changes. |
| Risk hidden as polish | Simple wording conceals failed checks or assumptions. | Use DoneWithRisk when any material gap remains. |
| Learnback dump | Every comment becomes durable knowledge. | Preserve candidate versus stable status and require promotion gates. |

---

## 16. Verifier Checklist

Hermes or Verifier can check that this interface contract was respected by asking:

- Does the creator-facing flow use idea, direction, status, preview, satisfaction, and correction as the primary actions?
- Does the interface avoid requiring the creator to operate `.loop`, work orders, verifier commands, raw research, git, or KB schemas?
- Does every visible state map to an internal owner and next route?
- Does the direction check ask only about high-level value, scope, risk, or output?
- Does status include current state, product target, decision need, preview readiness, and risk where relevant?
- Does preview show the artifact-level result rather than only internal execution details?
- Do approve, adjust, reject, continue, and stop each have concrete internal destinations?
- Does correction routing distinguish direction failure from detail repair, evidence gap, continuation, stop, Research, and KB candidate?
- Does HumanGate appear for user-owned decisions and not for routine mechanics?
- Are hidden internals still represented by summarized evidence, changed artifacts, risks, and stop state?
- Is Done based on verifier evidence rather than Codex self-report?
- Is DoneWithRisk used when the result is usable but evidence or assumptions remain incomplete?
- Does the MVP implication name the next product slice and exclude overbuilt internals?
- Are interface anti-patterns checkable before implementation?

If any answer is no, the future product slice should stop in Repair, HumanGate, or DoneWithRisk rather than claim Done.

