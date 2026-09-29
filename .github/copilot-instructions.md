# Copilot instructions

## Architecture diagrams
- Architecture diagrams live in `docs/architecture/` as `.drawio` files (draw.io XML, uncompressed).
- For any AWS diagram request, use the `aws-drawio-diagram` skill in `.github/skills/aws-drawio-diagram/`.
- Start from a template in that skill; use only shapes from its `references/aws-shape-catalog.md`.
- Run the skill's validator before declaring a diagram done.
- When code changes add, remove, or rename AWS resources (Terraform/CDK/CloudFormation), flag that the matching diagram in `docs/architecture/` needs updating.
