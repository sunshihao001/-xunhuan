# Clean Source Candidates

Status: cleaned candidate evidence. This file summarizes source relevance, quality, limits, and intended use. It does not promote any claim into final kb.

## S1 - Loop Engineering: Designing Systems That Prompt AI Agents

- URL: https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide
- Source type: methodology article.
- Relevance: high.
- Quality: medium-high for conceptual coverage; not authoritative as a formal standard.
- Summary: The source frames loop engineering as designing a system that prompts, checks, remembers, and continues work with AI agents. It emphasizes moving beyond one-off prompts toward stateful agent operation with memory, worktrees, subagents, skills, and verification.
- Limitations: The article is interpretive and field-facing. It should be used as trend and vocabulary evidence, not as definitive proof that any specific implementation pattern is correct.
- Use_for: compare current `.loop`, WORK_ORDER, STOP_GATE, and Verifier design against external loop-engineering vocabulary; generate patch candidates for connection checks and loop audit logs.

## S2 - Context Engineering - How to Design Memory for AI Agents

- URL: https://www.youngju.dev/blog/ai/2026-06-12-context-engineering-ai-agent-memory.en
- Source type: methodology article.
- Relevance: high.
- Quality: medium-high for context and memory concepts; needs triangulation with official provider docs, RAG patterns, and production case studies.
- Summary: The source distinguishes prompt text from context design. It focuses on what information an agent sees, how memory is selected or compressed, how retrieval differs from persistent memory, and why too much or wrong context can degrade agent behavior.
- Limitations: Memory models vary by platform, and the article does not by itself define a durable schema for this repository.
- Use_for: audit whether the workflow separates transient chat context from durable knowledge and whether Codex receives curated context instead of raw source piles.

## S3 - Spec-Driven Development with AI Coding Agents

- URL: https://amux.io/guides/spec-driven-development
- Source type: engineering practice guide.
- Relevance: high.
- Quality: medium-high for software-agent workflow practice; needs comparison to official Codex, GitHub, and other agent documentation.
- Summary: The source argues that AI coding agents work better from specs with goals, requirements, constraints, and acceptance criteria than from vague prompts. It supports reusable, auditable task definitions and review against criteria.
- Limitations: The practice can become heavy for discovery work. The current workflow should distinguish research cognition rounds from implementation rounds so spec overhead matches risk.
- Use_for: audit Demand Contract, `.loop/WORK_ORDER.md`, allowed/forbidden paths, acceptance criteria, verification commands, and completion reports.

## S4 - The Audit Trail: Keeping Humans in the Loop for Accountable Agentic AI

- URL: https://www.kamiwaza.ai/insights/ai-audit-trail-keeping-humans-in-the-loop
- Source type: governance and audit article.
- Relevance: high.
- Quality: medium-high for accountability framing; needs concrete schema examples and implementation references.
- Summary: The source argues that as AI systems move from recommendation to action, they need traceable evidence about authorization, input data, permissions, actions, outputs, and human intervention points.
- Limitations: The source is stronger on why auditability matters than on exact file formats or verifier implementation.
- Use_for: audit HumanGate, LOOP_LOG, HANDOFF, provenance, verifier evidence, and maker-checker separation.
