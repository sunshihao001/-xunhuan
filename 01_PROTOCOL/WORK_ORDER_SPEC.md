# WORK_ORDER_SPEC

每轮只给 Agent 一个 WORK_ORDER。

## 必备字段

```text
# WORK_ORDER — Round N

## Read first
- .loop/TARGET.md
- .loop/PATH.md
- .loop/ACCEPTANCE.md
- .loop/STATE.md
- .loop/STOP_GATE.md

## Objective
本轮唯一目标。

## Allowed files
允许修改的文件。

## Forbidden files/directories
禁止修改的文件和目录。

## Requirements
本轮要求。

## Required verification before returning
必须运行的命令。

## Completion report
必须返回：改动文件、实现摘要、命令输出、风险/阻塞。
```

## 约束

- 不扩大范围。
- 不自行 commit。
- 不修改 forbidden paths。
- 不把“看起来完成”当作完成。
- 必须返回证据。
