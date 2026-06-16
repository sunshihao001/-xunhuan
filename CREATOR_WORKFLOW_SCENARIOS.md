# Creator Workflow Scenarios

Version: v1.0  
Status: scenario mapping for creator-first theory  
Scope: practical behavior from idea intake to failure recovery

---

## Scenario Matrix

Each scenario maps creator-facing experience to Hermes, Codex, Loop, Verifier, Knowledge Base, Research, HumanGate, and acceptance signal.

| # | Scenario | User sees | Hermes does | Codex does if involved | Loop preserves | Verifier checks | KB/Research receives | HumanGate trigger | Acceptance signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Rough idea intake | A natural place to say an incomplete idea. | Preserves original wording and infers objective. | Nothing unless already bounded. | No long state unless work begins. | Demand is not prematurely executed. | Possible research need. | Multiple incompatible directions. | User recognizes the idea summary. |
| 2 | Direction confirmation | A short "is this the direction?" check. | States intended output, non-goals, and risk. | Waits for bounded work order. | Direction decision if execution starts. | Scope clarity. | No promotion. | Direction, value, or scope uncertainty. | User confirms or corrects direction. |
| 3 | Demand interrogation | Only necessary questions. | Defines goal, target user, outputs, allowed scope, forbidden scope, acceptance, stop states. | None yet. | Contract inputs if round begins. | Demand is executable. | Research question if needed. | User-owned ambiguity remains. | A Demand Contract or work order can be written. |
| 4 | External research request | Concise conclusion, source confidence, and conflicts. | Routes to Research and asks for decision only when needed. | Uses curated context only if instructed. | Research task state if multi-round. | Provenance and layer separation. | Raw, clean, reading, insights, kb candidates. | Sources change direction or risk. | Research informs decision without becoming raw clutter. |
| 5 | Research audit and knowledge preservation | Stable conclusions or candidate warnings. | Separates stable assumptions from candidates. | Does not promote raw evidence. | Audit trail and handoff if needed. | No raw claim is treated as stable. | Stable conclusion candidates and workflow patch candidates. | Behavior-changing rule needs approval. | Source trail, confidence, and boundaries exist. |
| 6 | Codex long task execution | Status, changed artifact preview, evidence summary. | Compiles bounded work order. | Reads context, edits allowed files, runs checks, reports risks. | Work order, status, log, handoff. | File existence, terms, commands, diff scope, forbidden paths. | Learnback candidate if repeated friction. | Scope expansion, dependencies, commits, forbidden files. | Required outputs exist and checks pass. |
| 7 | Loop state and handoff | Resumable status, not raw state machinery. | Updates user-facing report. | Reports enough for continuation. | Target, acceptance, state, log, stop gate, handoff. | State reconstructs authorization and evidence. | None unless reusable. | Handoff requires user decision. | Future actor can resume without chat memory. |
| 8 | Verifier review | Pass, risk, repair, HumanGate, or blocked result. | Summarizes evidence and route. | Repairs if allowed and requested. | Verification result and stop state. | Required artifacts, commands, semantic fit, boundaries. | Candidate verifier lesson. | Risk acceptance or blocked decision. | Stop state is evidence-based. |
| 9 | Product preview | A concrete artifact/result to judge. | Converts internal work into product language. | None unless preview exposes defect. | Current result and evidence. | Preview matches required output. | User feedback destination. | Satisfaction or risk decision. | User can judge without reading internals. |
| 10 | Satisfaction feedback | Satisfied, not satisfied, direction wrong, detail wrong, continue, stop. | Classifies and routes feedback. | Receives repair or continuation work order if needed. | Feedback and next state. | Feedback changes route, not ignored. | Learnback candidate. | Ambiguous dissatisfaction or scope expansion. | Feedback has a concrete destination. |
| 11 | Direction correction | A chance to say the product is aimed wrong. | Reopens objective and contract. | Pauses detail work. | Revised direction and reason. | Existing output is marked semantic mismatch if needed. | Candidate anti-pattern lesson. | New direction is user-owned. | New work follows corrected objective. |
| 12 | Detail repair | A bounded fix request. | Creates repair scope. | Fixes allowed details and reruns checks. | Repair round and evidence. | Corrected artifact and no forbidden path change. | Reusable defect pattern if repeated. | Repair exceeds allowed scope. | Detail is fixed without restarting direction. |
| 13 | Continue/deepen request | Continue in the same direction or deepen result. | Checks if continuation is within authorized scope. | Executes next bounded slice. | Next round target and acceptance. | New criteria and evidence. | Productization path candidate. | Deeper work changes scope, cost, or risk. | Output expands coherently. |
| 14 | Stop request | Clear stop and preserved state. | Stops automatic continuation. | Stops. | Stop reason, status, handoff. | No further unauthorized changes. | Reason if reusable. | None unless user asks resume conditions. | Work halts cleanly. |
| 15 | HumanGate decision | A short decision prompt. | Frames options around value, direction, risk, scope, or authorization. | Waits. | Decision pending or resolved. | HumanGate was necessary and not bypassed. | Candidate lesson if repeated. | Always active by definition. | User decision controls next route. |
| 16 | Workflow patch promotion | Candidate behavior change with reason. | Keeps patch as candidate unless promotion is authorized. | Does not edit protocols in this theory round. | Candidate status if tracked. | Candidate has source trail and verifier gate. | Workflow patch candidate. | Behavior change affects future agents. | Candidate remains labeled until accepted. |
| 17 | Knowledge-base update | A concise note that knowledge was captured or held. | Routes stable material to KB candidate only after evidence. | Uses accepted knowledge when supplied. | Learnback destination. | Source trail, confidence, boundary. | KB candidate or rejected claim. | Stable conclusion changes behavior. | Raw, candidate, and stable material stay separate. |
| 18 | Future creator-facing interface | Controls for idea, direction, preview, satisfaction, correction. | Defines interface states and reports. | Supplies execution results behind the surface. | State backing for UI. | UI does not hide evidence or expose internals as routine work. | Product interface lessons. | UI requires product-direction choice. | User operates through creator actions. |
| 19 | MVP product loop | A small complete loop from idea to verified artifact. | Selects smallest useful slice. | Builds only authorized slice. | MVP state and next path. | Acceptance criteria and usability fit. | Productization learnback. | MVP scope tradeoff. | Creator can complete one full cycle. |
| 20 | Failure recovery when output is not satisfying | A correction path, not blame or restart by default. | Distinguishes direction failure, detail failure, missing evidence, or scope mismatch. | Repairs only when bounded. | Failure reason and recovery route. | Mismatch evidence and corrected result. | Anti-pattern or workflow candidate. | Direction or risk decision. | Failure leads to repair, revised contract, stop, or learnback. |

---

## Scenario Notes

### Intake Through Demand

Scenarios 1-3 protect the user from premature execution. Hermes must not let Codex free-run from a vague idea when the direction, product boundary, acceptance signal, or forbidden scope is unclear. The creator-first behavior is not endless questioning; it is enough interrogation to make execution safe.

### Research and Knowledge

Scenarios 4-5 and 17 protect the Knowledge Base. External evidence is useful only if provenance and confidence survive. Raw source material may inform a round, but it should not become accepted workflow behavior until stable conclusions and promotion gates exist.

### Execution, Loop, and Verifier

Scenarios 6-8 define the internal rigor behind an apparently simple product surface. Codex executes, Loop preserves, and Verifier checks. This division prevents false completion and makes long work resumable.

### Preview, Satisfaction, and Correction

Scenarios 9-14 and 20 treat satisfaction as product evidence. A verified artifact may still fail the creator's intent. In that case the correct route depends on the type of dissatisfaction: direction correction, detail repair, continuation, stop, HumanGate, or learnback.

### Productization

Scenarios 18-19 show how the theory becomes a future product. The interface should expose creator actions and concise evidence, while internal subsystems preserve contracts, state, verification, and durable knowledge.

---

## Acceptance Rule

The scenario system works when each practical situation can answer:

- what the user sees,
- what Hermes does,
- whether Codex is involved,
- what Loop preserves,
- what Verifier checks,
- what Research or Knowledge Base receives,
- when HumanGate is required,
- what proves the scenario is successful.

If any scenario cannot answer those questions, it is not ready for implementation or productization.
