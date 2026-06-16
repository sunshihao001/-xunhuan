# AI Workflow Map

版本：v0.1  
定位：个人 AI Operating System 的总图文件  
适用对象：Human Owner / Hermes / Codex / 外部工具与资料 / 项目知识库

---

## 1. 核心定义

你的 AI 工作流不是“向 AI 提问并获得回答”，而是一个分层工作系统：

```text
Human Goal
→ Demand Cognition
→ Demand Contract
→ Loop Brief Compiler
→ Agent / Tool Execution
→ Verifier Gate
→ Learnback / Knowledge Base / Skill
```

核心原则：

> 表达专业，执行才能专业。

如果目标、边界、验证标准和交还点没有被表达清楚，任何执行 agent 都容易“看似完成，实际跑偏”。

---

## 2. 总体架构

```text
L0 Human Owner / 人类意图层
  ↓
L1 Demand Cognition / 需求认知层
  ↓
L2 Demand Contract / 表达契约层
  ↓
L3 Loop Brief Compiler / 有界闭环编译层
  ↓
L4 Execution Agents / 执行代理层
  ↓
L5 Verifier Gate / 验证审计层
  ↓
L6 Learnback / 认知沉淀层
```

### L0 Human Owner

负责：

- 提出方向
- 判断价值
- 裁定优先级
- 确认边界
- 在 HumanGate 时做决策
- 最终判断是否符合真实意图

Human Owner 不应长期承担：

- 每一步都重新提示
- 手动推动 agent 下一步
- 替执行 agent 补需求
- 替验证层定义验收标准

### L1 Demand Cognition

目标：把模糊请求变成可理解的问题世界。

包括：

- Surface Ask Intake
- Cognitive Routing
- Problem World Modeling
- Divergence before Convergence
- Current Convergence Slice

### L2 Demand Contract

目标：把认知收敛后的任务表达成可执行契约。

包含：

- Goal
- Scope
- Non-goals
- Definitions
- Input
- Output
- Acceptance Criteria
- Risks
- Stop Conditions
- Handoff Conditions

### L3 Loop Brief Compiler

目标：当任务需要多轮推进时，把 Demand Contract 编译成有界闭环。

标准文件：

```text
.loop/
  TARGET.md
  PATH.md
  ACCEPTANCE.md
  STATE.md
  LOOP_LOG.md
  STOP_GATE.md
  HANDOFF.md
  WORK_ORDER.md
```

### L4 Execution Agents

执行层包括：

- Codex
- Hermes tools
- Browser / terminal / web / GitHub
- 其他 autonomous agents

原则：

```text
Codex executes.
Hermes verifies.
Human owns direction.
```

### L5 Verifier Gate

目标：防止“自称完成”。

验证对象：

- 文件是否真的生成
- 代码是否真的修改
- 测试是否真的执行
- 输出是否符合契约
- 是否越界
- 是否存在 Done-with-Risk

### L6 Learnback

目标：把一次任务的有效经验沉淀为长期资产。

可能沉淀到：

- 项目知识库
- AI_WORKFLOW_VERSION
- skills
- reference docs
- reusable templates

---

## 3. 角色分工

## 3.1 Human Owner

角色：方向拥有者、价值判断者、边界裁决者。

主要职责：

- 定义长期目标
- 判断什么值得做
- 确认关键取舍
- 在 HumanGate 做最终裁决

## 3.2 Hermes

角色：需求认知前端、理论建模器、执行契约编译器、Verifier、知识沉淀器。

Hermes 负责：

- 需求澄清
- 问题世界建模
- Demand Contract 编写
- Loop Brief 编译
- Codex Work Order 生成
- 结果验证
- Learnback 沉淀

Hermes 不应只做：

- 临时聊天
- 泛泛总结
- 无验证的建议

## 3.3 Codex

角色：受约束的代码执行 agent。

Codex 负责：

- 写代码
- 改代码
- 跑测试
- 修 bug
- 重构
- 生成工程文件

Codex 不应负责：

- 自己重新定义目标
- 自己扩大范围
- 自己判断业务 Done
- 自己替代 Hermes 做需求收敛
- 自己自证完成

## 3.4 External Sources / Tools

角色：证据输入层。

包括：

- Web
- GitHub
- Twitter / X
- Reddit
- YouTube
- Bilibili
- API docs
- papers
- community discussions

这些来源的作用不是“下载资料”，而是给认知更新、决策和知识库提供证据。

---

## 4. 五大主工作流

## Workflow A：Demand Cognition Workflow

适用场景：

- 目标模糊
- 需求复杂
- 需要项目规划
- 涉及研究、知识库、工作流设计或 agent 协作

流程：

```text
Surface Ask
→ Cognitive Routing
→ Problem World Modeling
→ Divergence
→ Convergence Slice
→ Demand Contract
→ Verifier Gate
```

产物：

```text
Demand Contract
```

---

## Workflow B：Loop Engineering Workflow

适用场景：

- 任务不是一轮能完成
- 需要保存状态
- Codex 需要连续执行
- 需要每轮验证
- 人类只应在关键点介入

流程：

```text
User Goal
→ Demand Cognition Front-End
→ Loop Brief Compiler
→ WORK_ORDER per round
→ Codex bounded execution
→ Hermes verification
→ STATE / LOOP_LOG update
→ Continue / Repair / Done / DoneWithRisk / Blocked / HumanGate
```

核心原则：

> Codex 每次只拿一个 bounded WORK_ORDER，不拿无限开放任务。

---

## Workflow C：Code Implementation Workflow

适用场景：

- 写功能
- 修 bug
- 重构
- 跑测试
- 修改已有 repo

流程：

```text
Hermes compiles contract
→ Codex implements
→ Codex runs local checks
→ Hermes reviews diff / tests / evidence
→ repair if needed
→ handoff when verified
```

Codex Task Package 应包含：

- Goal
- Relevant files
- Allowed changes
- Forbidden changes
- Acceptance criteria
- Test commands
- Required evidence
- Failure reporting format

---

## Workflow D：Research / Cognitive Update Workflow

适用场景：

- 调研趋势
- 抓取文章 / 帖子 / 评论
- 研究工具或项目
- 更新 AI 使用方法

流程：

```text
Cognitive Question
→ Evidence Pool
→ Clean
→ AI Reading
→ Cross-source Synthesis
→ Cognitive Update
→ Knowledge Base
→ Workflow Patch
```

标准目录：

```text
raw/
clean/
reading/
insights/
kb/
workflow/
```

原则：

```text
raw ≠ insight
summary ≠ cognition update
knowledge base ≠ temporary notes
```

---

## Workflow E：Layered Knowledge Base Workflow

适用场景：

- GMGN 知识库
- 项目源码理解
- capability cards
- metrics / quant prep
- MVP 前置准备

推荐顺序：

```text
Capability Overview
→ Code-level Design Specs
→ Capability Cards
→ Metrics / Quant Prep
→ MVP
→ Deep Implementation
```

目录建议：

```text
overview/
design-specs/
capability-cards/
metrics/
mvp/
deep-implementation/
```

原则：

> 先让知识结构足够清楚，再让代码实现稳定落地。

---

## 5. 工作流路由规则

| 输入类型 | 应走工作流 | Hermes 角色 | Codex 角色 |
|---|---|---|---|
| “我想做一个项目” | Demand Cognition + Loop Engineering | 建模、编译 loop | 后续执行 |
| “帮我实现功能” | Code Implementation | contract + verifier | 实现 |
| “帮我研究一下” | Research / Cognitive Update | 定义认知问题、综合 | 通常不用 |
| “帮我整理知识库” | Layered Knowledge Base | 结构设计、内容审查 | 批量生成 |
| “这个 bug 怎么修” | Debugging + Code Implementation | 根因分析、验证 | 修改 |
| “这个方向对不对” | Demand Cognition | 发散、比较、收敛 | 不参与 |
| “把这事持续跑完” | Loop Engineering | 控制闭环 | 每轮执行 |

---

## 6. 决策规则

### Rule 1：模糊任务先 Demand Cognition

触发词：

```text
研究 / 整理 / 规划 / 全量 / 系统性 / 最优 / 工作流 / 知识库 / 项目化 / 长期 / 自动化
```

不要直接执行，先定义：

- 目标
- 问题世界
- 范围
- 非目标
- 验收标准

### Rule 2：超过一轮就编译 Loop

满足任一条件即进入 Loop：

- 多轮执行
- 状态需要保存
- 需要 Codex 连续推进
- 需要中途验证
- 需要自动判断 Done / Blocked / HumanGate

### Rule 3：代码任务由 Codex 执行，Hermes 验证

```text
Hermes: contract + verification
Codex: implementation + local tests
```

### Rule 4：资料抓取不能停在 raw

研究任务必须经过：

```text
Evidence → Reading → Synthesis → Cognitive Update → Stable Knowledge
```

### Rule 5：复杂任务结束必须 Learnback

检查：

- 是否形成可复用方法？
- 是否暴露 workflow 缺陷？
- 是否需要更新 skill？
- 是否需要进入知识库？

---

## 7. 成熟度模型

## Stage 1：Chat-based AI

```text
临时问
临时答
靠上下文推进
边界不稳定
完成标准模糊
```

## Stage 2：Contract-based AI

```text
先澄清
再表达
再执行
有验收标准
有明确输出
```

核心资产：

- Demand Contract
- Codex Task Package
- Verifier Gate

## Stage 3：Loop Engineering AI

```text
任务被编译成有界闭环
状态外置
每轮有 WORK_ORDER
执行和验证分离
只有 Done / DoneWithRisk / Blocked / HumanGate 才交还
```

核心资产：

- `.loop/`
- `WORK_ORDER.md`
- `STATE.md`
- `LOOP_LOG.md`
- `STOP_GATE.md`
- `HANDOFF.md`

当前状态判断：

> 你正在从 Stage 2 走向 Stage 3。

---

## 8. 推荐的正式工作流资产

本文件是总图，后续应继续拆成：

```text
AI_WORKFLOW_MAP.md
AI_WORKFLOW_ROUTER.md
DEMAND_CONTRACT_TEMPLATE.md
LOOP_BRIEF_TEMPLATE.md
HERMES_CODEX_HANDOFF_PROTOCOL.md
```

### Codex 配置层级规则

在本环境中，Codex CLI 0.139.0 对项目级 `.codex/config.toml` 的 `model_provider` / `model_providers` 支持不稳定，实测会忽略这些项目局部 provider 定义。因而：

- **用户级 `~/.codex/config.toml`**：放真正生效的 provider/model 配置
- **项目级 `.codex/config.toml`**：只放项目行为约束、approval、sandbox、web_search 等项目默认项
- **单次运行**：可用 `codex -c key=value` 覆盖

这条规则应视为本仓库的当前配置约定。

### AI_WORKFLOW_ROUTER.md

任务入口路由器：判断任务应走哪条工作流。

### DEMAND_CONTRACT_TEMPLATE.md

需求契约模板：把目标表达成可执行、可验证的任务。

### LOOP_BRIEF_TEMPLATE.md

有界闭环模板：把多轮任务编译为 `.loop/` 状态文件。

### HERMES_CODEX_HANDOFF_PROTOCOL.md

Hermes 和 Codex 的交接协议：定义执行单、证据、验证、返工和交还条件。

---

## 9. 下一步

建议下一步创建：

```text
AI_WORKFLOW_ROUTER.md
```

目标：让每个新任务进入前，都先经过统一路由：

```text
1. 这是研究、代码、知识库、项目规划，还是 workflow 本身？
2. 是否需要 Demand Cognition？
3. 是否需要 Loop Brief？
4. 是否需要 Codex？
5. 验收证据是什么？
6. 什么情况下 Done / DoneWithRisk / Blocked / HumanGate？
```

---

## 10. 一句话总结

```text
Prompting → Contracting → Loop Engineering → Personal AI Operating System
```

你的目标不是更会“问 AI”，而是建立一套可以持续推进项目、更新认知、约束执行、验证结果、沉淀经验的个人 AI 工作系统。
