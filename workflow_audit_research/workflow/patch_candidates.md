# Workflow Patch Candidates

Status: candidates only. These are not final workflow patches and do not modify protocol, templates, scripts, or forbidden paths in this round.

## PATCH-AUDIT-001 - Loop Connection Statement

- Source evidence: S1, S3, `THEORY_TO_PRODUCT_CONNECTION.md`.
- Target artifact / behavior: future `.loop/WORK_ORDER.md` and verifier review behavior.
- Proposed change: require each loop round to state upstream artifact, current bounded objective, downstream destination, and why the round is not a standalone document.
- Verifier gate: reject Done if the round cannot be mapped to contract, loop, kb, workflow patch, verifier evidence, or learnback.
- Status: candidate.

## PATCH-AUDIT-002 - Research Context Field

- Source evidence: S2, S3, `RESEARCH_TO_PRODUCT_LOOP.md`.
- Target artifact / behavior: future work orders that use external evidence.
- Proposed change: add `research_context` with accepted kb, candidate sources allowed, raw allowed yes/no, citation required yes/no, and unsupported claim policy.
- Verifier gate: check that raw/clean claims were not promoted into stable kb without reading and synthesis.
- Status: candidate.

## PATCH-AUDIT-003 - Work Order Type Classification

- Source evidence: S3 and the risk of over-specifying exploratory work.
- Target artifact / behavior: Demand Contract and work order drafting.
- Proposed change: classify rounds as research, theory, implementation, verification, or learnback. Define minimum fields for each type.
- Verifier gate: implementation rounds must include acceptance criteria, forbidden paths, and executable checks; research rounds must include evidence-layer gates.
- Status: candidate.

## PATCH-AUDIT-004 - Minimum Loop Audit Trail Fields

- Source evidence: S4, S1, current `.loop` model.
- Target artifact / behavior: future `LOOP_LOG` and `HANDOFF` entries.
- Proposed change: record initiator, objective, upstream artifact, read-first files, allowed paths, changed files, verification commands, verifier result, stop state, HumanGate status, and learnback destination.
- Verifier gate: durable artifact rounds cannot be marked Done without enough information to reconstruct authorization, action, evidence, and stop state.
- Status: candidate.

## PATCH-AUDIT-005 - Maker-checker Evidence Boundary

- Source evidence: S1, S3, S4.
- Target artifact / behavior: verifier completion decisions.
- Proposed change: make Codex completion report evidence for review, not final verification. Verifier must independently check files, diff scope, commands, required terms, and semantic fit.
- Verifier gate: completion report that lacks command results, changed files, or forbidden-path check is DoneWithRisk or Repair, not Done.
- Status: candidate.

## PATCH-AUDIT-006 - Cautious KB Promotion Rule

- Source evidence: S2, S4, `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md`.
- Target artifact / behavior: knowledge pipeline promotion.
- Proposed change: require stable conclusions to include source trail, applicability boundary, confidence, exceptions, and last reviewed date before final kb promotion.
- Verifier gate: reject broad stable claims that do not distinguish support evidence, challenge evidence, and limitations.
- Status: candidate.
