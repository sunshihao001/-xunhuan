# Init Research Pack CLI

`scripts/init_research_pack.py` creates a layered research evidence pack that turns external research into durable workflow knowledge.

## Usage

```bash
python scripts/init_research_pack.py --name ai-workflow-research --dir /path/to/research --question "How should external research become durable AI workflow knowledge?"
```

The command writes a pack under `/path/to/research/ai-workflow-research/` with these layers:

- `raw/`: original evidence, links, captures, transcripts, and repository notes.
- `raw/source_captures/`: copied or exported source material.
- `clean/`: deduplicated source inventory and source quality notes.
- `reading/`: AI reading cards for important sources.
- `insights/`: synthesis across sources, disagreements, risks, and open questions.
- `kb/`: stable, sourced conclusions with explicit limits.
- `workflow/`: candidate workflow patches and next execution plans.

## Starter Files

- `README.md`
- `clean/sources.json`
- `clean/source_quality.md`
- `insights/synthesis.md`
- `kb/stable_conclusions.md`
- `workflow/patches.md`
- `workflow/next_execution_plan.md`

Existing generated files are preserved unless `--force` is provided.

## Options

- `--name`: research pack directory name.
- `--dir`: parent directory where the pack will be created.
- `--question`: cognition question the pack investigates.
- `--dry-run`: list planned directories and files without writing.
- `--force`: overwrite generated starter files.

## Examples

Preview without writing:

```bash
python scripts/init_research_pack.py --name dry --dir /tmp/research --question "x" --dry-run
```

Overwrite generated starter files:

```bash
python scripts/init_research_pack.py --name ai-workflow-research --dir /tmp/research --question "x" --force
```

## Hermes / Codex / Loop Flow

Hermes uses the pack to preserve evidence, synthesize claims, and decide what can enter `kb/` or `workflow/`. Codex should receive curated `insights/`, `kb/`, and `workflow/` handoff material rather than raw evidence. Loop work orders can then implement accepted workflow patches with bounded verification, while Verifier checks that every promoted change remains sourced, scoped, and traceable.
