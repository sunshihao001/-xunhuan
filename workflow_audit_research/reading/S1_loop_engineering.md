# S1 Reading Card - Loop Engineering

## Source Metadata

- Title: Loop Engineering: Designing Systems That Prompt AI Agents
- URL: https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide
- Source type: methodology article.
- Audit dimension: Loop Engineering, Verifier, maker-checker, memory, worktree isolation.
- Evidence status: candidate external evidence, medium-high relevance, not an official standard.

## Core Thesis

The useful unit of AI-agent operation is no longer a single prompt. The stronger pattern is a loop that gives an agent goal, state, memory, context, execution space, verification, and a way to continue or stop. In that model the human becomes a loop/system designer and gate owner rather than a person manually advancing every tiny step.

## Useful Claims

- Agent performance depends on the surrounding loop: what triggers it, what files it reads, how it remembers, how it verifies, and when it stops.
- Loops can amplify good decisions and bad decisions. A flawed objective or unchecked context can be executed at scale.
- Stateful artifacts, worktrees, subagents, skills, and verifier behavior are part of the agent system, not incidental tooling.
- A maker-checker split is safer than letting the executor declare its own success.

## Evidence Strength

The source is strong as vocabulary and practice-pattern evidence. It aligns with observed agent workflow trends and directly maps to Codex-style bounded execution. It is weaker as normative evidence because it is not a formal standard, benchmark paper, or official product manual.

## Limits / Risks

The source can encourage over-engineering if every small task becomes a loop. It also does not prove that this repository's exact `.loop` structure is optimal. Its claims should guide audit questions rather than become final rules.

## Relation To Current Workflow

The current workflow already externalizes state into `.loop`, separates Codex execution from Hermes/Verifier review, and requires work orders with allowed and forbidden paths. That strongly matches the loop-engineering direction. The gap is that some loop evidence is still informal: why a round exists, what prior artifact it connects to, and how verifier evidence is reconstructed later.

## Audit Implications

The workflow is directionally aligned, but it needs stronger connection checks and audit trail structure. Each round should prove it is part of a chain from theory to Demand Contract to work order to verification to learnback.

## Candidate Workflow Patch

Patch candidate: require every loop round to include a connection statement naming the upstream artifact, the current bounded objective, and the downstream promotion or verification target. Verifier gate: reject a round whose output is only a standalone document without a named next role in contract, loop, kb, or workflow.
