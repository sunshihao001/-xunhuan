# Loop Engineering Theory

## 核心命题

Loop Engineering 的核心不是写更好的 prompt，而是设计一个能 prompt agent、检查 agent、更新状态并决定继续或停止的系统。

```text
Prompt Engineering: 怎么和 AI 说话
Loop Engineering: 怎么让 AI 在系统里持续工作
```

## 有界闭环

Loop 必须 bounded：

- 有目标
- 有路径
- 有最多轮数
- 有每轮检查
- 有状态文件
- 有停止条件
- 有人类交还点

## 适合 loop 化的任务

- CI/test failure repair
- 文档索引生成与检查
- 研究资料收集 → reading card → synthesis
- issue → patch → verify
- 知识库更新
- 低风险重复 QA

## 不适合自动 loop 的任务

- 产品方向决策
- 密钥/账号/生产数据
- 不可逆 Git/部署/数据库操作
- 技术栈替换
- 没有验收标准的大改
- 需要审美或战略判断的工作

这些必须进入 HumanGate。
