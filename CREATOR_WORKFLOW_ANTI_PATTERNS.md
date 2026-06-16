# Creator Workflow Anti-Patterns

Version: v1.0  
Status: failure-mode catalog for creator-first workflow theory  
Scope: prevention, verifier signal, and productization risk

---

## Purpose

This document lists failure modes that can break the creator-first AI workflow operating system. Each anti-pattern names the failure, why it matters, how to prevent it, and what Verifier signal should catch it.

The goal is not to add new protocol or implementation code in this round. The goal is to make future productization safer by defining what must not happen.

---

## Anti-Pattern Matrix

| Anti-pattern | Failure mode | Prevention | Verifier signal |
| --- | --- | --- | --- |
| User forced to operate internals | The creator must inspect work orders, `.loop`, raw research, git diffs, or verifier commands before giving ordinary feedback. | Hermes reports product status, artifact preview, evidence summary, risk, and feedback choices in plain language. | User-facing report requires only idea, direction, satisfaction, correction, or HumanGate decision. |
| Codex free-running | Codex executes from a vague idea or expands scope beyond authorization. | Require bounded work order with objective, allowed files, forbidden files, outputs, checks, and stop states. | Diff scope and output match work order; no unapproved tools, dependencies, protocol changes, or commits. |
| Verifier skipped | Codex self-report is treated as Done. | Verifier independently checks required artifacts, commands, terms, forbidden paths, semantic fit, and stop state. | Completion lacks independent evidence and must become Repair or DoneWithRisk. |
| Research promoted too early | Raw or candidate research becomes Knowledge Base or workflow rule. | Preserve raw, clean, reading, insights, kb, and workflow layers; require source trail, confidence, boundary, and promotion status. | Stable claims include source trail and limits; candidate patches remain candidate. |
| Theory document drift | Documents become internally consistent but do not change product behavior. | Map each theory claim to scenarios, acceptance signals, work order behavior, verifier gates, interface behavior, or learnback. | Theory section has productization consequence; scenario table covers behavior. |
| HumanGate overuse | The user is asked to make routine mechanical decisions. | Ask only about direction, value, risk, scope, satisfaction, authorization, or irreversible action. | HumanGate prompt is tied to user-owned judgment, not implementation minutiae. |
| HumanGate bypass | System changes scope, risk, dependencies, forbidden paths, or direction without user approval. | Work orders name HumanGate triggers; Hermes stops when user authority is required. | Scope/risk change without decision record blocks Done. |
| Context overload | Codex or Hermes receives too much raw context and loses the governing contract. | Provide curated read-first context, accepted knowledge, and explicit candidate boundaries. | Work order distinguishes required context from candidate evidence; output does not rely on unsupported claims. |
| Satisfaction ignored | User dissatisfaction is treated as subjective noise after technical checks pass. | Route feedback to repair, revised Demand Contract, HumanGate, continuation, stop, or learnback. | Every feedback item changes state, route, artifact, contract, or learnback candidate. |
| Implementation before demand | Code, tools, dependencies, or UI are created before the product demand is clear. | Demand before execution; theory and scenario rounds must not implement unless authorized. | Diff shows no unauthorized implementation files and objective remains theory/productization. |
| Evidence hidden by simplification | Product surface is simple but gives no proof, risk, or changed-file summary. | Expose concise evidence summaries while hiding routine mechanics. | Report includes changed files, checks, boundaries, stop state, and risk. |
| Overbuilt loop for trivial work | The full operating system is applied to tiny one-off answers. | Scale rigor with risk and durability; use lightweight handling for simple answers. | Work artifact size and process fit task risk; unnecessary state is not required. |
| Spec becomes waterfall | Demand Contract becomes rigid and blocks useful correction. | Treat satisfaction and correction as first-class routes back to contract or repair. | Direction correction can reopen demand; detail repair can proceed without full restart. |
| Knowledge Base becomes a dump | Durable memory stores unfiltered notes without confidence or applicability. | Promote only stable conclusions with source trail, boundaries, confidence, and limitations. | KB candidate or stable note states status, source trail, confidence, and scope. |
| Loop state depends on chat | Future execution cannot resume without conversation memory. | Preserve target, path, acceptance, state, log, stop gate, handoff, and work order where needed. | Handoff reconstructs objective, authorization, changes, checks, risks, and next action. |
| Verifier checks only syntax | Required files exist but semantic fit, satisfaction, and productization are not checked. | Include semantic alignment and scenario/product behavior checks. | Verifier names semantic fit or gap; DoneWithRisk if semantic review is incomplete. |
| Candidate patches silently accepted | Audit patch candidates become operating rules without authorization. | Label candidates clearly and require promotion round for behavior changes. | Patch remains candidate unless accepted in allowed artifact and verified. |
| Stop request ignored | System continues after the user asks to stop. | Treat stop as a creator-owned authority signal. | Loop records stop state and no further changes occur without new authorization. |
| Wrong correction type | Detail repair is applied when direction is wrong, or demand is reopened for a small typo. | Hermes classifies dissatisfaction: direction, detail, depth, evidence, scope, or stop. | Correction route matches feedback type. |
| Product preview absent | User receives internal summaries but no artifact-level result to judge. | Reports include artifact preview or clear pointer to changed product artifact. | User can evaluate satisfaction without reading raw internals. |

---

## High-Risk Anti-Patterns

### Codex free-running

This is the highest execution risk. It collapses the role boundary between Hermes and Codex. Codex should not decide product direction, expand scope, or invent allowed files. Future productization must keep Codex powerful inside a narrow contract.

### Verifier skipped

This creates false completion. A passing final message is not evidence. Done requires file, command, diff, boundary, and semantic evidence. DoneWithRisk is acceptable only when the remaining risk is named.

### Research promoted too early

Research is useful only when its confidence and source trail survive. Raw articles, candidate claims, and stable conclusions are different things. The system must preserve that distinction even when the user sees only a concise summary.

### Satisfaction ignored

The product is creator-first, so user satisfaction is evidence. Technical completion without creator fit may still require repair, revised direction, HumanGate, or stop.

---

## Productization Implications

Future interfaces should make these anti-patterns difficult:

- normal controls should be idea, direction, preview, satisfaction, correction, continue, and stop;
- internal evidence should be summarized but inspectable;
- HumanGate should appear only when a user-owned decision exists;
- verifier status should be separate from creator satisfaction;
- Knowledge Base and workflow patch status should show candidate versus accepted;
- stop states should be explicit.

This anti-pattern list should be used as a review checklist for future Demand Contracts, work orders, verifier gates, and MVP product slices.
