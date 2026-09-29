# AWS shape catalog (draw.io `mxgraph.aws4`)

Source of truth for every AWS shape Copilot may emit. **Every name below was render-tested in draw.io.**
`scripts/validate_drawio.py` reads this file as its allowlist, so a shape not listed here fails validation.
To add a shape: find it in draw.io (More Shapes → AWS 2025 / Networking → search), copy its style
(Edit Style), render-test it, then add a row here.

## 1. Style skeletons — copy exactly, swap only the `{{...}}` tokens

### 1a. Resource icon (square, colored background) — most services
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor={{CATEGORY_COLOR}};strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{{RES_ICON}};
```
Geometry: `width="48" height="48"`.

### 1b. General / networking glyph (outline, no square) — gateways, load balancers, actors
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor={{COLOR}};strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.{{SHAPE}};
```
Geometry: `width="48" height="48"`.

### 1c. Group containers — see §4.

## 2. Category colors (`fillColor`)

| Category | Color |
|---|---|
| Compute, Containers | `#ED7100` |
| Storage | `#7AA116` |
| Database | `#C925D1` |
| Networking & Content Delivery, Analytics | `#8C4FFF` |
| Security, Identity & Compliance | `#DD344C` |
| App Integration, Management & Governance | `#E7157B` |
| AI / ML | `#01A88D` |
| Actors (users, clients) | `#232F3D` |

## 3. Resource icons (`shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.<name>`)

| Service | resIcon | Color |
|---|---|---|
| Amazon EC2 | `mxgraph.aws4.ec2` | `#ED7100` |
| AWS Lambda | `mxgraph.aws4.lambda` | `#ED7100` |
| Amazon ECS | `mxgraph.aws4.ecs` | `#ED7100` |
| Amazon EKS | `mxgraph.aws4.eks` | `#ED7100` |
| AWS Fargate | `mxgraph.aws4.fargate` | `#ED7100` |
| AWS App Runner | `mxgraph.aws4.app_runner` | `#ED7100` |
| Amazon ECR | `mxgraph.aws4.ecr` | `#ED7100` |
| Amazon S3 | `mxgraph.aws4.s3` | `#7AA116` |
| Amazon EFS | `mxgraph.aws4.elastic_file_system` | `#7AA116` |
| AWS Backup | `mxgraph.aws4.backup` | `#7AA116` |
| Amazon RDS | `mxgraph.aws4.rds` | `#C925D1` |
| Amazon Aurora | `mxgraph.aws4.aurora` | `#C925D1` |
| Amazon DynamoDB | `mxgraph.aws4.dynamodb` | `#C925D1` |
| Amazon ElastiCache | `mxgraph.aws4.elasticache` | `#C925D1` |
| Amazon Route 53 | `mxgraph.aws4.route_53` | `#8C4FFF` |
| Amazon CloudFront | `mxgraph.aws4.cloudfront` | `#8C4FFF` |
| AWS Transit Gateway | `mxgraph.aws4.transit_gateway` | `#8C4FFF` |
| Elastic Load Balancing (generic) | `mxgraph.aws4.elastic_load_balancing` | `#8C4FFF` |
| AWS Direct Connect | `mxgraph.aws4.direct_connect` | `#8C4FFF` |
| AWS Site-to-Site VPN | `mxgraph.aws4.site_to_site_vpn` | `#8C4FFF` |
| Amazon API Gateway | `mxgraph.aws4.api_gateway` | `#E7157B` |
| Amazon Kinesis | `mxgraph.aws4.kinesis` | `#8C4FFF` |
| AWS Glue | `mxgraph.aws4.glue` | `#8C4FFF` |
| Amazon Athena | `mxgraph.aws4.athena` | `#8C4FFF` |
| Amazon Redshift | `mxgraph.aws4.redshift` | `#8C4FFF` |
| Amazon OpenSearch Service | `mxgraph.aws4.elasticsearch_service` | `#8C4FFF` |
| Amazon SQS | `mxgraph.aws4.sqs` | `#E7157B` |
| Amazon SNS | `mxgraph.aws4.sns` | `#E7157B` |
| Amazon EventBridge | `mxgraph.aws4.eventbridge` | `#E7157B` |
| AWS Step Functions | `mxgraph.aws4.step_functions` | `#E7157B` |
| AWS AppSync | `mxgraph.aws4.appsync` | `#E7157B` |
| Amazon MQ | `mxgraph.aws4.mq` | `#E7157B` |
| Amazon CloudWatch | `mxgraph.aws4.cloudwatch_2` | `#E7157B` |
| AWS CloudTrail | `mxgraph.aws4.cloudtrail` | `#E7157B` |
| AWS Systems Manager | `mxgraph.aws4.systems_manager` | `#E7157B` |
| AWS Config | `mxgraph.aws4.config` | `#E7157B` |
| AWS Organizations | `mxgraph.aws4.organizations` | `#E7157B` |
| AWS IAM | `mxgraph.aws4.identity_and_access_management` | `#DD344C` |
| Amazon Cognito | `mxgraph.aws4.cognito` | `#DD344C` |
| AWS WAF | `mxgraph.aws4.waf` | `#DD344C` |
| AWS Shield | `mxgraph.aws4.shield` | `#DD344C` |
| AWS KMS | `mxgraph.aws4.key_management_service` | `#DD344C` |
| AWS Secrets Manager | `mxgraph.aws4.secrets_manager` | `#DD344C` |
| AWS Certificate Manager | `mxgraph.aws4.certificate_manager_3` | `#DD344C` |
| Amazon GuardDuty | `mxgraph.aws4.guardduty` | `#DD344C` |
| Amazon Bedrock | `mxgraph.aws4.bedrock` | `#01A88D` |
| Amazon SageMaker | `mxgraph.aws4.sagemaker` | `#01A88D` |

## 4. General / networking glyphs (`shape=mxgraph.aws4.<name>`, style 1b)

| Element | shape | Color |
|---|---|---|
| Application Load Balancer | `mxgraph.aws4.application_load_balancer` | `#8C4FFF` |
| Gateway Load Balancer | `mxgraph.aws4.gateway_load_balancer` | `#8C4FFF` |
| Internet gateway | `mxgraph.aws4.internet_gateway` | `#8C4FFF` |
| NAT gateway | `mxgraph.aws4.nat_gateway` | `#8C4FFF` |
| VPC endpoints (PrivateLink) | `mxgraph.aws4.endpoints` | `#8C4FFF` |
| Endpoint (single) | `mxgraph.aws4.endpoint` | `#8C4FFF` |
| Network ACL | `mxgraph.aws4.network_access_control_list` | `#8C4FFF` |
| Router | `mxgraph.aws4.router` | `#8C4FFF` |
| Flow logs | `mxgraph.aws4.flow_logs` | `#8C4FFF` |
| ENI | `mxgraph.aws4.elastic_network_interface` | `#8C4FFF` |
| Internet | `mxgraph.aws4.internet_alt1` | `#232F3D` |
| Users (group) | `mxgraph.aws4.users` | `#232F3D` |
| User (single) | `mxgraph.aws4.user` | `#232F3D` |
| Client / workstation | `mxgraph.aws4.client` | `#232F3D` |
| On-prem server | `mxgraph.aws4.traditional_server` | `#232F3D` |

## 5. Group containers

All groups except AZ share this prefix (call it `GRP`):
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;verticalAlign=top;align=left;spacingLeft=30;
```

| Group | Append to `GRP` |
|---|---|
| AWS Cloud / account | `grIcon=mxgraph.aws4.group_aws_cloud_alt;strokeColor=#232F3E;fillColor=none;fontColor=#232F3E;dashed=0;` |
| Region | `grIcon=mxgraph.aws4.group_region;strokeColor=#00A4A6;fillColor=none;fontColor=#147EBA;dashed=1;` |
| VPC | `grIcon=mxgraph.aws4.group_vpc2;strokeColor=#8C4FFF;fillColor=none;fontColor=#AAB7B8;dashed=0;` |
| Public subnet | `grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#7AA116;fillColor=#F2F6E8;fontColor=#248814;dashed=0;` |
| Private subnet | `grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#00A4A6;fillColor=#E6F6F7;fontColor=#147EBA;dashed=0;` |

Availability Zone (plain dashed box, not an aws4 group):
```
fillColor=none;strokeColor=#147EBA;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#147EBA;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;
```

## 6. Connectors

| Meaning | Style |
|---|---|
| Synchronous request | `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeColor=#545B64;fontSize=11;` |
| Async / event / replication | same as above + `dashed=1;` |
| Association (WAF↔CloudFront, authorizer) | `edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;dashed=1;dashPattern=1 3;strokeColor=#879196;` |

## 7. Title block (required, top-left)
```
text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;fontSize=12;fontColor=#232F3E;strokeColor=#D5DBDB;fillColor=#FAFAFA;spacing=8;
```
id `title-block`, geometry `x=20 y=20 width=460 height=70`.
