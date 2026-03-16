# 代码示例

## npm 包（推荐）

```bash
npm install @myreels/skills
```

```typescript
import { MyReelsSkills } from '@myreels/skills';

const client = new MyReelsSkills({
  apiKey: 'YOUR_ACCESS_TOKEN',
});

// 提交任务并等待完成
const result = await client.runTask({
  slug: 'pr-376ebd94',
  taskType: 'image',
  title: 'My first task',
  userInput: {
    prompt: 'A cinematic portrait with soft studio lighting',
  },
});

console.log(result.result?.artifacts);
```

## JavaScript / TypeScript（直接调用）

```typescript
const TOKEN = 'YOUR_ACCESS_TOKEN';
const MODEL = 'pr-376ebd94'; // 在开发者中心查看模型 slug

// 1. 提交任务
const submitRes = await fetch(`https://api.myreels.ai/generation/build/${MODEL}`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    token: TOKEN,
    userInput: { prompt: 'A cinematic portrait with soft studio lighting' },
  }),
});
const { data: { taskID } } = await submitRes.json();

// 2. 轮询任务状态（建议间隔 3-5 秒）
async function pollTask(taskID: string) {
  while (true) {
    const res = await fetch(`https://api.myreels.ai/generation/task/${taskID}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ token: TOKEN }),
    });
    const { data } = await res.json();
    if (data.status === 'completed') return data;
    if (data.status === 'failed') throw new Error('Task failed');
    await new Promise(r => setTimeout(r, 3000));
  }
}

const result = await pollTask(taskID);
console.log(result.artifacts);
```

## Python

```python
import requests, time

TOKEN = "YOUR_ACCESS_TOKEN"
MODEL = "pr-376ebd94"  # 在开发者中心查看模型 slug

# 1. 提交任务
resp = requests.post(
    f"https://api.myreels.ai/generation/build/{MODEL}",
    json={"token": TOKEN, "userInput": {"prompt": "A cinematic portrait"}},
)
task_id = resp.json()["data"]["taskID"]

# 2. 轮询任务状态
while True:
    r = requests.post(
        f"https://api.myreels.ai/generation/task/{task_id}",
        json={"token": TOKEN},
    )
    data = r.json().get("data", {})
    if data.get("status") == "completed":
        print(data["artifacts"])
        break
    elif data.get("status") == "failed":
        raise Exception("Task failed")
    time.sleep(3)
```

## cURL

```bash
# 1. 提交任务
curl -X POST "https://api.myreels.ai/generation/build/pr-376ebd94" \
  -H "Content-Type: application/json" \
  -d '{"token": "YOUR_ACCESS_TOKEN", "userInput": {"prompt": "A cinematic portrait"}}'

# 2. 查询任务状态
curl -X POST "https://api.myreels.ai/generation/task/TASK_ID" \
  -H "Content-Type: application/json" \
  -d '{"token": "YOUR_ACCESS_TOKEN"}'
```

## 环境变量配置

```bash
# .env
MYREELS_API_KEY=your_access_token_here
```
