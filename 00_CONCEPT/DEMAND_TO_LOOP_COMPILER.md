# Demand Interrogation → Loop Brief Compiler

## 旧定义

需求拷问端旧模式：

```text
用户给模糊目标
→ Hermes 追问需求
→ 用户回答
→ Hermes 给 Codex 一次任务包
→ 人看结果
→ 人决定下一步
```

问题：人仍然在每轮循环中，是系统最慢的部分。

## 新定义

需求拷问端升级为 Loop Brief Compiler：

```text
用户给目标
→ Hermes 编译 TARGET/PATH/ACCEPTANCE/STOP_GATE
→ Codex 按 WORK_ORDER 执行
→ Hermes 验证并更新 STATE
→ 只在 Done/Risk/Blocked/HumanGate 交还
```

## 新职责

| 旧问题 | 新文件 |
|---|---|
| 目标是什么？ | TARGET.md |
| 怎么走？ | PATH.md |
| 怎么算完成？ | ACCEPTANCE.md |
| 当前到哪了？ | STATE.md |
| 每轮做了什么？ | LOOP_LOG.md |
| 什么时候停？ | STOP_GATE.md |
| 怎么交还？ | HANDOFF.md |
| 给 Agent 哪个任务？ | WORK_ORDER.md |

## 专业表达

不要说：

> 我先做需求澄清。

应该说：

> 我先将目标编译成一个有界执行闭环：明确目标、路径、验收、状态、停止条件和交还点。Codex 每轮只执行一个 bounded work order；Hermes 每轮验证证据并决定继续、完成、风险交还或阻塞。
