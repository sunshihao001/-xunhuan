# Next Research Plan

Status: next research/search steps. This plan identifies missing source types and evidence needed before candidate patches become accepted workflow rules.

## 1. Official Documentation

Search for official docs from OpenAI Codex, Anthropic Claude Code, GitHub Copilot coding agent, and other agent platforms about work orders, context files, tool approvals, memory, verification, and autonomous coding constraints.

Purpose: confirm which loop, context, and verifier patterns are supported by official provider guidance rather than only methodology articles.

Expected output: raw URLs, clean candidates, and reading cards for official docs that affect Codex handoff, context selection, and verification.

## 2. GitHub Repositories And Real Workflow Examples

Search for repositories that implement agent loops, task specs, audit logs, or maker-checker automation for coding agents.

Purpose: compare the current `.loop` model with working examples and identify practical schemas for logs, work order files, and verifier evidence.

Expected output: source candidates for repos, notes on file structures, and patch candidates only when behavior is concrete and verifiable.

## 3. Academic And Industry Frameworks

Search for papers and industry frameworks around human-agent collaboration, HITL governance, agent evaluation, software engineering with LLM agents, provenance, and accountable AI.

Purpose: strengthen evidence quality beyond blog and practice-guide level sources.

Expected output: at least two reading cards that either challenge or refine current assumptions around HumanGate, verifier independence, and auditability.

## 4. Audit Trail Schema Examples

Search specifically for examples of audit log schema, provenance records, approval records, event sourcing for AI systems, model governance logs, and agent action traces.

Purpose: convert PATCH-AUDIT-004 from broad candidate into a concrete schema candidate with fields, required/optional status, and examples.

Expected output: a schema comparison document and one candidate loop log schema.

## 5. Context Selection And Memory Failure Modes

Search for context rot, context poisoning, RAG failure modes, memory contamination, retrieval evaluation, and agent context-window management.

Purpose: improve PATCH-AUDIT-002 so it defines when raw, clean, reading, insights, kb, and workflow material should be given to Codex.

Expected output: context selection policy candidate with verifier checks for overbroad context and unsupported promotion.

## 6. Verifier And Evaluation Practices

Search for maker-checker patterns, independent verifier agents, eval harnesses, CI evidence, test-first agent workflows, and code review automation for AI-generated changes.

Purpose: strengthen PATCH-AUDIT-005 and prevent Codex self-certification.

Expected output: verifier evidence checklist and examples of semantic checks beyond file existence.

## 7. Productization Sequencing

Search for examples of turning internal AI workflow theory into product artifacts: source-of-truth documents, templates, UI/control surfaces, automation, and governance gates.

Purpose: decide whether the next productization move should be source-of-truth specification, verifier implementation, executor bridge, research-pack checker, or interface design.

Expected output: next-round work order candidates, with HumanGate decision points if the evidence supports multiple viable product directions.
