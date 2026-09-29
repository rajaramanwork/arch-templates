---
agent: agent
description: ARB-style review of an AWS .drawio diagram
---
Review ${file} against the `aws-drawio-diagram` skill's catalog and layout rules, then check:
multi-AZ for stateful tiers, public vs private subnet placement, edge protection (WAF/Shield),
secrets and encryption (Secrets Manager/KMS), observability (CloudWatch/CloudTrail), labelled flows,
completed title block. Run the validator. Output: pass/fail per item, then concrete fixes.
