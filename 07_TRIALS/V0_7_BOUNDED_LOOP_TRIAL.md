# v0.7 Bounded Loop Trial

## 目标

把研究包索引生成器升级成可检查的 bounded loop 能力。

## Round 1

Codex 增加：

```bash
python tools/build_index.py --check
```

Hermes 验证：

- generate pass
- check pass
- py_compile pass
- stale probe fails correctly
- forbidden paths unchanged

## Round 2

Codex 增加 grouped counts：

```text
## workflow (9 files)
## reading (9 files)
## raw (10 files)
## clean (3 files)
## kb (1 file)
```

Hermes 验证：

- generate pass
- check pass
- py_compile pass
- grouped count regex pass
- forbidden paths unchanged

## Stop State

Done。

## 试点结论

这证明了：Hermes 可以把目标编译成 bounded loop；Codex 每轮执行一个 WORK_ORDER；Hermes 作为 verifier 决定继续或停止。用户不需要参与每轮 prompt。
