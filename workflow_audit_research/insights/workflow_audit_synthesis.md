# Workflow Audit Synthesis

Status: cross-source synthesis. This file compares candidate sources by audit dimension and remains upstream of final kb/workflow acceptance.

## Loop Engineering

Support evidence: S1 strongly supports moving from manual prompt-by-hand execution to a loop with state, memory, checks, and continuation. S3 supports this indirectly by treating specs and acceptance criteria as reusable execution units.

Challenge / risk evidence: S1 also implies that loops amplify errors. If the objective, context, or verifier is weak, a longer loop can execute the wrong thing efficiently.

Current workflow assessment: The workflow has a strong loop skeleton through `.loop`, WORK_ORDER, stop states, and Verifier. The gap is reconstructability: why a round exists and how it connects to upstream and downstream artifacts is not always formal.

Improvement direction: Add a connection statement and minimum audit fields to future loop rounds.

## Context Engineering

Support evidence: S2 supports the raw / clean / reading / insights / kb / workflow pipeline and the distinction between transient chat context and durable knowledge. S3 supports explicit read-first context in work orders.

Challenge / risk evidence: S2 warns that more context is not automatically better. Excessive, stale, or conflicting context can confuse an agent.

Current workflow assessment: The workflow has the right layered model, and this research pack implements it. The missing piece is a policy for what layer Codex may consume in each task type.

Improvement direction: Add `research_context` to work orders and verifier checks against raw-to-kb promotion errors.

## Spec-driven Development

Support evidence: S3 supports Demand Contract, WORK_ORDER, allowed files, forbidden files, acceptance criteria, verification commands, and completion reports. S1 supports bounded task loops around agent execution.

Challenge / risk evidence: S3-style controls can become too heavy for exploratory research. The workflow should scale rigor with risk.

Current workflow assessment: This round is well specified: required output tree, allowed/forbidden files, verification commands, and completion report are explicit.

Improvement direction: Classify work order types and define minimum required fields per type.

## Human-in-the-loop

Support evidence: S4 supports HumanGate as an accountability mechanism. S1 supports humans as loop designers and gate owners rather than constant prompt operators.

Challenge / risk evidence: S4 implies symbolic approval is not enough. HITL needs traceable authority and decisions. Too many gates can also slow execution.

Current workflow assessment: HumanGate is conceptually strong, but the audit record does not yet consistently capture human decision status, authority, or escalation reason.

Improvement direction: Formalize HumanGate status and decision fields in loop logs and handoffs.

## Verifier / Maker-checker

Support evidence: S1 and S3 both support explicit verification outside agent self-report. S4 supports independent accountability and evidence trails.

Challenge / risk evidence: A verifier that only checks file existence can miss semantic failure. A verifier that trusts Codex completion text recreates self-certification.

Current workflow assessment: Required verification commands are concrete, and forbidden-path checks are explicitly required. Semantic checks are present but still mostly encoded per work order rather than reusable verifier rules.

Improvement direction: Preserve command output, diff scope, required terms, and semantic acceptance checks as standard verifier evidence.

## Audit Trail / Provenance

Support evidence: S4 directly supports provenance: authorization, input data, permissions, actions, outputs, and human interventions. S2 supports source-layer provenance for research material.

Challenge / risk evidence: Provenance can become noisy if every intermediate thought is logged. The useful level is enough to reconstruct decisions and evidence.

Current workflow assessment: LOOP_LOG and research layers are good foundations. The missing piece is a minimum schema that names source trail, changed files, verifier evidence, and stop state.

Improvement direction: Add an audit trail schema candidate before implementing tools.

## Knowledge Pipeline

Support evidence: S2 supports durable context and memory layers. S4 supports provenance. S3 supports turning accepted knowledge into executable contracts.

Challenge / risk evidence: The biggest risk is premature promotion: a source candidate becomes stable knowledge without reading, synthesis, and limits.

Current workflow assessment: The repository theory already defines raw -> clean -> reading -> insights -> kb -> workflow. This pack operationalizes that pattern for the audit.

Improvement direction: Keep `kb/stable_conclusions.md` conservative and use patch candidates for behavior changes that still need acceptance.
