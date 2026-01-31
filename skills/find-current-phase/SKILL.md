---
name: find-current-phase
description: Find the active phase directory based on status. Use when you need to locate which phase to work on.
---

# Find Current Phase

Locate the active phase directory in `.ushabti/phases/`.

## By Status

Different agents work on phases in different statuses:

| Status | Agent | Meaning |
|--------|-------|---------|
| `planned` | Builder | Ready to start implementation |
| `building` | Builder | Implementation in progress or fixes requested |
| `review` | Overseer | Ready for review |
| `complete` | — | Phase is green, no work needed |

## Commands

**List all phases:**
```bash
ls -1 .ushabti/phases/
```

**Find phase by status:**
```bash
for dir in .ushabti/phases/*/; do
  status=$(grep "^  status:" "$dir/progress.yaml" | awk '{print $2}')
  echo "$dir -> $status"
done
```

**Find phase with specific status (e.g., "building"):**
```bash
for dir in .ushabti/phases/*/; do
  if grep -q "status: building" "$dir/progress.yaml" 2>/dev/null; then
    echo "$dir"
  fi
done
```

**Get highest-numbered phase (most recent):**
```bash
ls -1 .ushabti/phases/ | sort -V | tail -1
```

## For Builder

Look for `status: building` or `status: planned`. If multiple exist, work on the lowest-numbered one first.

## For Overseer

Look for `status: review`. If none exist, no phase is ready for review.
