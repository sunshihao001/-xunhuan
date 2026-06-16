# Workflow Theory Audit Brief

版本：v0.1  
状态：需求拷问后的理论审计说明  
目的：先说明当前在讲什么，再定义如何用外部资料多角度审计当前 AI 工作流

---

## 1. 这次需求的专业表达

用户的初步想法不是“继续写文档”或“继续做工具”，而是：

```text
对当前正在构建的 Hermes + Codex + Loop + Knowledge Base 工作流，
先做理论总结和需求澄清，弄清楚现在到底在讲什么；
再把这个问题表达成可搜索、可审计、可保存的研究任务；
然后检索外部类似文章、工程实践、方法论和反例，
从多角度审计当前工作流是否方向正确、缺什么、哪里可能空洞、哪里可以产品化。
```

更专业的 Demand Contract 形式是：

```yaml
real_objective: >
  Audit the current personal AI workflow operating model by comparing it with
  external theories and practices around loop engineering, context engineering,
  spec-driven development, human-in-the-loop, verifier gates, and durable
  knowledge-base design.

problem_world: >
  The project already has theory, playbooks, connection docs, contracts, and
  work orders. The risk is that they become internally consistent but externally
  unvalidated. We need external references to challenge, support, and improve the
  workflow.

output_contract:
  - summarize what the current workflow is actually about
  - define audit dimensions
  - collect external source candidates
  - separate candidate evidence from stable conclusions
  - decide what future research pack / Codex work order should do

verifier_gate:
  - sources are labeled by category and authority
  - claims distinguish external evidence from internal assumptions
  - no candidate article is promoted directly into stable knowledge
  - each audit dimension maps back to current repository artifacts
```

---

## 2. 当前我们到底在讲什么

当前项目不是单纯在写一个“AI 使用说明”，而是在构建一个个人 AI 工作流操作系统。

它的核心链路是：

```text
Human initial idea
→ Hermes demand interrogation
→ external research and evidence preservation
→ theory framework
→ Demand Contract
→ .loop state and WORK_ORDER
→ Codex bounded execution
→ Hermes / Verifier evidence check
→ feedback / correction / learnback
→ Knowledge Base / workflow patch
```

这说明当前话题包含 6 个层面。

### 2.1 Human control model

人不是每一步提示 AI 的操作员，而是：

```text
方向拥有者
边界裁判
价值判断者
HumanGate 决策者
最终验收者
```

### 2.2 Hermes cognition and orchestration

Hermes 不是单纯回答问题，而是：

```text
需求拷问端
理论框架整理端
外部资料阅读和知识沉淀端
Demand Contract 编译端
Loop Brief 编译端
Verifier 端
```

### 2.3 Codex bounded executor

Codex 不是战略决策者，而是：

```text
读 WORK_ORDER
在允许范围内执行
跑测试 / 检查
产出 diff / 文档 / 证据
报告风险
```

### 2.4 Loop control surface

`.loop/` 不是装饰目录，而是把任务状态从聊天上下文中拿出来：

```text
TARGET
PATH
ACCEPTANCE
STATE
LOOP_LOG
STOP_GATE
HANDOFF
WORK_ORDER
```

### 2.5 Research knowledge pipeline

外部搜索不是一次性回答，而是：

```text
raw → clean → reading → insights → kb → workflow
```

### 2.6 Productization connection

理论不是终点。理论必须进入：

```text
Demand Contract → .loop → Codex work order → Verifier → feedback
```

否则就会变成“理论文档堆”。

---

## 3. 需求拷问后的关键问题

这次需求要审计的不是“文章数量够不够”，而是这些问题：

### Q1：当前工作流是否符合外部 Loop Engineering 趋势？

要审计：

```text
是否从 prompt-by-hand 走向 system-prompts-agent？
是否有 trigger / goal / verification / state / memory？
是否避免每一步都由人手动提示？
```

### Q2：当前工作流是否符合 Context Engineering？

要审计：

```text
是否把正确上下文保存到正确文件？
是否区分 transient chat context 和 durable knowledge？
是否避免把所有资料直接塞给 Codex？
```

### Q3：当前工作流是否符合 Spec-driven Development？

要审计：

```text
是否先有 spec / contract / acceptance criteria，再让 agent 执行？
是否把 spec 保存在 repo，而不是聊天里？
是否按验收标准 review，而不是凭感觉？
```

### Q4：当前 HumanGate 设计是否合理？

要审计：

```text
人是否只在方向、风险、价值、不可逆操作上介入？
是否避免人每一步都被迫决策？
是否有清楚的 approval / reject / repair / timeout 模型？
```

### Q5：当前 Verifier 是否足够独立？

要审计：

```text
Codex 是否能自证 Done？如果能，就是风险。
Hermes 是否重新跑检查？
是否检查 forbidden paths、文件存在、概念覆盖、链接、测试？
```

### Q6：当前知识库是否能避免空洞理论？

要审计：

```text
外部资料是否保存到 raw/clean/reading/insights/kb/workflow？
是否有 promotion gate？
是否把候选观点和稳定结论区分开？
```

---

## 4. 外部审计的搜索表达

不要只搜索：

```text
AI workflow
```

太泛。

应该拆成 6 组关键词：

```text
1. loop engineering AI agents Codex Claude Code verifier memory worktree
2. context engineering AI agents RAG memory knowledge base context poisoning
3. spec-driven development AI coding agents acceptance criteria work orders
4. human-in-the-loop AI agents approval gates audit trail escalation
5. agent verifier maker checker Codex Claude Code subagents evaluation
6. AI agent workflow evidence provenance citations auditability knowledge base
```

---

## 5. 审计维度

### 5.1 支持性证据

外部资料是否支持我们当前方向？例如：

```text
人从 prompt 操作者变成 loop/system designer
spec 比 prompt 更适合 agent 执行
context engineering 比单轮 prompt 更重要
human-in-the-loop 应该是 gate，不是每步干预
```

### 5.2 反对性证据

外部资料是否指出当前风险？例如：

```text
过度设计 loop
理论太多但不执行
上下文堆叠造成 context confusion
spec 变成 waterfall
human gate 太多导致自动化失效
```

### 5.3 缺口证据

外部资料是否指出我们还缺什么？例如：

```text
实际 audit log
可运行 verifier
source provenance model
research pack checker
worktree isolation
CI / test evidence
human approval protocol
```

### 5.4 产品化证据

外部资料是否能指导下一步做什么？例如：

```text
先做 source-of-truth 层
再做 verifier checker
再做 Codex executor bridge
再做 research pack promotion gate
```

---

## 6. 当前初步判断

当前工作流方向与外部趋势大体一致：

```text
Prompting → Context Engineering → Spec-driven Development → Loop Engineering → HumanGate / Verifier / Durable KB
```

但是风险也很明确：

```text
如果理论不能驱动下一轮执行，就会变成文档堆。
如果外部资料不能分层保存，就会变成一次性搜索。
如果 Codex 没有 bounded work order，就会重新变成开放式执行。
如果 Verifier 不独立，Codex 会自证完成。
```

所以当前最正确的审计方向是：

```text
拿外部资料反向审计当前 workflow 的六个层面：
loop / context / spec / HITL / verifier / knowledge base。
```

---

## 7. 下一步执行建议

下一步应创建一个正式研究包：

```text
workflow_audit_research/
  raw/
  clean/
  reading/
  insights/
  kb/
  workflow/
```

并把外部资料候选进入：

```text
clean/source_candidates.md
reading/<source>.md
insights/workflow_audit_synthesis.md
workflow/audit_patch_candidates.md
```

Codex 后续可以接收一个 bounded work order：

```text
读取外部资料候选和当前 workflow 文档，
生成多角度审计报告，
判断哪些外部观点支持/反驳/修正当前工作流，
输出 workflow patch candidates。
```

---

## 8. 一句话总结

现在讲的是：

```text
如何把一个人用 Hermes 表达的模糊 AI 工作流想法，
通过需求拷问、外部资料、知识库、Demand Contract、Codex 长任务、Loop 和 Verifier，
变成一个可持续产品化的个人 AI 工作流操作系统。
```

接下来要做的是：

```text
用外部资料多角度审计这个操作系统是否真的合理。
```
