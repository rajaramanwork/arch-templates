# draw.io + GitHub Copilot: AWS diagram kit

Copy this folder's contents into your repo root. Then in VS Code Copilot Chat (Agent mode):
- `/new-aws-diagram orders API: API Gateway, Lambda, DynamoDB, SQS worker, us-east-1`
- `/aws-drawio-diagram` (the skill, invoked directly)
- `/review-aws-diagram` with a `.drawio` file open (ARB-style check)

Open the generated `.drawio` in VS Code with the Draw.io Integration extension (recommended in `.vscode/extensions.json`) or at app.diagrams.net.

| Path | Purpose |
|---|---|
| `.github/copilot-instructions.md` | Repo-wide: where diagrams live, always use the skill |
| `.github/instructions/drawio.instructions.md` | Auto-applied when editing `*.drawio` |
| `.github/skills/aws-drawio-diagram/SKILL.md` | The workflow Copilot follows |
| `.../references/aws-shape-catalog.md` | Render-verified AWS styles (also the validator's allowlist) |
| `.../references/layout-rules.md` | Nesting, grid, ids, edge routing |
| `.../templates/*.drawio` | 3-tier web, serverless API, empty VPC skeleton |
| `.../scripts/validate_drawio.py` | `python .../validate_drawio.py docs/architecture/x.drawio` |
| `.github/prompts/*.prompt.md` | `/new-aws-diagram`, `/review-aws-diagram` |

Add a shape: render-test it in draw.io, then add a row to the catalog. Add a template: drop a `.drawio` in `templates/` and list it in SKILL.md step 1.

test
