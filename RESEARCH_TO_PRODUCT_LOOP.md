# Research to Product Loop

Version: v0.1  
Status: first complete workflow draft  
Scope: external research to durable knowledge to product execution

---

## 1. Core Flow

External research should move through a controlled pipeline before it changes theory or product behavior:

```text
external research
-> raw
-> clean
-> reading
-> insights
-> kb
-> workflow
-> theory
-> Codex task
-> loop execution
-> product
-> correction
-> learnback
```

The purpose is to prevent temporary search results from becoming unverified doctrine. The system needs traceable evidence, stable conclusions, and behavior-changing workflow patches.

---

## 2. Layer Definitions

### raw

The raw layer stores original evidence with minimal interpretation.

Examples:

- Search result exports.
- Source URLs.
- Article captures.
- Official documentation links.
- GitHub repository notes.
- Video transcripts.
- Community discussions.
- Screenshots or copied excerpts when allowed.

Required metadata:

```yaml
source_id: <stable id>
title: <source title>
url: <source url if any>
source_type: official | article | repo | discussion | video | paper | other
captured_at: <date>
captured_by: Hermes | tool | human
raw_location: <path>
```

Gate rule: raw is evidence, not conclusion. Nothing from raw may directly become a product rule without review.

### clean

The clean layer deduplicates and classifies raw sources.

It answers:

- Is this source relevant?
- Is it official, community, marketing, experimental, or anecdotal?
- Is it duplicate or superseded?
- Is it high, medium, low, or unknown quality?

Recommended fields:

```yaml
source_id:
title:
url:
source_type:
quality: high | medium | low | unknown
relevance: high | medium | low
reason:
use_for: background | citation | comparison | risk | discard
```

Promotion gate from raw to clean:

- Source identity is preserved.
- Relevance is explained.
- Low-quality or duplicate sources are marked, not silently deleted.

### reading

The reading layer converts an important source into an AI reading card.

Each card should include:

- Core claims.
- Evidence strength.
- Author or source position.
- Applicability to Hermes, Codex, Loop, Verifier, or Knowledge Base.
- Limits and assumptions.
- Risks or counterexamples.
- Candidate stable conclusion.
- Candidate workflow patch.

Promotion gate from clean to reading:

- Source is relevant enough to read.
- The card separates claim from interpretation.
- The card states whether the source can affect product behavior.

### insights

The insights layer synthesizes multiple reading cards.

It should identify:

- Consensus across sources.
- Disagreements.
- Repeated failure modes.
- Strong practices.
- Weak or unsupported claims.
- Open questions.
- Product implications.
- Workflow implications.

Promotion gate from reading to insights:

- More than one source is compared when possible.
- Single-source claims are labeled as such.
- Conflicts are preserved instead of flattened.

### kb

The kb layer stores stable knowledge.

A kb item must include:

- Stable conclusion.
- Source trail.
- Applicability boundary.
- Confidence level.
- Known exceptions.
- Last reviewed date.
- Related workflow rules if any.

Promotion gate from insights to kb:

- The conclusion has enough evidence for reuse.
- It is not merely a temporary observation.
- It has clear scope and limits.
- It will help future Hermes or Codex runs.

### workflow

The workflow layer stores behavior-changing patches.

Examples:

- Add a required work order field.
- Add a HumanGate trigger.
- Add a Verifier check.
- Change how research is promoted.
- Change what Codex is allowed to receive.
- Add a stop condition.
- Update a template or playbook.

Promotion gate from kb to workflow:

- The knowledge implies a concrete operational behavior.
- The behavior can be checked.
- The patch names affected roles: Hermes, Codex, Loop, Verifier, Human, or Knowledge Base.
- The patch can be tested in a future loop round.

---

## 3. Theory Integration

Hermes uses kb and workflow layers to update theory. Theory should not cite raw material as if it were settled knowledge.

Theory update checklist:

- Does the new claim come from kb or only raw/reading?
- Does it change role boundaries?
- Does it change the Codex work order shape?
- Does it add a HumanGate?
- Does it add a Verifier requirement?
- Does it change product direction?
- Does it require a correction loop?

If the answer changes execution behavior, create or update a workflow patch before giving Codex a long task.

---

## 4. Codex Task Handoff

Codex should receive curated context:

- Relevant theory files.
- Demand Contract.
- Work order.
- Accepted kb conclusions.
- Accepted workflow patches.
- Specific source summaries when needed.

Codex should not receive an unfiltered pile of raw sources unless the work order is specifically a research organization task. Unfiltered raw evidence increases ambiguity and lets Codex invent conclusions.

Codex task handoff should state:

```yaml
research_context:
  accepted_kb:
    - <path or summary>
  workflow_patches:
    - <path or summary>
  raw_sources_allowed: yes | no
  citation_required: yes | no
  unsupported_claim_policy: mark_as_risk | exclude | ask_HumanGate
```

---

## 5. Loop Execution

The loop turns theory into product by repeated bounded rounds:

```text
Round N WORK_ORDER
-> Codex executes
-> commands run
-> Verifier checks evidence
-> state decision
-> correction or next round
```

Loop state decisions:

- Done: product or artifact meets acceptance criteria.
- DoneWithRisk: product is usable but has explicit unverified or risky areas.
- Blocked: cannot continue because a required input, tool, file, permission, or source is missing.
- HumanGate: human judgment is needed.
- Repair: the current round failed but can be fixed within the same scope.

Each round should produce:

- Changed files or artifacts.
- Verification output.
- Known risks.
- Learnback candidates.

---

## 6. Product Correction

Correction starts when the product does not fit the theory, user intent, or evidence.

Correction inputs:

- Human feedback.
- Verifier failure.
- Failed tests.
- Conflicting sources.
- Missing acceptance criteria.
- Codex implementation report.
- Usage evidence.

Correction process:

1. Hermes identifies the mismatch.
2. Hermes decides whether the mismatch is theory, contract, implementation, or verification.
3. If value or direction is unclear, trigger HumanGate.
4. If the fix is bounded, create a Codex work order.
5. Verifier checks the correction.
6. Stable lessons are promoted to kb or workflow.

Correction should not be treated as failure. It is the mechanism that turns the first version into a product-grade workflow.

---

## 7. Promotion Gate Summary

```text
raw -> clean
  requires source identity and relevance classification

clean -> reading
  requires enough source value to justify a reading card

reading -> insights
  requires synthesis, conflict handling, and applicability analysis

insights -> kb
  requires stable conclusion, source trail, boundaries, and confidence

kb -> workflow
  requires concrete behavior change and verifiable operating rule

workflow -> theory
  requires integration with role model, gates, artifacts, and stop states

theory -> Codex task
  requires bounded work order, allowed files, forbidden files, and verification

Codex task -> product
  requires execution evidence and Verifier approval

product -> correction
  requires mismatch evidence or human feedback

correction -> learnback
  requires reusable lesson, stable conclusion, or workflow patch candidate
```

---

## 8. Verifier Rules

The Verifier must check:

- raw, clean, reading, insights, kb, and workflow terms are used correctly.
- raw evidence is not promoted without gates.
- Codex output follows the accepted theory and work order.
- Forbidden paths are unchanged.
- HumanGate was triggered where required.
- DoneWithRisk is used when checks are incomplete.
- Blocked is used when missing inputs prevent honest completion.
- New reusable lessons have a destination.

The Verifier should reject reports that only say "completed" without evidence.

---

## 9. Operating Rule

External research becomes valuable only when it can survive the current conversation.

The durable path is:

```text
preserve source
-> clean source
-> read source
-> synthesize sources
-> promote stable knowledge
-> patch workflow behavior
-> guide Codex execution
-> verify product evidence
-> correct and learn back
```

This loop is the knowledge engine underneath the Hermes + Codex operating model.
