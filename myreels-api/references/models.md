# Live Model Metadata

[English](#english) | [日本語](#日本語)

## English

The single source of truth for available models, parameter definitions, defaults, options, and field descriptions is:

`GET https://api.myreels.ai/api/v1/models/api`

Verified on March 18, 2026:

- currently accessible without `Authorization`
- currently does not require `VITE_API_KEY`

If your runtime can access this endpoint, prefer the live response over any static model list.

### Cost Display Rule

Do not display raw dollar price as the final user-facing cost.

- source field: `serviceConfig.estimatedPrice`
- display rule: `ceil(estimatedPrice * 100)`
- display unit: `points`
- example: `0.0872` -> `9 points`

### Quick Request

```bash
curl -s "https://api.myreels.ai/api/v1/models/api"
```

### Minimal JavaScript Example

```typescript
const res = await fetch('https://api.myreels.ai/api/v1/models/api');
if (!res.ok) throw new Error(`Load models failed: HTTP ${res.status}`);

const payload = await res.json();
for (const item of payload?.data?.items ?? []) {
  const displayPoints = Math.ceil(Number(item.serviceConfig?.estimatedPrice ?? 0) * 100);
  console.log(item.modelName, item.name, item.tags, displayPoints, 'points');
}
```

### Minimal Python Example

```python
import math
import requests

r = requests.get("https://api.myreels.ai/api/v1/models/api")
r.raise_for_status()
for item in r.json().get("data", {}).get("items", []):
    price = float(item.get("serviceConfig", {}).get("estimatedPrice") or 0)
    display_points = math.ceil(price * 100)
    print(item.get("modelName"), item.get("name"), item.get("tags"), display_points, "points")
```

### Important Top-Level Fields

- `modelName`
  - the real identifier used in `POST /generation/:modelName`
- `name`
  - display name
- `tags`
  - capability tags such as `t2i`, `i2i`, `i2e`, `t2v`, `i2v`, `t2a`, `m2a`
- `description`
  - model-level description and usage notes
- `serviceConfig.estimatedPrice`
-  - raw price source used to compute points
- computed display points
  - `ceil(serviceConfig.estimatedPrice * 100)`
- `displayConfig.estimatedTime`
  - estimated generation time
- `estimatedPoints`
  - optional backend-provided points field; for public display use `ceil(estimatedPrice * 100)`
- `userInputSchema`
  - full parameter schema for this model

### How To Read `userInputSchema`

Each entry in `userInputSchema` is a request parameter. These fields matter most:

- `type`
- `label`
- `description`
- `required`
- `default` / `defaultValue`
- `options`
- `min` / `max` / `step`
- `placeholder`

When mapping natural-language instructions to parameters, prioritize `label` and `description`.

Example:

- user says: "stronger motion"
- live schema may show:
  - `strength.label = "Motion Strength"` or an equivalent localized label
  - `strength.description` explains that larger values increase motion freedom

Without the live description, agents can easily map the request incorrectly.

### Recommended Selection Flow

1. Call `GET /api/v1/models/api`.
2. Filter models by `tags`.
3. Inspect `name`, `description`, display points, and `estimatedTime`.
4. Read `userInputSchema`.
5. Build the request body from `label`, `description`, `default`, and `options`.

### Polling Guidance

- image generation / image editing: every 10 seconds
- video generation: every 30 seconds to 1 minute

### Fallback

If your runtime cannot access `api.myreels.ai`, use the rest of the local reference docs only as a fallback. When live access is available, the live schema should take priority.

## 日本語

利用可能なモデル、パラメータ定義、デフォルト値、選択肢、フィールド説明の唯一の正しい情報源は次です。

`GET https://api.myreels.ai/api/v1/models/api`

2026-03-18 時点で確認済み:

- 現在は `Authorization` なしで取得可能
- 現在は `VITE_API_KEY` 不要

実行環境からこのエンドポイントにアクセスできる場合は、静的なモデル一覧よりライブレスポンスを優先してください。

### コスト表示ルール

最終的なユーザー向けコスト表示に生のドル価格をそのまま使わないでください。

- 元フィールド: `serviceConfig.estimatedPrice`
- 表示ルール: `ceil(estimatedPrice * 100)`
- 表示単位: `points`
- 例: `0.0872` -> `9 points`

### 簡易リクエスト

```bash
curl -s "https://api.myreels.ai/api/v1/models/api"
```

### JavaScript 最小例

```typescript
const res = await fetch('https://api.myreels.ai/api/v1/models/api');
if (!res.ok) throw new Error(`Load models failed: HTTP ${res.status}`);

const payload = await res.json();
for (const item of payload?.data?.items ?? []) {
  const displayPoints = Math.ceil(Number(item.serviceConfig?.estimatedPrice ?? 0) * 100);
  console.log(item.modelName, item.name, item.tags, displayPoints, 'points');
}
```

### Python 最小例

```python
import math
import requests

r = requests.get("https://api.myreels.ai/api/v1/models/api")
r.raise_for_status()
for item in r.json().get("data", {}).get("items", []):
    price = float(item.get("serviceConfig", {}).get("estimatedPrice") or 0)
    display_points = math.ceil(price * 100)
    print(item.get("modelName"), item.get("name"), item.get("tags"), display_points, "points")
```

### 重要なトップレベルフィールド

- `modelName`
  - `POST /generation/:modelName` で使う実際の識別子
- `name`
  - 表示名
- `tags`
  - `t2i`、`i2i`、`i2e`、`t2v`、`i2v`、`t2a`、`m2a` などの能力タグ
- `description`
  - モデル説明や利用上の注意
- `serviceConfig.estimatedPrice`
-  - ポイント計算に使う元の価格
- 表示用ポイント
  - `ceil(serviceConfig.estimatedPrice * 100)`
- `displayConfig.estimatedTime`
  - 推定生成時間
- `estimatedPoints`
  - バックエンドが返す補助フィールド。公開表示では `ceil(estimatedPrice * 100)` を優先
- `userInputSchema`
  - そのモデルで使える全パラメータ定義

### `userInputSchema` の見方

`userInputSchema` の各エントリがリクエストパラメータです。特に重要なのは次です。

- `type`
- `label`
- `description`
- `required`
- `default` / `defaultValue`
- `options`
- `min` / `max` / `step`
- `placeholder`

自然言語の要求をパラメータに対応付けるときは、`label` と `description` を優先してください。

例:

- ユーザーが「動きをもっと大きく」と言う
- ライブスキーマで:
  - `strength.label`
  - `strength.description`
  を確認すれば、値を上げるべきパラメータだと判断しやすくなります

ライブ説明を読まないと、agent が誤って別のパラメータに割り当てる可能性があります。

### 推奨選択フロー

1. `GET /api/v1/models/api` を呼び出す
2. `tags` でモデルを絞り込む
3. `name`、`description`、表示用 points、`estimatedTime` を確認する
4. `userInputSchema` を読む
5. `label`、`description`、`default`、`options` を使ってリクエストを組み立てる

### ポーリング指針

- 画像生成 / 画像編集: 10 秒ごと
- 動画生成: 30 秒から 1 分ごと

### フォールバック

実行環境から `api.myreels.ai` にアクセスできない場合のみ、ローカルの reference 文書をフォールバックとして使ってください。ライブアクセス可能な場合は、ライブスキーマを優先してください。
