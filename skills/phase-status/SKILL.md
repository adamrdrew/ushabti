---
name: phase-status
description: Query the status of a phase. Returns structured status information for external consumers.
user-invocable: true
---

# Phase Status Query

## Purpose

This skill provides a stable public API for external tools (e.g., Pharaoh) to query phase status
without directly coupling to Ushabti's internal file structure.

## Invocation

```
/phase-status [ARGUMENT]
```

Where `ARGUMENT` can be:
- `latest` — returns the most recently modified phase (default if empty)
- Full slug (e.g., `0002-welcome-banner`)
- Partial slug (e.g., `welcome-banner`)

## Finding Phases

### Latest Phase

Find the phase with the most recently modified `progress.yaml`:

```bash
latest_phase=$(find .ushabti/phases -name "progress.yaml" -type f -exec ls -t {} + 2>/dev/null | head -1)
if [ -n "$latest_phase" ]; then
  phase_dir=$(dirname "$latest_phase")
else
  # No phases found
fi
```

### Specific Phase by Slug

Match directory names (exact or partial):

```bash
slug="$ARGUMENTS"
# Try exact match first
if [ -d ".ushabti/phases/$slug" ]; then
  phase_dir=".ushabti/phases/$slug"
else
  # Try partial match (first alphabetically)
  phase_dir=$(find .ushabti/phases -maxdepth 1 -type d -name "*$slug*" | sort | head -1)
fi
```

## Output Format

### Success

Return exactly this format (parseable structured output):

```
PHASE_STATUS:
  slug: {phase directory name}
  status: {planned|building|review|complete}
  steps_implemented: {count}
  steps_total: {count}
```

### Error

If phase not found:

```
PHASE_STATUS:
  error: Phase not found
```

## Extracting Data from progress.yaml

Once you have the phase directory:

```bash
# Get slug (directory basename)
slug=$(basename "$phase_dir")

# Get status
phase_status=$(grep "^  status:" "$phase_dir/progress.yaml" 2>/dev/null | awk '{print $2}')

# Count implemented steps
steps_implemented=$(grep -c "implemented: true" "$phase_dir/progress.yaml" 2>/dev/null || echo 0)

# Count total steps
steps_total=$(grep -c "implemented:" "$phase_dir/progress.yaml" 2>/dev/null || echo 0)
```

Then output:

```bash
cat <<EOF
PHASE_STATUS:
  slug: $slug
  status: $phase_status
  steps_implemented: $steps_implemented
  steps_total: $steps_total
EOF
```

## Contract Stability

The output format is a **public contract**. External tools parse this format. Any change to the
structure is a breaking change and must be versioned appropriately.
