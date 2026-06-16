# Creator Workflow Theory v1

Version: v1.0  
Status: professional theory expansion  
Scope: creator-first AI workflow operating system, productization, verification, and learnback

---

## 1. Thesis

The creator-first AI workflow operating system exists to let a non-technical creator work through ideas, direction, satisfaction, and correction while rigorous internal subsystems handle demand clarification, research, bounded execution, verification, durable state, and learnback.

The product thesis is:

```text
The user owns creative authority.
Hermes owns translation and routing.
Codex owns bounded execution.
Loop owns durable state.
Verifier owns evidence.
Research and Knowledge Base own reusable context.
HumanGate protects decisions that belong to the user.
```

This is not a chat-only assistant and it is not an engineering console. It is a product boundary that keeps the user in the creator role while preserving professional operating rigor underneath.

---

## 2. Product Philosophy

Creator-first means the system is organized around the user's natural creative actions:

- state an idea,
- confirm or adjust direction,
- inspect a result,
- judge satisfaction,
- request correction,
- stop or continue.

The user should not need to operate prompt engineering, Codex work orders, `.loop` state, verifier implementation, research-pack promotion, git mechanics, or Knowledge Base schemas. Those mechanisms still exist, but they are assigned to internal roles.

The philosophy is therefore not "make the system less rigorous." It is:

```text
Make the creator surface simpler.
Make the internal operating system stricter.
```

Every theory claim must drive productization. If a principle does not affect a future interface, Demand Contract, work order, verifier gate, feedback route, stop state, or learnback rule, it risks becoming document drift.

---

## 3. Product Boundary Theory

The product boundary separates user-owned decisions from system-owned mechanics.

| Boundary question | Creator-facing answer | Internal answer |
| --- | --- | --- |
| What is wanted? | The user describes the idea and desired value. | Hermes preserves the ask and infers the executable objective. |
| Is this the right direction? | The user confirms, corrects, or rejects. | Hermes compiles scope, non-goals, and acceptance criteria. |
| How is work performed? | The user sees status and preview. | Codex executes a bounded work order through Loop state. |
| Is it complete? | The user judges satisfaction. | Verifier checks evidence and stop-state fit. |
| What is learned? | The user sees concise reuse or risk notes. | Research and Knowledge Base separate raw, candidate, stable, and workflow material. |

The boundary fails when it exposes too much machinery and turns the user into an AI workflow operator. It also fails when it hides so much evidence that the system becomes vague, self-certifying chat. The correct boundary hides routine mechanics but exposes status, artifact preview, evidence summary, risk, and meaningful HumanGate decisions.

---

## 4. Role Model

### User

The user owns idea, direction, value judgment, risk boundary, satisfaction, and major correction. The user should make product decisions, not routine implementation decisions.

### Hermes

Hermes is the product-facing orchestrator. It receives rough ideas, interrogates demand, identifies whether Research or Codex is needed, compiles Demand Contracts, produces bounded work orders, summarizes results, routes feedback, and prepares learnback candidates.

### Codex

Codex is the bounded executor. It reads the work order, modifies only allowed files, avoids forbidden paths, runs required checks, repairs in-scope failures, and reports evidence. Codex is not the product owner and must not expand scope, add dependencies, create tools, or commit unless explicitly authorized.

### Loop

Loop preserves durable state: target, path, acceptance, current status, log, stop gate, handoff, and work order context. Loop makes long work resumable and auditable without relying only on chat memory.

### Verifier

Verifier checks evidence independently from Codex self-report. It inspects required artifacts, command output, file size, required terms, diff scope, forbidden paths, semantic fit, and stop-state classification.

### Research

Research handles external evidence. It separates raw sources, clean inventories, reading cards, insights, Knowledge Base candidates, and workflow patch candidates. It prevents temporary search from becoming unearned durable knowledge.

### Knowledge Base

Knowledge Base stores stable conclusions with source trail, confidence, applicability boundaries, and limitations. It is durable memory, not a dumping ground.

### Git and GitHub

Git and GitHub are internal safety and collaboration mechanisms. The creator should receive scoped change summaries and risk notes, not be forced to inspect diffs before expressing satisfaction.

---

## 5. Idea, Direction, Satisfaction, Correction

The creator-facing vocabulary maps directly to internal behavior.

| Creator action | Hermes | Codex | Loop | Verifier | Research / Knowledge Base |
| --- | --- | --- | --- | --- | --- |
| Idea | Preserve original ask; infer objective. | None unless task is already bounded. | Record only if work starts. | Check demand is not prematurely executed. | Identify whether evidence is needed. |
| Direction | Confirm scope, non-goals, output, risk. | Receive bounded work order if execution is authorized. | Preserve work state and stop conditions. | Check contract completeness. | Provide curated context if relevant. |
| Satisfaction | Classify satisfied, unsatisfied, direction wrong, detail wrong, continue, or stop. | Repair only if feedback is bounded. | Update stop state and handoff. | Confirm evidence still supports result. | Capture reusable feedback. |
| Correction | Route to repair, revised contract, HumanGate, continuation, stop, or learnback. | Execute correction inside explicit limits. | Preserve new state. | Recheck corrected output. | Promote only stable lessons. |

This mapping is the central product mechanism. It lets the user speak naturally while preserving executable structure.

---

## 6. HumanGate

HumanGate protects user authority. It is required when the next step depends on direction, value, satisfaction, risk, scope expansion, hard boundary changes, irreversible action, dependencies, integrations, commits, or accepting known gaps.

HumanGate is not a way to push routine work back onto the user. The system should not ask the user to choose implementation minutiae when the task is already authorized, bounded, and verifiable.

Good HumanGate prompts are short, choice-oriented, and about user-owned judgment:

```text
This can continue in the original direction, or it can shift toward a simpler MVP. Which direction should govern the next round?
```

HumanGate productization behavior:

- future interfaces should display HumanGate as a decision state, not as an error;
- work orders should name HumanGate triggers;
- Verifier should flag HumanGate bypass when scope or risk changed without user approval;
- Loop should preserve the decision and stop state.

---

## 7. Evidence and Verification

False completion is one of the main risks in AI workflow systems. Completion must be based on evidence, not agent confidence.

The Verifier should check:

- required files exist and are large enough to be meaningful,
- required concepts are covered,
- commands passed or failures are named,
- diffs touch only allowed files,
- forbidden paths are unchanged,
- content fits the Demand Contract,
- candidate research remains candidate unless promoted through gates,
- stop state is justified.

Codex can report what it did, but that report is evidence for review, not final acceptance. The creator may still be unsatisfied even when verification passes. That dissatisfaction is product evidence and must route to correction, not be dismissed as subjective noise.

---

## 8. Theory to Productization

Theory drives productization when it changes how the system behaves. The immediate productization path is:

| Theory claim | Product behavior |
| --- | --- |
| Creator stays creator | Interface centers idea, direction, preview, satisfaction, correction. |
| Encapsulation preserves rigor | Internal artifacts keep scope, evidence, state, and verifier gates. |
| Demand before execution | Hermes compiles demand before Codex long tasks. |
| Codex is bounded | Work orders define allowed files, forbidden files, outputs, and checks. |
| Verification is independent | Verifier checks evidence before Done. |
| State outlives chat | Loop records resumable state and handoff. |
| Knowledge has gates | Research separates raw, candidate, stable, and workflow layers. |
| HumanGate protects authority | User decisions are requested only for direction, risk, value, scope, and satisfaction. |
| Satisfaction is evidence | Feedback changes route, state, artifact, contract, or learnback. |

Candidate workflow patches from the audit research remain candidates. They may inform future work orders, but this theory round does not promote them into protocol changes.

---

## 9. Acceptance Theory

A creator-first workflow round is successful when:

- the user can understand the result without operating internals,
- Hermes can explain the demand and route,
- Codex stays inside bounds,
- Loop preserves resumable state when needed,
- Verifier can prove what passed and what remains risky,
- Research and Knowledge Base do not promote weak claims too early,
- HumanGate appears only for user-owned decisions,
- satisfaction feedback has a concrete destination,
- the theory maps to productization behavior and scenarios.

Stop state: Done means the artifact and evidence satisfy the work order. DoneWithRisk means usable output with named residual risk. HumanGate means a user-owned decision is needed. Repair means verification failed but can be fixed inside allowed scope. Blocked means progress requires missing input, files, permissions, tools, or external state.
