# WORK_ORDER — Round 1: v0.2 Loop 初始化器

## Read first

- README.md
- INDEX.md
- PRODUCT_POSITIONING.md
- 01_PROTOCOL/LOOP_SPEC.md
- 02_TEMPLATES/*.template.md
- .loop/TARGET.md
- .loop/PATH.md
- .loop/ACCEPTANCE.md
- .loop/STOP_GATE.md

## Objective

Implement the minimum runnable CLI for Xunhuan Agent OS:

```bash
python scripts/init_loop.py --name demo --dir <target-dir>
```

It should initialize a `.loop/` directory with the standard 8 loop files.

## Allowed files

- `scripts/init_loop.py`
- `docs/INIT_LOOP.md` or equivalent documentation
- `README.md`
- `INDEX.md`
- `.loop/STATE.md`
- `.loop/LOOP_LOG.md`
- `.loop/HANDOFF.md`

## Forbidden files/directories

Do not modify:

- `00_CONCEPT/**`
- `01_PROTOCOL/**`
- `02_TEMPLATES/**` unless strictly necessary
- `03_RUNNERS/**`
- `04_VERIFIERS/**`
- `05_WORKFLOWS/**`
- `06_KNOWLEDGE_BASE/**`
- `07_TRIALS/**`
- `.git/**`

## Requirements

1. Python standard library only.
2. Create `scripts/init_loop.py`.
3. CLI options:
   - `--name`: loop/task name, default `default-loop`.
   - `--dir`: target project directory, default current directory.
   - `--force`: overwrite existing `.loop` files.
   - `--dry-run`: print what would be written without writing files.
4. Generate exactly these files under target `.loop/`:
   - `TARGET.md`
   - `PATH.md`
   - `ACCEPTANCE.md`
   - `STATE.md`
   - `LOOP_LOG.md`
   - `STOP_GATE.md`
   - `HANDOFF.md`
   - `WORK_ORDER.md`
5. Prefer reading templates from repository `02_TEMPLATES/*.template.md` when running from repo checkout, but the script must still work from a copied script by falling back to built-in minimal templates.
6. If files already exist and `--force` is not set, exit non-zero and do not overwrite.
7. Add docs explaining examples.
8. Do not commit.

## Required verification before returning

Run:

```bash
python scripts/init_loop.py --help
python -m py_compile scripts/init_loop.py
TMP=$(mktemp -d)
python scripts/init_loop.py --name demo --dir "$TMP"
python scripts/init_loop.py --name demo --dir "$TMP" # should fail non-zero
python scripts/init_loop.py --name demo --dir "$TMP" --force
DRY=$(mktemp -d)
python scripts/init_loop.py --name dry --dir "$DRY" --dry-run
test ! -d "$DRY/.loop"
find "$TMP/.loop" -maxdepth 1 -type f | sort
git status --short
git diff --stat
git diff --name-only
```

## Completion report

Return:

- Files changed.
- Implementation summary.
- Exact verification commands/results.
- Any risk/blocker.
