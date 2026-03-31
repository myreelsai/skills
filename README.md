# MyReels Skills

[English](#english) | [日本語](#日本語)

## English

This repository provides public skills for `myreels.ai` users who want to use MyReels generation capabilities inside AI agents that support skills.

### What This Repository Includes

The current public skill is:

#### `myreels-api`

This skill is an executable API skill for the MyReels public API. It now includes bundled shell scripts plus fallback reference docs. It covers:

- environment checks
- live model discovery
- task submission
- task list queries
- task status polling
- result retrieval guidance
- authentication
- parameter references
- error handling guidance

Bundled scripts:

- `myreels-doctor.sh`
- `myreels-models.sh`
- `myreels-generate.sh`
- `myreels-tasks-list.sh`
- `myreels-task-get.sh`

Related documents:

- [myreels-api/SKILL.md](./myreels-api/SKILL.md)
- [myreels-api/references/models.md](./myreels-api/references/models.md)
- [myreels-api/references/code-examples.md](./myreels-api/references/code-examples.md)
- [myreels-api/references/errors.md](./myreels-api/references/errors.md)

### Installation

Install from GitHub:

```bash
npx skills add https://github.com/myreelsai/skills --skill myreels-api -g
```

Remove `-g` for a project-level install.

Install from ClawHub:

```bash
npx clawhub install myreels-api
```

### Supported Capabilities

The skill currently covers:

- image generation and editing: `t2i` / `i2i` / `i2e`
- video generation: `t2v` / `i2v`
- speech and music generation: `t2a` / `m2a`

For the latest `modelName` list, parameter schema, defaults, options, and field descriptions, use:

- `GET https://api.myreels.ai/api/v1/models/api`

This endpoint was verified on March 18, 2026 and currently does not require `Authorization`.

Point display rule:

- use `estimatedCost` as the user-facing points field

### Recommended Usage Flow

1. Run `scripts/myreels-models.sh --summary` to load the live model schema.
2. Choose a model by `modelName`, tags, and parameter definitions.
3. If you need existing task history, use `scripts/myreels-tasks-list.sh`.
4. Submit a task with `scripts/myreels-generate.sh`.
5. Save the returned `taskID`.
6. Poll with `scripts/myreels-task-get.sh`.
7. Read and persist the final result URLs after completion.

Recommended polling intervals:

- image generation / image editing: 10 seconds
- video generation: 30 seconds to 1 minute

### Security Notes

- Do not expose your AccessToken in public repositories, screenshots, or chat logs.
- Store your AccessToken only in your own secure environment.
- Save and manage result URLs on your side.

## 日本語

このリポジトリは、`myreels.ai` のユーザー向けに公開されている skill を提供します。skill に対応した AI agent 内で、MyReels の生成機能を利用しやすくするためのものです。

### 含まれているもの

現在公開されている skill は次のとおりです。

#### `myreels-api`

この skill は MyReels Public API を実行しやすくするための executable skill です。shell script と参照ドキュメントを同梱しています。主に次の内容を含みます。

- 環境チェック
- ライブモデル取得
- タスク送信
- タスクリスト取得
- タスク状態のポーリング
- 結果取得の指針
- 認証
- パラメータ参照
- エラーハンドリング指針

同梱スクリプト:

- `myreels-doctor.sh`
- `myreels-models.sh`
- `myreels-generate.sh`
- `myreels-tasks-list.sh`
- `myreels-task-get.sh`

関連ドキュメント:

- [myreels-api/SKILL.md](./myreels-api/SKILL.md)
- [myreels-api/references/models.md](./myreels-api/references/models.md)
- [myreels-api/references/code-examples.md](./myreels-api/references/code-examples.md)
- [myreels-api/references/errors.md](./myreels-api/references/errors.md)

### インストール

GitHub からインストール:

```bash
npx skills add https://github.com/myreelsai/skills --skill myreels-api -g
```

プロジェクト単位で入れたい場合は `-g` を外してください。

ClawHub からインストール:

```bash
npx clawhub install myreels-api
```

### 対応機能

現在の skill は次のタイプを扱います。

- 画像生成・編集: `t2i` / `i2i` / `i2e`
- 動画生成: `t2v` / `i2v`
- 音声・音楽生成: `t2a` / `m2a`

最新の `modelName` 一覧、パラメータ定義、デフォルト値、選択肢、フィールド説明は次のエンドポイントを利用してください。

- `GET https://api.myreels.ai/api/v1/models/api`

このエンドポイントは 2026-03-18 時点で `Authorization` なしでも取得できることを確認しています。

ポイント表示ルール:

- ユーザー向け points 表示には `estimatedCost` を使用

### 推奨フロー

1. `scripts/myreels-models.sh --summary` を実行して最新のモデル定義を取得します。
2. `modelName`、タグ、パラメータ定義を見てモデルを選びます。
3. 既存タスク履歴が必要なら `scripts/myreels-tasks-list.sh` を使います。
4. `scripts/myreels-generate.sh` でタスクを送信します。
5. 返却された `taskID` を保存します。
6. `scripts/myreels-task-get.sh` をポーリングします。
7. 完了後に結果 URL を読み取り、自分側でも保存します。

推奨ポーリング間隔:

- 画像生成 / 画像編集: 10 秒
- 動画生成: 30 秒から 1 分

### セキュリティ注意事項

- AccessToken を公開リポジトリ、スクリーンショット、チャットログに載せないでください。
- AccessToken は自分の安全な環境だけに保存してください。
- 結果 URL は自分側で保存・管理してください。
