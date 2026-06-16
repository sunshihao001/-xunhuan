# AI Workflow Knowledge Pipeline

版本：v0.1  
定位：把外部搜索资料从一次性搜索结果升级为可持续复用的 AI 工作流知识储备  
上游文件：`AI_WORKFLOW_CONTROL_MODEL.md`、`AI_WORKFLOW_MAP.md`、`AI_WORKFLOW_ROUTER.md`  
下游文件：`DEMAND_CONTRACT_TEMPLATE.md`、`.loop/`、Codex bounded work orders、workflow patches

---

## 1. 当前认知结论

外部搜索资料不应该只用于当时那一轮回答。

正确方向是：

```text
外部搜索 / 文章 / 讨论 / 仓库 / 视频
→ 分层保存
→ AI 阅读
→ 横向综合
→ 稳定知识库
→ workflow patch
→ 反哺 Hermes / Codex / Loop
```

如果只把外部资料当作临时搜索结果，AI 的回答容易变成：

```text
自然语言理解 + 临时概念拼接
```

这会让理论看起来完整，但缺少证据、文件、来源、上下文和可持续沉淀。

真正需要的是：

```text
可追溯的资料层
+ 可阅读的认知层
+ 可验证的知识层
+ 可执行的工作流补丁层
```

---

## 2. 为什么这很重要

用户的真实目标不是“多搜几篇文章”，而是：

```text
让 Hermes / Codex / Loop 系统拥有长期知识储备，
以后能根据资料、文件和上下文理解当前要做什么，
而不是每次只靠用户自然语言重新解释。
```

也就是说，外部资料的作用不是一次性回答，而是构建：

```text
Personal AI Operating System 的知识燃料层
```

没有这一层，会出现以下问题：

```text
- AI 只能根据当前聊天猜测用户意图
- 理论框架容易空洞
- Codex 没有足够上下文来跑长任务
- Verifier 缺少判断依据
- 下次任务又要重新解释背景
- 外部理论无法变成 workflow patch
```

---

## 3. 外部资料的分层保存模型

### 3.1 raw/ 原始证据层

保存原始搜索结果、网页链接、抓取文本、视频字幕、GitHub 仓库信息、社区讨论等。

用途：

```text
保留证据，不急着解释。
```

要求：

```text
- 保留 URL / 来源 / 抓取时间
- 保留平台类型
- 标记是否为官方、社区、博客、仓库、评论
- 不把 raw 直接当结论
```

### 3.2 clean/ 清洗候选层

对 raw 资料进行去重、分类、来源质量标注。

用途：

```text
从噪声中筛出可读候选。
```

字段建议：

```yaml
source_id:
title:
url:
source_type: official | article | repo | discussion | video | docs
quality: high | medium | low | unknown
relevance: high | medium | low
reason:
```

### 3.3 reading/ AI 阅读层

每条重要资料生成一张 AI reading card。

阅读卡应包含：

```text
- 核心观点
- 作者立场
- 证据强度
- 与当前 AI workflow 的关系
- 可迁移实践
- 风险 / 反例
- 是否可升级为 workflow patch
```

### 3.4 insights/ 横向综合层

把多条 reading cards 进行综合。

输出：

```text
- 共识
- 分歧
- 新趋势
- 关键风险
- 可执行建议
- 待验证问题
```

### 3.5 kb/ 稳定知识层

只有经过阅读和综合后，且对当前系统长期有价值的结论，才进入 kb。

要求：

```text
- 不保存临时观点
- 不保存未验证噪声
- 不把单篇文章观点当稳定知识
- 必须有来源和适用边界
```

### 3.6 workflow/ 工作流补丁层

当某个外部资料或综合结论能改变实际工作流时，升级为 workflow patch。

进入条件：

```text
1. 有外部理论或实践来源
2. 能映射到当前 Hermes / Codex / Loop 工作流
3. 能产生具体行为变化
4. 有可验证输出
```

例子：

```text
- Demand Contract 新字段
- WORK_ORDER 新结构
- STOP_GATE 新规则
- Codex handoff 新协议
- Verifier 新检查
- Knowledge Pipeline 新目录
```

---

## 4. 外部资料如何进入 Hermes / Codex 工作流

### 4.1 Hermes 的使用方式

Hermes 不应只把外部资料总结成答案，而应把资料转成：

```text
- Demand Cognition 的背景知识
- Demand Contract 的上下文字段
- Loop Brief 的目标/风险/验收依据
- Verifier Gate 的检查规则
- Workflow Patch 的候选项
```

Hermes 的职责：

```text
搜索 → 筛选 → 阅读 → 综合 → 判断能否进入 kb/workflow
```

### 4.2 Codex 的使用方式

Codex 不应直接面对杂乱外部资料。

Codex 应接收：

```text
- 已清洗的背景摘要
- 明确的 WORK_ORDER
- 允许/禁止修改范围
- 验证命令
- 验收标准
```

即：

```text
raw evidence 不直接喂 Codex
reading / insights / contract / work_order 才喂 Codex
```

### 4.3 Verifier 的使用方式

Verifier 使用外部资料判断：

```text
- Codex 是否符合当前理论框架
- 是否违背已沉淀的 workflow patch
- 是否缺少引用或证据
- 是否把候选观点误当稳定知识
```

---

## 5. 需求拷问端如何修正

当用户提出初步想法时，需求拷问端不应只问“你要什么产物”。

它应该先判断：

```text
这个想法是否需要外部知识补强？
需要哪些来源？
资料最终进入哪一层？raw / clean / reading / insights / kb / workflow？
什么样的资料能改变当前工作流？
哪些资料只能作为候选，不进入稳定知识？
```

### 5.1 新的需求拷问问题

```text
1. 这次外部资料的目标是回答问题，还是更新长期知识库？
2. 需要哪些来源类型：官方文档、博客、论文、GitHub 仓库、社区讨论、视频？
3. 资料最终要进入哪一层：raw、reading、insights、kb、workflow？
4. 哪些发现才算 workflow patch？
5. 是否需要 Codex 根据这些资料生成文档/代码/工具？
6. Hermes 验证时依据哪些资料和验收标准？
7. 哪些结论只能作为候选，不能进入稳定知识？
```

### 5.2 新的执行收敛

需求拷问端的输出不只是 Demand Contract，还应该包括：

```yaml
research_cognition_contract:
  cognitive_question:
  source_scope:
  evidence_layers:
    raw:
    clean:
    reading:
    insights:
    kb:
    workflow:
  promotion_gate:
  codex_handoff:
  verifier_gate:
  learnback_target:
```

---

## 6. 推荐目录结构

在项目内建议使用：

```text
research/
  README.md
  raw/
    search_results.json
    source_captures/
  clean/
    sources.json
    source_quality.md
  reading/
    <source_id>.md
  insights/
    synthesis.md
    disagreements.md
    risks.md
  kb/
    stable_conclusions.md
  workflow/
    patches.md
    next_execution_plan.md
    changelog.md
```

对于 `-xunhuan` 这类 AI workflow OS 项目，也可以使用：

```text
workflow_research/
  README.md
  raw/
  clean/
  reading/
  insights/
  kb/
  workflow/
```

---

## 7. 与当前工具链的关系

当前 `-xunhuan` 已经具备：

```text
compile_loop.py    intent → proposed_loop / guarded write
check_loop.py      validate .loop
run_loop.py        read loop state
plan_next.py       WORK_ORDER → checklist
init_loop.py       create standard .loop
```

知识管线应补在这些工具之前和旁边：

```text
external research
→ knowledge pipeline
→ Demand Contract / Intent Brief
→ compile_loop.py
→ .loop
→ plan_next.py
→ Codex
→ Verifier
→ workflow patch / kb update
```

也就是说：

```text
知识库不是最后的总结，而是 loop 的燃料。
```

---

## 8. 下一步正确方向

下一步不应该只是继续加执行器，而应该补一个稳定的研究知识入口：

```text
v0.8 / v0.9: research evidence pipeline
```

可能工具：

```text
scripts/init_research_pack.py
scripts/check_research_pack.py
scripts/promote_research_patch.py
```

目标：

```text
让外部资料能被保存、阅读、综合、升级为 workflow patch。
```

这会让后续 Hermes 和 Codex 不再只靠自然语言，而是有长期上下文与资料底座。

---

## 9. 操作原则

以后当用户说：

```text
搜索外部资料来完善这个想法
```

不应只返回搜索摘要。

应默认理解为：

```text
建立一个 research cognition update loop，
把资料保存为分层资产，
再判断哪些资料能进入 kb 或 workflow patch。
```

除非用户明确说：

```text
只要临时搜索结果，不保存。
```

---

## 10. 一句话总结

外部资料不是一次性答案，
而是 Personal AI Operating System 的知识燃料。

正确路径是：

```text
搜索资料
→ 分层保存
→ AI 阅读
→ 认知综合
→ 稳定知识
→ 工作流补丁
→ Codex 执行
→ Hermes 验证
→ 继续沉淀
```
