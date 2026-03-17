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

当前应以响应体 `code` 字段为准：

- `code === 200`：成功
- `code !== 200`：异常

```json
{ "code": 401, "status": "failed", "message": "Missing required header: Authorization" }
```

## 错误处理示例

```typescript
const res = await fetch(`https://api.myreels.ai/generation/build/${modelName}`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${ACCESS_TOKEN}`,
  },
  body: JSON.stringify(userInput),
});

const data = await res.json();
if (data.code === 401) throw new Error('Invalid AccessToken');
if (data.code === 402) throw new Error('Insufficient points');
if (data.code === 403) throw new Error('Subscription or permission required');
if (data.code !== 200) throw new Error(data.message || 'Task submission failed');
```

## 限流说明

- 查询接口限制：60次/分钟
- 推荐轮询间隔：3-5 秒
- 超出限制后按 429 退避重试
