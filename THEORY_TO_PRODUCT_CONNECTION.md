# Theory to Product Connection

Version: v0.1  
Status: connection contract for the next productization loop  
Scope: theory artifacts, Demand Contract, .loop, Codex work order, Verifier gate, and feedback learnback

---

## 1. Why Theory Can Become Disconnected

The completed theory is useful, but it is not the product. It describes how Human, Hermes, Codex, Loop, Verifier, and Knowledge Base should cooperate. If that theory stays only as explanatory documentation, future work can still fall back into the old pattern:

```text
read a broad idea
-> produce another document
-> declare progress
-> leave no executable next round
```

That is the disconnect the user flagged. A theory document can feel complete because it names roles and principles, but a productization system only exists when those principles control the next execution round. The bridge must be explicit enough that Hermes can compile it into a Demand Contract, Codex can execute a bounded task, the Verifier can check evidence, and user feedback can return to the workflow instead of remaining in chat.

The failure mode is not that the theory is wrong. The failure mode is that no artifact forces the theory to become:

- a concrete productization objective,
- allowed and forbidden work boundaries,
- a next `.loop/WORK_ORDER.md`,
- Verifier checks,
- HumanGate triggers,
- and a feedback learnback route.

When those carriers are absent, the system can produce good-sounding concepts without changing the way future rounds execute.

---

## 2. Prevention Rule

Theory must not be treated as an end state. Every accepted theory artifact needs a downstream role in the productization loop.

The prevention rule is:

```text
No theory artifact is complete until it names how it affects the next Demand Contract,
the next .loop package, the next Codex work order, the Verifier gate, or feedback learnback.
```

That rule turns theory into operating control. It also limits Codex. Codex should not infer the product from a whole theory stack; Hermes must compile the relevant part into a bounded work order. The Verifier should then check evidence against the contract rather than trusting Codex self-report.

The required gates are:

- **Contract Gate**: Does the theory produce a Demand Contract with goal, scope, non-goals, constraints, outputs, acceptance criteria, verification, stop states, and HumanGate triggers?
- **Loop Gate**: Does the Demand Contract compile into `.loop` state files and a bounded `WORK_ORDER.md` for one round?
- **Codex Gate**: Does Codex receive only the read-first context, allowed paths, forbidden paths, required artifacts, and verification commands needed for that round?
- **Verifier Gate**: Does verification check files, content coverage, diffs, forbidden paths, and semantic fit against the work order?
- **Feedback Gate**: Does user or verifier feedback become Repair, HumanGate, DoneWithRisk, or learnback material instead of being lost?

---

## 3. Artifact Role Map

| Artifact | Role in the next productization loop | Gate it feeds |
| --- | --- | --- |
| `AI_WORKFLOW_THEORY_V0_1.md` | Source-of-truth role model for Human, Hermes, Codex, Loop, Verifier, and Knowledge Base. It defines why a broad idea must become contract, work order, execution evidence, correction, and learnback. | Contract Gate and Verifier Gate |
| `HERMES_CODEX_EXECUTION_PLAYBOOK.md` | Operational procedure for intake, demand interrogation, research promotion, theory drafting, work order creation, Codex execution, verification, loop build, correction, and learnback. | Loop Gate and Codex Gate |
| `RESEARCH_TO_PRODUCT_LOOP.md` | Evidence-to-product route. It prevents raw research or temporary reasoning from being handed directly to Codex as if it were stable knowledge. | Contract Gate and Feedback Gate |
| `AI_WORKFLOW_CONTROL_MODEL.md` | Control allocation. It states that the Human owns direction and boundaries, Hermes owns compilation and verification, Codex owns bounded execution, and HumanGate is required for value or scope decisions. | HumanGate and Stop Gate |
| `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md` | Knowledge durability model. It explains how external material becomes reusable context and workflow patches instead of one-time chat memory. | Feedback Gate and learnback |
| `INDEX.md` | Navigation surface. It makes the theory and productization documents discoverable for future Hermes and Codex rounds. | Handoff Gate |
| `.loop/HANDOFF.md` | Current state bridge. It tells the next executor that the completed theory must now compile into a bounded product-building loop. | Loop Gate |

The key connection is that none of these artifacts should be read as standalone essays. Each one supplies a decision rule or context slice for the next loop.

---

## 4. Connection Contract

The connection contract is the handoff from theory to product:

```text
theory
-> Demand Contract
-> .loop package
-> Codex bounded work order
-> Verifier evidence gate
-> feedback, correction, and learnback
```

### 4.1 Theory to Demand Contract

Hermes reads the theory artifacts and compiles a specific Demand Contract. The contract must not restate the entire theory. It must select the next product target and define:

- goal,
- target user or workflow,
- non-goals,
- allowed files,
- forbidden files,
- required outputs,
- acceptance criteria,
- verification commands,
- stop states,
- HumanGate triggers.

For this project, the immediate product target is not another CLI tool. The target is an executable productization loop specification that tells future Codex rounds how to turn the workflow theory into a usable system.

### 4.2 Demand Contract to `.loop`

Hermes converts the Demand Contract into loop control files:

- `.loop/TARGET.md`: one round objective,
- `.loop/PATH.md`: phase sequence,
- `.loop/ACCEPTANCE.md`: evidence requirements,
- `.loop/STOP_GATE.md`: Done, DoneWithRisk, Blocked, HumanGate, Repair rules,
- `.loop/STATE.md`: current status,
- `.loop/HANDOFF.md`: resume context,
- `.loop/WORK_ORDER.md`: the bounded Codex task.

The `.loop` package is what prevents productization from depending on the current conversation. It preserves the executable state for the next actor.

### 4.3 `.loop` to Codex

Codex receives one bounded `WORK_ORDER.md`. Codex should not decide which theory matters, create new tools, add dependencies, or broaden the product. Codex executes the requested round inside allowed paths and returns evidence.

The work order must include:

- read-first files,
- required artifacts,
- allowed files,
- forbidden files and directories,
- quality requirements,
- verification commands,
- forbidden-path check,
- completion report format.

### 4.4 Codex to Verifier

The Verifier checks evidence, not confidence. It should inspect:

- whether required artifacts exist,
- whether they contain the required concepts,
- whether `INDEX.md` points to them,
- whether forbidden paths changed,
- whether the diff is scoped,
- whether stop states and HumanGate triggers are present,
- whether the output actually connects theory to productization.

Codex can report completion, but Verifier decides whether the round is Done, DoneWithRisk, Repair, Blocked, or HumanGate.

### 4.5 Verifier to Feedback

Feedback enters the system through state, not only conversation. Feedback can produce:

- **Repair** when the current round failed but remains fixable inside scope.
- **HumanGate** when the next move requires value, scope, risk, or direction judgment.
- **DoneWithRisk** when the artifact is usable but a check is incomplete or a risk remains.
- **Learnback** when a stable lesson should update future contracts, workflow patches, or verifier rules.

Hermes should ask the user only when the feedback requires a human decision. Hermes should continue automatically when the next action is already authorized by the contract, the work remains in allowed files, verification is available, and no new value judgment is needed.

---

## 5. Next Productization Round Direction

The next Codex long-task round should use `PRODUCTIZATION_LOOP_V0_1.md` as the controlling loop spec and create the first bounded product artifact derived from the theory. It should not create CLI tools. It should not modify forbidden directories unless a later HumanGate explicitly authorizes that product implementation phase.

Exact next work order direction:

```text
Read AI_WORKFLOW_THEORY_V0_1.md, HERMES_CODEX_EXECUTION_PLAYBOOK.md,
RESEARCH_TO_PRODUCT_LOOP.md, THEORY_TO_PRODUCT_CONNECTION.md, and
PRODUCTIZATION_LOOP_V0_1.md. Compile a bounded Demand Contract and .loop
WORK_ORDER for the first productization implementation round. The output must
name the product slice, allowed files, forbidden files, acceptance criteria,
Verifier checks, HumanGate triggers, and stop states. Do not implement the
product yet. Do not create CLI tools. Do not add dependencies. Do not commit.
```

That direction keeps the theory connected to executable work while still preserving control. The next round is a compilation round, not a blind implementation round.

---

## 6. Operating Summary

The theory is the map. The Demand Contract is the selected route. The `.loop` package is the trip state. Codex is the bounded executor. The Verifier is the evidence gate. Feedback is the correction and learnback input.

The connection layer exists to make that chain explicit. Without it, the theory can look complete while the product remains undefined. With it, every future round has a clear question: which theory rule changes the next contract, work order, verifier check, or feedback path?
