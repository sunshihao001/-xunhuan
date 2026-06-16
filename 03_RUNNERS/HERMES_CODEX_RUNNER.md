# Hermes + Codex Runner

## 分工

```text
Hermes = Loop Designer + Verifier + Knowledge Manager
Codex  = Bounded Executor
```

## Hermes 负责

- 需求编译
- 目标/路径/验收/停止门设计
- 上下文组织
- WORK_ORDER 生成
- Verifier 检查
- STATE/LOOP_LOG/HANDOFF 更新
- 知识沉淀

## Codex 负责

- 读取 WORK_ORDER
- 执行一轮 bounded task
- 修改允许文件
- 运行要求命令
- 返回证据

## Codex 不负责

- 不扩大目标
- 不决定最终 Done
- 不自行引入高风险操作
- 不修改 forbidden paths
- 不用自我报告替代验证

## 调用示例

```bash
codex exec --sandbox danger-full-access "Read .loop/WORK_ORDER.md and execute exactly one bounded loop round. Do not modify forbidden files. Do not commit. Return the required completion report."
```
