# WORK_ORDER

## Round

creator mvp loop prototype refinement v0.2

## Source documents

- `CODEX_WORK_ORDER_CREATOR_MVP_PROTOTYPE_REFINEMENT_V0_2.md`
- `prototypes/creator-mvp-loop-v0-1.html`
- `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`
- `CREATOR_INTERFACE_CONTRACT_V0_1.md`
- `CREATOR_WORKFLOW_OPERATING_MODEL.md`
- `CREATOR_WORKFLOW_ANTI_PATTERNS.md`

## Objective

Create a refined v0.2 static prototype that improves creator-facing hierarchy, product feel, and interaction clarity while preserving the v0.1 prototype and staying inside the original MVP loop boundary.

The v0.2 prototype must still demonstrate:

```text
idea intake -> direction check -> status -> preview -> evidence summary -> satisfaction feedback -> correction/stop
```

and must keep internals summarized:

```text
Hermes -> Demand Contract -> Loop -> Codex -> Verifier -> feedback/learnback
```

## Allowed files for Codex execution

```text
prototypes/creator-mvp-loop-v0-2.html
INDEX.md
```

Codex must not modify:

```text
prototypes/creator-mvp-loop-v0-1.html
```

Hermes may update `.loop/*` after verification.

## Forbidden scope

- No dependencies or package files.
- No CLI tools.
- No full app architecture.
- No real `.loop` automation.
- No services, databases, auth, integrations, or network behavior.
- No default exposure of raw `.loop`, work order, verifier transcript, git, research layers, or KB schemas.
- No protocol/template/runner/verifier/workflow/knowledge-base/trial/script/test directory changes.
- No README modification.
- Codex must not commit.

## Required output

- `CODEX_WORK_ORDER_CREATOR_MVP_PROTOTYPE_REFINEMENT_V0_2.md`
- `prototypes/creator-mvp-loop-v0-2.html`
- updated `INDEX.md`

## Verification gates

Hermes must verify:

- v0.2 artifact exists and is substantive;
- v0.1 artifact remains unchanged;
- required labels and concepts are present;
- approve / adjust / reject / continue / stop actions are present;
- HumanGate options are present;
- optional evidence detail is hidden behind disclosure/details;
- no static network/dependency patterns exist;
- `INDEX.md` links both v0.1 and v0.2;
- forbidden directories are unchanged;
- HTML parses with Python stdlib parser;
- extracted inline JavaScript passes `node --check`;
- browser render/interaction is verified if possible.

## Stop-state policy

- `Done` if artifact and browser interaction checks pass and no material open risk remains.
- `DoneWithRisk` if artifact passes but the worktree still carries unrelated dirty state or browser verification is unavailable.
- `Blocked` if required tools or files prevent verification.
