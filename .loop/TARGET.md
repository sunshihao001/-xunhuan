# TARGET — v0.2 Loop 初始化器

## Target

把 Xunhuan Agent OS 从“理论 + 协议 + 模板”推进到“可运行的最小工具”：提供 `scripts/init_loop.py`，用于在任意项目中初始化 `.loop/` 状态目录。

## Value

让 Xunhuan 不只保存工作流文档，而能实际启动一个 bounded-loop 工作区。

## Human Role

用户确认产品方向：v0.2 做最小 Loop 初始化器。

## Hermes Role

编译本轮 loop、生成 Codex WORK_ORDER、执行 verifier、更新状态、提交推送。

## Codex Role

实现脚本和必要文档，不扩大范围。

## Non-goals

- 不做复杂包发布。
- 不引入第三方依赖。
- 不实现完整 runner 调度器。
- 不接入真实 Codex 自动运行。
