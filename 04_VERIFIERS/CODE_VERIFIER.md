# Code Verifier

代码型 loop 的验证不能只看 Agent 报告。

## 最小检查

- 测试 / build / lint / typecheck
- `git diff --name-only`
- forbidden paths
- 生成副产物
- 失败分支

## 原则

```text
没有命令证据，不算完成。
没有 diff 审查，不算安全。
没有停止门，不算 loop。
```
