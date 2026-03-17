# MyReels Skills

[中文](#中文) | [日本語](#日本語) | [English](#english)

## 中文

这个仓库提供面向 `myreels.ai` 用户的 skills，目的是让你在支持 skill 的 AI agent 中，更方便地使用 MyReels 的生成能力。

如果你希望通过 AI 助手或自动化流程调用 MyReels API，这个仓库里的 skill 可以帮助你更快完成接入。

### 它能帮你做什么

当前仓库提供的 `myreels-api` skill 可以帮助你：

- 调用 MyReels 的图像、视频、语音生成接口
- 了解任务提交和结果查询的标准流程
- 查阅常用模型和输入参数
- 直接参考 JavaScript、TypeScript、Python、cURL 示例
- 处理常见错误和限流场景

### 适合谁使用

这个仓库适合以下用户：

- 已经在使用 `myreels.ai`
- 想把 MyReels 接入自己的 AI agent、脚本或工作流
- 需要快速查 API 用法，而不是从零摸索

### 当前包含的 Skill

#### `myreels-api`

这是一个 MyReels API 使用指南型 skill，主要覆盖：

- 认证方式
- 提交生成任务
- 查询任务状态
- 获取生成结果
- 模型参数说明
- 错误处理建议

相关文档：

- [myreels-api/SKILL.md](./myreels-api/SKILL.md)
- [myreels-api/references/models.md](./myreels-api/references/models.md)
- [myreels-api/references/code-examples.md](./myreels-api/references/code-examples.md)
- [myreels-api/references/errors.md](./myreels-api/references/errors.md)

### 安装

推荐使用 `npx skills add` 安装：

```bash
npx skills add https://github.com/myreelsai/skills --skill myreels-api -g
```

如果只想安装到当前项目，可去掉 `-g`。

### 支持的能力

当前文档覆盖以下类型：

- 图像生成：`t2i` / `i2i`
- 视频生成：`t2v`
- 语音生成：`t2a`

文档中包含的示例模型包括：

- `nano-banana2`
- `nano-banana-pro`
- `gpt-image-1.5`
- `wan2.6-t2i`
- `wan2.6-image`
- `wan2.6-t2v`
- `veo3.1-pro`
- `qwen3-tts-instruct-flash`

### 如何使用

使用前，你需要：

- 拥有有效的 MyReels 订阅
- 在 `myreels.ai` 开发者中心创建 AccessToken

基本流程：

1. 选择一个可用模型。
2. 调用提交任务接口 `POST /generation/:modelName`。
3. 记录返回的 `taskID`。
4. 调用查询接口 `GET /query/task/:taskID` 轮询状态。
5. 在任务完成后获取结果资源地址。

详细示例见：

- [myreels-api/references/code-examples.md](./myreels-api/references/code-examples.md)

### 隐私与安全

为避免泄露敏感信息，请注意：

- 不要在公开仓库、Issue、截图或聊天记录中暴露你的 AccessToken
- AccessToken 只应保存在你自己的安全环境中
- 生成结果链接请自行保存和管理

## 日本語

このリポジトリは、`myreels.ai` のユーザー向けに skills を提供するものです。skill をサポートする AI agent 上で、MyReels の生成機能をより簡単に使えるようにすることを目的としています。

AI アシスタントや自動化フローから MyReels API を利用したい場合、このリポジトリの skill を使うことで導入をより早く進められます。

### できること

現在提供している `myreels-api` skill では、次のことができます。

- MyReels の画像、動画、音声生成 API を利用する
- タスク送信と結果確認の基本フローを理解する
- よく使うモデルと入力パラメータを確認する
- JavaScript、TypeScript、Python、cURL のサンプルを参照する
- よくあるエラーやレート制限への対応方法を確認する

### 対象ユーザー

このリポジトリは次のようなユーザーに向いています。

- すでに `myreels.ai` を利用している方
- MyReels を自分の AI agent、スクリプト、ワークフローに組み込みたい方
- API の使い方を素早く確認したい方

### 含まれている Skill

#### `myreels-api`

この skill は MyReels API の利用ガイドで、主に次の内容を含みます。

- 認証方法
- 生成タスクの送信
- タスク状態の確認
- 生成結果の取得
- モデルパラメータの説明
- エラーハンドリングの指針

関連ドキュメント：

- [myreels-api/SKILL.md](./myreels-api/SKILL.md)
- [myreels-api/references/models.md](./myreels-api/references/models.md)
- [myreels-api/references/code-examples.md](./myreels-api/references/code-examples.md)
- [myreels-api/references/errors.md](./myreels-api/references/errors.md)

### インストール

`npx skills add` でのインストールを推奨します。

```bash
npx skills add https://github.com/myreelsai/skills --skill myreels-api -g
```

現在のプロジェクトのみに入れたい場合は `-g` を外します。

### 対応している機能

現在のドキュメントでは、以下の生成タイプを扱っています。

- 画像生成: `t2i` / `i2i`
- 動画生成: `t2v`
- 音声生成: `t2a`

サンプルとして掲載されているモデル：

- `nano-banana2`
- `nano-banana-pro`
- `gpt-image-1.5`
- `wan2.6-t2i`
- `wan2.6-image`
- `wan2.6-t2v`
- `veo3.1-pro`
- `qwen3-tts-instruct-flash`

### 使い方

利用前に必要なもの：

- 有効な MyReels サブスクリプション
- `myreels.ai` 開発者センターで作成した AccessToken

基本的な流れ：

1. 利用するモデルを選択します。
2. `POST /generation/:modelName` でタスクを送信します。
3. 返却された `taskID` を保存します。
4. `GET /query/task/:taskID` で状態をポーリングします。
5. 完了後に生成結果の URL を取得します。

サンプルコード：

- [myreels-api/references/code-examples.md](./myreels-api/references/code-examples.md)

### プライバシーと安全性

機密情報を漏らさないため、次の点に注意してください。

- 公開リポジトリ、Issue、スクリーンショット、チャット履歴に AccessToken を載せない
- AccessToken は自分の安全な環境だけで保管する
- 生成結果のリンクは自分で保存、管理する

## English

This repository provides skills for `myreels.ai` users so they can use MyReels generation capabilities more easily inside AI agents that support skills.

If you want to call the MyReels API from an AI assistant or an automated workflow, the skills in this repository help you get started faster.

### What It Helps With

The current `myreels-api` skill helps you:

- call MyReels image, video, and audio generation APIs
- understand the standard flow for submitting tasks and checking results
- look up common models and input parameters
- reuse JavaScript, TypeScript, Python, and cURL examples
- handle common errors and rate limit cases

### Who This Is For

This repository is useful if you:

- already use `myreels.ai`
- want to connect MyReels to your AI agent, scripts, or workflows
- need a faster way to understand the API

### Included Skill

#### `myreels-api`

This skill is a practical usage guide for the MyReels API. It covers:

- authentication
- submitting generation tasks
- checking task status
- retrieving generated results
- model parameter references
- error handling guidance

Related documents:

- [myreels-api/SKILL.md](./myreels-api/SKILL.md)
- [myreels-api/references/models.md](./myreels-api/references/models.md)
- [myreels-api/references/code-examples.md](./myreels-api/references/code-examples.md)
- [myreels-api/references/errors.md](./myreels-api/references/errors.md)

### Installation

Recommended installation via `npx skills add`:

```bash
npx skills add https://github.com/myreelsai/skills --skill myreels-api -g
```

Remove `-g` if you only want a project-level install.

### Supported Capabilities

The current documentation covers:

- image generation: `t2i` / `i2i`
- video generation: `t2v`
- audio generation: `t2a`

Example models included in the docs:

- `nano-banana2`
- `nano-banana-pro`
- `gpt-image-1.5`
- `wan2.6-t2i`
- `wan2.6-image`
- `wan2.6-t2v`
- `veo3.1-pro`
- `qwen3-tts-instruct-flash`

### How To Use

Before using the API, you need:

- an active MyReels subscription
- an AccessToken created in the `myreels.ai` developer center

Basic flow:

1. Choose a model.
2. Submit a task with `POST /generation/:modelName`.
3. Save the returned `taskID`.
4. Poll `GET /query/task/:taskID` for status updates.
5. Retrieve the result URL after completion.

Code examples:

- [myreels-api/references/code-examples.md](./myreels-api/references/code-examples.md)

### Privacy And Security

To avoid leaking sensitive information:

- do not expose your AccessToken in public repositories, issues, screenshots, or chat logs
- store your AccessToken only in your own secure environment
- save and manage generated result links on your side
