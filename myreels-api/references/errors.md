# Error Handling

[English](#english) | [日本語](#日本語)

## English

### Task Submission Status Codes

| Status | Meaning |
|--------|------|
| 200 | Task created successfully |
| 400 | Empty body, invalid field format, or missing required parameters |
| 401 | Missing Authorization header, or invalid / expired token |
| 402 | Insufficient points |
| 403 | Model requires extra permission or subscription |
| 404 | `modelName` not found |
| 500 | Server-side processing error |
| 507 | Insufficient storage |

### Task Query Status Codes

| Status | Meaning |
|--------|------|
| 200 | Query succeeded |
| 400 | Invalid task ID format or invalid request |
| 401 | Missing Authorization header, or invalid / expired token |
| 404 | Task not found, or not accessible for the current user |
| 429 | Query rate too high |
| 500 | Server-side processing error |

### Response Evaluation Order

- If the upstream response includes `code`, Worker uses it as the final HTTP status.
- Otherwise Worker falls back to the upstream HTTP status.
- Check the final HTTP status first.
- If the HTTP status is `2xx`, then inspect the response body `status`.
- `status === "ok"` means success.
- `status === "failed"` means failure.

Example:

```json
{ "status": "failed", "message": "Missing required header: Authorization" }
```

### Error Handling Example

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

### Rate Limit Guidance

- query endpoint limit: 60 requests per minute
- image generation / image editing polling: 10 seconds
- video generation polling: 30 seconds to 1 minute
- if you receive `429`, back off and retry later

### Cost Display Guidance

- use `serviceConfig.estimatedPrice` only as the raw source
- final user-facing display should be `ceil(estimatedPrice * 100)` points
- example: `0.0872` -> `9 points`

### Public Path Scope

Public paths:

- `POST /generation/:modelName`
- `GET /query/task/:taskID`
- `GET|POST /api/v1/*`

Other paths may return:

```json
{ "status": "failed", "message": "Path not allowed" }
```

## 日本語

### タスク送信のステータスコード

| Status | Meaning |
|--------|------|
| 200 | タスク作成成功 |
| 400 | 空の body、無効なフィールド形式、または必須パラメータ不足 |
| 401 | Authorization ヘッダー欠落、またはトークン無効 / 期限切れ |
| 402 | ポイント不足 |
| 403 | 追加権限またはサブスクリプションが必要 |
| 404 | `modelName` が存在しない |
| 500 | サーバー処理エラー |
| 507 | ストレージ不足 |

### タスク照会のステータスコード

| Status | Meaning |
|--------|------|
| 200 | 照会成功 |
| 400 | task ID 形式不正またはリクエスト不正 |
| 401 | Authorization ヘッダー欠落、またはトークン無効 / 期限切れ |
| 404 | タスクが存在しない、または現在のユーザーが参照不可 |
| 429 | 照会頻度が高すぎる |
| 500 | サーバー処理エラー |

### レスポンス判定順

- 上流レスポンスに `code` があれば、それが最終 HTTP ステータスになります。
- ない場合は上流 HTTP ステータスにフォールバックします。
- まず最終 HTTP ステータスを確認してください。
- HTTP ステータスが `2xx` の場合に body の `status` を確認してください。
- `status === "ok"` は成功です。
- `status === "failed"` は失敗です。

例:

```json
{ "status": "failed", "message": "Missing required header: Authorization" }
```

### エラーハンドリング例

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

### レート制限の指針

- 照会エンドポイント上限: 1 分あたり 60 回
- 画像生成 / 画像編集のポーリング: 10 秒
- 動画生成のポーリング: 30 秒から 1 分
- `429` を受けた場合は待ってから再試行してください

### コスト表示指針

- `serviceConfig.estimatedPrice` は元データとしてのみ使ってください
- 最終表示は `ceil(estimatedPrice * 100)` points にしてください
- 例: `0.0872` -> `9 points`

### 公開パス範囲

公開パス:

- `POST /generation/:modelName`
- `GET /query/task/:taskID`
- `GET|POST /api/v1/*`

それ以外のパスでは次のようなレスポンスになる場合があります。

```json
{ "status": "failed", "message": "Path not allowed" }
```
