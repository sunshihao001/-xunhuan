# TARGET

## Target

v0.8 adds a Research Evidence Pack initializer: `scripts/init_research_pack.py`.

## Value

External research stops being one-off chat evidence and becomes a durable, layered knowledge asset that can feed Hermes, Codex, verifier gates, and workflow patches.

## Human Role

Define the cognition question, source boundaries, and promotion criteria.

## Agent Role

Hermes compiles the demand into a bounded loop, Codex implements the initializer, Hermes verifies evidence and updates state.

## Non-goals

- Do not perform a full external research crawl in this loop.
- Do not build vector/RAG infrastructure yet.
- Do not mutate existing research packs without explicit force.
- Do not add dependencies.
