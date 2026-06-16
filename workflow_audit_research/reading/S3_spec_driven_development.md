# S3 Reading Card - Spec-Driven Development

## Source Metadata

- Title: Spec-Driven Development with AI Coding Agents
- URL: https://amux.io/guides/spec-driven-development
- Source type: engineering practice guide.
- Audit dimension: Spec-driven development, acceptance criteria, bounded execution.
- Evidence status: candidate external evidence, high relevance, practice-oriented.

## Core Thesis

AI coding agents perform better when delegated a specification rather than a vague natural-language prompt. A useful spec defines goal, requirements, constraints, outputs, acceptance criteria, and verification so the agent can act autonomously within boundaries.

## Useful Claims

- Specs are more auditable and reusable than chat prompts.
- Constraints and acceptance criteria reduce agent scope drift.
- Work can be reviewed against explicit criteria instead of subjective completion claims.
- Specs make parallel or repeated execution easier because the source of truth exists outside the current conversation.

## Evidence Strength

The source is strong as engineering practice evidence. It directly supports Demand Contract, `.loop/WORK_ORDER.md`, allowed files, forbidden paths, verification commands, and completion report requirements. It is not enough by itself to define the whole workflow because research and theory rounds may need lighter controls than implementation rounds.

## Limits / Risks

Spec-driven development can become waterfall-like if applied rigidly to discovery. The current workflow includes exploratory research, theory drafting, and product implementation; these should not all use identical specification depth. A heavy spec gate for a small cognition update could slow useful iteration.

## Relation To Current Workflow

The current work order is strongly spec-driven: it lists read-first documents, required tree, content requirements, allowed and forbidden files, required verification, forbidden-path checks, and completion report format. That is a good match. The gap is standardization of which fields are mandatory across different round types.

## Audit Implications

The workflow should keep spec-driven controls for Codex execution, especially when writing files. It should also distinguish research pack rounds from implementation rounds. Spec weight should scale with risk, affected paths, and whether the output changes operating behavior.

## Candidate Workflow Patch

Patch candidate: classify work orders as `research`, `theory`, `implementation`, `verification`, or `learnback`, each with minimum required fields. Verifier gate: check that implementation rounds always include acceptance criteria, forbidden paths, and executable verification, while research rounds include evidence-layer promotion gates.
