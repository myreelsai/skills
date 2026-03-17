# 代码示例

## npm 包（推荐）

```bash
npm install @myreels/skills
```

```typescript
import { MyReelsSkills } from '@myreels/skills';

const client = new MyReelsSkills({
  accessToken: 'YOUR_ACCESS_TOKEN',
});

// 提交任务并等待完成
const result = await client.runTask({
  modelName: 'nano-banana2',
  taskType: 'image',
  title: 'My first task',
  input: {
    prompt: 'A cinematic portrait with soft studio lighting',
  },
});

console.log(result.result?.resultUrls);
```

## JavaScript / TypeScript（直接调用）

```typescript
const TOKEN = 'YOUR_ACCESS_TOKEN';
const MODEL = 'nano-banana2'; // 在开发者中心查看模型 modelName

// 1. 提交任务
const submitRes = await fetch(`https://api.myreels.ai/generation/${MODEL}`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${TOKEN}`,
  },
  body: JSON.stringify({
    prompt: 'A cinematic portrait with soft studio lighting',
  }),
});
const { data: { taskID } } = await submitRes.json();

// 2. 轮询任务状态（建议间隔 3-5 秒）
async function pollTask(taskID: string) {
  while (true) {
    const res = await fetch(`https://api.myreels.ai/query/task/${taskID}`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${TOKEN}`,
      },
    });
    const payload = await res.json();
    if (!res.ok) {
      throw new Error(payload.message || `Query failed: HTTP ${res.status}`);
    }
    if (payload.status !== 'ok') {
      throw new Error(payload.message || 'Query failed');
    }
    const { data } = payload;
    if (data.status === 'completed') return data;
    if (data.status === 'failed') throw new Error('Task failed');
    await new Promise(r => setTimeout(r, 3000));
  }
}

const result = await pollTask(taskID);
console.log(result.resultUrls);
```

## Python

```python
import requests, time

TOKEN = "YOUR_ACCESS_TOKEN"
MODEL = "nano-banana2"  # 在开发者中心查看模型 modelName

# 1. 提交任务
resp = requests.post(
    f"https://api.myreels.ai/generation/{MODEL}",
    headers={"Authorization": f"Bearer {TOKEN}"},
    json={"prompt": "A cinematic portrait"},
)
task_id = resp.json()["data"]["taskID"]

# 2. 轮询任务状态
while True:
    r = requests.get(
        f"https://api.myreels.ai/query/task/{task_id}",
        headers={"Authorization": f"Bearer {TOKEN}"},
    )
    payload = r.json()
    if not r.ok:
        raise Exception(payload.get("message") or f"Query failed: HTTP {r.status_code}")
    if payload.get("status") != "ok":
        raise Exception(payload.get("message") or "Query failed")
    data = payload.get("data", {})
    if data.get("status") == "completed":
        print(data["resultUrls"])
        break
    elif data.get("status") == "failed":
        raise Exception("Task failed")
    time.sleep(3)
```

## cURL

```bash
# 1. 提交任务
curl -X POST "https://api.myreels.ai/generation/nano-banana2" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A cinematic portrait"}'

# 2. 查询任务状态
curl -X GET "https://api.myreels.ai/query/task/TASK_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 环境变量配置

```bash
# .env
MYREELS_ACCESS_TOKEN=your_access_token_here
```
