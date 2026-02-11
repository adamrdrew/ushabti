---
name: set-phase-status
description: Set the status field in a phase's progress.yaml. Use instead of manual Edit calls when transitioning phase status.
user-invocable: false
---

## Set Phase Status

Updates the `status` field in a phase's `progress.yaml`. Handles both nested and flat YAML formats.

### Usage

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/set-phase-status/set-phase-status.py <phase-dir> <status>
```

### Arguments

- `phase-dir`: Path to the phase directory (e.g., `.ushabti/phases/0005-my-phase`)
- `status`: One of `planned`, `building`, `review`, `complete`

### Examples

```bash
# Builder finishing implementation
python3 ${CLAUDE_PLUGIN_ROOT}/skills/set-phase-status/set-phase-status.py .ushabti/phases/0005-my-phase review

# Overseer kicking back
python3 ${CLAUDE_PLUGIN_ROOT}/skills/set-phase-status/set-phase-status.py .ushabti/phases/0005-my-phase building
```
