# ACCEPTANCE — v0.2

## Final Done Criteria

- `scripts/init_loop.py` 存在。
- `python scripts/init_loop.py --help` 退出 0。
- `python -m py_compile scripts/init_loop.py` 退出 0。
- 在临时目录运行 `python scripts/init_loop.py --name demo --dir <tmp>` 后生成：
  - `.loop/TARGET.md`
  - `.loop/PATH.md`
  - `.loop/ACCEPTANCE.md`
  - `.loop/STATE.md`
  - `.loop/LOOP_LOG.md`
  - `.loop/STOP_GATE.md`
  - `.loop/HANDOFF.md`
  - `.loop/WORK_ORDER.md`
- 第二次无 `--force` 运行应非零失败，避免误覆盖。
- 加 `--force` 后可覆盖。
- `--dry-run` 不写文件。
- README 或 docs 中说明使用方法。
- Markdown 链接检查通过。
- 无第三方依赖。

## Evidence Required

- 命令和输出。
- 生成文件列表。
- git diff / status。
