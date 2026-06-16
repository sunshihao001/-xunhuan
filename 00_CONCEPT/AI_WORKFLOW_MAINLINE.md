# AI Workflow Mainline / AI 工作流主线

## 一句话认知

AI 工作流当前不是一个已经完全产品化的整体，而是一套正在成熟的系统工程范式。正确方向是把 prompt、agent、memory、tool、verification、state、handoff 这些部件组织成有边界、有验证、有状态、有停止门的 Loop Engineering 主线。

## 四代演化

### 1. Prompt Engineering

```text
人写 prompt → AI 回答 → 人继续追问
```

人是驾驶员，AI 是副驾驶。适合问答、文案、简单总结，但人是瓶颈。

### 2. Agentic Workflow

```text
人给任务 → Agent 使用工具执行 → Agent 汇报 → 人检查
```

Agent 能读文件、改代码、跑命令，但边界、验证、状态仍然容易失控。

### 3. Demand Contract

```text
目标 / 上下文 / 约束 / 验收 / 执行包 / 验证门
```

它解决了“不要把模糊需求直接扔给 Agent”的问题，但仍偏一次性任务包。

### 4. Loop Engineering

```text
目标 → 路径 → 检查 → 执行 → 验证 → 状态更新 → 继续/停止/交还
```

人从每轮 prompt 中退出，变成 loop designer。

## 完整主线

```text
User Intent
  ↓
Goal Intake
  ↓
Loop Brief Compiler
  ↓
TARGET / PATH / ACCEPTANCE / STOP_GATE
  ↓
Context Pack
  ↓
WORK_ORDER Round N
  ↓
Agent Runner
  ↓
Verifier
  ↓
STATE / LOOP_LOG
  ↓
Continue or Stop
  ↓
HANDOFF
  ↓
Knowledge Patch
```

## 关键原则

1. 不追求无界自治，先追求有界闭环。
2. 不让 Agent 自证成功，必须有外部 verifier。
3. 不依赖聊天记忆，状态写进项目文件。
4. 不让人参与每一轮，只在 HumanGate 参与。
5. 不把需求拷问端放在中心，而是让它成为 Loop Brief Compiler。
