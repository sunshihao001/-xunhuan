# VERIFIER_SPEC

Verifier 是 Loop OS 的安全核心。

## 原则

> Agent 自己说完成，不等于完成。

Hermes 或独立 verifier 必须重新运行关键检查。

## 最小检查

```bash
# 示例，按项目替换
python tools/build_index.py
python tools/build_index.py --check
python -m py_compile tools/build_index.py
git diff --name-only
git status --short
```

## 必查项

- 命令是否真的退出 0
- 产物是否存在
- 产物是否非空
- forbidden paths 是否被修改
- 是否有未授权副产物
- 是否有失败分支测试
- 是否需要 HumanGate

## 负向验证

如果有 check mode，要验证失败分支：

```text
故意制造 stale/bad state
→ check 应该非零失败
→ 恢复正常状态
→ check 应该通过
```
