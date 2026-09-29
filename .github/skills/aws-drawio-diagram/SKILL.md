---
name: aws-drawio-diagram
description: Generate or update AWS reference-architecture diagrams as draw.io (.drawio) XML using approved templates, the verified AWS shape catalog, and layout rules. Use when asked to draw, create, update, or review an AWS architecture diagram.
argument-hint: Describe the system (services, tiers, flows) or point to a .drawio file to update
---

# AWS draw.io diagram skill

## Inputs to collect (ask only for what's missing)
System name, owner, environment, region, VPC CIDR, services per tier, key flows, ARB id.

## Steps
1. **Pick a template** from `templates/`:
   - [aws-3tier-web.drawio](./templates/aws-3tier-web.drawio) — CloudFront/ALB/ECS Fargate/Aurora across 2 AZs
   - [aws-serverless-api.drawio](./templates/aws-serverless-api.drawio) — API Gateway/Lambda/DynamoDB/SQS/EventBridge
   - [aws-bedrock-genai.drawio](./templates/aws-bedrock-genai.drawio) — API Gateway/Cognito/Lambda orchestrator/Bedrock model + Knowledge Base/OpenSearch vector store/S3/DynamoDB
   - [aws-hybrid-saas-corp-access.drawio](./templates/aws-hybrid-saas-corp-access.drawio) — corporate desktops/laptops over Direct Connect → Transit Gateway → internal ALB → ECS Fargate/RDS across 2 AZs, SAML IdP → Cognito federation, PrivateLink endpoints
   - [aws-vpc-skeleton.drawio](./templates/aws-vpc-skeleton.drawio) — empty Cloud/Region/VPC/2-AZ/3-tier frame for anything else
2. **Copy it** to `docs/architecture/<system-name>.drawio`. Never edit the template itself.
3. **Replace every `{{PLACEHOLDER}}`** (title block, region, CIDRs, service names).
4. **Add/remove services** using ONLY styles from [aws-shape-catalog.md](./references/aws-shape-catalog.md). If a service isn't in the catalog, use the closest listed one and say so — never invent a `resIcon` name.
5. **Place and connect** per [layout-rules.md](./references/layout-rules.md): correct parent container, relative coordinates, semantic ids, labelled orthogonal edges.
6. **Validate**: run `python .github/skills/aws-drawio-diagram/scripts/validate_drawio.py docs/architecture/<file>.drawio` and fix every error before finishing.
7. **Report** a short summary: file path, services shown, assumptions, anything omitted.

## Hard rules
- Output is uncompressed draw.io XML (`<mxfile><diagram><mxGraphModel>…`), one `<diagram>` per view.
- Cells `0` and `1` must exist; every other cell has a valid `parent`.
- Every edge has `source` and `target` that exist.
- No leftover `{{…}}` in finished diagrams, no secrets/account IDs/ARNs.
