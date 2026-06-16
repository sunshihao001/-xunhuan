# Xunhuan Agent OS / 循环代理操作系统

> 一个面向个人与项目级 AI 工作流的初步循环代理操作系统：把模糊目标编译成有边界、有路径、有验证、有状态、有停止门、有交还点的 Agent Loop。

## 这是什么

`-xunhuan` 不是一个单独 prompt，也不是单个 AI Agent。它的产品方向是：

```text
AI Workflow OS / Loop Engineering OS
```

它把当前分散的 AI 工作流部件组织成一条主线：

```text
目标进入
→ 编译闭环
→ 生成单轮任务
→ Agent 执行
→ Verifier 验证
→ 状态更新
→ 决定继续/停止/交还
→ 沉淀认知
```

## 当前认知定位

当前 AI 工作流还不是完全成熟统一的整体产品，而是处在：

```text
部件已经基本齐全，但整体操作系统仍在形成
```

成熟的部件包括：Prompt、Agent、Tools、Memory、Context Files、Verifier、Hooks、Subagents、CI、Scheduler、State、Human Gate。

本仓库要做的是把这些部件组织为一个可复用的循环代理操作系统。

## 核心结论

需求拷问端不是废掉，而是升级：

```text
Demand Interrogation
→ Loop Brief Compiler
→ Bounded WORK_ORDER Generator
→ Verifier Gate
→ State / Stop / Handoff Manager
```

也就是：

> 需求拷问端不再是每一步都问人的聊天澄清器，而是把目标编译成可执行、可验证、可停止、可交还的 Agent Loop。

## Hermes + Codex 分工

```text
User    = Goal Owner + HumanGate Approver
Hermes  = Loop Designer + Verifier + Knowledge Manager
Codex   = Bounded Executor
Files   = State / Contract / Evidence
```

## 仓库结构

```text
00_CONCEPT/        理论主线与认知方向
01_PROTOCOL/       Loop 协议、停止门、工作单、验证协议
02_TEMPLATES/      .loop 文件模板
03_RUNNERS/        Codex / Hermes 执行分工
04_VERIFIERS/      验证器与失败分支设计
05_WORKFLOWS/      可复用工作流
06_KNOWLEDGE_BASE/ 认知更新、案例、失败模式
07_TRIALS/         试点记录与证据
```

## 最小运行协议

复杂任务先生成 `.loop/`：

```text
.loop/TARGET.md
.loop/PATH.md
.loop/ACCEPTANCE.md
.loop/STATE.md
.loop/LOOP_LOG.md
.loop/STOP_GATE.md
.loop/HANDOFF.md
.loop/WORK_ORDER.md
```

然后执行：

```text
Hermes 编译 Loop
→ Codex 执行一个 WORK_ORDER
→ Hermes 验证证据
→ 更新 STATE/LOOP_LOG
→ Continue / Done / DoneWithRisk / Blocked / HumanGate
```

## 当前版本

当前仓库保存的是 **v0.6 初步循环代理操作系统**：

- 已完成理论主线整理
- 已完成 Loop 协议初版
- 已完成 Hermes + Codex bounded loop 试点
- 已沉淀模板与验证规则
- 已提供最小可运行 Loop 初始化器：`scripts/init_loop.py`
- 已提供最小可运行 Loop 结构检查器：`scripts/check_loop.py`
- 已提供只读 Loop Bootstrap Runner：`scripts/run_loop.py`
- 已提供只读 Work Order Plan Compiler：`scripts/plan_next.py`
- 已提供只读高层 Intent Compiler：`scripts/compile_loop.py`

下一步：把这些只读编译器升级为更完整的 guarded writer/runner 工具，但仍然要保留 HumanGate。

## Init Loop CLI

Create the standard `.loop/` files in another project:

```bash
python scripts/init_loop.py --name demo --dir <target-dir>
```

Use `--dry-run` to preview writes and `--force` to overwrite existing `.loop` files. See [Init Loop CLI](docs/INIT_LOOP.md) for examples.

## Check Loop CLI

Verify that a target project has a structurally complete `.loop/` workspace:

```bash
python scripts/check_loop.py --dir <target-dir>
```

Use `--json` when another tool needs machine-readable readiness results. See [Check Loop CLI](docs/CHECK_LOOP.md) for examples.

## Run Loop CLI

Render a read-only bootstrap briefing for the current `.loop/` state:

```bash
python scripts/run_loop.py --dir <target-dir>
```

This command checks readiness, reports `status` / `round` / `next_action`, and points to the current `WORK_ORDER.md`. It does not execute agents or mutate files. See [Run Loop CLI](docs/RUN_LOOP.md) for examples.

## Plan Next CLI

Compile the current `WORK_ORDER.md` into a read-only execution and verifier checklist:

```bash
python scripts/plan_next.py --dir <target-dir>
```

Use `--json` when another tool or agent needs structured plan data. It does not execute agents, commands, or mutate files. See [Plan Next CLI](docs/PLAN_NEXT.md) for examples.

## Compile Loop CLI

Compile a high-level intent brief into a proposed loop package without writing files:

```bash
python scripts/compile_loop.py --intent <intent-file>
```

Use `--json` when another tool needs structured proposal data. It does not write files or execute agents. See [Compile Loop CLI](docs/COMPILE_LOOP.md) for examples.
