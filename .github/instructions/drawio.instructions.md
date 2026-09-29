---
applyTo: "**/*.drawio"
---
# Editing .drawio files
- Keep XML uncompressed and human-diffable; preserve existing cell ids.
- Use styles only from `.github/skills/aws-drawio-diagram/references/aws-shape-catalog.md`.
- Coordinates are relative to the parent container; follow `references/layout-rules.md`.
- New ids are semantic kebab-case (`svc-*`, `sn-*`, `az-*`, `e-*`), never random.
- After editing, run `python .github/skills/aws-drawio-diagram/scripts/validate_drawio.py <file>`.
