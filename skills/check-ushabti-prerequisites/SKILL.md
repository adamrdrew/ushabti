---
name: check-ushabti-prerequisites
description: Verify required Ushabti files exist before proceeding. Use when starting agent work to ensure prerequisites are met.
user-invocable: false
---

# Ushabti Prerequisites

## Current Status

!`[ -f .ushabti/laws.md ] && echo "✓ laws.md exists" || echo "✗ laws.md MISSING (run Lawgiver)"`
!`[ -f .ushabti/style.md ] && echo "✓ style.md exists" || echo "✗ style.md MISSING (run Artisan)"`
!`[ -f .ushabti/docs/index.md ] && echo "✓ docs/index.md exists" || echo "✗ docs/index.md MISSING (run Surveyor)"`
!`[ -d .ushabti/phases ] && echo "✓ phases/ exists" || echo "✗ phases/ MISSING (run Scribe)"`

## Required Files by Agent

| Agent | laws.md | style.md | docs/ | phases/ |
|-------|---------|----------|-------|---------|
| Lawgiver | Creates | — | — | — |
| Artisan | Required | Creates | — | — |
| Surveyor | — | — | Creates | — |
| Scribe | Required | Required | Required | Creates |
| Builder | Required | Required | Recommended | Required |
| Overseer | Required | Required | Recommended | Required |

## Recommended Bootstrap Order

For a new project: Surveyor → Lawgiver → Artisan → Scribe → Builder → Overseer
