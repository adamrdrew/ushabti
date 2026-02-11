---
name: mark-step-done
description: Mark a step as implemented in progress.yaml with notes and touched files. Use after completing each step instead of manual Edit calls.
user-invocable: false
---

## Mark Step Done

Updates a step entry in `progress.yaml` to set `implemented: true`, and optionally sets notes and touched file list. Handles both `touched` and `files` field names.

### Usage

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/mark-step-done/mark-step-done.py <phase-dir> <step-id> [--notes "..."] [--files file1 file2 ...]
```

### Arguments

- `phase-dir`: Path to the phase directory
- `step-id`: The step ID to mark done (e.g., `S001` or `1`)
- `--notes`: Optional description of what was done
- `--files`: Optional list of files touched by this step

### Examples

```bash
# Simple completion
python3 ${CLAUDE_PLUGIN_ROOT}/skills/mark-step-done/mark-step-done.py .ushabti/phases/0005-my-phase S001 --notes "Protocol defined" --files src/protocol.ts src/types.ts

# Without notes or files
python3 ${CLAUDE_PLUGIN_ROOT}/skills/mark-step-done/mark-step-done.py .ushabti/phases/0005-my-phase S002
```

This replaces the manual read-edit-write cycle on progress.yaml after each step.
