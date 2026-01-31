---
name: get-phase-status
description: Check the current status of a phase. Use when you need to understand where a phase is in the workflow.
---

# Get Phase Status

Check the status of a phase and understand what it means.

## Status Values

| Status | Meaning | Next Action |
|--------|---------|-------------|
| `planned` | Phase created, not started | Builder begins implementation |
| `building` | Implementation in progress | Builder continues or addresses fixes |
| `review` | Implementation complete | Overseer reviews |
| `complete` | Phase is green | Scribe plans next phase |

## Commands

**Get status of a specific phase:**
```bash
grep "status:" .ushabti/phases/PHASE_DIR/progress.yaml
```

**Get status of all phases:**
```bash
for dir in .ushabti/phases/*/; do
  name=$(basename "$dir")
  status=$(grep "^  status:" "$dir/progress.yaml" 2>/dev/null | awk '{print $2}')
  echo "$name: $status"
done
```

**Find phases in a specific status:**
```bash
# Replace STATUS with: planned, building, review, or complete
for dir in .ushabti/phases/*/; do
  if grep -q "status: STATUS" "$dir/progress.yaml" 2>/dev/null; then
    basename "$dir"
  fi
done
```

## Status Transitions

```
planned → building    (Builder starts)
building → review     (Builder finishes all steps)
review → building     (Overseer requests fixes)
review → complete     (Overseer approves)
```

## Quick Summary Command

```bash
echo "=== Phase Status Summary ==="
for dir in .ushabti/phases/*/; do
  name=$(basename "$dir")
  status=$(grep "^  status:" "$dir/progress.yaml" 2>/dev/null | awk '{print $2}')
  impl=$(grep -c "implemented: true" "$dir/progress.yaml" 2>/dev/null || echo 0)
  total=$(grep -c "implemented:" "$dir/progress.yaml" 2>/dev/null || echo 0)
  echo "$name: $status ($impl/$total steps)"
done
```
