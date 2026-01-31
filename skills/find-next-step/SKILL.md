---
name: find-next-step
description: Find the next unimplemented step in a phase. Use when determining what to work on next.
---

# Find Next Step

Identify the next step to implement in the current phase.

## How Steps Are Tracked

In `progress.yaml`, each step has:
- `id`: Step identifier (S001, S002, ...)
- `implemented`: false until Builder completes it
- `reviewed`: false until Overseer verifies it

## Commands

**Show all steps with status:**
```bash
grep -E "(id:|implemented:|reviewed:)" .ushabti/phases/PHASE_DIR/progress.yaml
```

**Find first unimplemented step:**
```bash
# Replace PHASE_DIR with actual phase directory
awk '/- id:/{id=$3} /implemented: false/{print id; exit}' .ushabti/phases/PHASE_DIR/progress.yaml
```

**Count implemented vs total:**
```bash
total=$(grep -c "implemented:" .ushabti/phases/PHASE_DIR/progress.yaml)
done=$(grep -c "implemented: true" .ushabti/phases/PHASE_DIR/progress.yaml)
echo "$done / $total steps implemented"
```

## Workflow

1. Find the current phase (use find-current-phase)
2. Read `progress.yaml` to find first step with `implemented: false`
3. Read that step's details in `steps.md`
4. Implement the step
5. Update `progress.yaml`: set `implemented: true`, add notes, list touched files
6. Repeat until all steps are implemented

## When All Steps Are Done

If no steps have `implemented: false`, the phase is ready for review. Set `phase.status: review` in progress.yaml and hand off to Overseer.
