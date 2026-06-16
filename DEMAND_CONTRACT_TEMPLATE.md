# Demand Contract Template

版本：v0.1  
定位：把模糊目标表达成可执行、可验证、可交接的任务契约  
上游文件：`AI_WORKFLOW_MAP.md`、`AI_WORKFLOW_ROUTER.md`  
下游文件：`LOOP_BRIEF_TEMPLATE.md`、`HERMES_CODEX_HANDOFF_PROTOCOL.md`

---

## 1. 目的

`DEMAND_CONTRACT_TEMPLATE.md` 的作用是：

> 当 Router 判断一个任务不能直接执行，或需要明确边界、产物、验收标准时，Hermes 应先把任务编译成 Demand Contract。

它解决的问题是：

```text
用户目标可能是模糊的
执行 agent 需要的是明确契约
验证层需要的是可检查标准
人类需要的是清楚的交还点
```

核心原则：

```text
Demand Contract 不是思考的起点，
而是 Demand Cognition 之后的收敛产物。
```

---

## 2. 使用时机

当任务满足以下任一条件，应使用 Demand Contract：

```text
- 目标有价值，但表述不够可执行
- 任务涉及 Codex / agent / 工具执行
- 任务有明显边界和非目标风险
- 需要验收标准
- 需要防止执行 agent 自行扩大范围
- 任务可能进入 Loop Engineering
- 任务完成后需要交接或沉淀
```

不一定需要完整 Demand Contract 的情况：

```text
- 极简单的一步操作
- 明确的查找 / 读取 / 小修改
- 无长期影响的临时问答
```

但即使是简单任务，也至少应有：

```text
Goal + Output + Verification
```

---

## 3. Demand Contract 总结构

```yaml
demand_contract:
  metadata:
  surface_ask:
  real_objective:
  context:
  problem_world:
  scope:
  non_goals:
  definitions:
  inputs:
  outputs:
  execution_route:
  acceptance_criteria:
  verification_plan:
  risks:
  assumptions:
  stop_conditions:
  handoff:
  learnback:
```

---

## 4. 标准模板

复制以下模板使用。

```markdown
# Demand Contract: <task name>

版本：v0.1  
状态：draft | active | verified | done | done-with-risk | blocked | human-gate  
创建者：Hermes  
执行主体：Hermes | Codex | Tools | Human | Mixed  
上游来源：<user ask / router decision / project file>

---

## 1. Surface Ask

用户原始请求：

```text
<保留用户原话>
```

表面任务：

```text
<看起来用户要做什么>
```

---

## 2. Real Objective

真实目标：

```text
<这次任务真正要达成的价值>
```

为什么这不是一个普通执行任务：

```text
<说明它为什么需要契约、边界或验证>
```

---

## 3. Context

相关背景：

```text
<项目、代码库、已有文档、上游文件、用户偏好、约束>
```

相关文件 / 系统：

```text
- <file or system>
- <file or system>
```

---

## 4. Problem World

问题世界：

```text
<当前真正的问题域是什么>
```

解决世界：

```text
<我们准备用什么方式解决>
```

关键概念：

```text
- <concept>: <definition>
- <concept>: <definition>
```

---

## 5. Scope

本次包括：

```text
- <included item>
- <included item>
```

本次不包括：

```text
- <excluded item>
- <excluded item>
```

允许修改 / 执行范围：

```text
- <allowed file / repo / API / directory / command type>
```

禁止修改 / 执行范围：

```text
- <forbidden area>
```

---

## 6. Definitions

为避免语义漂移，先定义关键术语。

| 术语 | 定义 | 非此含义 |
|---|---|---|
| <term> | <meaning> | <not meaning> |

---

## 7. Inputs

输入来源：

```text
- 用户提供：<...>
- 文件来源：<...>
- 工具来源：<...>
- 外部来源：<...>
```

缺失输入：

```text
- <missing input>
```

缺失输入处理方式：

```text
<assume / retrieve / ask / block / downgrade>
```

---

## 8. Outputs

必须产出的内容：

```text
- <artifact 1>
- <artifact 2>
```

输出格式：

```text
<markdown / json / code diff / directory tree / report / loop files>
```

输出位置：

```text
<path or delivery target>
```

质量要求：

```text
- 结构完整
- 可阅读
- 可执行
- 可验证
- 可交接
```

---

## 9. Execution Route

执行路径：

```text
1. <step>
2. <step>
3. <step>
```

执行主体：

```text
Hermes: <responsibility>
Codex: <responsibility>
Tools: <responsibility>
Human: <responsibility>
```

是否需要 Loop Engineering：

```text
Yes / No
```

如果需要，进入：

```text
LOOP_BRIEF_TEMPLATE.md
```

---

## 10. Acceptance Criteria

完成标准：

```text
- [ ] <check 1>
- [ ] <check 2>
- [ ] <check 3>
```

最低可接受版本：

```text
<minimum viable completion>
```

不可接受版本：

```text
- <failure mode>
- <failure mode>
```

---

## 11. Verification Plan

验证方式：

```text
- 文件检查：<how>
- 命令检查：<command>
- 测试检查：<test command>
- 语义检查：<criteria>
- 人类检查：<when needed>
```

证据要求：

```text
- <file path>
- <diff>
- <test output>
- <URL>
- <log>
```

原则：

```text
不能只接受 agent 自述，必须有可检查证据。
```

---

## 12. Risks

已知风险：

```text
- <risk>
- <risk>
```

风险缓解：

```text
- <mitigation>
- <mitigation>
```

Done-with-Risk 条件：

```text
<什么情况下可交付但必须标注风险>
```

---

## 13. Assumptions

当前假设：

```text
- <assumption>
- <assumption>
```

如果假设不成立：

```text
<repair / block / human gate / re-route>
```

---

## 14. Stop Conditions

Done：

```text
<全部验收通过>
```

DoneWithRisk：

```text
<主要目标完成，但有明确风险>
```

Blocked：

```text
<缺权限、工具、文件、网络、关键输入>
```

HumanGate：

```text
<需要用户判断价值、方向、范围或授权>
```

Repair：

```text
<未通过验收但可自动修复>
```

Abandon：

```text
<目标失效或不值得继续>
```

---

## 15. Handoff

交付给用户时必须说明：

```text
- 完成了什么
- 产物在哪里
- 用什么证据验证过
- 还有什么风险
- 下一步建议是什么
```

如果交给 Codex，必须提供：

```text
- 任务目标
- 修改范围
- 禁止事项
- 验收标准
- 测试命令
- 输出证据要求
```

---

## 16. Learnback

任务结束后检查：

```text
- 是否需要更新 AI_WORKFLOW_MAP.md？
- 是否需要更新 AI_WORKFLOW_ROUTER.md？
- 是否需要创建或修改 skill？
- 是否需要沉淀到项目知识库？
- 是否暴露新的失败模式？
```
```

---

## 5. 简化版 Demand Contract Lite

适用于中低复杂度任务。

```yaml
demand_contract_lite:
  goal: <what to achieve>
  scope: <what is included>
  non_goals: <what is excluded>
  output: <artifact / answer / code / file>
  executor: Hermes | Codex | Tools | Human
  acceptance:
    - <check>
    - <check>
  verification:
    - <evidence>
  stop_gate:
    done: <criteria>
    blocked: <criteria>
    human_gate: <criteria>
```

---

## 6. Codex Task Package 转换规则

当 Demand Contract 需要交给 Codex 执行时，应转换成 Codex Task Package。

### 必须包含

```text
1. Goal
2. Repository / working directory
3. Relevant files
4. Allowed changes
5. Forbidden changes
6. Implementation steps
7. Test commands
8. Acceptance criteria
9. Evidence required
10. Stop conditions
```

### Codex 不应获得

```text
- 无限开放目标
- 未定义的“自己看着办”
- 没有测试要求的实现任务
- 可以自行扩大范围的权限
- 自己判断业务 Done 的权力
```

---

## 7. Loop Brief 转换规则

当任务满足以下条件，应把 Demand Contract 编译成 Loop Brief：

```text
- 需要多轮执行
- 需要保存状态
- 需要 Codex 多次接力
- 需要每轮验证
- 需要 Done / DoneWithRisk / Blocked / HumanGate 判断
```

转换关系：

| Demand Contract 字段 | Loop Brief 文件 |
|---|---|
| Real Objective | `TARGET.md` |
| Scope / Non-goals | `PATH.md` |
| Acceptance Criteria | `ACCEPTANCE.md` |
| Risks / Stop Conditions | `STOP_GATE.md` |
| Execution Route | `WORK_ORDER.md` |
| Verification Plan | `ACCEPTANCE.md` + `LOOP_LOG.md` |
| Current Assumptions | `STATE.md` |
| Handoff | `HANDOFF.md` |
| Learnback | `LOOP_LOG.md` + workflow docs |

---

## 8. 验证清单

一个合格 Demand Contract 必须满足：

```text
- [ ] 真实目标明确
- [ ] 范围和非目标明确
- [ ] 关键术语已定义
- [ ] 输出产物明确
- [ ] 执行主体明确
- [ ] 验收标准可检查
- [ ] 风险和假设明确
- [ ] 停止条件明确
- [ ] 可转换为 Codex Task Package 或 Loop Brief
```

失败信号：

```text
- 看起来很完整，但没有可检查验收标准
- 写了很多背景，但不知道谁执行
- 输出格式不明确
- Codex 仍可自由扩大范围
- Done 条件只靠 agent 自述
- 没有 Blocked / HumanGate 条件
```

---

## 9. 与其他文件的关系

```text
AI_WORKFLOW_MAP.md
  ↓ defines system layers
AI_WORKFLOW_ROUTER.md
  ↓ decides whether a contract is needed
DEMAND_CONTRACT_TEMPLATE.md
  ↓ expresses the task as a verifiable contract
LOOP_BRIEF_TEMPLATE.md
  ↓ converts multi-round contracts into loop state files
HERMES_CODEX_HANDOFF_PROTOCOL.md
  ↓ governs Codex execution and Hermes verification
```

---

## 10. 下一步

建议下一步创建：

```text
LOOP_BRIEF_TEMPLATE.md
```

它应该回答：

```text
当 Demand Contract 判断任务需要多轮推进时，如何生成：
- TARGET.md
- PATH.md
- ACCEPTANCE.md
- STATE.md
- LOOP_LOG.md
- STOP_GATE.md
- HANDOFF.md
- WORK_ORDER.md
```

---

## 11. 一句话总结

```text
Demand Contract 是把人的模糊目标转换成 agent 可执行、Hermes 可验证、人类可验收的任务契约。
```
