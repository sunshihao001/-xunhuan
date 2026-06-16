# Core Principles Application Matrix

Version: v0.1  
Status: scenario mapping for creator-first workflow productization  
Scope: practical use of core principles across user-facing and internal workflow scenarios

---

## Purpose

This matrix maps the core principles to concrete product and workflow scenarios. It exists to prevent the principles from becoming abstract theory. Each scenario states what the user sees, what the system does internally, which principles apply, and what acceptance or verifier signal proves the scenario is working.

Principle keys:

- P1 Creator Stays Creator
- P2 Encapsulation Preserves Rigor
- P3 Demand Before Execution
- P4 Bounded Executor, Not Product Owner
- P5 Verification Is Independent Evidence
- P6 State Must Outlive Chat
- P7 Knowledge Promotion Has Gates
- P8 HumanGate Protects Authority
- P9 Satisfaction Is Product Evidence
- P10 Theory Must Drive Productization

---

## Application Matrix

| Scenario | User sees | System does internally | Core principles applied | Acceptance / verifier signal |
| --- | --- | --- | --- | --- |
| Idea intake | A natural place to state a rough idea, expected outcome, or dissatisfaction. | Hermes preserves the original wording, guesses the real objective, identifies domain, output, constraints, and risk of wrong execution. | P1, P3, P8 | Intake keeps the user's words, names the suspected objective, and flags ambiguity without turning intake into implementation. |
| Demand interrogation | A short direction check with only necessary questions. | Hermes asks about goal, non-goals, target user, scope, allowed and forbidden areas, acceptance, and stop states when needed. | P1, P3, P8 | The task becomes executable without requiring the user to answer routine mechanical questions. |
| External research | A concise conclusion, confidence level, and any decision-relevant conflict. | Research collects sources, separates raw from clean, creates reading or insight layers, and prevents unsupported claims from becoming rules. | P2, P7, P8 | Sources have provenance, stable conclusions have boundaries, and conflicting value or direction issues trigger HumanGate. |
| Knowledge-base update | A short note that reusable knowledge was captured or held as candidate. | Hermes or Research promotes only stable, scoped conclusions into Knowledge Base candidates and workflow patch candidates. | P7, P10 | Knowledge Base material includes source trail, confidence, applicability boundary, and no raw source is promoted directly. |
| Codex long task | A product-status update, artifact preview, changed files, evidence summary, and risk note. | Codex reads the work order, stays inside allowed files, avoids forbidden paths, runs checks, repairs in scope, and reports results. | P2, P4, P5, P6 | Required files exist, checks pass, `git diff --name-only` is inside allowed scope, and Codex does not decide product direction. |
| Loop execution | A resumable status such as running, repair needed, HumanGate, or done with evidence. | Loop preserves target, path, acceptance criteria, state, log, stop gate, handoff, and work order content. | P2, P6, P10 | A future executor can resume from Loop artifacts without relying only on chat memory. |
| Verifier review | A concise pass, risk, repair, blocked, or HumanGate result. | Verifier independently checks file existence, required terms, file size, diff scope, forbidden paths, command output, and semantic fit. | P5, P2, P4 | The stop state is based on evidence, not Codex self-report. |
| Product preview | A concrete artifact or changed product surface that can be judged for usefulness. | Hermes translates internal work into creator-facing status, preview, evidence, risk, and feedback options. | P1, P2, P9 | The user can judge satisfaction without reading raw work order, verifier, research, or git internals. |
| Satisfaction feedback | Simple feedback such as satisfied, unsatisfied, wrong direction, wrong detail, continue, or stop. | Hermes classifies feedback and routes it to Done, Repair, revised Demand Contract, HumanGate, continuation, stop, or learnback. | P1, P8, P9 | Every feedback item has an internal destination and changes state, scope, artifact, or learnback. |
| Correction / repair | A bounded correction flow, not a restart from scratch. | Hermes determines whether the issue is direction, detail, quality, missing evidence, or scope; Codex receives a bounded repair work order if authorized. | P3, P4, P5, P9 | Detail errors create Repair; direction errors revisit Demand Contract or HumanGate; verifier failures are rechecked. |
| HumanGate | A short decision prompt about direction, risk, value, scope, cost, boundary, or authorization. | Hermes stops automatic execution when user-owned judgment is required and records the decision route. | P1, P8, P6 | HumanGate is used for meaningful authority decisions, not routine execution details. |
| Stop / handoff | A clear stop state and what can happen next. | Loop records Done, DoneWithRisk, Blocked, HumanGate, or Repair; HANDOFF preserves what a future actor must know. | P6, P8, P10 | The next round can continue, repair, or stop based on explicit state and evidence. |
| Workflow patch promotion | A candidate behavior change with reason, source trail, and verifier gate. | Hermes converts stable repeated lessons into workflow patch candidates and keeps candidates separate from accepted rules. | P7, P10, P5 | Patch candidates state target behavior, evidence source, verifier gate, and candidate status before promotion. |
| Future UI / interface | A creator-facing control surface for idea, direction, preview, satisfaction, and correction. | The interface hides internal mechanics while preserving access to status, evidence summary, risk, stop state, and correction route. | P1, P2, P8, P9, P10 | UI design does not expose raw machinery as normal user work and does not hide verification or risk needed for trust. |

---

## Scenario Details

### Idea intake

The product should accept incomplete human language. The first response should not be a work order unless the goal is already bounded. Hermes should reflect the intended direction in plain language and identify what needs clarification.

Acceptance signal: the user can recognize their idea in the system's summary, and the system can identify whether the next step is demand interrogation, research, Codex, HumanGate, or stop.

### Demand interrogation

Demand interrogation must be deep enough to prevent wrong execution but short enough to preserve creator momentum. The right question is not "what command should Codex run?" The right question is "what outcome would satisfy you, and what boundaries matter?"

Acceptance signal: the resulting Demand Contract or work order has goal, scope, non-goals, allowed files, forbidden files, outputs, acceptance criteria, verification, and stop states.

### External research and Knowledge Base

Research is useful only when it changes decision quality or future reuse. Temporary search can answer a temporary question. Durable workflow knowledge must preserve provenance and promotion gates.

Acceptance signal: raw material, candidate insights, stable conclusions, and workflow patches are not mixed. Knowledge Base entries include source trail, boundary, confidence, and limitations.

### Codex, Loop, and Verifier

Codex performs deep execution inside a narrow contract. Loop makes execution resumable. Verifier prevents self-certified Done. These three roles are the internal backbone of the operating system.

Acceptance signal: a future actor can inspect artifacts and know what was requested, what changed, what passed, what remains risky, and whether the round is Done, DoneWithRisk, Blocked, HumanGate, or Repair.

### Preview, satisfaction, and correction

The product preview is where internal rigor meets creator judgment. A technically valid artifact can still be unsatisfying. Satisfaction feedback must therefore be routed like product evidence, not treated as casual commentary.

Acceptance signal: dissatisfied feedback produces a concrete route: repair details, revisit direction, ask HumanGate, continue deeper, stop, or create learnback.

### Future interface

The future interface should be built around the creator loop, not the internal file structure. The normal surface should show product status, artifact preview, evidence summary, risk, stop state, and feedback controls. Advanced internals can remain inspectable, but they should not be required for routine creative operation.

Acceptance signal: the user can operate the workflow through idea, direction, satisfaction, and correction, while Hermes, Codex, Loop, Verifier, Research, and Knowledge Base preserve the full internal discipline.

---

## Productization Rule

Every future productization scenario must answer four questions:

1. What does the creator see and decide?
2. What does the system do internally?
3. Which core principles govern the behavior?
4. What evidence proves the behavior worked?

If a scenario cannot answer those questions, it is not ready for implementation.
