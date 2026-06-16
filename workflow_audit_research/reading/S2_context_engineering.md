# S2 Reading Card - Context Engineering

## Source Metadata

- Title: Context Engineering - How to Design Memory for AI Agents
- URL: https://www.youngju.dev/blog/ai/2026-06-12-context-engineering-ai-agent-memory.en
- Source type: methodology article.
- Audit dimension: Context Engineering, memory, retrieval, compression, durable knowledge.
- Evidence status: candidate external evidence, medium-high relevance, needs further triangulation.

## Core Thesis

Prompt engineering is not enough for agentic work. Context engineering decides what the agent sees, what it remembers, what it forgets, what is retrieved, and how source material is structured. The wrong context can be as harmful as too little context.

## Useful Claims

- Context should be selected and structured, not dumped into the agent.
- Durable memory and transient task context have different jobs.
- Raw material, cleaned summaries, reading cards, stable knowledge, and behavior rules should not be conflated.
- Retrieval and memory need quality control because stale, excessive, or conflicting context can degrade decisions.

## Evidence Strength

The source is strong for the concept that context is an engineered asset. It matches the current workflow's raw / clean / reading / insights / kb / workflow model. It is weaker on exact implementation because memory architectures vary across agents and platforms.

## Limits / Risks

Context engineering can become a documentation burden if selection rules are vague. A large research pack can still create confusion if future work orders ask Codex to read everything. The workflow needs a context selection policy, not only a directory tree.

## Relation To Current Workflow

The current workflow distinguishes durable repository artifacts from chat context and already defines layered research promotion. The current work order also lists read-first files, which is a concrete context-selection mechanism. The remaining gap is policy: when should Codex receive raw, clean, reading, insights, kb, or workflow material, and when should it be excluded?

## Audit Implications

The workflow is aligned with context engineering, but the verifier should check that future work orders do not overload Codex with raw evidence unless the task is specifically a research organization task. Stable knowledge and workflow patches need stronger promotion boundaries.

## Candidate Workflow Patch

Patch candidate: add a `research_context` field to future work orders that states accepted kb, candidate evidence allowed, raw sources allowed yes/no, citation required yes/no, and unsupported claim policy. Verifier gate: check that Codex did not promote raw or clean claims into stable conclusions without reading and synthesis.
