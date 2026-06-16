# Workflow Audit Research Pack

Status: candidate evidence pack, not final kb.

This pack audits the current Hermes + Codex + Loop + Knowledge Base operating model against external literature and practice. Its purpose is to keep candidate evidence, source reading, cross-source synthesis, cautious conclusions, and workflow patch candidates in separate layers so future rounds can inspect how a claim moved from source material into a possible operating rule.

This is not final Knowledge Base material. The `kb/` file contains only cautiously promoted conclusions that are stable enough to reuse as working assumptions. It also names conclusions that remain candidates. No source in `raw/` or `clean/` should be treated as an accepted workflow rule without passing through reading, synthesis, and a verifier gate.

## Reading Order

1. `raw/source_urls.md`: raw/candidate source identities, URLs, source type, and audit dimension.
2. `clean/source_candidates.md`: deduplicated source summaries with relevance, quality, limitations, and intended use.
3. `reading/S1_loop_engineering.md`: loop engineering reading card.
4. `reading/S2_context_engineering.md`: context engineering reading card.
5. `reading/S3_spec_driven_development.md`: spec-driven development reading card.
6. `reading/S4_human_in_loop_audit_trail.md`: human-in-the-loop, audit trail, and provenance reading card.
7. `insights/workflow_audit_synthesis.md`: cross-source audit by dimension.
8. `insights/risk_register.md`: current workflow risks, evidence, severity, mitigation, and target artifact.
9. `kb/stable_conclusions.md`: cautious stable conclusions and still-candidate conclusions.
10. `workflow/patch_candidates.md`: behavior-changing patch candidates, not final patches.
11. `workflow/next_research_plan.md`: missing evidence types and next searches.

## Promotion Gates

`raw/` preserves source identity and capture context. Raw is evidence, not conclusion. It can prove that a candidate exists and is reachable, but it cannot directly change the workflow.

`clean/` classifies and rates sources. Clean material may be used to choose reading priorities, but it still remains candidate evidence.

`reading/` converts important sources into reading cards. Cards separate source claims from interpretation, name evidence strength, and map claims to the current workflow.

`insights/` compares reading cards across audit dimensions. It should preserve support, challenge, risk, and gaps rather than flattening everything into agreement.

`kb/` receives only conclusions that are stable enough to reuse with clear boundaries. The default is caution: contested, single-source, or implementation-specific claims remain candidates.

`workflow/` contains patch candidates when a conclusion implies a concrete behavior change. A patch is not final until a future HumanGate or Verifier round accepts it and updates the relevant operating artifact.
