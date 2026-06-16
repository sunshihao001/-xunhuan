# Raw Source URLs

Status: raw/candidate evidence. These sources are listed for audit use only. They are not final kb and do not directly authorize workflow changes.

Captured during workflow external audit research pack round on 2026-06-16. Reachability check returned HTTP 200 for all four URLs during this round.

| Source ID | Title | URL | Source Type | Audit Dimension |
| --- | --- | --- | --- | --- |
| S1 | Loop Engineering: Designing Systems That Prompt AI Agents | https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide | Methodology article | Loop Engineering, verifier, memory, worktrees, agent loops |
| S2 | Context Engineering - How to Design Memory for AI Agents | https://www.youngju.dev/blog/ai/2026-06-12-context-engineering-ai-agent-memory.en | Methodology article | Context Engineering, memory tiers, retrieval, compression, context risk |
| S3 | Spec-Driven Development with AI Coding Agents | https://amux.io/guides/spec-driven-development | Engineering practice guide | Spec-driven development, acceptance criteria, bounded agent execution |
| S4 | The Audit Trail: Keeping Humans in the Loop for Accountable Agentic AI | https://www.kamiwaza.ai/insights/ai-audit-trail-keeping-humans-in-the-loop | Governance/audit article | Human-in-the-loop, audit trail, accountability, provenance |

## Raw Evidence Notes

S1 is useful because it names a shift from manually prompting an agent to designing the loop around the agent: state, memory, continuation, checks, and decomposition. It maps directly to `.loop/WORK_ORDER.md`, stop states, and the maker-checker model. Limitation: it is an explanatory article, not an official standard.

S2 is useful because it frames context as an engineered asset: what the agent sees, what it should remember, what should be compressed, and what should be excluded. It maps directly to the raw / clean / reading / insights / kb / workflow pipeline. Limitation: it is a methodology article, and the exact memory categories need validation against official docs and working systems.

S3 is useful because it argues for specs, constraints, and acceptance criteria as the unit of delegation to AI coding agents. It maps directly to Demand Contract, WORK_ORDER, allowed files, forbidden files, and verifier commands. Limitation: spec-driven guidance can overfit implementation work and may not apply equally to exploratory research rounds.

S4 is useful because it treats human-in-the-loop as an accountability and audit trail mechanism rather than symbolic approval. It maps directly to HumanGate, LOOP_LOG, HANDOFF, verifier evidence, and provenance. Limitation: it is a governance article, so implementation details and schemas require more concrete source types.
