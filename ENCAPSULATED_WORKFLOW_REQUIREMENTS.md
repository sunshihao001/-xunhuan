# Encapsulated Workflow Requirements

Version: v0.1  
Status: product requirements for creator-first encapsulation  
Scope: Hermes, Codex, Loop, Verifier, Knowledge Base, Research, HumanGate, and feedback

---

## 1. Product Principle

The user is not expected to be a professional AI programming person. The workflow must encapsulate scattered AI capabilities so the user can create ideas, adjust broad direction, judge satisfaction, and request changes.

The system must not reduce internal rigor. It must keep Demand Contracts, Codex work orders, Loop state, Verifier gates, Research evidence, Knowledge Base promotion, forbidden path checks, and stop states. The product requirement is to hide that complexity behind a simple creator-facing workflow.

This repository is still building the encapsulation. It is not yet a finished UI or complete product surface.

---

## 2. Functional Requirements

### 2.1 Hermes

Hermes must act as the user's product-facing orchestrator.

Hermes must:

- accept rough ideas in natural language,
- identify the likely real objective,
- ask only necessary direction questions,
- compile ideas into Demand Contracts when execution needs structure,
- decide whether Research, Codex, Loop, Verifier, or Knowledge Base is needed,
- create bounded Codex work orders without exposing work order complexity to the user by default,
- summarize execution results in creator-facing language,
- route user feedback into Repair, HumanGate, continuation, stop, or learnback.

Hermes must not require the user to manually operate demand interrogation, research collection, Codex, `.loop`, verifier checks, or git.

### 2.2 Codex

Codex must remain a bounded executor.

Codex must:

- read the work order and required context,
- modify only allowed files,
- avoid forbidden paths,
- avoid creating CLI tools, dependencies, or commits unless explicitly authorized,
- run required checks,
- repair failures that are inside scope,
- report changed files, verification results, and risks.

Codex must not:

- decide product direction,
- decide HumanGate outcomes,
- expand scope on its own,
- treat its own report as final verification,
- ask the user to make implementation micro-decisions that Hermes or the work order already authorizes.

### 2.3 Loop

Loop must preserve state behind the creator-facing product.

Loop must:

- keep target, path, acceptance, state, log, stop gate, handoff, and work order information,
- make long tasks resumable,
- record enough audit trail to reconstruct authorization, action, evidence, and stop state,
- support Done, DoneWithRisk, Blocked, HumanGate, and Repair outcomes.

Loop details should not be the user's normal operating surface. The user should see product status and next decision, not raw `.loop` machinery.

### 2.4 Verifier

Verifier must check evidence independently from Codex self-report.

Verifier must:

- check required files exist,
- check content coverage against acceptance criteria,
- inspect diff scope,
- confirm forbidden paths are unchanged,
- run or inspect verification command output,
- evaluate semantic fit with the Demand Contract,
- classify the result as Done, DoneWithRisk, Blocked, HumanGate, or Repair.

Verifier output to the user must be concise:

- what passed,
- what remains risky,
- what needs the user's judgment,
- whether correction is required.

### 2.5 Knowledge Base

Knowledge Base must store durable memory only after evidence is stable enough.

Knowledge Base must:

- preserve stable conclusions,
- include source trail and applicability boundaries,
- avoid promoting raw claims directly into accepted workflow behavior,
- support future Hermes and Codex rounds with curated context,
- receive learnback when a correction creates reusable knowledge.

The user should not need to manage Knowledge Base promotion manually.

### 2.6 Research

Research must support product decisions without becoming user workload.

Research must:

- collect external material when needed,
- keep raw, clean, reading, insights, kb, and workflow layers separate,
- distinguish candidate evidence from stable conclusions,
- summarize relevant evidence for Hermes, Verifier, and the user,
- trigger HumanGate when research changes direction, risk, value, or scope.

The user should see the conclusion and confidence, not the entire research pack unless requested.

---

## 3. User-Facing Workflow Requirements

The product surface must support this loop:

```text
idea -> direction check -> system execution -> artifact preview -> satisfaction feedback -> correction
```

The user-facing loop must be simple enough that the user can operate it through broad feedback.

Required feedback options:

```text
满意
不满意
方向错
细节错
继续深化
停止
```

Feedback routing requirements:

- `满意` means the artifact can be accepted or moved to the next authorized stage.
- `不满意` means Hermes should ask what kind of dissatisfaction exists if it is not obvious.
- `方向错` means Hermes should revisit the objective, Demand Contract, and HumanGate, not only patch wording.
- `细节错` means Hermes should create a bounded repair task.
- `继续深化` means Hermes may continue if scope is already authorized; otherwise it must ask for HumanGate.
- `停止` means Loop must preserve state and stop execution.

---

## 4. HumanGate Rules For Non-Technical Users

HumanGate must be phrased as a meaningful product decision, not a technical burden.

Ask the user when:

- the system is unsure which direction the user wants,
- the next step changes the value target,
- the next step expands scope,
- the next step accepts known risk,
- the next step changes hard boundaries,
- the next step modifies forbidden paths,
- the next step adds a tool, dependency, integration, or commit,
- the artifact may be technically correct but not satisfying,
- research reveals conflicting directions,
- continuation would cost materially more time or complexity.

Do not ask the user when:

- the work is a mechanical repair inside allowed files,
- a verifier failure has an obvious fix inside scope,
- Codex needs to run an already authorized check,
- Hermes can summarize internal details without requiring judgment,
- Loop state needs routine updating.

HumanGate prompts should be short and choice-oriented. They should ask about direction, risk, value, scope, or satisfaction.

---

## 5. Reporting Requirements

The system must report back using concise product status.

Each completion report should include:

- artifact status,
- what changed,
- evidence summary,
- whether forbidden boundaries were respected,
- what needs user feedback,
- current stop state,
- risks or gaps.

The report should avoid exposing raw implementation machinery unless it is needed for trust or debugging. For example, the user should not have to read all verifier implementation details to decide whether the product is satisfying.

---

## 6. Non-Goals

This requirements document does not authorize:

- creating CLI tools,
- adding dependencies,
- implementing a UI,
- changing protocol, template, runner, verifier, workflow, knowledge base, trial, script, test, or docs directories,
- committing changes,
- replacing internal engineering workflow with a vague chat-only flow,
- removing Verifier rigor,
- letting Codex self-certify completion,
- treating raw research as accepted Knowledge Base,
- requiring the user to operate `.loop`, Codex, git, verifier commands, or research packs manually.

---

## 7. Acceptance Criteria

The creator-first encapsulation model is acceptable when:

- the user's role is clearly defined as creator, direction owner, and satisfaction judge,
- Hermes, Codex, Loop, Verifier, Knowledge Base, and Research each have clear encapsulation responsibilities,
- the user-facing loop is simpler than the internal engineering workflow,
- HumanGate protects direction, risk, value, scope, and satisfaction decisions,
- routine mechanical execution stays inside the system,
- feedback options are defined and routed,
- reports explain status, evidence, changes, and needed feedback in plain language,
- internal rigor is preserved through contracts, loop state, verifier evidence, and learnback,
- the model warns that the current repo is still building this encapsulation and is not yet a finished UI/product.

---

## 8. Stop States

Every encapsulated round must end in one state:

- **Done**: the artifact is complete, verified, and ready for user satisfaction judgment or next authorized stage.
- **DoneWithRisk**: the artifact is usable, but the report must name the remaining risk.
- **Blocked**: the system cannot continue without missing input, permission, file, tool, or external condition.
- **HumanGate**: the user must decide direction, risk, value, scope, satisfaction, or authorization.
- **Repair**: verification failed, but the fix is bounded and can proceed without a new user decision.

---

## 9. Requirement Summary

The product must let the user work like this:

```text
I have an idea.
Is this the right direction?
Show me the artifact.
I am satisfied, not satisfied, or want a correction.
```

The system must handle this underneath:

```text
Hermes intake and contract
Codex bounded execution
Loop state and handoff
Verifier evidence gate
Research evidence pipeline
Knowledge Base learnback
HumanGate when judgment is required
```

Encapsulation is successful when the user can stay in the role of creator while the system keeps the discipline of an auditable engineering workflow.
