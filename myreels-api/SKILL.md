---
name: myreels-api
description: MyReels.ai 平台的外部开发者 API 集成指南。当用户需要调用 myreels.ai API 进行 AI 图像/视频/语音/音乐生成时触发。包含认证方式、任务提交与查询流程、模型列表与参数、多语言代码示例（JavaScript/Python/cURL）和错误处理。
---

# MyReels API 集成指南

## 前提条件

- 需要有效的订阅（API 仅对订阅用户开放）
- 在 [myreels.ai/developer](https://myreels.ai/developer) 开发者中心创建 AccessToken
- 平台不提供生成结果转存服务，结果 URL 需自行保存

## 认证

token 放在请求 body 中（不是 Header）：

```json
{
  "token": "YOUR_ACCESS_TOKEN",
  "userInput": { ... }
}
```

AccessToken 在开发者中心创建后仅展示一次，请妥善保存。

## 核心流程

### 1. 提交任务

```
POST https://api.myreels.ai/generation/build/:modelName
Content-Type: application/json
```

`:modelName` 为模型的 slug，在开发者中心模型列表中查看（如 `pr-376ebd94`）。

请求体：
```json
{
  "token": "YOUR_ACCESS_TOKEN",
  "userInput": {
    "prompt": "A cinematic portrait with soft studio lighting"
  }
}
```

响应：
```json
{
  "code": 0,
  "status": "queued",
  "data": { "taskID": "task_xxx" }
}
```

### 2. 查询任务状态

```
POST https://api.myreels.ai/generation/task/:taskID
Content-Type: application/json
```

请求体：
```json
{ "token": "YOUR_ACCESS_TOKEN" }
```

响应（完成时）：
```json
{
  "code": 0,
  "status": "ok",
  "data": {
    "status": "completed",
    "progress": 100,
    "artifacts": ["https://cdn.example.com/result.png"]
  }
}
```

任务状态流转：`queued` → `processing` → `completed` / `failed`

限流：60次/分钟，超出返回 429。

## 模型分类

| 类别 | 标签 | 说明 |
|------|------|------|
| 图像 | t2i / i2i | 文生图、图生图 |
| 视频 | t2v | 文生视频 |
| 语音 | t2a | 文本转语音 |

具体模型 slug、输入参数、费用见 [references/models.md](references/models.md)

## 代码示例

详见 [references/code-examples.md](references/code-examples.md)

## 模型列表与参数

详见 [references/models.md](references/models.md)

## 错误处理

详见 [references/errors.md](references/errors.md)
