# AI Workflow Router

版本：v0.1  
定位：个人 AI Operating System 的任务入口路由器  
上游文件：`AI_WORKFLOW_MAP.md`  
下游文件：`DEMAND_CONTRACT_TEMPLATE.md`、`LOOP_BRIEF_TEMPLATE.md`、`HERMES_CODEX_HANDOFF_PROTOCOL.md`

---

## 1. 目的

`AI_WORKFLOW_ROUTER.md` 的作用是：

> 每当一个新任务进入时，先判断它应该走哪条 AI 工作流，而不是直接执行。

它解决的问题是：

```text
用户提出一个目标
→ Hermes 不立即泛答或盲目执行
→ 先识别任务类型、复杂度、执行主体、验证方式、停止条件
→ 再进入合适的工作流
```

核心原则：

```text
先路由，再契约；
先契约，再执行；
先验证，再交还；
有经验，再沉淀。
```

---

## 2. Router 总流程

```text
New Task Intake
→ Task Type Classification
→ Ambiguity Check
→ Complexity Check
→ Execution Owner Routing
→ Artifact Routing
→ Verification Routing
→ Stop Gate Routing
→ Workflow Selection
```

对应中文：

```text
新任务进入
→ 判断任务类型
→ 判断是否模糊
→ 判断复杂度
→ 判断谁执行
→ 判断需要什么产物
→ 判断如何验证
→ 判断何时停止/交还
→ 选择工作流
```

---

## 3. Intake：新任务进入时先记录什么

每个任务进入时，先捕捉 8 个字段：

```yaml
surface_ask: 用户原话
apparent_task: 表面任务
suspected_real_objective: 可能的真实目标
domain: 领域 / 项目 / 资料源 / 代码库
urgency: 紧急程度
expected_artifact: 期望产物
execution_need: 是否需要实际执行
risk_of_wrong_execution: 直接执行的跑偏风险
```

示例：

```yaml
surface_ask: 继续推进
apparent_task: 继续生成 AI workflow 文件
suspected_real_objective: 把工作流从总图推进到可执行路由协议
domain: personal AI operating system
expected_artifact: AI_WORKFLOW_ROUTER.md
execution_need: write_file + verification
risk_of_wrong_execution: medium
```

---

## 4. 任务类型分类

### 4.1 一级任务类型

| 类型 | 说明 | 默认工作流 |
|---|---|---|
| research | 外部资料、趋势、项目、社区调研 | Research / Cognitive Update |
| code | 功能实现、bug 修复、重构、测试 | Code Implementation |
| kb | 知识库、文档体系、能力卡、规格 | Layered Knowledge Base |
| planning | 项目规划、路线设计、MVP 定义 | Demand Cognition |
| workflow | AI 工作流、Hermes/Codex 分工、skill 化 | Demand Cognition + Loop Engineering |
| debugging | 错误定位、根因分析、修复验证 | Debugging + Code Implementation |
| ops | 安装、配置、环境、自动化任务 | Ops / Tool Execution |
| creative | 设计、图像、原型、表达物 | Creative Artifact Workflow |
| communication | 邮件、消息、汇报、总结 | Communication Workflow |

### 4.2 快速判断规则

```text
如果用户说“研究 / 调研 / 搜 / 找 / 看看外面怎么做” → research
如果用户说“实现 / 修 / 改代码 / 跑测试” → code
如果用户说“知识库 / 文档 / 结构 / 能力卡” → kb
如果用户说“规划 / 路线 / 怎么做 / 是否可行” → planning
如果用户说“工作流 / Hermes / Codex / agent / skill” → workflow
如果用户说“报错 / 不工作 / 为什么失败” → debugging
如果用户说“安装 / 配置 / 启动 / 部署” → ops
```

---

## 5. 模糊度检查 Ambiguity Check

如果任务满足任一条件，不能直接执行，应先进入 Demand Cognition：

```text
1. 目标词宽泛：研究、整理、系统性、全量、最好、最火、优化、升级
2. 产物不清：不知道最终要文件、代码、报告、列表还是决策
3. 排序不清：Top、最好、重要、优先级没有指标
4. 范围不清：平台、时间窗、语言、项目边界未知
5. 执行主体不清：Hermes 做还是 Codex 做未知
6. 验收不清：不知道什么算完成
7. 风险较高：直接执行可能生成大量错误资产
```

### 模糊度分级

| 级别 | 特征 | 动作 |
|---|---|---|
| Low | 目标、产物、验证都清楚 | 直接执行并验证 |
| Medium | 有目标，但范围或产物需收敛 | Demand Contract Lite |
| High | 目标、范围、验证都不清 | Deep Demand Cognition |
| Critical | 会影响长期架构或大量执行 | Heavy Mode + Loop Brief |

---

## 6. 复杂度检查 Complexity Check

判断任务是否需要 Loop Engineering。

### 6.1 一轮任务

特征：

```text
单个产物
单次执行
无需保存状态
失败可直接返工
```

处理方式：

```text
Demand Contract Lite → Execute → Verify → Handoff
```

### 6.2 多轮任务

特征：

```text
需要多个阶段
需要保存状态
需要 Codex 多次执行
需要持续验证
需要中间产物
需要停止门
```

处理方式：

```text
Demand Cognition → Loop Brief Compiler → WORK_ORDER → Execution → Verification → State Update
```

### 6.3 必须进入 Loop 的触发条件

```text
- 用户说“持续推进 / 自动跑 / 做完为止 / 分阶段”
- 任务涉及代码库大改
- 任务涉及知识库多层建设
- 任务涉及长期研究和认知更新
- 任务需要多个 agents 协作
- 任务结果不能只靠聊天上下文保存
```

---

## 7. 执行主体路由 Execution Owner Routing

| 判断问题 | 如果答案是 Yes | 执行主体 |
|---|---|---|
| 需要代码实现吗？ | Yes | Codex |
| 需要需求建模 / 理论判断吗？ | Yes | Hermes |
| 需要文件生成 / 文档整理吗？ | Yes | Hermes 或 Codex，取决于规模 |
| 需要跑测试 / 改 repo 吗？ | Yes | Codex，Hermes 验证 |
| 需要外部资料搜索吗？ | Yes | Hermes tools / Agent Reach |
| 需要长期循环执行吗？ | Yes | Loop + Codex/Hermes |
| 需要人类价值判断吗？ | Yes | HumanGate |

### 默认分工

```text
Hermes: cognition / contract / loop / verification / learnback
Codex: implementation / tests / refactor / repo edits
Human: direction / priority / tradeoff / final acceptance
Tools: evidence / execution / file system / web / APIs
```

---

## 8. 产物路由 Artifact Routing

根据任务类型选择产物。

| 任务类型 | 推荐产物 |
|---|---|
| research | `research_plan.md`、`raw/`、`reading/`、`insights/`、`cognitive_update.md` |
| code | `DEMAND_CONTRACT.md`、`CODEX_WORK_ORDER.md`、diff、test evidence |
| kb | `overview/`、`design-specs/`、`capability-cards/`、`metrics/` |
| planning | `PLAN.md`、`ROADMAP.md`、`MVP_SCOPE.md` |
| workflow | `AI_WORKFLOW_*.md`、templates、protocols、skills |
| debugging | `ROOT_CAUSE.md`、patch、test evidence、regression note |
| ops | setup log、verified command output、config diff |

---

## 9. 验证路由 Verification Routing

每个任务必须定义验证方式。

| 产物类型 | 验证方式 |
|---|---|
| Markdown 文档 | 文件存在、结构完整、与上游目标一致 |
| 代码修改 | diff、tests、lint/typecheck、运行结果 |
| 研究资料 | 来源可追溯、去重、阅读笔记、综合结论 |
| 知识库 | 层级完整、链接关系、无明显重复或错位 |
| 配置 / 安装 | 命令真实执行、doctor/check 通过 |
| Loop 任务 | STATE / LOOP_LOG / STOP_GATE 已更新 |

验证原则：

```text
不能只相信 agent 自述。
必须看证据：文件、diff、命令输出、测试结果、URL、日志。
```

---

## 10. Stop Gate Routing

每个任务结束时只能进入以下状态之一：

| 状态 | 含义 |
|---|---|
| Done | 达成验收标准，无已知重大风险 |
| DoneWithRisk | 基本完成，但存在明确风险或未验证项 |
| Blocked | 工具、权限、环境或信息缺失导致无法继续 |
| HumanGate | 需要人类做价值判断、授权或范围选择 |
| Repair | 未达标，但可自动返工 |
| Abandon | 目标失效或不值得继续 |

### Stop Gate 决策规则

```text
如果验收全部通过 → Done
如果主要目标完成但有风险 → DoneWithRisk
如果缺工具/权限/API/文件 → Blocked
如果需要用户判断方向/取舍 → HumanGate
如果可自动修复 → Repair
如果任务价值消失 → Abandon
```

---

## 11. Workflow Selection Matrix

| 条件 | 选择工作流 |
|---|---|
| 模糊 + 高价值 | Demand Cognition Workflow |
| 多轮 + 状态保存 | Loop Engineering Workflow |
| 明确代码实现 | Code Implementation Workflow |
| 资料抓取 + 认知更新 | Research / Cognitive Update Workflow |
| 知识结构建设 | Layered Knowledge Base Workflow |
| 报错 / 失败 / 不工作 | Systematic Debugging Workflow |
| 安装 / 配置 / 运维 | Ops Verification Workflow |
| 工作流本身升级 | Demand Cognition + Skillization Review |

---

## 12. Router 输出格式

每次完成路由后，Hermes 应能产出一个简短 Router Decision。

```yaml
router_decision:
  task_type: workflow | code | research | kb | planning | debugging | ops
  ambiguity: low | medium | high | critical
  complexity: one_shot | multi_round | loop_required
  selected_workflow: <workflow name>
  execution_owner: Hermes | Codex | Tools | Human
  required_artifacts:
    - <artifact>
  verifier_gate:
    - <check>
  stop_gate:
    done: <criteria>
    risk: <criteria>
    blocked: <criteria>
    human_gate: <criteria>
  next_action: <immediate action>
```

示例：

```yaml
router_decision:
  task_type: workflow
  ambiguity: low
  complexity: one_shot
  selected_workflow: Workflow Asset Creation
  execution_owner: Hermes
  required_artifacts:
    - AI_WORKFLOW_ROUTER.md
  verifier_gate:
    - file exists
    - references AI_WORKFLOW_MAP.md
    - includes task classification, ambiguity, complexity, stop gates
  stop_gate:
    done: file written and verified
    risk: missing downstream templates
    blocked: file write failure
    human_gate: user must choose next template priority
  next_action: write and verify AI_WORKFLOW_ROUTER.md
```

---

## 13. Router Pseudocode

```python
def route_task(task):
    intake = capture_intake(task)
    task_type = classify_task(task)
    ambiguity = assess_ambiguity(task)
    complexity = assess_complexity(task)

    if ambiguity in ["high", "critical"]:
        workflow = "Demand Cognition"
    elif complexity == "loop_required":
        workflow = "Loop Engineering"
    elif task_type == "code":
        workflow = "Code Implementation"
    elif task_type == "research":
        workflow = "Research / Cognitive Update"
    elif task_type == "kb":
        workflow = "Layered Knowledge Base"
    elif task_type == "workflow":
        workflow = "Workflow Asset Creation"
    else:
        workflow = "Direct Execute + Verify"

    owner = select_execution_owner(task_type, workflow)
    artifacts = select_artifacts(task_type, workflow)
    verifier = define_verifier(task_type, artifacts)
    stop_gate = define_stop_gate(task_type, verifier)

    return RouterDecision(
        task_type=task_type,
        ambiguity=ambiguity,
        complexity=complexity,
        workflow=workflow,
        owner=owner,
        artifacts=artifacts,
        verifier=verifier,
        stop_gate=stop_gate,
    )
```

---

## 14. Router 与后续文件的关系

```text
AI_WORKFLOW_MAP.md
  ↓ defines the whole system
AI_WORKFLOW_ROUTER.md
  ↓ chooses the right path
DEMAND_CONTRACT_TEMPLATE.md
  ↓ expresses bounded one-shot or pre-loop tasks
LOOP_BRIEF_TEMPLATE.md
  ↓ compiles multi-round work into stateful loops
HERMES_CODEX_HANDOFF_PROTOCOL.md
  ↓ governs implementation handoff and verification
```

---

## 15. 下一步

建议下一步创建：

```text
DEMAND_CONTRACT_TEMPLATE.md
```

它应该回答：

```text
当 Router 判断需要 Demand Contract 时，Hermes 应该如何把任务表达成：
- clear goal
- scoped boundaries
- definitions
- output contract
- acceptance criteria
- risks
- stop conditions
- execution handoff
```

---

## 16. 一句话总结

```text
AI Workflow Router 是任务入口控制面：它决定任务先思考、先契约、先循环、先执行，还是先交还人类。
```
