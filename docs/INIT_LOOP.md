# Init Loop CLI

`scripts/init_loop.py` creates the standard Xunhuan `.loop/` directory for a target project.

## Usage

```bash
python scripts/init_loop.py --name demo --dir /path/to/project
```

The command writes exactly these files under `/path/to/project/.loop/`:

- `TARGET.md`
- `PATH.md`
- `ACCEPTANCE.md`
- `STATE.md`
- `LOOP_LOG.md`
- `STOP_GATE.md`
- `HANDOFF.md`
- `WORK_ORDER.md`

## Options

- `--name`: loop/task name recorded in generated files. Defaults to `default-loop`.
- `--dir`: target project directory. Defaults to the current directory.
- `--force`: overwrite existing `.loop` files.
- `--dry-run`: print planned writes without creating files or directories.

When run from this repository, the script reads `02_TEMPLATES/*.template.md`. If the script is copied elsewhere without the repository templates, it falls back to built-in minimal templates.

## Examples

Preview without writing:

```bash
python scripts/init_loop.py --name dry --dir /tmp/example --dry-run
```

Initialize the current directory:

```bash
python scripts/init_loop.py --name default-loop
```

Overwrite an existing loop workspace:

```bash
python scripts/init_loop.py --name demo --dir /tmp/example --force
```
