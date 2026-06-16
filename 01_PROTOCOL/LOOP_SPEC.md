# LOOP_SPEC

## Object Model

```yaml
loop:
  id: xunhuan-agent-os-loop
  human_role:
    - define target
    - approve risk / direction / irreversible actions
    - final product judgment
  hermes_role:
    - compile loop brief
    - maintain state files
    - run verifier gate
    - decide continue/done/risk/blocked
    - update workflow cognition
  agent_role:
    - execute one bounded work order per round
    - return evidence
    - never expand scope
    - never self-certify final success
  files:
    - TARGET.md
    - PATH.md
    - ACCEPTANCE.md
    - STATE.md
    - LOOP_LOG.md
    - STOP_GATE.md
    - HANDOFF.md
    - WORK_ORDER.md
  stop_states:
    - Done
    - DoneWithRisk
    - Blocked
    - HumanGate
```

## Cycle

```text
select next bounded step
→ generate WORK_ORDER
→ agent executes
→ collect evidence
→ verifier checks
→ update state/log
→ continue or stop
```

## Rules

1. 每轮只执行一个 bounded work order。
2. 每轮必须有验证证据。
3. Agent 不决定最终 Done。
4. 缺信息不是继续猜，而是 Blocked。
5. 涉及密钥、账号、生产数据、不可逆操作、方向冲突，必须 HumanGate。
6. 状态写文件，不依赖聊天上下文。
7. 人不参与每轮 prompt，只参与 gate。
