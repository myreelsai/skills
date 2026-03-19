# Code Examples

### Install The Skill

```bash
npx skills add https://github.com/myreelsai/skills --skill myreels-api -g
```

Remove `-g` for a project-level install.

### Load Live Model Metadata

`GET https://api.myreels.ai/api/v1/models/api` was verified on March 18, 2026 and currently does not require `Authorization`.

#### JavaScript / TypeScript

```typescript
const res = await fetch('https://api.myreels.ai/api/v1/models/api');
if (!res.ok) throw new Error(`Load models failed: HTTP ${res.status}`);

const payload = await res.json();
const items = payload?.data?.items ?? [];

for (const item of items) {
  console.log(item.modelName, item.tags);
  console.log('displayPoints', item.estimatedCost);
  for (const [key, field] of Object.entries(item.userInputSchema ?? {})) {
    console.log(
      key,
      field.type,
      field.required,
      field.default ?? field.defaultValue,
      field.description
    );
  }
}
```

Display cost rule:

- use `estimatedCost` as the display points field

#### Python

```python
import requests

r = requests.get("https://api.myreels.ai/api/v1/models/api")
r.raise_for_status()
payload = r.json()

for item in payload.get("data", {}).get("items", []):
    print(item.get("modelName"), item.get("tags"))
    print("displayPoints", item.get("estimatedCost"))
    for key, field in (item.get("userInputSchema") or {}).items():
        print(
            key,
            field.get("type"),
            field.get("required"),
            field.get("default", field.get("defaultValue")),
            field.get("description"),
        )
```

### Submit And Poll A Task

#### JavaScript / TypeScript

```typescript
const TOKEN = 'YOUR_ACCESS_TOKEN';
const MODEL = 'nano-banana2';

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

async function pollTask(taskID: string, intervalMs = 10_000) {
  while (true) {
    const res = await fetch(`https://api.myreels.ai/query/task/${taskID}`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${TOKEN}`,
      },
    });

    const payload = await res.json();
    if (!res.ok) throw new Error(payload.message || `Query failed: HTTP ${res.status}`);
    if (payload.status !== 'ok') throw new Error(payload.message || 'Query failed');

    const { data } = payload;
    if (data.status === 'completed') return data;
    if (data.status === 'failed') throw new Error('Task failed');

    await new Promise(r => setTimeout(r, intervalMs));
  }
}

const result = await pollTask(taskID, 10_000);
console.log(result.resultUrls);
```

Polling guidance:

- image generation / image editing: 10 seconds
- video generation: 30 seconds to 1 minute

#### Python

```python
import requests
import time

TOKEN = "YOUR_ACCESS_TOKEN"
MODEL = "nano-banana2"

resp = requests.post(
    f"https://api.myreels.ai/generation/{MODEL}",
    headers={"Authorization": f"Bearer {TOKEN}"},
    json={"prompt": "A cinematic portrait"},
)
task_id = resp.json()["data"]["taskID"]

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
    if data.get("status") == "failed":
        raise Exception("Task failed")

    time.sleep(10)
```

#### cURL

```bash
curl -X POST "https://api.myreels.ai/generation/nano-banana2" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A cinematic portrait"}'

curl -X GET "https://api.myreels.ai/query/task/TASK_ID" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Environment Variable Example

```bash
MYREELS_ACCESS_TOKEN=your_access_token_here
```
