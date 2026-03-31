# Multilingual Support Reference

## Supported Languages

- 🇨🇳 Chinese (zh)
- 🇯🇵 Japanese (ja)
- 🇬🇧 English (en)

## User Input Handling

### Story Input

User can input story or outline in any language:

- **Chinese**: 「一个女孩在樱花树下微笑，阳光洒落」
- **Japanese**: 「桜の下で笑う少女、陽光が差し込む」
- **English**: 「A girl smiling under a cherry tree, sunlight filtering through」

### AI Response Language

| User Language | AI Response Language | Notes |
|--------------|---------------------|-------|
| Chinese | Chinese | Storyboard descriptions in Chinese |
| Japanese | Japanese | Storyboard descriptions in Japanese |
| English | English | Storyboard descriptions in English |
| Mixed / Other | Chinese | Default to Chinese |

### visual_prompt is Always English

Regardless of user input language, the `visual_prompt` field **must be in English** for AI image generation.

### description Field - User Language Summary

The `description` field provides a **human-readable summary** of each shot in the **user's input language**:

| User Language | description Field | Example |
|--------------|------------------|---------|
| Chinese | 中文 | "女主角在废弃殖民地入口扫描周围环境" |
| Japanese | 日本語 | "女主角が廃墟になった植民地の入り口をスキャンしている" |
| English | English | "Female lead scanning surroundings at colony entrance" |

**Purpose**: Helps user quickly understand each shot without reading the full AI prompt.

**NOT for AI generation**: This field is ignored by myreels-api; only `visual_prompt` is used for image/video generation.

## Shot Terminology Reference

| English | Chinese | Japanese |
|---------|---------|----------|
| Wide / Long Shot | 远景 | 遠景 |
| Full Shot | 全景 | フルショット |
| Medium Shot | 中景 | ミディアムショット |
| Close-up | 近景 | 近い |
| Extreme Close-up | 特写 | クローズアップ |
| Eye-level | 平视 | レベルショット |
| Low-angle | 仰视 | 下から仰角 |
| High-angle | 俯视 | 上から俯瞰 |
| Bird's Eye | 鸟瞰 | トップショット |
| Dutch | 荷兰角 | ドイツアングル |
| Dolly In | 推近 | ドリーイン |
| Dolly Out | 拉远 | ドリーアウト |
| Pan | 摇镜 | パン |
| Follow | 跟拍 | フォロー |
| Fixed / Static | 固定 | 固定 |
| Orbit | 环绕 | 周回 |
| Tilt | 倾斜 | ティルト |

## Dialogue Handling

- User-provided dialogue is kept in original language
- Recorded in the `dialogue` field without translation
- Japanese/English dialogue remains in original text

## CSV Output

CSV file encoding is UTF-8, correctly storing all three languages' characters.

## Language Auto-Detection

Detect language from user input:

```python
def detect_language(text):
    # Simple detection logic
    if re.search(r'[\u4e00-\u9fff]', text):  # Chinese
        return 'zh'
    elif re.search(r'[\u3040-\u309f\u30a0-\u30ff]', text):  # Japanese
        return 'ja'
    else:
        return 'en'
```

## Storyboard Generation Rules

1. User input → Detect language
2. Storyboard content → Generate in same language as input (for `description`)
3. visual_prompt → **Always English**, including style and quality tags
4. User confirmation → Table displays user-language descriptions for easy review
