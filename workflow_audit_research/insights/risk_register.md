# Workflow Audit Risk Register

Status: candidate risk register for the current Hermes + Codex + Loop + Knowledge Base workflow.

| Risk | Why It Matters | Evidence Source | Severity | Mitigation | Target Artifact To Improve |
| --- | --- | --- | --- | --- | --- |
| Loop amplifies wrong objective | A bounded long task can efficiently create many artifacts from a mistaken premise. | S1, S3 | High | Require upstream artifact and connection statement in each work order. | `.loop/WORK_ORDER.md`, future Work Order Spec |
| Codex self-certifies completion | If executor report is treated as verification, errors can pass without independent evidence. | S1, S3, S4 | High | Preserve command output, diff scope, semantic criteria, and forbidden-path checks. | Verifier rules, LOOP_LOG |
| Raw evidence promoted too early | Candidate articles can become doctrine without limits or source comparison. | S2, S4 | High | Enforce raw -> clean -> reading -> insights -> kb -> workflow gates. | research pack README, kb promotion rules |
| Context overload | Giving Codex too many files or raw sources can create confusion and unsupported synthesis. | S2 | Medium-High | Add `research_context` policy naming allowed evidence layers. | WORK_ORDER template candidates |
| Audit trail too informal | Future reviewers may not reconstruct who authorized what, which files changed, or why stop state was chosen. | S4 | Medium-High | Define minimum loop log schema for durable artifact rounds. | `.loop/LOOP_LOG.md`, `.loop/HANDOFF.md` |
| HumanGate becomes symbolic | Human approval without explicit decision, scope, or risk record does not improve accountability. | S4 | Medium | Record HumanGate status: not needed, required, approved, rejected, deferred. | STOP_GATE, LOOP_LOG |
| Over-specified exploratory work | Applying implementation-grade specs to every research or theory round can slow discovery and produce bureaucracy. | S3 | Medium | Classify work order types and scale required fields by risk and artifact type. | Work order guidance |
| Stable kb becomes too broad | Conclusions without applicability boundaries can be reused in the wrong task. | S2, S3 | Medium | Every stable conclusion must include source trail, boundary, confidence, and exceptions. | `kb/stable_conclusions.md` |
| Missing official and academic triangulation | Current four sources are useful but mostly articles/guides. | All source limitations | Medium | Next plan should add official docs, repos, papers, and schema examples. | `workflow/next_research_plan.md` |
| Productization stalls at documentation | The workflow can produce high-quality docs without changing future execution behavior. | S1, S3, internal theory docs | High | Every insight should map to a patch candidate, verifier gate, or explicit non-promotion. | `workflow/patch_candidates.md` |

## Risk Reading

The highest risks are not that the direction is unsupported. The external candidates mostly support the current direction. The main risks are operational: premature promotion, weak audit trail, self-verification, and theory that does not create future behavior changes.

The most urgent mitigation is to keep this pack layered. The second mitigation is to create candidate patches with verifier gates instead of editing core protocol files in this round. That keeps the audit useful while respecting the work order's forbidden path constraints.
