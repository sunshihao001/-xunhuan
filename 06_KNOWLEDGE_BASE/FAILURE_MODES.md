# Failure Modes

## 常见失败模式

1. 把 loop 当成无限自治。
2. Agent 自己说完成就相信。
3. 没有 forbidden paths。
4. 状态只留在聊天里。
5. 没有 HumanGate。
6. 没有失败分支测试。
7. 每轮任务太大。
8. 人仍然每轮决定下一步，导致 loop 失效。

## 对策

- max rounds
- STOP_GATE
- Verifier
- STATE/LOOP_LOG
- narrow WORK_ORDER
- forbidden paths
- negative checks
