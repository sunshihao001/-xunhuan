# WORK_ORDER

## Round

creator mvp loop prototype v0.1

## Source documents

- `CREATOR_MVP_LOOP_DEMAND_CONTRACT_V0_1.md`
- `CREATOR_INTERFACE_CONTRACT_V0_1.md`
- `CODEX_WORK_ORDER_CREATOR_MVP_PROTOTYPE_V0_1.md`

## Objective

Implement the first browsable `Creator MVP Loop v0.1` prototype as a bounded static artifact.

The prototype must demonstrate:

```text
idea intake -> direction check -> executing/status -> preview -> evidence summary -> satisfaction feedback -> correction/stop
```

It must also summarize the internal route without making the creator operate internals:

```text
Hermes -> Demand Contract -> Loop -> Codex -> Verifier -> feedback/learnback
```

## Allowed files for Codex execution

```text
prototypes/creator-mvp-loop-v0-1.html
INDEX.md
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
- Codex must not commit.

## Required output

- `CODEX_WORK_ORDER_CREATOR_MVP_PROTOTYPE_V0_1.md`
- `prototypes/creator-mvp-loop-v0-1.html`
- updated `INDEX.md`

## Verification gates

Hermes must verify:

- HTML artifact exists and is substantive;
- required flow steps are present;
- approve / adjust / reject / continue / stop controls exist;
- HumanGate is visible;
- preview and evidence summary are visible;
- stop behavior and HumanGate continuation behavior are represented;
- internal route is summarized, not exposed as required creator work;
- no network/dependency patterns are present;
- `INDEX.md` links the work order and prototype;
- changed file scope is allowed;
- forbidden directories are not changed;
- JS syntax extracted from the HTML passes `node --check`.

## Stop-state policy

- `Done` if prototype exists, checks pass, and no material open risk remains.
- `DoneWithRisk` if prototype is usable but browser rendering has not been manually verified.
- `Blocked` if required tools or files prevent implementation.
- `HumanGate` if continuation would expand beyond the prototype slice.
