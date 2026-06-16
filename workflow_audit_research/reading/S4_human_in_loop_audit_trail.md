# S4 Reading Card - Human In Loop Audit Trail

## Source Metadata

- Title: The Audit Trail: Keeping Humans in the Loop for Accountable Agentic AI
- URL: https://www.kamiwaza.ai/insights/ai-audit-trail-keeping-humans-in-the-loop
- Source type: governance and audit article.
- Audit dimension: Human-in-the-loop, HumanGate, audit trail, provenance, accountability.
- Evidence status: candidate external evidence, high relevance, schema needs further sources.

## Core Thesis

When AI systems move from advice to action, human-in-the-loop must be auditable. The system should preserve who authorized action, what data and permissions were used, what steps occurred, what outputs were produced, and where humans approved, rejected, escalated, or repaired the process.

## Useful Claims

- Human-in-the-loop is not just a person present in the process; it is an accountability mechanism.
- Audit trails should support after-the-fact reconstruction of decisions and actions.
- Provenance matters: source data, permissions, actor, action, and result should be traceable.
- Human intervention points should be meaningful gates, not constant micromanagement.

## Evidence Strength

The source is strong for governance framing and accountability requirements. It supports the current HumanGate, LOOP_LOG, HANDOFF, and Verifier concepts. It is weaker for concrete implementation because it does not provide a repository-specific audit log schema.

## Limits / Risks

A heavy audit trail can add friction if it records too much low-value detail. The current workflow should capture enough to reconstruct decisions without turning every minor edit into a compliance exercise. HumanGate should remain reserved for direction, value, risk, scope, irreversible action, or authorization decisions.

## Relation To Current Workflow

The workflow already names HumanGate, stop states, LOOP_LOG, HANDOFF, and verifier evidence. The current gap is that audit trail fields are not yet formal enough. For example, initiator, objective, read-first evidence, changed files, verifier commands, stop state, and human decision status should be captured consistently.

## Audit Implications

The workflow is aligned with HITL accountability in concept, but it needs a clearer audit trail schema and provenance record. The Verifier should be able to reconstruct what was authorized, what changed, what evidence was checked, and whether a human decision was required.

## Candidate Workflow Patch

Patch candidate: define minimum loop log fields for each round: initiator, objective, upstream artifact, read-first files, allowed paths, changed files, verification commands, verifier result, stop state, HumanGate status, and learnback destination. Verifier gate: reject Done if these fields are missing when a round modifies durable artifacts.
