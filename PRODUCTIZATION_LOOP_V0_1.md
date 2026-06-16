# Productization Loop v0.1

Version: v0.1  
Status: executable loop definition for turning the workflow theory into a usable product/system  
Scope: Demand Contract, .loop package, Codex bounded execution, Verifier gates, HumanGate, feedback, and learnback

---

## 1. Purpose

This loop defines the next executable path after the theory round. The theory is now input. The productization loop turns it into a controlled system by repeatedly compiling a bounded objective, executing one Codex round, checking evidence, and routing feedback.

This document intentionally does not create CLI tools. It defines the loop that should govern future product work. Implementation comes later, after Hermes compiles a specific Demand Contract and `.loop/WORK_ORDER.md`.

Core flow:

```text
accepted theory
-> Demand Contract
-> .loop package
-> Codex bounded round
-> Verifier gate
-> feedback route
-> next productization round or stop state
```

---

## 2. Productization Target

The product is not "more theory." The product is a usable AI workflow operating system pattern where:

- the Human gives direction, boundaries, and value judgment,
- Hermes compiles intent into contracts and loop state,
- Codex executes bounded work orders,
- the Verifier checks evidence,
- `.loop` preserves state across rounds,
- feedback becomes Repair, HumanGate, DoneWithRisk, or learnback.

The first productization objective is to create a bounded implementation round plan from the theory, not to implement every subsystem at once.

---

## 3. Phases

| Phase | Owner | Deliverable | Verifier gate |
| --- | --- | --- | --- |
| 0. Intake Confirmation | Hermes | Short statement of product slice, non-goals, and known constraints | Confirms the target is productization, not another abstract theory pass |
| 1. Demand Contract Compilation | Hermes | Demand Contract for one product slice | Goal, scope, outputs, constraints, acceptance criteria, verification, stop states, and HumanGate triggers are present |
| 2. Loop Package Compilation | Hermes | `.loop` plan and `WORK_ORDER.md` content for one round | Allowed files, forbidden files, read-first context, required artifacts, checks, and report format are explicit |
| 3. Codex Execution | Codex | Changed files or artifacts requested by the work order | Codex stayed in scope, did not create CLI tools unless authorized, did not modify forbidden paths, and returned command evidence |
| 4. Verifier Review | Verifier | Done, DoneWithRisk, Blocked, HumanGate, or Repair decision | Evidence matches acceptance criteria and semantic contract |
| 5. Feedback Routing | Hermes and Verifier | Correction work order, HumanGate question, or learnback candidate | Feedback has a destination and does not remain only in chat |
| 6. Learnback | Hermes | Knowledge Base or workflow patch candidate if the lesson is reusable | The lesson is stable, scoped, and behavior-changing |

---

## 4. Allowed Owners

### Human

The Human owns:

- product direction,
- value judgment,
- hard boundaries,
- priority,
- acceptance of risk,
- HumanGate decisions.

The Human should be asked when a decision changes value, direction, risk, cost, scope, irreversible action, or forbidden paths.

### Hermes

Hermes owns:

- demand interrogation,
- Demand Contract compilation,
- loop package compilation,
- work order drafting,
- verification review,
- feedback routing,
- learnback selection.

Hermes should continue automatically when the next action is already authorized, bounded, verifiable, and inside allowed files.

### Codex

Codex owns:

- reading the work order,
- modifying only allowed files,
- producing required artifacts,
- running required checks,
- repairing failures inside the same scope,
- reporting changed files, commands, results, and risks.

Codex does not own product direction, HumanGate decisions, scope expansion, or final verification.

### Verifier

The Verifier owns:

- evidence checks,
- forbidden path checks,
- semantic checks against the Demand Contract,
- stop-state decision support,
- distinction between self-report and verified completion.

### Knowledge Base

The Knowledge Base owns durable memory after a lesson is stable enough to reuse. It should not receive every temporary observation.

---

## 5. Verifier Gates

Every productization round must pass these gates or stop in a named state:

### Gate A: Contract Completeness

The Demand Contract must include:

- goal,
- scope,
- non-goals,
- required artifacts,
- allowed files,
- forbidden files,
- acceptance criteria,
- verification commands,
- HumanGate triggers,
- stop states.

### Gate B: Loop Executability

The `.loop` package or proposed `.loop` content must identify:

- target,
- path,
- acceptance evidence,
- state,
- stop gate,
- handoff,
- next `WORK_ORDER.md`.

### Gate C: Codex Boundedness

The Codex work order must be executable without requiring Codex to infer the entire product strategy. It must explicitly state whether CLI tools, dependencies, commits, network calls, and forbidden paths are allowed.

For the immediate next round:

```text
CLI tools: not allowed
dependencies: not allowed
commits: not allowed
forbidden paths: not allowed
```

### Gate D: Evidence Check

The Verifier checks:

- required files exist,
- required sections or terms are present,
- file sizes or content depth are sufficient,
- verification commands passed,
- `git diff --name-only` only lists allowed paths,
- forbidden directories are unchanged,
- the result directly advances productization.

### Gate E: Feedback Destination

Any feedback must be routed to:

- Repair,
- HumanGate,
- DoneWithRisk,
- Blocked,
- next work order,
- workflow patch candidate,
- Knowledge Base candidate.

Unrouted feedback means the round is not complete.

---

## 6. HumanGate Triggers

Hermes must ask the user instead of continuing automatically when:

- the product slice has multiple plausible directions with different value outcomes,
- the next step requires modifying a forbidden path,
- implementation would add a CLI tool, dependency, network integration, or commit not already authorized,
- verification cannot prove a required outcome,
- the work requires accepting known risk,
- user feedback contradicts the current Demand Contract,
- scope expands from documentation into implementation,
- a decision changes the Human/Hermes/Codex/Verifier responsibility model.

Hermes should not ask the user when:

- the next action is a direct repair inside allowed files,
- verification failure is mechanical and fixable within scope,
- the Demand Contract already authorizes the next productization step,
- the stop state is clear from evidence.

---

## 7. Stop States

Every round ends in exactly one state:

- **Done**: Required artifacts exist, checks passed, forbidden paths are unchanged, and no material unresolved risk remains.
- **DoneWithRisk**: The productization artifact is usable, but a named check, assumption, or downstream dependency remains unresolved.
- **Blocked**: A required file, tool, permission, input, or external condition prevents progress.
- **HumanGate**: A human decision is required before continuing.
- **Repair**: Verification failed, but the fix is bounded and authorized inside the current scope.

The stop state must be part of the completion report. "Completed" without a stop state is not enough.

---

## 8. Concrete Next Codex Long-Task Objective

The next Codex round should be a compilation round:

```text
Objective:
Compile the accepted theory and connection docs into a bounded first
productization implementation work order. The output should define the first
product slice, the Demand Contract, proposed .loop updates, allowed and
forbidden files, acceptance criteria, Verifier checks, HumanGate triggers, and
stop states. Do not implement the product yet. Do not create CLI tools. Do not
add dependencies. Do not commit.
```

Recommended required artifacts for that next round:

- `DEMAND_CONTRACT_PRODUCTIZATION_V0_1.md`
- `.loop/WORK_ORDER.md` update for the first implementation slice, if allowed by that future work order
- optional `.loop/HANDOFF.md` state note, if needed

Recommended read-first files:

- `AI_WORKFLOW_THEORY_V0_1.md`
- `HERMES_CODEX_EXECUTION_PLAYBOOK.md`
- `RESEARCH_TO_PRODUCT_LOOP.md`
- `THEORY_TO_PRODUCT_CONNECTION.md`
- `PRODUCTIZATION_LOOP_V0_1.md`
- `.loop/HANDOFF.md`

Recommended forbidden scope for that next round:

- no CLI tools,
- no dependencies,
- no commits,
- no changes to existing protocol, template, runner, verifier, workflow, knowledge base, trial, script, test, or docs directories unless the Human explicitly authorizes implementation.

---

## 9. Feedback and Learnback Rules

Feedback is product input. It must be classified before action:

- If feedback says the direction feels wrong, trigger HumanGate or revise the Demand Contract.
- If feedback says the connection is unclear, create a Repair work order for the connection artifact.
- If feedback reveals a missing verifier rule, create a workflow patch candidate.
- If feedback reveals a reusable principle, promote it toward Knowledge Base only after it is stable and scoped.
- If feedback asks for implementation, compile a new work order before Codex changes product files.

This rule keeps user feedback connected to the operating model. It prevents the system from collecting comments without changing future execution.

---

## 10. Minimum Completion Report for Future Rounds

Future productization rounds must report:

- files created or updated,
- product slice advanced,
- Demand Contract or work order used,
- verification commands and results,
- forbidden path check result,
- stop state,
- risks or remaining gaps,
- recommended next state: continue, Repair, HumanGate, Done, DoneWithRisk, or Blocked.

The report is evidence for Hermes and the Verifier, not the final source of truth.

---

## 11. Operating Rule

Productization begins when theory changes the next executable round. The immediate next move is therefore not to add another explanatory layer or another CLI. It is to compile the theory into a bounded product slice, route it through `.loop`, give Codex a narrow work order, verify evidence, and feed results back into the system.
