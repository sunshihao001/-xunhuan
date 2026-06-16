# Stable Conclusions

Status: cautious kb candidate. This file separates stable-enough conclusions from still-candidate claims. It is not a final Knowledge Base promotion and does not modify operating rules by itself.

## Stable Enough For Reuse As Working Assumptions

### SC1 - Workflow execution should be bounded by externalized state and verification.

Source trail: S1, S3, internal `AI_WORKFLOW_THEORY_V0_1.md`, `HERMES_CODEX_EXECUTION_PLAYBOOK.md`.

Conclusion: The current direction of using `.loop`, work orders, acceptance criteria, stop states, and verifier evidence is supported by external practice. Agents should not be driven only by ad hoc chat prompts when durable execution is required.

Boundary: This applies to multi-step, file-writing, productization, and research-pack rounds. Small one-off answers may not need the full loop.

Confidence: medium-high.

### SC2 - Raw research and stable knowledge must remain separate.

Source trail: S2, S4, internal `RESEARCH_TO_PRODUCT_LOOP.md`, `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md`.

Conclusion: The raw / clean / reading / insights / kb / workflow model is a defensible context-engineering and provenance pattern. Raw candidate evidence should not directly become a workflow rule.

Boundary: This applies when external material is intended for reuse, auditing, or workflow change. It is less relevant to temporary one-off lookups explicitly not meant to be saved.

Confidence: medium-high.

### SC3 - Spec-driven delegation is appropriate for Codex execution rounds.

Source trail: S3, S1, internal `PRODUCTIZATION_LOOP_V0_1.md`.

Conclusion: Codex work should be bounded by explicit objective, read-first files, allowed paths, forbidden paths, required outputs, verification commands, and completion report. This is especially important when writing files.

Boundary: Spec depth should scale with risk. Exploratory research can use lighter contracts if it preserves evidence and limits promotion.

Confidence: medium-high.

### SC4 - HumanGate should be a meaningful accountability gate, not constant micromanagement.

Source trail: S4, S1, internal stop-state model.

Conclusion: Human involvement is most useful at value, direction, risk, scope, authorization, and irreversible-action gates. Routine mechanical execution should remain with Codex when already authorized and verifiable.

Boundary: Exact HumanGate record schema remains a candidate until more concrete audit trail examples are collected.

Confidence: medium.

## Still Candidate, Not Stable Yet

- Exact loop log schema fields are candidates. S4 supports the need for audit trails, but more schema examples are needed.
- Exact context memory taxonomy is candidate. S2 supports context engineering, but provider docs and production systems should be compared.
- Worktree and parallel-agent isolation are candidate improvements. S1 suggests relevance, but this round did not audit implementation costs.
- A reusable research-pack verifier is candidate. The current command checks prove this pack exists and covers terms, but no general tool should be created in this round.
- Official productization order remains candidate. The likely order is source-of-truth, verifier, executor bridge, and promotion gate, but this needs another research pass.
