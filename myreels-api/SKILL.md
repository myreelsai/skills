---
name: myreels-api
description: Practical integration guide for the MyReels API. Use the live `GET /api/v1/models/api` endpoint to discover available models, parameters, defaults, options, and field descriptions before submitting generation tasks.
---

# MyReels API Integration Guide

[English](#english) | [日本語](#日本語)

## English

### Prerequisites

- An active subscription is required for generation and task query endpoints.
- Create an AccessToken in [myreels.ai/developer](https://myreels.ai/developer).
- Result URLs are not stored for you permanently. Save them on your side.
- `GET https://api.myreels.ai/api/v1/models/api` was verified on March 18, 2026 and currently does not require `Authorization`.

### Installation

```bash
npx skills add https://github.com/myreelsai/skills --skill myreels-api -g
```

Remove `-g` for a project-level install.

### Authentication

Use:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Recommended Flow

#### 0. Load live model metadata first

Before mapping user intent to request fields, call:

```http
GET https://api.myreels.ai/api/v1/models/api
```

Prioritize these fields:

- `modelName`
- `name`
- `tags`
- `description`
- `serviceConfig.estimatedPrice`
- computed display points: `ceil(serviceConfig.estimatedPrice * 100)`
- `displayConfig.estimatedTime`
- `userInputSchema`
- `userInputSchema.<param>.label`
- `userInputSchema.<param>.description`
- `userInputSchema.<param>.default`
- `userInputSchema.<param>.options`

Display cost as points instead of dollars:

- formula: `ceil(estimatedPrice * 100)`
- example: `0.0872` -> `9 points`

For natural-language requests such as "stronger motion", "disable prompt extension", or "higher human fidelity", map user intent from `label` and `description`, not from field names alone.

#### 1. Submit a task

```http
POST https://api.myreels.ai/generation/:modelName
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN
```

`:modelName` must be the actual `modelName`, not the slug.

Example:

```json
{
  "prompt": "A cinematic portrait with soft studio lighting"
}
```

Example success response:

```json
{
  "status": "ok",
  "message": "Successfully created task",
  "data": { "taskID": "task_xxx" }
}
```

#### 2. Query task status

```http
GET https://api.myreels.ai/query/task/:taskID
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Example completed response:

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

Task states:

- `pending`
- `processing`
- `completed`
- `failed`

Polling guidance:

- image generation / image editing: 10 seconds
- video generation: 30 seconds to 1 minute

Query rate limit:

- 60 requests per minute

### Response Rules

- If the upstream response includes `code`, Worker uses it as the final HTTP status.
- If upstream does not include `code`, Worker falls back to the upstream HTTP status.
- Check the final HTTP status first.
- If the HTTP status is `2xx`, then inspect `status`.
- For task queries, check `data.status` after `status === "ok"`.

Public paths:

- `POST /generation/:modelName`
- `GET /query/task/:taskID`
- `GET|POST /api/v1/*`

### Model Categories

| Category | Tags | Description |
|------|------|------|
| Image and editing | `t2i` / `i2i` / `i2e` | text-to-image, image-to-image, image editing |
| Video | `t2v` / `i2v` | text-to-video, image-to-video, avatar/video motion |
| Speech and music | `t2a` / `m2a` | text-to-speech, music generation |

Use the live schema described in [references/models.md](references/models.md) for current models, parameters, defaults, options, and field descriptions.

### References

- [references/models.md](references/models.md)
- [references/code-examples.md](references/code-examples.md)
- [references/errors.md](references/errors.md)

## 日本語

### 前提条件

- 生成およびタスク照会エンドポイントには有効なサブスクリプションが必要です。
- [myreels.ai/developer](https://myreels.ai/developer) で AccessToken を作成してください。
- 結果 URL は恒久保存されません。自分側で保存してください。
- `GET https://api.myreels.ai/api/v1/models/api` は 2026-03-18 時点で `Authorization` なしでも取得できることを確認しています。

### インストール

```bash
npx skills add https://github.com/myreelsai/skills --skill myreels-api -g
```

プロジェクト単位の場合は `-g` を外してください。

### 認証

次のヘッダーを使用します。

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### 推奨フロー

#### 0. 先に最新のモデル情報を取得する

ユーザーの意図をどのパラメータに割り当てるか判断する前に、次を呼び出してください。

```http
GET https://api.myreels.ai/api/v1/models/api
```

特に重視すべきフィールド:

- `modelName`
- `name`
- `tags`
- `description`
- `serviceConfig.estimatedPrice`
- 表示用ポイント: `ceil(serviceConfig.estimatedPrice * 100)`
- `displayConfig.estimatedTime`
- `userInputSchema`
- `userInputSchema.<param>.label`
- `userInputSchema.<param>.description`
- `userInputSchema.<param>.default`
- `userInputSchema.<param>.options`

コストはドルではなくポイント表示にしてください。

- ルール: `ceil(estimatedPrice * 100)`
- 例: `0.0872` -> `9 points`

「動きをもっと大きく」「prompt extension を無効にしたい」「人物 fidelity を上げたい」といった自然言語要求は、フィールド名だけでなく `label` と `description` を読んで対応付けてください。

#### 1. タスク送信

```http
POST https://api.myreels.ai/generation/:modelName
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN
```

`:modelName` には slug ではなく実際の `modelName` を使います。

例:

```json
{
  "prompt": "A cinematic portrait with soft studio lighting"
}
```

成功レスポンス例:

```json
{
  "status": "ok",
  "message": "Successfully created task",
  "data": { "taskID": "task_xxx" }
}
```

#### 2. タスク状態照会

```http
GET https://api.myreels.ai/query/task/:taskID
Authorization: Bearer YOUR_ACCESS_TOKEN
```

完了時レスポンス例:

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

タスク状態:

- `pending`
- `processing`
- `completed`
- `failed`

推奨ポーリング間隔:

- 画像生成 / 画像編集: 10 秒
- 動画生成: 30 秒から 1 分

照会レート制限:

- 1 分あたり 60 回

### レスポンス判定ルール

- 上流レスポンスに `code` があれば、それが最終 HTTP ステータスになります。
- 上流に `code` がなければ、上流 HTTP ステータスを使います。
- まず最終 HTTP ステータスを確認してください。
- HTTP ステータスが `2xx` の場合に `status` を確認してください。
- タスク照会では `status === "ok"` の後に `data.status` を確認してください。

公開パス:

- `POST /generation/:modelName`
- `GET /query/task/:taskID`
- `GET|POST /api/v1/*`

### モデルカテゴリ

| Category | Tags | Description |
|------|------|------|
| Image and editing | `t2i` / `i2i` / `i2e` | text-to-image, image-to-image, image editing |
| Video | `t2v` / `i2v` | text-to-video, image-to-video, avatar/video motion |
| Speech and music | `t2a` / `m2a` | text-to-speech, music generation |

最新のモデル、パラメータ、デフォルト値、選択肢、フィールド説明は [references/models.md](references/models.md) にあるライブスキーマの説明を優先してください。

### 参照

- [references/models.md](references/models.md)
- [references/code-examples.md](references/code-examples.md)
- [references/errors.md](references/errors.md)
