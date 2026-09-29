# Layout rules for AWS draw.io diagrams

These rules produce diagrams that open cleanly in draw.io with no manual tidying. They match the
three templates in `../templates/`, so start from a template and follow the same numbers.

## Coordinates are relative to the parent
A cell's `x`/`y` is measured from the top-left of its **parent** container, not the page.
Put every icon inside the smallest container it belongs to (subnet → AZ → VPC → Region → Cloud).

## Nesting order (outside → in)
```
page (parent="1")
└─ cloud          AWS Cloud / account
   ├─ edge/global services (Route 53, CloudFront, WAF, IAM) — left column of the cloud
   └─ region
      ├─ vpc
      │  ├─ az-a / az-b              (side by side)
      │  │  ├─ sn-pub-{az}          public subnet   (top row)
      │  │  ├─ sn-app-{az}          private app     (middle row)
      │  │  └─ sn-data-{az}         private data    (bottom row)
      │  ├─ svc-igw                 left edge of VPC
      │  └─ svc-alb                 child of VPC, centered on the gap between AZs, public row
      └─ regional managed services (S3, KMS, Secrets Manager, CloudWatch, SQS…) — right column of region
actors (users, on-prem) — parent="1", left of the cloud
```

## Grid and sizes
- Icons: 48 × 48. Place them on a 10 px grid.
- Keep ≥ 120 px between icon centers in a row and ≥ 150 px between rows (labels sit under icons).
- Inside a container, keep ≥ 40 px from the top edge (the group label lives there) and ≥ 20 px elsewhere.
- Center a lone icon in a 270-wide subnet at `x=111`.
- Standard sizes from the 3-tier template:
  - AZ: 310 × 700, subnets inside: 270 × 180–200 at `x=20`, rows at `y=40 / 250 / 480`.
  - VPC with 2 AZs: 760 wide; AZ-A at `x=100`, AZ-B at `x=430`.
  - Regional services column: `x = vpc.x + vpc.width + 50`, rows every 170 px.

## Flow direction
- Left → right for the request path (users → edge → ALB/API → compute → data).
- Top → bottom inside the VPC (public → app → data).
- Put the thing that calls on the left/top and the thing being called on the right/bottom.

## Edges
- All edges use `parent="1"` and reference `source`/`target` ids, even across containers.
- Use `edgeStyle=orthogonalEdgeStyle`. Never draw free-floating lines.
- When an edge would cross icons, first try moving the icons so the path is straight. If that
  isn't possible, pin it with `exitX/exitY/entryX/entryY` (add `exitDx=0;exitDy=0;entryDx=0;entryDy=0;`)
  and at most two waypoints in `<Array as="points">`. Waypoints are **absolute page coordinates**.
- Label edges with protocol or intent in ≤ 3 words: `HTTPS`, `SQL/TLS`, `enqueue`, `replication`.
- Don't connect every service to CloudWatch/KMS. Show them as present in the region; add an edge only
  when the call is architecturally significant (e.g. envelope encryption of a specific store).

## IDs
Stable, semantic, kebab-case, so diffs stay readable in PRs:
- containers: `cloud`, `region`, `vpc`, `az-a`, `sn-pub-a`, `sn-app-b`, `sn-data-a`
- services: `svc-<service>[-<qualifier>]` e.g. `svc-alb`, `svc-app-a`, `svc-db-primary`
- actors: `actor-<name>`; edges: `e-<from>-<to>`; notes: `note-<topic>`
- Never reuse an id, never use draw.io's random ids in generated files.

## Labels
- Official service name on line 1, role on line 2: `Amazon Aurora PostgreSQL<br>(writer)`.
- Subnets carry their CIDR when known: `Private app subnet A 10.0.10.0/24`.
- No secrets, account IDs, ARNs, or hostnames — use aliases.

## Multi-page files
One `<diagram>` per view in the same `.drawio` file, named for what it shows:
`context`, `network`, `data-flow`, `dr`. Keep ids unique across pages.
