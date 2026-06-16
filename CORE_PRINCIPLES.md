# Core Principles

Version: v0.1  
Status: governing principles for creator-first productization  
Scope: Human, Hermes, Codex, Loop, Verifier, Research, Knowledge Base, HumanGate, and future interface design

---

## Purpose

These principles define the non-negotiable operating layer for the creator-first AI workflow operating system. They are not slogans. Each principle must govern future design, work orders, verifier checks, product interfaces, and learnback decisions.

The user is the creator, direction owner, satisfaction judge, and boundary authority. The user is not expected to become a professional AI programming operator. Internally, Hermes, Codex, Loop, Verifier, Research, Knowledge Base, Git, and GitHub can remain rigorous. Externally, the product must let the user work through idea, direction, preview, satisfaction, and correction.

---

## P1 - Creator Stays Creator

**Principle statement:** The user must remain in the creator role: idea, direction, satisfaction, boundary, and correction.

**Why it exists:** The product fails if it makes the user operate prompt engineering, loop files, verifier commands, research packs, git, or Codex mechanics.

**What it forbids:** Forcing the user to micromanage internal execution, choose routine implementation steps, inspect raw verifier output before giving satisfaction feedback, or operate `.loop` files directly.

**What it requires:** User-facing flows must ask for meaningful creative decisions and translate those decisions into internal contracts, work orders, checks, and repairs.

**Related internal subsystem:** Hermes as product-facing orchestrator; HumanGate as authority boundary.

**Verifier signal:** Reports and interfaces can be understood through idea, direction, preview, satisfaction, and correction without exposing internal machinery as required user work.

## P2 - Encapsulation Preserves Rigor

**Principle statement:** Encapsulation hides complexity from the creator; it does not remove evidence, contracts, state, or verification.

**Why it exists:** A simple product surface is only trustworthy if the hidden workflow remains auditable and bounded.

**What it forbids:** Replacing Demand Contracts, work orders, stop states, forbidden path checks, research provenance, or verifier evidence with vague chat confidence.

**What it requires:** Internal artifacts must continue to preserve scope, allowed files, forbidden files, acceptance criteria, command evidence, state, and stop decisions.

**Related internal subsystem:** Loop, Verifier, Demand Contract, and Git/GitHub safety boundaries.

**Verifier signal:** A simple user report has backing evidence that can be inspected: files changed, checks run, scope respected, stop state named.

## P3 - Demand Before Execution

**Principle statement:** Ambiguous ideas must become executable demand before Codex performs bounded work.

**Why it exists:** Codex execution without clarified demand turns the system back into open-ended prompting and creates scope drift.

**What it forbids:** Starting implementation from a vague request when direction, output, constraints, or acceptance criteria are materially unclear.

**What it requires:** Hermes must preserve the original idea, infer the likely real objective, ask only necessary questions, and compile a Demand Contract or work order when execution needs structure.

**Related internal subsystem:** Hermes demand interrogation and Demand Contract compilation.

**Verifier signal:** A Codex round has a clear objective, read-first context, allowed scope, forbidden scope, required output, verification plan, and stop conditions.

## P4 - Bounded Executor, Not Product Owner

**Principle statement:** Codex executes bounded work; it must not own product direction, scope expansion, or HumanGate decisions.

**Why it exists:** The system needs a reliable maker role that can act deeply without silently changing the product goal.

**What it forbids:** Codex redefining the objective, expanding allowed files, creating CLI tools, adding dependencies, committing, modifying forbidden paths, or accepting risk without authorization.

**What it requires:** Work orders must provide enough context for Codex to complete the task inside explicit limits and report evidence, risks, and changed files.

**Related internal subsystem:** Codex long-task execution and Loop work order.

**Verifier signal:** `git diff --name-only`, file inspection, and command evidence show Codex stayed inside the authorized surface.

## P5 - Verification Is Independent Evidence

**Principle statement:** Completion is decided by evidence, not by Codex self-report.

**Why it exists:** Self-certification creates false Done states and hides scope, quality, or forbidden-path failures.

**What it forbids:** Treating a completion message as final verification, accepting unchecked artifacts, or skipping semantic fit review.

**What it requires:** Verifier must inspect required files, terms, sizes, diffs, forbidden paths, commands, acceptance criteria, and semantic alignment with the Demand Contract.

**Related internal subsystem:** Verifier and Hermes review.

**Verifier signal:** Each round ends in Done, DoneWithRisk, Blocked, HumanGate, or Repair based on checkable evidence.

## P6 - State Must Outlive Chat

**Principle statement:** Durable workflow state must live in explicit artifacts, not only in conversation memory.

**Why it exists:** Long tasks need resumability, auditability, and handoff across rounds.

**What it forbids:** Relying on chat history as the only record of target, path, acceptance, stop gate, handoff, or work order.

**What it requires:** Loop state must preserve authorization, objective, path, acceptance evidence, status, stop state, handoff, and work order content when a task spans rounds.

**Related internal subsystem:** Loop files including `STATE`, `LOOP_LOG`, `HANDOFF`, and `WORK_ORDER`.

**Verifier signal:** A later executor can reconstruct what was authorized, what happened, what passed, what failed, and what should happen next.

## P7 - Knowledge Promotion Has Gates

**Principle statement:** Raw research, candidate claims, stable conclusions, and workflow patches must remain separate.

**Why it exists:** Durable memory is useful only when it preserves provenance, confidence, applicability boundaries, and promotion status.

**What it forbids:** Promoting raw search results directly into Knowledge Base rules, treating candidate sources as accepted behavior, or losing source trails.

**What it requires:** Research must pass through raw, clean, reading, insights, Knowledge Base, and workflow layers when it is intended for reuse.

**Related internal subsystem:** Research pipeline and Knowledge Base.

**Verifier signal:** Stable conclusions include source trail, boundary, confidence, and no unsupported behavior-changing rule is promoted without synthesis.

## P8 - HumanGate Protects Authority

**Principle statement:** HumanGate must ask the user only for decisions that belong to the user.

**Why it exists:** The user must retain control over value, direction, risk, scope, and irreversible action without being burdened by routine mechanics.

**What it forbids:** Asking the user to decide implementation minutiae that are already authorized, or bypassing the user on scope expansion, risk acceptance, forbidden paths, dependencies, tools, integrations, or commits.

**What it requires:** HumanGate prompts must be short, choice-oriented, and tied to direction, value, satisfaction, risk, cost, scope, boundary, or authorization.

**Related internal subsystem:** Hermes routing and Loop stop states.

**Verifier signal:** HumanGate appears when a user-owned decision is required, and routine repairs continue without unnecessary interruption.

## P9 - Satisfaction Is Product Evidence

**Principle statement:** User satisfaction feedback is a first-class product signal and must route to a concrete internal destination.

**Why it exists:** Technical correctness is insufficient when the product is meant to serve the creator's intent.

**What it forbids:** Treating feedback as casual chat, ignoring dissatisfaction, patching details when the direction is wrong, or continuing after a stop request.

**What it requires:** Hermes must route satisfaction, dissatisfaction, wrong direction, wrong detail, continue, and stop feedback into Done, Repair, revised Demand Contract, HumanGate, continuation, learnback, or stop state.

**Related internal subsystem:** Hermes feedback routing, Loop, Verifier, and Knowledge Base learnback.

**Verifier signal:** Every feedback item has a destination and changes either the artifact, the contract, the stop state, or a learnback candidate.

## P10 - Theory Must Drive Productization

**Principle statement:** Theory is accepted only when it governs future design, execution, verification, and product behavior.

**Why it exists:** The project risk is document drift: internally consistent documents that do not change how the workflow operates.

**What it forbids:** Adding abstract theory with no connection to Demand Contracts, work orders, verifier gates, feedback routing, product interfaces, or workflow patches.

**What it requires:** Each principle or theory claim must map to productization scenarios, acceptance signals, future UI behavior, or verifier checks.

**Related internal subsystem:** Productization loop, workflow patch candidates, Verifier, and future interface layer.

**Verifier signal:** A future work order can cite the principle and translate it into allowed behavior, required output, acceptance criteria, or stop-state handling.

---

## Operating Summary

The core system contract is:

```text
creator-facing surface:
idea -> direction -> preview -> satisfaction -> correction

internal operating system:
Hermes demand -> Research evidence -> Demand Contract -> Loop state
-> Codex bounded execution -> Verifier evidence -> feedback route
-> Knowledge Base / workflow learnback
```

The principles are successful when they make the product simpler for the creator and stricter for the internal system at the same time.
