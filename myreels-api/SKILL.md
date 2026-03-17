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

使用请求头：

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

AccessToken 在开发者中心创建后仅展示一次，请妥善保存。

## 核心流程

### 1. 提交任务

```
POST https://api.myreels.ai/generation/:modelName
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN
```

`:modelName` 为模型的 `modelName`，不是 slug，例如 `nano-banana2`、`veo3.1-pro`。

请求体：
```json
{
  "prompt": "A cinematic portrait with soft studio lighting"
}
```

响应：
```json
{
  "status": "ok",
  "message": "Successfully created task",
  "data": { "taskID": "task_xxx" }
}
```

### 2. 查询任务状态

```
GET https://api.myreels.ai/query/task/:taskID
Authorization: Bearer YOUR_ACCESS_TOKEN
```

响应（完成时）：
```json
{
  "status": "ok",
  "message": "Successfully obtained task info",
  "data": {
    "status": "completed",
    "progress": 100,
    "resultUrls": [{ "url": "https://cdn.example.com/result.png" }]
  }
}
```

任务状态流转：`pending` → `processing` → `completed` / `failed`

限流：60次/分钟，超出返回 429。

## 返回规则

- 先看 HTTP Status，非 `2xx` 视为接口失败
- HTTP Status 为 `2xx` 时，再看响应体中的 `status`
- 查询任务时，`status = ok` 后再看 `data.status`
- 当前公开入口仅包括：
  - `POST /generation/:modelName`
  - `GET /query/task/:taskID`
  - `GET|POST /api/v1/*`

## 模型分类

| 类别 | 标签 | 说明 |
|------|------|------|
| 图像 | t2i / i2i | 文生图、图生图 |
| 视频 | t2v | 文生视频 |
| 语音 | t2a | 文本转语音 |

具体模型 `modelName`、输入参数、费用见 [references/models.md](references/models.md)

## 代码示例

详见 [references/code-examples.md](references/code-examples.md)

## 模型列表与参数

详见 [references/models.md](references/models.md)

## 错误处理

详见 [references/errors.md](references/errors.md)
