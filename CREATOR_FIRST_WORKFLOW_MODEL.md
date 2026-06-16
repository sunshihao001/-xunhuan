# Creator-First Workflow Model

Version: v0.1  
Status: creator-facing product model  
Scope: Human, Hermes, Codex, Loop, Verifier, Knowledge Base, and Research encapsulation

---

## 1. Purpose

This model defines how the AI workflow should feel to a non-professional AI programming user.

The user should not need to understand prompt engineering, Codex work orders, `.loop` files, verifier implementation, research pack internals, git, or the exact path from evidence to Knowledge Base. The user should be able to create ideas, adjust the broad direction, judge whether the result is satisfying, and request corrections.

The system must still keep its internal rigor. The difference is that the rigor should be hidden behind a clear product boundary. Hermes, Codex, Loop, Verifier, Knowledge Base, and Research continue to operate with contracts, evidence, stop states, and audit trails, but the user sees a simpler creative workflow.

This repository is still building that encapsulation. It is not yet a finished UI or polished product. The current artifacts define the operating model that future product work should implement.

---

## 2. User Role

The user is the creator, direction owner, and satisfaction judge.

The user owns:

- the original idea or desired outcome,
- the broad direction,
- value judgment,
- risk tolerance,
- hard boundaries,
- scope approval,
- satisfaction with the finished artifact,
- major correction requests.

The user should be asked questions such as:

- Is this the direction you meant?
- Is this useful enough to continue?
- Is this risk acceptable?
- Should the system make the product deeper, simpler, wider, or stop?
- Are you satisfied with this artifact?

The user should not be treated as an AI operator who must manually drive every subsystem. The user should not have to repeatedly tell Codex the next tiny step, decide which loop file to edit, inspect raw research folders, run verifier commands, or understand git diffs before expressing whether the result feels right.

---

## 3. What The User Should Not Need To Understand

The creator-facing product should hide the following details by default:

- prompt engineering patterns,
- Codex execution mechanics,
- `.loop/WORK_ORDER.md`, `.loop/STATE.md`, `.loop/HANDOFF.md`, and related loop files,
- verifier implementation details,
- research pack layers such as raw, clean, reading, insights, kb, and workflow,
- Demand Contract structure,
- Knowledge Base promotion rules,
- git branches, commits, diffs, and forbidden path checks,
- test command syntax,
- internal stop-state naming unless a decision is needed.

These details still matter internally. They are not removed. They are encapsulated so the user can focus on creation, direction, and satisfaction instead of operating the workflow machinery.

---

## 4. What The System Should Encapsulate

Hermes should encapsulate intake, demand interrogation, research routing, contract compilation, work order creation, verifier review, feedback routing, and learnback selection.

Codex should encapsulate bounded execution. It should read the work order, modify only allowed files, run checks, and report evidence without asking the user to micromanage implementation details.

Loop should encapsulate state. It should preserve target, path, acceptance criteria, current status, logs, stop gates, handoff, and work order content so the workflow can resume without depending on chat memory.

Verifier should encapsulate evidence checks. It should inspect files, commands, diffs, forbidden paths, required terms, and semantic fit. The user should receive a concise result, not a raw pile of command output.

Knowledge Base should encapsulate durable memory. It should preserve stable conclusions, applicability boundaries, source trails, workflow patches, and reusable lessons after evidence is strong enough.

Research should encapsulate external evidence handling. Raw sources, reading cards, synthesis, and promotion decisions should happen behind the product boundary unless the user asks to inspect them.

Git and file-safety rules should be encapsulated. The system should protect forbidden paths, avoid unauthorized commits, and report scoped changes in plain language.

---

## 5. Internal Workflow vs User-Facing Workflow

The internal engineering workflow is strict:

```text
idea
-> Hermes demand interrogation
-> research evidence if needed
-> Demand Contract
-> .loop state
-> Codex WORK_ORDER
-> bounded execution
-> Verifier evidence check
-> stop state
-> feedback routing
-> Knowledge Base or workflow learnback
```

This internal workflow is for control, auditability, and repeatability.

The user-facing workflow should be simple:

```text
idea
-> direction check
-> system execution
-> artifact preview
-> satisfaction feedback
-> correction
```

These are not competing workflows. The user-facing loop is the product surface. The internal engineering workflow is the machinery underneath it.

The user should experience the system as a creative partner that can ask a small number of meaningful questions, produce a preview, explain what changed, and accept feedback. Hermes should translate the user's feedback into the correct internal action: repair, HumanGate, more research, a new Codex work order, verifier review, or learnback.

---

## 6. Creator-Facing Loop

### Step 1: Idea

The user gives an idea in natural language. It can be rough, incomplete, or non-technical.

Hermes should preserve the user's words and infer the likely real objective without erasing the user's constraints.

### Step 2: Direction Check

Hermes reflects the intended direction in plain language. The check should be short and decision-oriented:

- what the system thinks the user wants,
- what will be produced first,
- what will not be done yet,
- which decision, if any, needs the user.

### Step 3: System Execution

Hermes compiles the internal plan. Codex executes bounded work. Loop preserves state. Verifier checks evidence. Research and Knowledge Base are used only when they are relevant.

The user should not need to operate these parts manually.

### Step 4: Artifact Preview

The system shows the created or changed artifact in a way the user can judge. The preview should emphasize the product result, not internal mechanics.

The report should include:

- concise product status,
- what changed,
- evidence summary,
- what needs feedback,
- any risk or decision that belongs to the user.

### Step 5: Satisfaction Feedback

The user gives simple feedback. The product should support feedback such as:

```text
满意
不满意
方向错
细节错
继续深化
停止
```

The user may also explain the reason in natural language.

### Step 6: Correction

Hermes routes feedback:

- `满意`: finish or move to the next authorized product slice.
- `不满意`: ask whether the problem is direction, quality, missing detail, or scope.
- `方向错`: return to direction and Demand Contract, not only edit details.
- `细节错`: create a bounded repair work order.
- `继续深化`: expand within allowed scope or trigger HumanGate if scope changes.
- `停止`: stop and preserve state.

---

## 7. HumanGate In The Creator Model

HumanGate should protect the user's authority without making the user operate the workflow.

Ask the user when the decision concerns:

- direction,
- value,
- satisfaction,
- risk acceptance,
- scope expansion,
- cost or time tradeoff,
- irreversible action,
- modifying forbidden paths,
- adding tools, dependencies, external integrations, or commits,
- accepting a result with known gaps.

Do not ask the user for routine mechanical choices when the work is already authorized, bounded, and verifiable.

---

## 8. Reporting Rule

The system should report back in product language:

```text
Status: what happened
Artifact: what was created or changed
Evidence: what was checked
Feedback needed: what the user should judge
Risk: what remains uncertain, if anything
```

The report should not force the user to read raw verifier implementation, research internals, loop files, or git details. Those should remain available as evidence for Hermes and Verifier, but the normal user-facing surface should be concise.

---

## 9. Operating Principle

The creator-first model is successful when the user can stay focused on:

```text
idea -> direction -> preview -> satisfaction -> correction
```

and the system reliably handles:

```text
prompt shaping -> research -> contract -> work order -> execution -> verification -> state -> learnback
```

The product should make the user more powerful without requiring the user to become a professional AI workflow engineer.
