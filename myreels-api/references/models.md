# 模型列表与参数

数据来源：`GET https://api.myreels.ai/api/v1/models/api`

> 本文档已按 2026-03-18 拉取到的接口结果同步。API 路径中使用 `modelName`，不是 `slug`。

## 当前可用 modelName

### 图像生成（t2i / i2i / i2e）
- `nano-banana2` (Nano Banana2) | 标签：`t2i / i2i` | 预估费用：`$0.0872` / 次
- `nano-banana-pro` (Nano Banana Pro) | 标签：`t2i / i2i` | 预估费用：`$0.1890` / 次
- `sora-image` (Sora Image) | 标签：`t2i / i2i` | 预估费用：`$0.0420` / 次
- `gpt-image-1.5` (GPT Image 1.5) | 标签：`t2i / i2i` | 预估费用：`$0.0420` / 次
- `doubao-seedream-5-0-260128` (Seedream 5.0) | 标签：`t2i / i2i` | 预估费用：`$0.2310` / 次
- `kling-image-create` (Kling Image) | 标签：`i2i / t2i` | 预估费用：`$0.1806` / 次
- `kling-omni-image` (Kling Omni Image) | 标签：`i2i / t2i` | 预估费用：`$0.0893` / 次
- `kling-multi-image-create` (Kling Multi Image) | 标签：`i2i` | 预估费用：`$0.3612` / 次
- `imagen-4` (Google Imagen4) | 标签：`t2i` | 预估费用：`$0.1575` / 次
- `wan2.6-image` (Wan2.6 I2I) | 标签：`i2i` | 预估费用：`$0.2100` / 次
- `wan2.6-t2i` (Wan2.6 T2I) | 标签：`t2i` | 预估费用：`$0.2100` / 次
- `qwen-image-edit-plus` (Qwen Image Edit) | 标签：`i2i / i2e` | 预估费用：`$0.2100` / 次

### 视频生成（t2v / i2v）
- `myreels-infinite-avatar` (MyReels Infinite Avatar) | 标签：`i2v` | 预估费用：`$1.2600` / 次
- `doubao-seedance-1-5-pro-251215` (Seedance 1.5 Pro SE) | 标签：`i2v` | 预估费用：`$1.8165` / 次
- `kling-image-to-video` (Kling Video) | 标签：`i2v` | 预估费用：`$2.2575` / 次
- `kling-omni-video` (Kling Omni Video) | 标签：`i2v / t2v` | 预估费用：`$1.3125` / 次
- `grok-video-3` (Grok Video 3) | 标签：`t2v / i2v` | 预估费用：`$0.2100` / 次
- `kling-text-to-video` (Kling T2V) | 标签：`t2v` | 预估费用：`$2.2575` / 次
- `veo3.1-pro` (Google Veo 3.1) | 标签：`t2v / i2v` | 预估费用：`$2.6250` / 次
- `MiniMax-Hailuo-2.3` (MiniMax-Hailuo-2.3) | 标签：`t2v / i2v` | 预估费用：`$2.1000` / 次
- `wan2.6-r2v` (Wan2.6 R2V) | 标签：`i2v` | 预估费用：`$3.1500` / 次
- `wan2.6-t2v` (Wan2.6 T2V) | 标签：`t2v` | 预估费用：`$3.1500` / 次
- `wan2.6-i2v` (Wan2.6 I2V) | 标签：`i2v` | 预估费用：`$1.5750` / 次
- `gen4_turbo` (Runway Gen4 Turbo) | 标签：`i2v` | 预估费用：`$2.1000` / 次

### 音频与音乐生成（t2a / m2a）
- `music-2.5` (MiniMax Music 2.5) | 标签：`m2a` | 预估费用：`$1.0500` / 次
- `chirp-v4` (Suno Music) | 标签：`m2a` | 预估费用：`$0.7875` / 次
- `qwen3-tts-instruct-flash` (Qwen-TTS) | 标签：`t2a` | 预估费用：`$0.0210` / 次

## 图像生成（t2i / i2i / i2e）

### Nano Banana2
- modelName：`nano-banana2`
- 标签：`t2i / i2i`
- 预估费用：`$0.0872` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `images` | `images` | — | — | — |
| `prompt` | `string` | ✅ | — | — |
| `imageSize` | `select` | — | `1K` | `0.5K` `1K` `2K` `4K` |
| `aspectRatio` | `select` | — | `1:1` | `1:1` `2:3` `3:2` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9` |

### Nano Banana Pro
- modelName：`nano-banana-pro`
- 标签：`t2i / i2i`
- 预估费用：`$0.1890` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `images` | `images` | — | — | — |
| `prompt` | `string` | ✅ | — | — |
| `imageSize` | `select` | — | `1K` | `1K` `2K` `4K` |
| `aspectRatio` | `select` | — | `1:1` | `1:1` `2:3` `3:2` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9` |

### Sora Image
- modelName：`sora-image`
- 标签：`t2i / i2i`
- 预估费用：`$0.0420` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `n` | `slider` | — | `1` | — |
| `size` | `select` | — | `1:1` | `1:1` `3:2` `2:3` |
| `image` | `images` | — | — | — |
| `prompt` | `string` | ✅ | — | — |

### GPT Image 1.5
- modelName：`gpt-image-1.5`
- 标签：`t2i / i2i`
- 预估费用：`$0.0420` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `n` | `slider` | — | `1` | — |
| `size` | `select` | — | `1:1` | `1:1` `3:2` `2:3` |
| `images` | `images` | — | — | — |
| `prompt` | `string` | ✅ | — | — |

### Seedream 5.0
- modelName：`doubao-seedream-5-0-260128`
- 标签：`t2i / i2i`
- 预估费用：`$0.2310` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `size` | `select` | — | `2048x2048` | `2048x2048` `2304x1728` `1728x2304` `2560x1440` `1440x2560` `2496x1664` `1664x2496` `3024x1296` `1K` `2K` `3K` `4K` |
| `image` | `images` | — | — | — |
| `model` | `select` | ✅ | `doubao-seedream-5-0-260128` | `doubao-seedream-5-0-260128` `doubao-seedream-4-5-251128` `doubao-seedream-4-0-250828` |
| `prompt` | `string` | ✅ | — | — |
| `sequential_image_generation` | `select` | — | `auto` | `auto` `disabled` |

### Kling Image
- modelName：`kling-image-create`
- 标签：`i2i / t2i`
- 预估费用：`$0.1806` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `n` | `slider` | — | `1` | — |
| `image` | `image` | — | — | — |
| `prompt` | `string` | ✅ | — | — |
| `model_name` | `select` | ✅ | `kling-v3` | `kling-v1` `kling-v1-5` `kling-v2` `kling-v2-new` `kling-v2-1` `kling-v3` |
| `resolution` | `select` | — | `1k` | `1k` `2k` |
| `aspect_ratio` | `select` | — | `16:9` | `16:9` `9:16` `1:1` `4:3` `3:4` `3:2` `2:3` `21:9` |
| `human_fidelity` | `slider` | — | `0.45` | — |
| `image_fidelity` | `slider` | — | `0.5` | — |
| `image_reference` | `select` | — | — | `subject` `face` |
| `negative_prompt` | `string` | — | — | — |

### Kling Omni Image
- modelName：`kling-omni-image`
- 标签：`i2i / t2i`
- 预估费用：`$0.0893` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `n` | `slider` | — | `1` | — |
| `images` | `images` | — | — | — |
| `prompt` | `string` | ✅ | — | — |
| `model_name` | `select` | ✅ | `kling-v3-omni` | `kling-image-o1` `kling-v3-omni` |
| `resolution` | `select` | — | `1k` | `1k` `2k` `4k` |
| `result_type` | `select` | ✅ | `single` | `single` `series` |
| `aspect_ratio` | `select` | — | `16:9` | `16:9` `9:16` `1:1` `4:3` `3:4` `3:2` `2:3` `21:9` |
| `series_amount` | `slider` | — | `4` | — |

### Kling Multi Image
- modelName：`kling-multi-image-create`
- 标签：`i2i`
- 预估费用：`$0.3612` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `n` | `slider` | — | `1` | — |
| `images` | `images` | ✅ | — | — |
| `prompt` | `string` | ✅ | — | — |
| `model_name` | `select` | ✅ | `kling-v2` | `kling-v2` `kling-v2-1` |
| `scene_image` | `image` | — | — | — |
| `style_image` | `image` | — | — | — |
| `aspect_ratio` | `select` | — | `16:9` | `16:9` `9:16` `1:1` `4:3` `3:4` `3:2` `2:3` `21:9` |

### Google Imagen4
- modelName：`imagen-4`
- 标签：`t2i`
- 预估费用：`$0.1575` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `model` | `select` | ✅ | `imagen-4` | `imagen-4` `imagen-4-fast` `imagen-4-ultra` |
| `prompt` | `string` | — | — | — |
| `aspectRatio` | `select` | — | `1:1` | `1:1` `9:16` `16:9` `3:4` `4:3` |

### Wan2.6 I2I
- modelName：`wan2.6-image`
- 标签：`i2i`
- 预估费用：`$0.2100` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `n` | `slider` | — | `1` | — |
| `seed` | `number` | — | `0` | — |
| `size` | `select` | — | `1280*1280` | `1024*1024` `1280*1280` `800*1200` `1200*800` `960*1280` `1280*960` `720*1280` `1280*720` `1344*576` |
| `images` | `images` | ✅ | — | — |
| `prompt` | `string` | ✅ | — | — |
| `negative_prompt` | `string` | — | — | — |
| `enable_interleave` | `switch` | ✅ | `false` | — |

### Wan2.6 T2I
- modelName：`wan2.6-t2i`
- 标签：`t2i`
- 预估费用：`$0.2100` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `n` | `slider` | — | `1` | — |
| `seed` | `number` | — | `0` | — |
| `size` | `select` | — | `1280*1280` | `1280*1280` `1104*1472` `1472*1104` `960*1696` `1696*960` |
| `prompt` | `string` | ✅ | — | — |
| `prompt_extend` | `switch` | — | `true` | — |
| `negative_prompt` | `string` | — | — | — |

### Qwen Image Edit
- modelName：`qwen-image-edit-plus`
- 标签：`i2i / i2e`
- 预估费用：`$0.2100` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `seed` | `number` | — | `0` | — |
| `images` | `images` | ✅ | — | — |
| `prompt` | `string` | ✅ | — | — |
| `negative_prompt` | `string` | — | — | — |

## 视频生成（t2v / i2v）

### MyReels Infinite Avatar
- modelName：`myreels-infinite-avatar`
- 标签：`i2v`
- 预估费用：`$1.2600` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `audio` | `audio` | ✅ | — | — |
| `image` | `image` | ✅ | — | — |
| `prompt` | `string` | — | `她向观众说话。` | — |
| `strength` | `slider` | — | `0.1` | — |

### Seedance 1.5 Pro SE
- modelName：`doubao-seedance-1-5-pro-251215`
- 标签：`i2v`
- 预估费用：`$1.8165` / 次
- 说明：接口中同一个 `modelName` 当前存在 `Seedance 1.5 Pro SE` / `Seedance 1.5 Pro` 两个展示名，调用时统一使用这个 `modelName`。

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `model` | `select` | ✅ | `doubao-seedance-1-5-pro-251215` | `doubao-seedance-1-5-pro-251215` `doubao-seedance-1-0-pro-250528` |
| `ratio` | `select` | — | `adaptive` | `16:9` `4:3` `1:1` `3:4` `9:16` `21:9` `adaptive` |
| `image1` | `image` | ✅ | — | — |
| `image2` | `image` | ✅ | — | — |
| `prompt` | `string` | ✅ | — | — |
| `duration` | `slider` | — | `5` | — |
| `resolution` | `select` | — | `720p` | `480p` `720p` `1080p` |
| `generate_audio` | `switch` | — | `true` | — |

### Kling Video
- modelName：`kling-image-to-video`
- 标签：`i2v`
- 预估费用：`$2.2575` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `mode` | `select` | — | `std` | `std` `pro` |
| `image` | `image` | ✅ | — | — |
| `sound` | `select` | — | `on` | `off` `on` |
| `prompt` | `string` | ✅ | — | — |
| `duration` | `select` | — | `5` | `5` `10` |
| `cfg_scale` | `slider` | — | `0.5` | — |
| `image_tail` | `image` | — | — | — |
| `model_name` | `select` | ✅ | `kling-v2-6` | `kling-v1` `kling-v1-5` `kling-v1-6` `kling-v2-master` `kling-v2-1` `kling-v2-1-master` `kling-v2-5-turbo` `kling-v2-6` `kling-v3` |

### Kling Omni Video
- modelName：`kling-omni-video`
- 标签：`i2v / t2v`
- 预估费用：`$1.3125` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `mode` | `select` | — | `std` | `std` `pro` |
| `sound` | `select` | — | `on` | `off` `on` |
| `video` | `video` | — | — | — |
| `image1` | `image` | — | — | — |
| `image2` | `image` | — | — | — |
| `images` | `images` | — | — | — |
| `prompt` | `string` | ✅ | — | — |
| `duration` | `slider` | — | `5` | — |
| `element_id` | `string` | — | — | — |
| `model_name` | `select` | ✅ | `kling-v3-omni` | `kling-video-o1` `kling-v3-omni` |
| `multi_shot` | `select` | — | `false` | `False` `True` |
| `video_type` | `select` | — | `base` | `feature` `base` |
| `aspect_ratio` | `select` | — | `16:9` | `1:1` `16:9` `9:16` |
| `multi_prompt` | `string` | — | — | — |
| `keep_original_sound` | `select` | — | `yes` | `yes` `no` |

### Grok Video 3
- modelName：`grok-video-3`
- 标签：`t2v / i2v`
- 预估费用：`$0.2100` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `model` | `select` | ✅ | `grok-video-3` | `grok-video-3` `grok-video-3-10s` `grok-video-3-15s` |
| `images` | `images` | — | — | — |
| `prompt` | `string` | — | — | — |
| `aspectRatio` | `select` | — | `1:1` | `1:1` `2:3` `3:2` `3:4` `4:3` `9:16` `16:9` |

### Kling T2V
- modelName：`kling-text-to-video`
- 标签：`t2v`
- 预估费用：`$2.2575` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `mode` | `select` | — | `std` | `std` `pro` |
| `sound` | `select` | — | `on` | `off` `on` |
| `prompt` | `string` | ✅ | — | — |
| `duration` | `select` | — | `5` | `5` `10` |
| `cfg_scale` | `slider` | — | `0.5` | — |
| `camera_pan` | `slider` | — | `0` | — |
| `model_name` | `select` | — | `kling-v2-6` | `kling-v1` `kling-v1-6` `kling-v2-master` `kling-v2-1-master` `kling-v2-5-turbo` `kling-v2-6` |
| `camera_roll` | `slider` | — | `0` | — |
| `camera_tilt` | `slider` | — | `0` | — |
| `camera_zoom` | `slider` | — | `0` | — |
| `aspect_ratio` | `select` | — | `16:9` | `16:9` `9:16` `1:1` |
| `camera_vertical` | `slider` | — | `0` | — |
| `negative_prompt` | `string` | — | — | — |
| `camera_horizontal` | `slider` | — | `0` | — |
| `camera_control_type` | `select` | — | — | `simple` `down_back` `forward_up` `right_turn_forward` `left_turn_forward` |

### Google Veo 3.1
- modelName：`veo3.1-pro`
- 标签：`t2v / i2v`
- 预估费用：`$2.6250` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `model` | `select` | ✅ | `veo3.1-pro` | `veo3.1-pro` `veo3.1-fast` |
| `image1` | `image` | ✅ | — | — |
| `image2` | `image` | — | — | — |
| `prompt` | `string` | — | — | — |
| `aspectRatio` | `select` | — | `16:9` | `16:9` `9:16` |

### MiniMax-Hailuo-2.3
- modelName：`MiniMax-Hailuo-2.3`
- 标签：`t2v / i2v`
- 预估费用：`$2.1000` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `model` | `select` | ✅ | `MiniMax-Hailuo-2.3` | `MiniMax-Hailuo-2.3` `MiniMax-Hailuo-2.3-Fast` |
| `image1` | `image` | ✅ | — | — |
| `prompt` | `string` | — | — | — |
| `duration` | `slider` | — | `6` | — |
| `resolution` | `select` | — | `768P` | `768P` `1080P` |
| `prompt_optimizer` | `switch` | — | `true` | — |
| `fast_pretreatment` | `switch` | — | `false` | — |

### Wan2.6 R2V
- modelName：`wan2.6-r2v`
- 标签：`i2v`
- 预估费用：`$3.1500` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `size` | `select` | — | `1920*1080` | `1280*720` `720*1280` `960*960` `1088*832` `832*1088` `1920*1080` `1080*1920` `1440*1440` `1632*1248` `1248*1632` |
| `prompt` | `string` | ✅ | — | — |
| `duration` | `slider` | — | `5` | — |
| `shot_type` | `select` | — | `single` | `single` `multi` |
| `reference_urls` | `files` | ✅ | — | — |
| `negative_prompt` | `string` | — | — | — |

### Wan2.6 T2V
- modelName：`wan2.6-t2v`
- 标签：`t2v`
- 预估费用：`$3.1500` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `size` | `select` | — | `1920*1080` | `1280*720` `1920*1080` |
| `prompt` | `string` | ✅ | — | — |
| `duration` | `slider` | — | `5` | — |
| `audio_url` | `audio` | — | — | — |
| `shot_type` | `select` | — | `single` | `single` `multi` |
| `negative_prompt` | `string` | — | — | — |

### Wan2.6 I2V
- modelName：`wan2.6-i2v`
- 标签：`i2v`
- 预估费用：`$1.5750` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `image` | `image` | ✅ | — | — |
| `model` | `select` | ✅ | `wan2.6-i2v` | `wan2.6-i2v` `wan2.6-i2v-flash` |
| `prompt` | `string` | ✅ | — | — |
| `duration` | `slider` | — | `5` | — |
| `audio_url` | `audio` | — | — | — |
| `shot_type` | `select` | — | `single` | `single` `multi` |
| `resolution` | `select` | — | `1080P` | `720P` `1080P` |
| `negative_prompt` | `string` | — | — | — |

### Runway Gen4 Turbo
- modelName：`gen4_turbo`
- 标签：`i2v`
- 预估费用：`$2.1000` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `ratio` | `select` | — | `1280:720` | `1280:720` `720:1280` `1104:832` `832:1104` `960:960` `1584:672` |
| `image1` | `image` | ✅ | — | — |
| `prompt` | `string` | ✅ | — | — |
| `duration` | `slider` | — | `5` | — |

## 音频与音乐生成（t2a / m2a）

### MiniMax Music 2.5
- modelName：`music-2.5`
- 标签：`m2a`
- 预估费用：`$1.0500` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `model` | `select` | ✅ | `music-2.5` | `music-2.5` `music-2.0` |
| `lyrics` | `string` | ✅ | — | — |
| `prompt` | `string` | ✅ | — | — |
| `bitrate` | `select` | — | `128000` | `32000` `64000` `128000` `256000` |
| `sample_rate` | `select` | — | `44100` | `16000` `24000` `32000` `44100` |

### Suno Music
- modelName：`chirp-v4`
- 标签：`m2a`
- 预估费用：`$0.7875` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `tags` | `string` | — | — | — |
| `title` | `string` | ✅ | `my music` | — |
| `prompt` | `string` | ✅ | — | — |
| `continue_at` | `string` | — | — | — |
| `continue_clip_id` | `string` | — | — | — |
| `make_instrumental` | `select` | — | `false` | `true` `false` |

### Qwen-TTS
- modelName：`qwen3-tts-instruct-flash`
- 标签：`t2a`
- 预估费用：`$0.0210` / 次

| 参数 | 类型 | 必填 | 默认值 | 可选值 |
|------|------|------|--------|--------|
| `voice` | `selectImg` | ✅ | `Cherry` | `Cherry` `Serena` `Ethan` `Chelsie` `Momo` `Vivian` `Moon` `Maia` `Kai` `Nofish` `Bella` `Mia` `Mochi` `Bellona` `Vincent` `Bunny` `Neil` `Elias` `Arthur` `Nini` `Ebona` `Seren` `Pip` `Stella` |
| `prompt` | `string` | ✅ | — | — |
| `instructions` | `string` | — | — | — |
| `language_type` | `select` | — | `Auto` | `Chinese` `English` `Japanese` `German` `Italian` `Portuguese` `Spanish` `Korean` `French` `Russian` |
| `optimize_instructions` | `select` | — | `false` | `True` `False` |
