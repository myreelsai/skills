---
name: myreels-storyboard
description: |
  Professional storyboard design tool for short drama/video production.
  Activates when user mentions: script, storyboard, story board, shot design, video production planning, short drama.
  Workflow: story → character design → storyboard design → CSV/table confirmation → guide user to myreels-api for image/video generation.
  This skill focuses on storyboard design and content planning; actual image/video generation requires myreels-api skill.
---

# MyReels Storyboard Design Tool

## Integration with myreels-api

```
myreels-storyboard (storyboard design)
       ↓ generates storyboard CSV
myreels-api (image/video generation) ← user must install this skill first
```

**Important**: This skill handles storyboard design. After completion, guide the user to use `myreels-api` skill for actual image and video generation.

## Complete Workflow

```
1. Story Input → User provides plot outline
2. Character Design → Design characters with three-view diagrams (front/side/back)
3. Shot Breakdown → Generate structured shots
4. User Confirmation → Output CSV + platform table
5. Image Generation → Guide user to myreels-api
6. Video Creation → Guide user to myreels-api (optional)
```

## Step 1: Collect User Requirements

Collect the following information:

| Question | Options |
|----------|---------|
| Story content | Plot outline or full script |
| Video style | cinematic / anime / 3d cartoon / realistic |
| Duration | e.g., 60 seconds, 2 minutes |
| Shot count | e.g., 10-15 shots |
| Aspect ratio | 16:9 / 9:16 / 1:1 (vertical = 9:16) |
| Has dialogue | Yes / No |

## Step 2: Character Design (Important!)

**Before shot design, establish character consistency using a three-view diagram (三相图).**

### Character Design Fields

| Field | Description |
|-------|-------------|
| `character_name` | Character name |
| `appearance` | Physical description (hair, eyes, face, build) |
| `outfit` | Clothing and accessories |
| `personality` | Key personality traits |
| `front_view` | English description for front view |
| `side_view` | English description for side view |
| `back_view` | English description for back view |
| `character_tags` | Consistency tags for AI prompts (e.g., "short hair, left face mole, red earrings") |

### Three-View Diagram Output

Generate character descriptions for AI image generation:

```
CHARACTER: [Name]
TAGS: [Consistency tags for prompt injection]

FRONT: A [age] [ethnicity] [gender] with [hair], [eyes], [build], wearing [outfit], [pose/expression]
SIDE: Same character from side profile showing [distinctive feature]
BACK: Same character from behind showing [hairstyle/back detail], [outfit back view]
```

### Character Consistency

For each character, build a **character tag library** that will be reused in all shot prompts:

```
# Example character tags
"短发女孩, 左脸有痣, 红色耳钉, 黑色皮夹克"
→ "short hair, beauty mark on left cheek, red earrings, black leather jacket"
```

## Step 3: Generate Storyboard

### Shot Structure

Each shot includes these fields:

| Field | Description |
|-------|-------------|
| `shot_id` | Scene + Shot number (e.g., S01-01) |
| `shot_type` | Shot size |
| `camera_angle` | Camera angle |
| `movement` | Camera movement |
| `duration` | Estimated seconds (2-5s typical) |
| `description` | **User language description** - brief summary in user's input language (Chinese/Japanese/English). NOT used for AI generation. |
| `visual_prompt` | English prompt for AI image generation |
| `action` | Character action description |
| `dialogue` | Dialogue/voiceover (optional) |
| `emotion` | Target audience emotion |
| `sound_fx` | Sound effects / music cues (optional) |
| `notes` | Additional notes |
| `difficulty` | 🟢 simple / 🟡 medium / 🔴 complex |
| `status` | pending / confirmed / generating / done |

### Shot Type Reference

| Type | Chinese | Use Case |
|------|---------|----------|
| Extreme Close-up / ECU | 大特写 | Key detail, extreme emotion |
| Close-up / CU | 特写 | Face, key object |
| Medium Close-up / MCU | 中近景 | Dialogue, slight conflict |
| Medium / MS | 中景 | Conversation, interaction |
| Full Shot / FS | 全景 | Full body, relationship |
| Wide / WS | 远景 | Environment, establishing |

### Camera Angles & Psychology

| Angle | Emotion Implication |
|-------|---------------------|
| Eye-level | Neutral, objective |
| Low-angle (仰视) | Power, authority, threat |
| High-angle (俯视) | Vulnerability, submission |
| Dutch | Unease, tension, chaos |
| POV | Subjective, immersion |
| Tilted | Unstable, danger |

### Camera Movement

- Fixed / Static
- Dolly In (推近) / Dolly Out (拉远)
- Pan (摇镜) / Tilt (倾斜)
- Follow / Tracking (跟拍)
- Orbit (环绕) / Crane (升降)
- Handheld (手持) / Breath-like (呼吸感)

### Shot Difficulty Grading

| Grade | Icon | Description |
|-------|------|-------------|
| Simple | 🟢 | Fixed camera, single subject, no complex interaction |
| Medium | 🟡 | Light camera movement, dual subject, simple effects |
| Complex | 🔴 | Fast motion, multiple subjects, complex choreography, special lighting/particles |

### Emotion Mapping

Each shot must specify target emotion:

| Emotion | Key | Description |
|---------|-----|-------------|
| Hook | 钩子 | Attention grab |
| Tension | 紧张 | Building suspense |
| Conflict | 冲突 | Confrontation |
| Sweet | 甜宠 | Romance, warmth |
| Twist | 反转 | Surprise |
| Climax | 高潮 | Peak emotional moment |
| Release | 释然 | Resolution |

## Step 4: AI Prompt Engineering

### Prompt Structure

```
[Subject] + [Action] + [Environment] + [Lighting] + [Quality] + [Style] + [Camera]
```

### Required Quality Tags

Always include:
- `cinematic`
- `8k` or `high resolution`
- `shallow depth of field` or `bokeh`
- `dynamic lighting`

### Control Tags

If needed, add:
- `no text` / `no watermark` / `no distorted face`
- `solo` / `two-shot` / `crowd`

### Character Consistency in Prompts

Always inject character tags from Step 2:

```
# Before
"A woman fighting aliens"

# After (with character tags)
"A young woman with short hair, beauty mark on left cheek, red leather jacket fighting aliens, cinematic, 8k..."
```

### Scene Consistency

Use scene code +固化环境描述:

```
SCENE-A: "abandoned colony base, red dust, two moons, ruins"
# All shots in SCENE-A reference this environment
```

## Step 5: Output Confirmation

### Multi-Platform Output

**Feishu**: Use feishu_bitable for online editing
**Telegram**: Formatted text table or CSV attachment
**Other**: Default to CSV

### Storyboard Table Fields

```
shot_id, scene_code, shot_type, camera_angle, movement, duration, description, visual_prompt, action, dialogue, emotion, sound_fx, notes, difficulty, status
```

**Note**: The `description` field uses **user's input language** (Chinese/Japanese/English) for human-readable summary. The `visual_prompt` field is **always in English** for AI image generation.

## Step 6: Guide to myreels-api

### Guidance Message (Image Generation)

```
Storyboard confirmed. Now use `myreels-api` skill for image generation.

Recommended workflow:
1. Generate character reference images first (front/side/back)
2. Generate key storyboard shots using: nano-banana2 / seedream 5.0 / kling v3 image
3. Verify character consistency across all shots
4. Confirm images before video generation

Say: "Use myreels-api to generate storyboard images"
```

### Guidance Message (Video Generation)

```
Images confirmed. Now use `myreels-api` skill for video.

Recommended models (image to video):
- Kling O3 / Kling V3 (general video)
- Seedance 1.5 Pro SE (high quality)
- Wan 2.6 i2v / Hailuo-2.3 (quick preview)

Note: For complex shots (🔴), consider longer duration or multiple takes.

Say: "Use myreels-api to convert these images to video"
```

## Step 7: Quality Control Checklist

For each shot, verify:

- [ ] Character matches design (outfit, hair, facial features)
- [ ] Lighting direction consistent with scene light source
- [ ] Motion trajectory physically possible (no clipping, floating)
- [ ] Shot type serves narrative rhythm
- [ ] Safe zone reserved (vertical: top/bottom 20% no key elements for subtitles)
- [ ] Emotion matches intended audience feeling

## Output Files

- `characters.csv` - Character design data
- `storyboard.csv` - Complete storyboard
- Character reference images (via myreels-api)
- Storyboard image URLs (via myreels-api)

## Notes

- `visual_prompt` must be in **English** with quality tags
- User can input in Chinese / Japanese / English
- Each shot: 2-5 seconds recommended
- Always establish character design before shot breakdown
- Use difficulty grading to manage AI generation expectations
- See references/ for detailed guides
