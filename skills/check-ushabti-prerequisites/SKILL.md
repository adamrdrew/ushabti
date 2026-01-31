---
name: check-ushabti-prerequisites
description: Verify required Ushabti files exist before proceeding. Use when starting agent work to ensure prerequisites are met.
---

# Check Ushabti Prerequisites

Verify that required files exist before agents can proceed.

## Required Files by Agent

| Agent | laws.md | style.md | docs/ | phases/ |
|-------|---------|----------|-------|---------|
| Lawgiver | Creates | — | — | — |
| Artisan | Required | Creates | — | — |
| Surveyor | — | — | Creates | — |
| Scribe | Required | Required | Required | Creates |
| Builder | Required | Required | Recommended | Required |
| Overseer | Required | Required | Recommended | Required |

## Commands

**Check if file exists:**
```bash
test -f .ushabti/laws.md && echo "laws.md exists" || echo "laws.md MISSING"
test -f .ushabti/style.md && echo "style.md exists" || echo "style.md MISSING"
test -f .ushabti/docs/index.md && echo "docs exist" || echo "docs MISSING"
test -d .ushabti/phases && echo "phases/ exists" || echo "phases/ MISSING"
```

**Full prerequisite check:**
```bash
echo "=== Ushabti Prerequisites ==="
[ -f .ushabti/laws.md ] && echo "✓ laws.md" || echo "✗ laws.md (run Lawgiver)"
[ -f .ushabti/style.md ] && echo "✓ style.md" || echo "✗ style.md (run Artisan)"
[ -f .ushabti/docs/index.md ] && echo "✓ docs/" || echo "✗ docs/ (run Surveyor)"
[ -d .ushabti/phases ] && echo "✓ phases/" || echo "✗ phases/ (run Scribe)"
```

## What to Do If Missing

| Missing | Run |
|---------|-----|
| laws.md | Ushabti Lawgiver |
| style.md | Ushabti Artisan |
| docs/ | Ushabti Surveyor |
| phases/ | Ushabti Scribe (to create first phase) |

## Recommended Order

For a new project: Surveyor → Lawgiver → Artisan → Scribe → Builder → Overseer
