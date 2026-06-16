# Core Principles Theory

Version: v0.1  
Status: professional theory layer for the creator-first AI workflow operating system  
Scope: product boundary, role theory, internal mapping, verification, and productization

---

## 1. Thesis

This project is building a creator-first AI workflow operating system. Its purpose is not to teach a user to become a professional AI programming operator. Its purpose is to let a creator provide ideas, adjust direction, judge satisfaction, and request correction while the system internally performs the disciplined work of demand interrogation, research, contract compilation, bounded execution, verification, state preservation, and learnback.

The core theory is:

```text
The user owns creative intent and judgment.
The system owns operational rigor.
The product boundary translates between them.
```

This means the external workflow must feel simple:

```text
idea -> direction check -> system execution -> artifact preview -> satisfaction feedback -> correction
```

The internal workflow must remain strict:

```text
Hermes intake -> demand interrogation -> Research if needed
-> Demand Contract -> Loop state and WORK_ORDER
-> Codex bounded execution -> Verifier evidence gate
-> HumanGate / Repair / Done / DoneWithRisk / Blocked
-> Knowledge Base or workflow learnback
```

These two workflows are not alternatives. The creator-facing workflow is the product surface. The internal workflow is the operating system underneath it.

---

## 2. Creator-First Does Not Mean Informal

Creator-first means the product is organized around the user's real role:

- idea owner,
- direction owner,
- value judge,
- satisfaction judge,
- boundary authority,
- correction requester.

It does not mean the internal system becomes casual. The internal system must become more rigorous because the user is no longer expected to manually supervise every detail. If the product hides research layers, Codex work orders, `.loop` state, verifier checks, and git boundaries, those controls must become more reliable, not less.

The non-negotiable design rule is:

```text
Simplify the user's surface. Preserve the system's evidence.
```

This is why the principles combine creator simplicity with internal requirements. A future UI may show a concise product preview and a satisfaction control, but behind that control Hermes must know whether feedback means Repair, HumanGate, revised Demand Contract, continuation, stop, or learnback.

---

## 3. Product Boundary Theory

Encapsulation is often misunderstood as simplification. In this system, encapsulation is product boundary design.

Simplification removes complexity. Encapsulation relocates complexity behind a boundary where it can be operated by the right subsystem. The creator does not need to read raw research folders, but Research still needs provenance. The creator does not need to inspect every `git diff`, but the Verifier still must check diff scope and forbidden paths. The creator does not need to write work orders, but Hermes still must compile bounded instructions for Codex.

The product boundary has three responsibilities:

1. Preserve user agency at meaningful decision points.
2. Hide internal machinery that would turn the user into an operator.
3. Expose enough status, evidence, risk, and preview for trust and satisfaction judgment.

The boundary fails in two opposite ways:

- It exposes too much machinery, forcing the user to operate Hermes, Codex, Loop, Verifier, Research, Knowledge Base, and git manually.
- It hides too much evidence, producing a vague chat experience where the system cannot prove what it changed, why it is Done, or whether it respected boundaries.

The correct boundary is a creator-facing control surface backed by auditable internal artifacts.

---

## 4. Role Mapping

### Human

The Human is not a prompt operator. The Human is the authority for direction, boundaries, value, risk, satisfaction, and correction. HumanGate exists to protect this authority.

### Hermes

Hermes is the cognition and orchestration layer. It receives rough ideas, identifies the likely real objective, performs demand interrogation, decides whether Research is needed, compiles Demand Contracts, writes Codex work orders, routes feedback, and manages learnback candidates.

Hermes is the main translator between creator language and internal operating structure.

### Codex

Codex is the bounded executor. It reads the work order, modifies only allowed files, avoids forbidden paths, runs required checks, repairs bounded failures, and reports evidence. Codex does not own the product direction or final verification.

### Loop

Loop is durable state. It externalizes target, path, acceptance, state, log, stop gate, handoff, and work order content so the workflow can resume without depending on chat memory.

### Verifier

Verifier is independent evidence review. It checks required files, terms, command output, diffs, forbidden paths, semantic fit, and stop-state classification. Codex self-report is evidence to inspect, not acceptance.

### Research

Research handles external evidence. It separates raw material from clean inventories, reading cards, insight synthesis, Knowledge Base candidates, and workflow patches. It prevents temporary search from becoming unearned durable knowledge.

### Knowledge Base

Knowledge Base stores stable conclusions with source trail, confidence, applicability boundaries, and reusable lessons. It is the durable memory layer, not a raw dump.

---

## 5. Idea, Direction, Satisfaction, Correction

The creator-facing loop uses four primary user actions.

**Idea:** The user states what they want in natural language. Hermes preserves the original words and infers the likely real objective without erasing constraints.

**Direction:** The user confirms or adjusts what the system is about to pursue. Hermes turns this into a Demand Contract, research question, work order, or HumanGate decision.

**Satisfaction:** The user judges whether the artifact is useful, fitting, and worth accepting. Verifier evidence can show technical completion, but satisfaction confirms product value.

**Correction:** The user asks for repair, deeper work, direction change, or stop. Hermes routes the correction to the right internal destination.

The internal mapping is:

| User action | Hermes internal response | Downstream subsystem |
| --- | --- | --- |
| Idea | Intake, objective guess, risk scan | Research or Demand Contract |
| Direction | Scope and acceptance clarification | Loop and Codex work order |
| Satisfaction | Acceptance or dissatisfaction classification | Verifier and feedback routing |
| Correction | Repair, HumanGate, revised contract, stop, or learnback | Codex, Loop, Knowledge Base |

This mapping is the core product mechanism. It lets the user speak like a creator while the system acts like an operating workflow.

---

## 6. Stop-State Theory

Every round must end in a named state because unnamed continuation creates drift.

- **Done:** Required evidence passed and no material risk remains.
- **DoneWithRisk:** The artifact is usable, but the report names a residual risk.
- **Blocked:** A required file, permission, tool, input, or external condition prevents progress.
- **HumanGate:** The user must decide direction, risk, value, scope, satisfaction, or authorization.
- **Repair:** Verification failed, but the fix is bounded and authorized.

These states are not only internal labels. They are product behavior. A future interface should not display a vague "completed" state when the correct condition is DoneWithRisk, HumanGate, or Repair.

---

## 7. Why Productization Must Follow Theory

Theory becomes useful only when it changes future behavior. A principle that does not affect a work order, verifier gate, interface state, feedback route, or Knowledge Base promotion rule is likely document drift.

The core principles therefore require productization links:

- Creator Stays Creator maps to future UI and report design.
- Encapsulation Preserves Rigor maps to hidden evidence and audit trails.
- Demand Before Execution maps to Hermes interrogation and contracts.
- Bounded Executor maps to Codex work orders.
- Verification Is Independent Evidence maps to verifier gates.
- State Must Outlive Chat maps to Loop.
- Knowledge Promotion Has Gates maps to Research and Knowledge Base.
- HumanGate Protects Authority maps to decision prompts.
- Satisfaction Is Product Evidence maps to feedback routing.
- Theory Must Drive Productization maps to future work orders and patch promotion.

The next productization layer should use these principles as acceptance criteria. For example, a future product preview is not accepted merely because it renders. It must let the creator judge satisfaction while preserving verifier evidence and a correction route.

---

## 8. Practical Consequence

The system must be designed as a two-sided operating model:

```text
Creator side:
simple, judgment-oriented, satisfaction-driven, correction-friendly

System side:
contracted, bounded, stateful, verified, evidence-backed, learnable
```

The professional theory is that creator-first AI workflow design is not achieved by lowering rigor. It is achieved by assigning rigor to the correct internal roles and exposing only the decisions that belong to the creator.

This theory should govern all future productization work. If a proposed feature makes the user operate internal machinery, it violates the creator-first boundary. If a proposed feature hides evidence or lets Codex self-certify, it violates internal rigor. If a proposed document cannot route to product behavior, verifier checks, or workflow patches, it risks becoming document drift.
