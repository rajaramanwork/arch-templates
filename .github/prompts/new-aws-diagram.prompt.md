---
agent: agent
description: Create a new AWS architecture diagram (.drawio) from a short system description
argument-hint: e.g. "orders API: API Gateway, Lambda, DynamoDB, SQS worker, us-east-1"
---
Use the `aws-drawio-diagram` skill to create a new diagram for: ${input:system:Describe the system}

Pick the closest template, save to `docs/architecture/`, fill all placeholders, run the validator, and summarize assumptions.
