# AI Workflow Control Model

版本：v0.1  
定位：解释 Human / Hermes / Codex / Agents 在循环代理操作系统中的控制权分配  
上游依据：`AI_WORKFLOW_MAP.md`、`AI_WORKFLOW_ROUTER.md`、`DEMAND_CONTRACT_TEMPLATE.md`、Loop Engineering / Spec-driven Development / Context Engineering 外部资料

---

## 1. 核心判断

你的理解方向是对的：

```text
人不应该长期逐步提示 AI 做每个细节。
人应该负责方向、边界、价值判断和关键决策。
AI 应该把需求编译成可执行契约、拆解任务、执行细节、验证结果、沉淀经验。
```

但这个判断需要补一个关键前提：

> 不是“写好一份整体需求文档，AI 就能自动可靠完成所有细节”，而是“把整体需求表达成可路由、可执行、可验证、可停止、可交还的控制系统”。

也就是说，真正的目标不是：

```text
需求文档 → AI 自动干完
```

而是：

```text
Human Intent
→ Demand Cognition
→ Demand Contract
→ Loop Brief Compiler
→ WORK_ORDER per round
→ Agent Execution
→ Verifier Gate
→ State / Stop / Handoff
→ Learnback
```

这也是 `-xunhuan` 当前正在从 CLI 工具链升级成 Loop Compiler Stack 的原因。

---

## 2. 为什么“整体需求文档”还不够

整体需求文档通常解决的是：

```text
我要什么
为什么做
大概包括什么
```

但 Agent 真正执行时还需要：

```text
哪些文件可以改
哪些文件不能改
每轮做多少
失败怎么判断
什么时候继续
什么时候停止
什么时候必须问人
完成证据是什么
谁来验证
状态保存在哪里
```

如果缺这些，AI 就会出现典型问题：

```text
- 看似理解，但自行补全错误假设
- 看似完成，但没有真实验证
- 做了很多文件，但偏离真实目标
- 遇到边界时继续硬做
- 把执行者的自证当成 Done
- 多轮任务依赖聊天上下文，状态丢失
```

所以正确的系统不是“更长的需求文档”，而是：

```text
需求文档
+ 路由器
+ 执行契约
+ Loop 状态文件
+ Verifier Gate
+ Stop Gate
+ Handoff Gate
```

---

## 3. 人类到底负责什么

Human Owner 不应该负责：

```text
- 每一步都催 AI 下一步
- 给 Codex 反复补 prompt
- 手动检查每个小文件
- 替 agent 定义测试命令
- 替 verifier 判断基础事实
```

Human Owner 应该负责：

```text
- 定义方向：这个目标是否值得做
- 定义价值：什么结果有业务/认知意义
- 定义边界：哪些事情不能做
- 定义优先级：先做哪一层
- HumanGate：遇到成本、风险、范围扩大、不可逆操作时裁决
- 最终验收：是否符合真实意图
```

一句话：

> 人从“操作员”升级为“方向拥有者 + 边界裁判 + 价值判断者”。

---

## 4. Hermes 应该负责什么

Hermes 不是单纯回答问题，也不是只负责聊天。

Hermes 在这个系统中应该是：

```text
Demand Cognition Front-End
+ Loop Brief Compiler
+ Verifier
+ Knowledge Manager
```

具体职责：

```text
1. 理解用户表面请求背后的真实目标
2. 判断任务类型、模糊度、复杂度
3. 产出 Demand Contract
4. 判断是否需要 Loop Engineering
5. 编译 .loop/TARGET.md、PATH.md、ACCEPTANCE.md、STOP_GATE.md 等
6. 给 Codex / Agent 生成单轮 bounded WORK_ORDER.md
7. 验证执行证据，而不是相信执行者自证
8. 根据 STOP_GATE 决定 Continue / Done / DoneWithRisk / Blocked / HumanGate
9. 把成功经验沉淀成知识库、模板或 skill
```

Hermes 的核心价值不是“亲自写所有代码”，而是：

> 把人的意图变成 Agent 可执行、可验证、可停止的系统。

---

## 5. Codex / Agent 应该负责什么

Codex / coding agent 的正确位置是：

```text
Bounded Executor
```

它负责：

```text
- 读 WORK_ORDER.md
- 在允许范围内改代码/文档
- 跑测试
- 修复失败
- 输出执行报告
```

它不应该负责：

```text
- 自己重新定义目标
- 自己扩大范围
- 自己判断业务价值
- 自己决定 HumanGate
- 自己自证 Done
```

这就是为什么 `WORK_ORDER.md` 必须包含：

```text
Objective
Allowed files
Forbidden files/directories
Requirements
Required verification
Completion report
```

---

## 6. 为什么我最近仍然一步步推进

这不是因为你没设置，也不是 Hermes 没调整过来。

主要原因是：当前我们还在建设 Loop OS 的底层控制件。

已经完成的是：

```text
init_loop.py       创建 .loop
check_loop.py      检查 .loop
run_loop.py        读取当前 loop 状态
plan_next.py       把 WORK_ORDER 编译成执行/验证清单
compile_loop.py    把高层 intent 编译成 loop package 提案
```

这说明系统正在从：

```text
人一步步说 → AI 一步步做
```

升级为：

```text
人给方向/边界
→ Hermes 编译 loop
→ Agent 执行 bounded work orders
→ Hermes 验证并自动推进/停止
```

但目前仍然有两个限制：

### 6.1 Codex CLI 当前不可用

最近每轮都尝试调用 Codex，但 Codex CLI 返回 usage limit。

所以暂时变成：

```text
Hermes 编译
→ Codex blocked
→ Hermes 直接实现
→ Hermes verifier 验证
```

这会让体验看起来像 Hermes 还在逐步做，但这是外部执行器阻塞，不是工作流理念错误。

### 6.2 还缺 guarded writer / guarded runner

当前工具大多是 read-only：

```text
compile_loop.py 只提案
plan_next.py 只编译 checklist
run_loop.py 只读状态
```

下一步要进入：

```text
guarded write mode
```

也就是：

```text
compile_loop.py 生成 loop proposal
→ HumanGate/approval
→ write_loop.py 或 compile_loop.py --write 写入 .loop
→ run_loop / plan_next 驱动执行
```

这一步做完后，系统才会更接近你说的“人只负责关键地方，AI 自动推进”。

---

## 7. 外部资料给出的判断

近期外部 AI workflow / agentic coding / loop engineering 资料给出的趋势基本一致：

### 7.1 Loop Engineering

核心趋势是：

```text
从人手动 prompt agent
→ 人设计能 prompt agent 的 loop/system
```

关键点不是“更会写 prompt”，而是：

```text
目标
状态
调度
隔离
验证
记忆
停止条件
```

这与 `-xunhuan` 的 `.loop/` 文件系统方向一致。

### 7.2 Spec-driven Development

外部 spec-driven development 资料强调：

```text
先写结构化 spec
再让 agent 实现
再按 acceptance criteria review
```

这支持你的判断：人不应逐步写实现细节，而应定义 specification / contract。

但它也说明：spec 不能只是“愿望文档”，必须包含：

```text
Goal
Requirements
Constraints
Acceptance Criteria
Verification
```

### 7.3 Context Engineering

context engineering 的核心判断是：

```text
Agent 成败不只取决于 prompt，而取决于它在执行时看到什么上下文、什么顺序、什么状态、什么边界。
```

这说明 `AGENTS.md`、`.loop/`、`WORK_ORDER.md`、`STATE.md`、`LOOP_LOG.md` 不是形式主义，而是让 agent 在长任务里保持一致性的 context infrastructure。

### 7.4 Human-in-the-loop

成熟系统不是完全无人参与，也不是人每步参与，而是：

```text
人类在高风险/高价值/不可逆/方向性节点介入
普通执行细节交给 agent 和 verifier
```

这与你的理解基本一致。

---

## 8. 对你的理解的校正

你的原始理解：

```text
写好整体需求文档，AI 自动实现具体内容细节，人只负责关键边界方向调整。
```

我的判断：

```text
方向正确，但需要升级表达。
```

更专业的表达应是：

```text
人提供 Intent / Direction / Boundary / Value Judgment。
Hermes 负责把它编译成 Demand Contract 和 Loop Brief。
Codex / Agents 只执行 bounded WORK_ORDER。
Verifier 负责证据检查。
Human 只在 HumanGate、Done-with-Risk、方向调整、价值判断时介入。
```

也就是说，不是：

```text
整体需求文档 → AI 自动做完
```

而是：

```text
Intent → Contract → Loop → Work Order → Execution → Verification → Stop/Handoff
```

---

## 9. 现在缺的不是理念，而是控制面自动化

你没有理解错。现在真正缺的是这些控制面能力：

```text
1. Router 自动判断任务是否需要 loop
2. Intent 自动编译 Demand Contract
3. Demand Contract 自动编译 .loop
4. .loop proposal 经 HumanGate 后写入
5. WORK_ORDER 自动分轮生成
6. Executor 自动运行 bounded task
7. Verifier 自动判断 Continue / Done / Risk / Blocked / HumanGate
8. Learnback 自动沉淀
```

目前 `-xunhuan` 已经做到了第 3 步的只读雏形：

```text
compile_loop.py 可以把 intent 编译成 proposed_loop
```

下一步应该做的是：

```text
v0.7 guarded write mode
```

也就是在明确 HumanGate 后，让系统真的把 proposal 写入 `.loop/`。

---

## 10. 下一步正确方向

不要继续无限增加只读 CLI。

下一步应该从“只读编译器”进入“受控写入器”：

```text
compile_loop.py --intent intent.md --json
→ 生成 proposed_loop
→ validate proposal
→ HumanGate / explicit --write
→ 写入 .loop/TARGET.md 等文件
→ check_loop.py 验证
→ run_loop.py briefing
→ plan_next.py checklist
```

这一步完成后，系统会明显更接近你的目标：

```text
人给整体意图和边界
AI 编译和写入 loop
Agent 执行细节
Verifier 监督
人只在关键门介入
```

---

## 11. 最终回答

你的理解不是错的。

更准确地说：

> 你理解的是最终目标；我最近一步步推进的是在补这个目标所需的控制系统。

真正的问题不是你没设置，也不是 Hermes 没调整，而是：

```text
从“理念上应该自动”
到“工程上可以可靠自动”
中间必须有 Contract / Loop / Verifier / StopGate / HumanGate 这些控制件。
```

现在 `-xunhuan` 已经有了 read-only compiler stack。下一步应该进入 guarded writer，让 AI 不只是提出 loop，而是在明确授权下写入 loop 文件，并自动验证。
