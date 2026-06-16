# Workflow External Audit Sources

版本：v0.1  
状态：外部审计候选资料初筛  
上游文件：`WORKFLOW_THEORY_AUDIT_BRIEF.md`  
目的：保存用于审计当前 Hermes + Codex + Loop + Knowledge Base 工作流的外部资料候选

---

## 1. 审计问题

当前要审计的问题是：

```text
当前这套 Hermes + Codex + Loop + Knowledge Base 工作流，
是否已经从“理论 / 文档堆”进化成“可执行、可验证、可持续的 AI Operating System”？
```

审计不是为了证明自己正确，而是为了发现：

```text
支持证据
反对证据
缺口证据
产品化建议
workflow patch 候选
```

---

## 2. 外部审计维度

| 维度 | 要审计什么 | 当前内部对应物 |
|---|---|---|
| Loop Engineering | 是否从手动 prompt 进入系统化 loop | `.loop/`, `WORK_ORDER`, `STOP_GATE` |
| Context Engineering | 是否把正确上下文保存、选择、压缩、隔离 | `AI_WORKFLOW_KNOWLEDGE_PIPELINE.md` |
| Spec-driven Development | 是否先 spec/contract 后执行 | `DEMAND_CONTRACT_*`, `CODEX_WORK_ORDER_*` |
| Human-in-the-loop | 人是否在高价值/高风险节点介入 | `HumanGate`, `STOP_GATE` |
| Verifier / Maker-checker | 执行者和验收者是否分离 | Hermes verifier vs Codex self-report |
| Audit Trail / Provenance | 是否保存可追溯证据链 | `LOOP_LOG`, research raw/clean/reading/insights/kb/workflow |

---

## 3. 候选资料

### S1. Loop Engineering: Designing Systems That Prompt AI Agents

- URL: https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide
- 来源类型：方法论文章
- 主题：Loop Engineering, Codex, Claude Code, memory, skills, worktrees, sub-agents
- 相关度：high
- 质量：medium-high，属于领域解释性文章，不是官方规范，但概念覆盖完整

核心观点：

```text
Loop engineering 是从“人手动 prompt agent”转向“设计一个系统来 prompt / check / remember / continue agent”。
```

与当前工作流关系：

```text
强支持当前路线：Human 不应每轮手动推进；Hermes 应设计 .loop / work order / verifier / memory，让 Codex 执行。
```

可审计当前 workflow 的点：

```text
1. 是否有外部状态文件？有：.loop。
2. 是否有 stop gate？有：Done / DoneWithRisk / Blocked / HumanGate / Repair。
3. 是否有 maker-checker？有：Codex 执行，Hermes verifier。
4. 是否有 memory？部分有：repo docs + .loop；但研究证据层还需要更系统。
```

风险提醒：

```text
文章强调 loop 会放大坏决策。如果 Demand Contract 错，Codex 长任务会把错误执行得更快。
```

候选 workflow patch：

```text
每个 loop round 必须有“为什么这个 round 不是孤立文档”的连接检查。
```

---

### S2. Context Engineering — How to Design Memory for AI Agents

- URL: https://www.youngju.dev/blog/ai/2026-06-12-context-engineering-ai-agent-memory.en
- 来源类型：方法论文章
- 主题：context engineering, memory tiers, retrieval, compression, forgetfulness, RAG vs memory
- 相关度：high
- 质量：medium-high

核心观点：

```text
Prompt engineering 只关注一句话怎么写；context engineering 关注 agent 每一步看到什么信息、以什么结构看到、哪些要记住、哪些要忘记。
```

与当前工作流关系：

```text
强支持“知识不是聊天总结，而是上下文工程资产”。
```

可审计当前 workflow 的点：

```text
1. 是否区分短期上下文和长期知识？部分有。
2. 是否区分 raw evidence 和 stable knowledge？有：raw/clean/reading/insights/kb/workflow。
3. 是否有上下文选择策略？还不够明确。
4. 是否避免把所有资料直接塞给 Codex？理论上有，但执行层还需要 verifier。
```

风险提醒：

```text
上下文不是越多越好。错误/过量/冲突上下文会造成 context confusion、context rot、成本上升。
```

候选 workflow patch：

```text
Codex work order 应显式列出 read-first 文件，并说明哪些外部资料不能直接进入 Codex。
```

---

### S3. Spec-Driven Development with AI Coding Agents

- URL: https://amux.io/guides/spec-driven-development
- 来源类型：工程实践指南
- 主题：spec-driven development, acceptance criteria, constraints, autonomous agents
- 相关度：high
- 质量：medium-high

核心观点：

```text
Spec 比 prompt 更适合 AI agent 执行，因为 spec 有 goal / requirements / constraints / acceptance criteria，可复用、可审计、可并行。
```

与当前工作流关系：

```text
强支持 Demand Contract 和 CODEX_WORK_ORDER 的方向。
```

可审计当前 workflow 的点：

```text
1. 是否先写 spec/contract 再让 Codex 执行？现在已有。
2. 是否有 constraints / forbidden paths？有。
3. 是否有 acceptance criteria？有，但可以进一步标准化。
4. 是否让 review against criteria，而不是凭感觉？Hermes verifier 正在做。
```

风险提醒：

```text
Spec-driven 并不适合所有任务。探索型/一次性任务过度 spec 化会拖慢。
```

候选 workflow patch：

```text
需求拷问端要区分 exploratory research、theory building、productization implementation；不是所有阶段都同样重 spec。
```

---

### S4. The Audit Trail: Keeping Humans in the Loop for Accountable Agentic AI

- URL: https://www.kamiwaza.ai/insights/ai-audit-trail-keeping-humans-in-the-loop
- 来源类型：治理/审计文章
- 主题：audit trail, human-in-the-loop, accountability, evidence, provenance
- 相关度：high
- 质量：medium-high

核心观点：

```text
当 AI 从建议走向行动，必须保留可追溯审计链：谁授权、用什么数据、受什么权限约束、经过哪些步骤、产出什么结果、哪里有人类介入。
```

与当前工作流关系：

```text
强支持 HumanGate / Verifier / LOOP_LOG / HANDOFF 的方向。
```

可审计当前 workflow 的点：

```text
1. 是否记录 action？部分记录在 LOOP_LOG。
2. 是否记录 human authority？目前还不够明确。
3. 是否记录 evidence trail？有验证输出，但外部资料 provenance 还需增强。
4. 是否支持事后重建？repo + .loop 可以，但应强化 audit trail schema。
```

风险提醒：

```text
Human-in-the-loop 不是象征性审批。它应该是可审计、可解释、可回放的治理机制。
```

候选 workflow patch：

```text
每个 loop round 的 LOOP_LOG 应记录：initiator / objective / read-first evidence / changed files / verifier evidence / stop state / human gate status。
```

---

## 4. 初步审计结论

### 4.1 当前方向被外部资料支持的地方

当前 workflow 与外部趋势高度一致：

```text
Prompt-by-hand → Loop Engineering
Prompt text → Context Engineering
Vibe coding → Spec-driven Development
Human micromanagement → HumanGate
Agent self-report → Verifier / maker-checker
Chat memory → Durable repo / .loop / knowledge base
```

这说明当前方向不是孤立想象，而是与 2026 AI agent 工程趋势一致。

---

### 4.2 当前明显缺口

外部资料也指出当前还有缺口：

```text
1. Audit trail schema 不够正式。
2. Context selection policy 还不够明确。
3. Research source promotion gate 还需要执行层 verifier。
4. Human authority / approval record 需要更清楚。
5. Productization source-of-truth 还没真正生成。
6. Worktree / parallel agent isolation 还没进入产品化层。
```

---

### 4.3 当前最大风险

最大风险不是方向错，而是：

```text
理论正确，但没有持续进入执行；
资料很多，但没有 promotion gate；
Codex 能跑，但没有足够审计链；
HumanGate 有概念，但没有 approval/audit schema；
Verifier 有执行，但还没有标准化为可复用检查。
```

---

## 5. 建议的下一步审计包

下一步应创建：

```text
workflow_audit_research/
  raw/
  clean/
  reading/
  insights/
  kb/
  workflow/
```

初始放入：

```text
clean/source_candidates.md
reading/S1_loop_engineering.md
reading/S2_context_engineering.md
reading/S3_spec_driven_development.md
reading/S4_human_in_loop_audit_trail.md
insights/workflow_audit_synthesis.md
workflow/patch_candidates.md
```

---

## 6. 建议的审计型 Codex 长任务

后续可以交给 Codex：

```text
读取当前 workflow 文档和 WORKFLOW_EXTERNAL_AUDIT_SOURCES.md，
创建 workflow_audit_research/ 分层研究包，
将候选资料转成 reading cards，
从 loop/context/spec/HITL/verifier/audit/provenance 六个维度审计当前 workflow，
输出 workflow patch candidates。
```

---

## 7. 审计状态

当前文件属于：

```text
clean/source_candidates + initial insights
```

还不是最终 kb。

只有经过后续阅读卡、横向综合、风险评估和 workflow patch 验证后，才可以提升到：

```text
kb/stable_conclusions.md
workflow/patches.md
```
