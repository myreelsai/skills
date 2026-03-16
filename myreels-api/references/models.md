# 模型列表与参数

数据来源：`GET https://api.myreels.ai/api/v1/models/api`

---

## 图像生成（t2i / i2i）

### Nano Banana2 `pr-376ebd94`
- 标签：`t2i` `i2i`
- 预估费用：$0.0872 / 次

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `prompt` | string | ✅ | — | 提示词，最长 2000 字符 |
| `images` | images | — | — | 参考图片，最多 14 张（用于 i2i） |
| `imageSize` | select | — | `1K` | 分辨率：`0.5K` `1K` `2K` `4K` |
| `aspectRatio` | select | — | `1:1` | 宽高比：`1:1` `2:3` `3:2` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9` |

---

### Nano Banana Pro `pr-9264a6e0`
- 标签：`t2i` `i2i`
- 预估费用：$0.1890 / 次

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `prompt` | string | ✅ | — | 提示词，最长 2000 字符 |
| `images` | images | — | — | 参考图片（用于 i2i） |
| `imageSize` | select | — | `1K` | 分辨率：`1K` `2K` `4K` |
| `aspectRatio` | select | — | `1:1` | 宽高比：`1:1` `2:3` `3:2` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9` |

---

### GPT Image 1.5 `pr-d2a95e26`
- 标签：`t2i` `i2i`
- 预估费用：$0.0420 / 次

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `prompt` | string | ✅ | — | 提示词 |
| `images` | images | — | — | 参考图片（用于 i2i） |
| `n` | slider | — | `1` | 生成数量 |
| `size` | select | — | `1:1` | 宽高比：`1:1` `3:2` `2:3` |

---

### Wan2.6 T2I `pr-d5d90151`
- 标签：`t2i`
- 预估费用：$0.2100 / 次

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `prompt` | string | ✅ | — | 提示词 |
| `negative_prompt` | string | — | — | 负向提示词 |
| `size` | select | — | `1280*1280` | 分辨率：`1280*1280` `1104*1472` `1472*1104` `960*1696` `1696*960` |
| `n` | slider | — | `1` | 生成数量 |
| `seed` | number | — | — | 随机种子 |
| `prompt_extend` | switch | — | `true` | 自动扩展提示词 |

---

### Wan2.6 I2I `pr-37f1d61a`
- 标签：`i2i`
- 预估费用：$0.2100 / 次

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `images` | images | ✅ | — | 参考图片 |
| `prompt` | string | ✅ | — | 提示词 |
| `enable_interleave` | switch | ✅ | — | 启用交错模式 |
| `negative_prompt` | string | — | — | 负向提示词 |
| `size` | select | — | `1280*1280` | 分辨率：`1024*1024` `1280*1280` `800*1200` `1200*800` `960*1280` `1280*960` `720*1280` `1280*720` `1344*576` |
| `n` | slider | — | `1` | 生成数量 |
| `seed` | number | — | — | 随机种子 |

---

## 视频生成（t2v）

### Wan2.6 T2V `pr-859b0de1`
- 标签：`t2v`
- 预估费用：$3.1500 / 次

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `prompt` | string | ✅ | — | 提示词 |
| `negative_prompt` | string | — | — | 负向提示词 |
| `size` | select | — | `1920*1080` | 分辨率：`1280*720` `1920*1080` |
| `duration` | slider | — | `5` | 时长（秒） |
| `shot_type` | select | — | `single` | 镜头类型：`single`（单镜头）`multi`（多镜头） |
| `audio_url` | audio | — | — | 背景音频 URL |

---

## 语音生成（t2a）

### Qwen-TTS `pr-e834b522`
- 标签：`t2a`
- 预估费用：$0.0210 / 次

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `prompt` | string | ✅ | — | 要转换的文本 |
| `voice` | select | ✅ | `Cherry` | 音色：`Cherry` `Serena` `Ethan` `Chelsie` `Momo` `Vivian` `Moon` `Maia` `Kai` `Nofish` `Bella` `Mia` `Mochi` `Bellona` `Vincent` `Bunny` `Neil` `Elias` `Arthur` `Nini` `Ebona` `Seren` `Pip` `Stella` |
| `language_type` | select | — | `Auto` | 语言：`Chinese` `English` `Japanese` `German` `Italian` `Portuguese` `Spanish` `Korean` `French` `Russian` |
| `instructions` | string | — | — | 语音风格指令 |
| `optimize_instructions` | select | — | — | 是否优化指令：`true` `false` |
