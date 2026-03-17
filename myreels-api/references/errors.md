# 错误处理

## 提交任务接口错误码

| 状态码 | 说明 |
|--------|------|
| 200 | 任务创建成功，返回任务 ID |
| 400 | 请求体为空、字段格式错误或缺少必要参数 |
| 401 | 缺少 Authorization，或 Bearer token 无效/过期 |
| 402 | 点数不足 |
| 403 | 当前模型需要额外权限或订阅 |
| 404 | 指定的 modelName 不存在 |
| 500 | 服务端处理异常 |
| 507 | 存储空间不足 |

## 查询任务接口错误码

| 状态码 | 说明 |
|--------|------|
| 200 | 查询成功，返回任务状态及结果数据 |
| 400 | TASK_ID 格式不正确或请求参数错误 |
| 401 | 缺少 Authorization，或 Bearer token 无效/过期 |
| 404 | 任务不存在，或当前用户无权访问 |
| 429 | 查询频率过高（60次/分钟），建议退避重试 |
| 500 | 服务端处理异常 |

## 业务错误

当前应按以下顺序判断：

- Worker 会优先使用上游返回的 `code` 作为最终 HTTP Status
- 如果上游没有 `code`，则回退为上游原始 HTTP Status
- 先看 HTTP Status，非 `2xx` 视为接口异常
- HTTP Status 为 `2xx` 时，再看响应体 `status`
- `status === "ok"`：接口成功
- `status === "failed"`：接口失败

```json
{ "status": "failed", "message": "Missing required header: Authorization" }
```

## 错误处理示例

```typescript
const res = await fetch(`https://api.myreels.ai/generation/${modelName}`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${ACCESS_TOKEN}`,
  },
  body: JSON.stringify(userInput),
});

const data = await res.json();
if (res.status === 401) throw new Error('Invalid AccessToken');
if (res.status === 402) throw new Error('Insufficient points');
if (res.status === 403) throw new Error('Subscription or permission required');
if (!res.ok || data.status !== 'ok') throw new Error(data.message || 'Task submission failed');
```

## 限流说明

- 查询接口限制：60次/分钟
- 推荐轮询间隔：3-5 秒
- 超出限制后按 429 退避重试

## 路径限制

对外公开入口仅包括：

- `POST /generation/:modelName`
- `GET /query/task/:taskID`
- `GET|POST /api/v1/*`

其他路径会返回：

```json
{ "status": "failed", "message": "Path not allowed" }
```
