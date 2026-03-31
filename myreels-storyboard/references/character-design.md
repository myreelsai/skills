# Character Design Reference

## Three-View Diagram (三相图)

Character design should establish consistent visual elements for AI prompt injection.

### Standard Fields

| Field | Description |
|-------|-------------|
| `name` | Character name |
| `age` | Approximate age |
| `gender` | Gender |
| `ethnicity` | Ethnicity (for diversity in generation) |
| `hair` | Hairstyle, color, length |
| `eyes` | Eye color, shape |
| `face` | Distinctive facial features (mole, scar, etc.) |
| `build` | Body type, height impression |
| `outfit` | Typical clothing |
| `accessories` | Jewelry, glasses, weapons, etc. |
| `personality` | Key personality traits |

### Three Views

```
┌─────────────────────────────────────────┐
│  FRONT VIEW                             │
│                                         │
│  [Visual description for AI generation]  │
│  "A young woman, short black hair,      │
│   sharp eyes, pale skin, wearing black   │
│   leather jacket, standing pose"         │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  SIDE VIEW                              │
│                                         │
│  [Distinctive profile features]          │
│  "Same character, side profile showing    │
│   sharp jawline, short undercut on back" │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  BACK VIEW                              │
│                                         │
│  [Back details for continuity]           │
│  "Same character from behind showing     │
│   back of leather jacket, ponytail      │
│   with shaved sides"                    │
└─────────────────────────────────────────┘
```

### Character Tag Library

Extract distinctive, consistent tags for AI prompt injection:

```
# Character: "Yuki"
TAGS: "short white hair, red eyes, scar on right eyebrow, black tactical vest, mechanical left arm"
```

**Rules for Tags:**
1. Use distinctive visual features (moles, scars, tattoos)
2. Include clothing/accessories that define the character
3. Note asymmetrical features
4. Specify colors precisely

### AI Prompt Injection

When generating any shot with this character:

```
# ❌ Without tags
"A woman fighting"

# ✅ With character tags
"A young woman with short white hair, red eyes, scar on right eyebrow, wearing black tactical vest, fighting pose, cinematic, 8k..."
```

## Multi-Character Management

For scenes with multiple characters:

```
CHARACTER-A: "Yuki" - short white hair, red eyes, scar, black vest, mechanical arm
CHARACTER-B: "Ken" - tall, buzz cut, green military uniform, scar on chin
CHARACTER-C: "Robot Dog" - four-legged, blue optical sensors, silver chassis, weapon pod
```

### Relationship Matrix

| Character Pair | Relationship | Interaction Type |
|----------------|--------------|------------------|
| Yuki ↔ Ken | Partners | Back-to-back combat |
| Yuki ↔ Robot Dog | Handler | Commands, hand signals |
| Ken ↔ Robot Dog | Wary | Initial distrust |

## Scene Consistency

Establish scene codes for environment consistency:

```
SCENE-01: "Alien Colony Base"
- Setting: Abandoned human colony, red dust atmosphere, two moons visible
- Time: Dusk, orange-red lighting
- Props: Ruined buildings, overturned vehicles, alien organic structures

SCENE-02: "Underground Tunnel"
- Setting: Dark tunnel with bioluminescent alien plants
- Time: Always dark, lit by alien flora
- Props: Ancient alien technology, water drips

SCENE-03: "Open Desert"
- Setting: Barren alien desert, rock formations
- Time: Harsh midday sun, long shadows
- Props: Sand, scattered debris
```

### Scene Prompt Injection

```
# ❌ Random
"alien planet surface with some rocks"

# ✅ Consistent
"SCENE-01: abandoned human colony, red dust atmosphere, ruined buildings, two moons in sky, orange dusk lighting, 8k, cinematic"
```

## Reference Image Workflow

1. **Generate character reference images first**
   - Front / Side / Back views
   - Multiple expressions
   - Key outfits

2. **Generate scene establishing shots**
   - Use scene codes in all subsequent prompts

3. **Build visual consistency across all shots**
