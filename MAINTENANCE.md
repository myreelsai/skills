# myreels-api skill 维护指南

## 文件位置

| 文件 | 说明 |
|------|------|
| `/home/comfyui/.claude/skills/myreels-api/SKILL.md` | skill 主文档，认证和流程说明 |
| `/home/comfyui/.claude/skills/myreels-api/references/models.md` | 模型列表与参数 |
| `/home/comfyui/.claude/skills/myreels-api/references/code-examples.md` | 代码示例 |
| `/home/comfyui/.claude/skills/myreels-api/references/errors.md` | 错误码说明 |
| `/home/comfyui/git/myreels-skills/` | GitHub 仓库本地目录 |

GitHub 仓库：https://github.com/myreelsai/skills

---

## 数据来源

### 模型列表（最重要）

```bash
VITE_API_KEY=$(grep VITE_API_KEY /home/comfyui/git/beautyai-webui/.env | cut -d= -f2)
curl -s "https://api.myreels.ai/api/v1/models/api" \
  -H "Authorization: Bearer $VITE_API_KEY" \
  -H "Content-Type: application/json"
```

返回每个模型的：
- `modelName` — API 路径中使用（如 `nano-banana-pro`）
- `slug` — 内部标识，不用于 API 路径
- `userInputSchema` — 所有输入参数的类型、必填、默认值、选项
- `serviceConfig.estimatedPrice` — 预估费用
- `tags` — 分类标签（t2i / i2i / t2v / t2a 等）

### API 路径（来自 worker 源码）

源码位置：`/home/comfyui/git/beautyai-webui/worker/src/generation.ts`

```
POST https://api.myreels.ai/generation/build/:modelName   # 提交任务
POST https://api.myreels.ai/generation/task/:taskID       # 查询任务
```

---

## 更新流程

### 1. 拉取最新模型数据

```bash
VITE_API_KEY=$(grep VITE_API_KEY /home/comfyui/git/beautyai-webui/.env | cut -d= -f2)
curl -s "https://api.myreels.ai/api/v1/models/api" \
  -H "Authorization: Bearer $VITE_API_KEY" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for item in data.get('data', {}).get('items', []):
    sc = item.get('serviceConfig', {})
    schema = item.get('userInputSchema', {})
    print(f\"modelName: {item.get('modelName')} | name: {item.get('name')} | tags: {item.get('tags')} | price: {sc.get('estimatedPrice')}\")
    for k, v in schema.items():
        print(f\"  {k} ({v.get('type')}) required={v.get('required')} default={v.get('default') or v.get('defaultValue')}\")
    print()
"
```

### 2. 更新 skill 文件

根据上面的输出更新 `references/models.md`，主要关注：
- 新增或下线的模型
- 参数变化（新增字段、选项变化、默认值变化）
- 费用变化

### 3. 推送到 GitHub

```bash
cp -r /home/comfyui/.claude/skills/myreels-api/. /home/comfyui/git/myreels-skills/myreels-api/
cd /home/comfyui/git/myreels-skills
git add .
git commit -m "update: sync model list from API"
GIT_TERMINAL_PROMPT=0 git push
```

### 4. 用户更新

```bash
npx skills update myreels-api
```

---

## 注意事项

- API 路径用 `modelName`，不是 `slug`（两者不同）
- token 放在请求 body 中，不是 Header
- 查询任务也用 POST，不是 GET
