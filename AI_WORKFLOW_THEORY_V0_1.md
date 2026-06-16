# AI Workflow Theory v0.1

Version: v0.1  
Status: first complete theory draft  
Scope: Human, Hermes, Codex, Loop, Verifier, and Knowledge Base operating model

---

## 1. Core Thesis

The goal of this system is not to make a human write longer prompts. The goal is to turn a rough human idea into a controlled AI operating workflow:

```text
Initial human idea
-> Hermes demand interrogation
-> external research captured as durable evidence
-> theory and Demand Contract
-> Codex long-task WORK_ORDER
-> loop-agent execution
-> Verifier evidence check
-> product correction
-> Knowledge Base and workflow learnback
```

The human should not manually push every implementation detail. The human owns direction, boundaries, priorities, value judgment, and HumanGate decisions. Hermes owns cognition, theory shaping, contract compilation, research promotion, and verification. Codex owns bounded long-task execution. The Loop owns state, sequencing, stop conditions, and handoff. The Verifier owns evidence-based checks. The Knowledge Base owns durable memory.

This is the difference between chat-based AI and workflow-based AI. Chat relies on the current conversation. Workflow-based AI externalizes intent, evidence, state, acceptance criteria, and stop gates into files that can be read, audited, resumed, and improved.

---

## 2. System Roles

### Human

The Human is the goal owner and boundary authority.

Responsibilities:

- Provide the initial idea, direction, and value target.
- Decide what is worth doing and what is not.
- Set hard boundaries, forbidden areas, and risk tolerance.
- Resolve HumanGate decisions when direction, cost, irreversible action, scope expansion, or value judgment is required.
- Accept or reject the final product based on real intent, not only agent self-report.

The Human should not be responsible for repeatedly telling Codex the next tiny step, manually preserving every research source, or inspecting every minor artifact without a verifier summary.

### Hermes

Hermes is the orchestration and cognition layer:

- Demand interrogation front end.
- Theory builder.
- External research curator.
- Demand Contract compiler.
- Loop brief compiler.
- Codex work order author.
- Verifier and evidence reviewer.
- Knowledge Base and workflow learnback manager.

Hermes should ask questions when the request is ambiguous, but the target is not endless questioning. The target is to converge the idea into artifacts Codex can execute and the Verifier can audit.

### Codex

Codex is a bounded executor. Codex receives a work order and completes the concrete detail work within explicit limits.

Codex may:

- Read the allowed context.
- Create or modify allowed files.
- Run required checks.
- Fix failures within the same allowed scope.
- Report changed files, verification commands, and risks.

Codex must not:

- Redefine the goal.
- Expand scope without authorization.
- Modify forbidden paths.
- Treat its own completion report as verification.
- Decide HumanGate outcomes.

### Loop

The Loop is the stateful control surface for multi-round work. It prevents long tasks from depending only on chat memory.

Core loop files include:

```text
.loop/TARGET.md
.loop/PATH.md
.loop/ACCEPTANCE.md
.loop/STATE.md
.loop/LOOP_LOG.md
.loop/STOP_GATE.md
.loop/HANDOFF.md
.loop/WORK_ORDER.md
```

The Loop converts high-level intent into bounded rounds. Each round has a specific objective, allowed files, forbidden files, acceptance criteria, verification commands, stop conditions, and a completion report format.

### Verifier

The Verifier checks evidence, not confidence. It distinguishes Codex self-report from actual completion.

Verifier evidence can include:

- File existence and size.
- Diff inspection.
- Test output.
- Lint or typecheck output.
- Search coverage.
- Link or citation checks.
- Forbidden path diff checks.
- Semantic checks against the work order.

The Verifier decides whether the state is Done, DoneWithRisk, Blocked, HumanGate, or Repair. Codex can recommend a state, but Verifier must check it.

### Knowledge Base

The Knowledge Base is durable memory. It stores stable conclusions, sourced research, reusable workflow patterns, accepted patches, failure modes, and decision records.

The Knowledge Base is not a dumping ground for raw search results. It is the final promoted layer after evidence has moved through raw, clean, reading, insights, kb, and workflow stages.

---

## 3. Why External Research Must Become Durable Evidence

External research cannot be used only as temporary context for one answer. Temporary search creates temporary cognition. A future Hermes or Codex run cannot reliably reuse it, audit it, or distinguish stable conclusions from weak claims.

The durable evidence model solves this:

```text
raw source
-> clean inventory
-> reading card
-> insights synthesis
-> kb stable conclusion
-> workflow patch
```

Each layer has a different job:

- raw: preserve original evidence, URL, source type, capture time, and unprocessed material.
- clean: deduplicate, classify, and rate source quality and relevance.
- reading: extract claims, evidence strength, limits, and applicability.
- insights: compare sources, identify consensus, disagreement, risks, and open questions.
- kb: store stable knowledge with source trail and applicability boundaries.
- workflow: convert stable knowledge into changed behavior, templates, checks, or work order rules.

This matters because Codex long tasks need curated context, not random raw evidence. Hermes should feed Codex the current theory, contract, accepted knowledge, and relevant insights. The Verifier should check whether execution followed the accepted knowledge and whether new findings deserve promotion.

---

## 4. Idea to Product Lifecycle

### Phase 1: Initial Idea in Hermes

The Human gives a rough idea. Hermes captures:

- Surface ask.
- Suspected real objective.
- Domain and constraints.
- Expected artifact or product.
- Risk of wrong execution.
- Whether external research is required.

The output is not yet a Codex task. It is an intake model and routing decision.

### Phase 2: Demand Interrogation and Research Question

Hermes turns the idea into a cognition question:

```text
What must be true for this idea to become a useful product?
What external practices or sources can improve the theory?
What must be preserved as evidence for future reuse?
```

If external research is needed, Hermes creates or uses a research evidence pack and routes sources through raw, clean, reading, insights, kb, and workflow.

### Phase 3: Theory and Demand Contract

Hermes integrates the human idea, existing repository docs, and promoted research into a theory. The theory then becomes a Demand Contract:

- Goal.
- Scope.
- Non-goals.
- Definitions.
- Inputs.
- Outputs.
- Constraints.
- Acceptance criteria.
- Verification plan.
- Stop conditions.
- HumanGate triggers.

This is where vague intent becomes executable.

### Phase 4: Codex Long-Task Work Order

Hermes compiles the contract into a bounded `WORK_ORDER.md`. A good work order contains:

- Objective.
- Read-first files.
- Required output artifacts.
- Allowed files.
- Forbidden files and directories.
- Content quality requirements.
- Required verification commands.
- Completion report format.

Codex executes the work order. Codex does not create a new theory of the task unless the work order asks it to complete theory content inside the allowed artifact set.

### Phase 5: Loop-Built Product

When the product requires multiple rounds, Hermes uses the Loop:

```text
WORK_ORDER per round
-> Codex execution
-> Verifier check
-> STATE / LOOP_LOG update
-> Continue / Repair / Done / DoneWithRisk / Blocked / HumanGate
```

The product grows by bounded rounds. Each round should leave evidence and state behind.

### Phase 6: Iterative Correction

After a product exists, Hermes and the Verifier compare it against:

- The original human direction.
- The Demand Contract.
- The accepted theory.
- User feedback.
- Test and usage evidence.
- Research-backed workflow rules.

Unsuitable parts become correction work orders. Strong new lessons become Knowledge Base updates or workflow patches.

---

## 5. Stop Conditions

Every round must end in one explicit state:

- Done: acceptance criteria passed and no known major risk remains.
- DoneWithRisk: the main goal is complete, but there are explicit residual risks or missing checks.
- Blocked: progress is stopped by missing files, tools, permissions, information, or external state.
- HumanGate: a human decision is required for value, direction, scope, cost, authorization, or irreversible action.
- Repair: verification failed, but the agent can fix it within the current scope.

These states prevent fake completion. They also prevent agents from continuing indefinitely when the correct action is to stop and return control.

---

## 6. Operating Principle

The system should be judged by whether it makes future execution easier to control:

```text
Can Hermes explain the target?
Can Codex execute without inventing scope?
Can the Verifier check evidence without trusting self-report?
Can the Human intervene only at meaningful gates?
Can future runs reuse the knowledge instead of rediscovering it?
```

If the answer is yes, the workflow is becoming an AI operating system rather than a collection of prompts.
