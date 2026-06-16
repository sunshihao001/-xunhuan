# Creator Workflow Operating Model

Version: v1.0  
Status: operating model for creator-first workflow execution  
Scope: idea intake through final correction, stop states, feedback routing, and learnback

---

## 1. Operating Principle

The operating model converts a creator's natural workflow into a rigorous internal workflow.

Creator-facing loop:

```text
idea -> direction check -> execution status -> artifact preview -> satisfaction feedback -> correction
```

Internal loop:

```text
Hermes intake -> demand interrogation -> Research if needed -> Demand Contract
-> Loop state -> Codex work order -> bounded execution
-> Verifier evidence gate -> stop state -> feedback route
-> Knowledge Base / workflow learnback
```

The user should experience the first loop. The system must preserve the second loop.

---

## 2. Lifecycle Stages

| Stage | User-facing state | Internal state | Primary owner | Output |
| --- | --- | --- | --- | --- |
| 1. Idea intake | "I have an idea." | Surface ask captured; objective guessed. | Hermes | Intake summary and route. |
| 2. Direction check | "Is this what you mean?" | Scope, non-goals, risk, and ambiguity identified. | Hermes / HumanGate | Confirmed direction or clarification. |
| 3. Demand formation | "The system is preparing the task." | Demand Contract or work order structure created. | Hermes | Bounded execution contract. |
| 4. Evidence preparation | "Research is being used if needed." | Raw/candidate/stable context separated. | Research / Knowledge Base | Curated context and candidate notes. |
| 5. Execution | "Work is running." | Codex executes allowed work only. | Codex | Artifact changes and command evidence. |
| 6. State preservation | "Progress can be resumed." | Loop records state, log, stop gate, handoff. | Loop | Durable execution record. |
| 7. Verification | "Result is being checked." | Verifier checks evidence and semantic fit. | Verifier | Done, DoneWithRisk, Repair, HumanGate, or Blocked. |
| 8. Preview | "Here is the result." | Hermes summarizes artifact, evidence, risk. | Hermes | Creator-facing report. |
| 9. Satisfaction | "Are you satisfied?" | Feedback classified and routed. | User / Hermes | Accept, repair, revise, continue, or stop. |
| 10. Learnback | "Reusable lesson captured if stable." | KB/workflow candidate updated only through gates. | Hermes / Research / Knowledge Base | Stable conclusion or candidate patch. |

---

## 3. Subsystem Responsibilities

| Subsystem | Responsibility | Must not do |
| --- | --- | --- |
| User | Own idea, direction, value, satisfaction, risk, stop/continue, correction. | Operate internals by default. |
| Hermes | Translate creator intent into contracts, routes, reports, HumanGate prompts, and learnback candidates. | Hide material risk or ask routine mechanical questions. |
| Codex | Execute bounded work, modify allowed files, run checks, report evidence. | Decide product direction or expand scope. |
| Loop | Preserve state, log, handoff, authorization, stop states, and resumability. | Become the normal user-facing interface. |
| Verifier | Independently check evidence, boundaries, commands, content, and stop state. | Treat Codex self-report as final proof. |
| Research | Preserve provenance and separate evidence layers. | Promote raw evidence directly into stable rules. |
| Knowledge Base | Store stable reusable conclusions and boundaries. | Store unsupported or temporary claims as accepted behavior. |
| HumanGate | Protect user-owned decisions. | Interrupt routine authorized execution. |

---

## 4. State Model

| User-facing state | Internal state | Meaning | Next route |
| --- | --- | --- | --- |
| Direction needed | HumanGate | The system cannot choose value, risk, or scope. | Ask the user a short decision question. |
| Preparing | Demand formation | Hermes is converting intent into executable shape. | Research, Codex, or HumanGate. |
| Running | Execution | Codex is operating inside allowed bounds. | Verification. |
| Checking | Verification | Verifier is evaluating evidence. | Done, DoneWithRisk, Repair, HumanGate, Blocked. |
| Preview ready | Done or DoneWithRisk | Artifact can be judged by the user. | Satisfaction feedback. |
| Needs repair | Repair | Check failed but fix is in scope. | Bounded correction. |
| Needs decision | HumanGate | A user-owned choice is required. | Continue after decision. |
| Stopped | Done, Blocked, or user stop | No automatic continuation. | Handoff or new demand. |

---

## 5. Feedback Routing

| Feedback | Meaning | Hermes route | Codex route | Verifier route | Learnback route |
| --- | --- | --- | --- | --- | --- |
| Satisfied | The result fits intent enough to accept. | Mark Done or next authorized slice. | None unless new work is requested. | Confirm evidence supports Done. | Capture reusable success pattern if stable. |
| Not satisfied | The result misses value or quality. | Ask whether issue is direction, detail, depth, or scope if unclear. | Wait for bounded correction. | Check mismatch against contract. | Candidate lesson. |
| Direction wrong | The objective or product framing is wrong. | Reopen direction and Demand Contract. | Do not patch details as if direction is valid. | Flag semantic mismatch. | Candidate workflow warning. |
| Detail wrong | The direction is right but artifact needs repair. | Create bounded repair task. | Fix allowed artifact details. | Recheck corrected output. | Capture if repeated. |
| Continue/deepen | More work is desired. | Continue if in scope; HumanGate if scope expands. | Execute next bounded round. | Check new acceptance criteria. | Candidate productization path. |
| Stop | User wants execution to stop. | Preserve status and handoff. | Stop. | Confirm stop state. | Record reason if reusable. |

Satisfaction is not merely sentiment. It is product evidence. It changes the internal route.

---

## 6. Stop States

| Stop state | Condition | User-facing report |
| --- | --- | --- |
| Done | Required artifacts exist, checks pass, forbidden paths unchanged, and no material gap remains. | "The artifact is ready for your satisfaction judgment." |
| DoneWithRisk | Usable artifact exists, but a named gap or unchecked assumption remains. | "The result is usable, with this risk." |
| Repair | Verification failed, but the fix is bounded and authorized. | "A correction is needed and can be handled inside scope." |
| HumanGate | Direction, value, risk, scope, authorization, or satisfaction decision is needed. | "A decision from you is needed before continuing." |
| Blocked | Missing input, file, tool, permission, or external condition prevents progress. | "The system cannot continue until this blocker changes." |

---

## 7. Operating Rules

1. Demand before execution: Hermes must not hand vague work to Codex when direction, output, or acceptance is unclear.
2. Bounded execution: Codex must obey allowed and forbidden files and avoid unauthorized tools, dependencies, protocol changes, and commits.
3. Independent verification: Verifier must inspect evidence rather than trust Codex self-report.
4. Durable state: Loop must preserve enough context for a future round to resume.
5. HumanGate discipline: ask only for decisions that belong to the user.
6. Knowledge gates: Research and Knowledge Base must keep raw, candidate, stable, and workflow material separate.
7. Productization link: each theory or scenario should affect interface behavior, work order shape, verifier checks, feedback routing, or learnback.

---

## 8. Learnback

Learnback happens after evidence or feedback exposes a reusable lesson. It may create:

- a Knowledge Base candidate,
- a workflow patch candidate,
- a future verifier check,
- a future Demand Contract field,
- a warning for HumanGate,
- a product interface requirement.

Candidate workflow patches from audit research remain candidate until an authorized promotion round accepts them. This operating model may cite their direction, but it does not change protocols or templates.

---

## 9. Productization Implication

The future creator-facing interface should not mirror repository internals. It should expose:

- idea intake,
- direction confirmation,
- execution state,
- artifact preview,
- evidence summary,
- risk note,
- satisfaction controls,
- correction route.

Internally, the system can continue using Hermes, Codex, Loop, Verifier, Research, Knowledge Base, HumanGate, and Git/GitHub. Product maturity means the user sees fewer mechanics while the system preserves more reliable evidence.
