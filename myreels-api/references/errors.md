# 错误处理

## 提交任务接口错误码

| 状态码 | 说明 |
|--------|------|
| 200 | 任务创建成功，返回任务 ID 及初始状态 |
| 400 | 请求参数不完整或字段格式不正确 |
| 401 | AccessToken 无效或未传入 Authorization |
| 403 | 当前模型需要额外权限或订阅 |
| 404 | 指定的 modelName 不存在 |
| 429 | 请求过于频繁，触发限流 |
| 500 | 服务端处理异常 |

## 查询任务接口错误码

| 状态码 | 说明 |
|--------|------|
| 200 | 查询成功，返回任务状态及结果数据 |
| 400 | TASK_ID 格式不正确 |
| 401 | AccessToken 无效或未传入 Authorization |
| 404 | 任务不存在，或当前用户无权访问 |
| 429 | 查询频率过高（60次/分钟），建议退避重试 |
| 500 | 服务端处理异常 |

## 业务错误

响应体 `code` 字段非 0 时表示业务错误：

```json
{ "code": 1, "status": "failed", "message": "Missing token" }
```

## 错误处理示例

```typescript
const res = await fetch(`https://api.myreels.ai/generation/${slug}`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ token: ACCESS_TOKEN, userInput }),
});

if (res.status === 401) throw new Error('Invalid AccessToken');
if (res.status === 403) throw new Error('Subscription required for this model');
if (res.status === 429) {
  await new Promise(r => setTimeout(r, 60000)); // 等待 60 秒后重试
}

const data = await res.json();
if (data.code !== 0) throw new Error(data.message || 'Task submission failed');
```

## 限流说明

- 查询接口限制：60次/分钟
- 推荐轮询间隔：3-5 秒
- 超出限制后等待 60 秒再重试
