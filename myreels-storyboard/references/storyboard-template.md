# Storyboard Template & Format Specification

## CSV File Format

File: `storyboard.csv`, UTF-8 encoding

### Character Design CSV

```
character_id, name, age, gender, ethnicity, hair, eyes, face, build, outfit, accessories, personality, front_view_prompt, side_view_prompt, back_view_prompt, character_tags
C001, Yuki, 25, Female, Asian, short white hair, red eyes, scar on right eyebrow, athletic, black tactical vest, mechanical left arm, fierce determined, "A 25-year-old Asian woman with short white hair, red eyes, scar on right eyebrow, wearing black tactical vest, standing pose", "Same character, side profile showing sharp jawline and mechanical arm", "Same character from behind, ponytail with shaved sides, back of tactical vest", "short white hair, red eyes, scar on right eyebrow, black tactical vest, mechanical left arm"
```

### Storyboard CSV

```
shot_id, scene_code, shot_type, camera_angle, movement, duration, visual_prompt, action, dialogue, emotion, sound_fx, notes, difficulty, status
S01-01, SCENE-01, Wide Shot, Eye-level, Fixed, 4s, "SCENE-01: alien colony base at dusk, two moons visible, abandoned buildings, red dust atmosphere, cinematic, 8k, dramatic lighting", "Establishing shot, hero approaches colony entrance", "", Hook, ambient wind, Opening scene, 🟢, pending
S01-02, SCENE-01, Medium Shot, Low-angle, Dolly In, 2s, "SCENE-01: young woman with short white hair, red eyes, wearing black tactical vest, entering frame, cinematic, 8k, shallow DOF", "Hero walks forward confidently", "", Tension, footsteps on gravel, Character introduction, 🟢, pending
...
```

### Full Field Reference

| Field | Description | Example |
|-------|-------------|---------|
| `shot_id` | Scene + Shot number | S01-01, S01-02 |
| `scene_code` | Scene identifier for consistency | SCENE-01 |
| `shot_type` | Shot size | Wide Shot, Medium, Close-up |
| `camera_angle` | Camera angle | Eye-level, Low-angle |
| `movement` | Camera movement | Fixed, Dolly In, Pan |
| `duration` | Estimated seconds | 3s, 5s |
| `description` | **User language description** (not for AI) | 中文/日文/英文 分镜描述 |
| `visual_prompt` | English prompt for AI | Full prompt with scene tags |
| `action` | Character action | "Hero draws weapon" |
| `dialogue` | Dialogue/voiceover | "You'll pay for this." |
| `emotion` | Target emotion | Hook, Tension, Climax |
| `sound_fx` | Sound/music cues | Gunshot, suspense music |
| `notes` | Additional notes | VFX required, safety note |
| `difficulty` | 🟢🟡🔴 | Generation complexity |
| `status` | pending/confirmed/generating/done | Workflow status |

### Description Field (多语言描述)

- **Language**: Match user's input language (Chinese/Japanese/English)
- **Purpose**: Human-readable summary of the shot for understanding
- **Content**: Brief description of what's happening in the shot
- **NOT for AI**: This field is NOT used for image/video generation
- **Example (Chinese)**:
  - `description`: "女主角在废弃殖民地入口扫描周围环境，橙色黄昏光线映照"`

## Platform-Specific Output

### Feishu (feishu_bitable)

Create table with fields above. Use:
- Single select for `shot_type`, `camera_angle`, `movement`, `emotion`, `difficulty`, `status`
- Text for others
- URL type for `image_url`, `video_url`

### Telegram

**Option 1: Formatted Text Table**
```
🟢 S01-01 | Wide | Eye-level | 4s | Hook
📍 SCENE-01: Alien colony base, dusk
📝 Hero approaches entrance
```

**Option 2: CSV Attachment**
Send as document for user download

### Other Platforms

Default to CSV attachment

## Visual Prompt Template

```
[Scene Code]: [Environment description]
[Subject]: [Character description with tags]
[Action]: [Specific action]
[Lighting]: [Time and quality]
[Camera]: [Shot type and movement]
[Quality]: [cinematic, 8k, etc.]
[Style]: [Additional style tags]
```

### Example

```
SCENE-01: abandoned human colony, red dust atmosphere, ruined buildings, two moons
A young woman with short white hair, red eyes, scar on right eyebrow, black tactical vest, standing at entrance
Hero surveys the area with suspicion
Orange dusk lighting, dramatic shadows
Medium shot, slow dolly in
cinematic, 8k, shallow depth of field, dynamic lighting
```

## Shot Rhythm Reference

| Duration | Typical Shot Count | Per-Shot Average |
|----------|-------------------|------------------|
| 30s | 8-10 shots | 3-4s |
| 60s | 15-20 shots | 3-4s |
| 120s | 30-40 shots | 3-4s |

## Quality Checklist Per Shot

Before marking as `done`:

- [ ] Character matches design (use character_tags)
- [ ] Scene matches scene_code environment
- [ ] Lighting direction consistent
- [ ] Motion physically possible
- [ ] Safe zones respected (vertical: 20% top/bottom)
- [ ] Emotion matches intended feeling
- [ ] Duration appropriate for content
