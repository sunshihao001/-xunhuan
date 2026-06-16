# Compile Loop CLI

`scripts/compile_loop.py` compiles a high-level intent brief / demand contract into a proposed Xunhuan loop package. Default mode remains read-only; guarded write mode can materialize standard `.loop/` files only when explicitly requested.

It is the v0.6 companion to the existing tool chain:

```text
Init Loop CLI     → creates .loop/
Check Loop CLI    → verifies .loop/ readiness
Run Loop CLI      → summarizes current loop state
Plan Next CLI     → structures WORK_ORDER into execution/verifier checklists
Compile Loop CLI  → compiles high-level intent into a proposed loop package
```

## Boundary

This command is intentionally safe and read-only by default.

In default mode it does **not**:

- write `.loop/` files
- execute Codex or another agent
- run shell commands from the intent brief
- write git commits
- call external services

It only reads an intent brief and produces a proposed loop draft in memory / stdout.

Guarded write mode requires both `--write` and `--dir <target-project>`. It writes only under `<target-project>/.loop/`, refuses to silently write to the current working directory, and refuses to overwrite existing target files unless `--force` is provided.

## Usage

```bash
python scripts/compile_loop.py --intent /path/to/intent.md
```

Machine-readable output:

```bash
python scripts/compile_loop.py --intent /path/to/intent.md --json
```

Guarded write mode:

```bash
python scripts/compile_loop.py --intent /path/to/intent.md --write --dir /path/to/project
```

Overwrite existing generated `.loop/` files:

```bash
python scripts/compile_loop.py --intent /path/to/intent.md --write --dir /path/to/project --force
```

Write mode creates:

- `TARGET.md`
- `PATH.md`
- `ACCEPTANCE.md`
- `STATE.md`
- `LOOP_LOG.md`
- `STOP_GATE.md`
- `HANDOFF.md`
- `WORK_ORDER.md`

## What it parses

The compiler recognizes these sections from the intent brief:

- `Goal`
- `Scope`
- `Non-goals`
- `Inputs`
- `Outputs`
- `Constraints`
- `Acceptance`
- `Risks`
- `HumanGate`

## Human-readable example

```text
Xunhuan compile loop: READY
Intent: /tmp/intent.md
Goal: Build a safe loop compiler.
Scope: Compile a brief into a proposed loop package.
Non-goals:
- Do not write files.
- Do not execute agents.
Proposed loop:
- TARGET.md: ['Target', 'Value', 'Human Role', 'Agent Role', 'Non-goals']
- PATH.md: ['Max rounds', 'Round 1']
- ACCEPTANCE.md: ['Final Done Criteria', 'Evidence Required Each Round']
- WORK_ORDER.md: ['Objective', 'Inputs', 'Outputs', 'Constraints', 'Risks', 'HumanGate']
Mode: read-only compiler; this CLI does not write files or execute agents.
Issues: none
```

If the intent brief is missing required sections, the compiler exits non-zero and lists the missing sections.

## JSON contract

`--json` emits parseable JSON with at least:

```json
{
  "ok": true,
  "intent_path": "/tmp/intent.md",
  "write": false,
  "target_dir": null,
  "written_files": [],
  "goal": "Build a safe loop compiler.",
  "scope": "Compile a brief into a proposed loop package.",
  "non_goals": ["Do not write files."],
  "inputs": ["An intent markdown file."],
  "outputs": ["Structured proposed loop data."],
  "constraints": ["Read-only.", "Standard library only."],
  "acceptance": ["Parse sections.", "Emit JSON."],
  "risks": ["Missing sections should be reported."],
  "human_gate": ["Writing files requires explicit approval."],
  "proposed_loop": {
    "TARGET.md": {},
    "PATH.md": {},
    "ACCEPTANCE.md": {},
    "WORK_ORDER.md": {}
  },
  "issues": []
}
```

## Typical flow

```bash
python scripts/plan_next.py --dir /path/to/project
python scripts/compile_loop.py --intent /path/to/intent.md
```

Use default mode for review and planning. Use guarded write mode only when the target project directory is explicit and the caller is ready for `.loop/` files to be created. After writing, verify the target with:

```bash
python scripts/check_loop.py --dir /path/to/project
```
