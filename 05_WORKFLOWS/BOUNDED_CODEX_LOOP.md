# Bounded Codex Loop Workflow

## 适用

- 小型实现
- 文档生成器
- 索引器
- issue 修复
- 可验证重构

## 流程

```text
1. Hermes 编译 .loop 文件
2. Hermes 写 Round N WORK_ORDER
3. Codex 执行一轮
4. Hermes verifier 重跑命令
5. Hermes 更新 STATE/LOOP_LOG
6. Continue / Done / Risk / Blocked / HumanGate
```

## 最多轮数

默认 3 轮：

- Round 1：实现核心能力
- Round 2：增强或补验证
- Round 3：只修 verifier 失败，不扩展范围
