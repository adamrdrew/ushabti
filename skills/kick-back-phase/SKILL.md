---
name: kick-back-phase
description: Kick a phase back to building — sets status and adds new step entries to progress.yaml. Use when requesting fixes from Builder.
user-invocable: false
---

## Kick Back Phase

Sets phase status to `building` and adds new follow-up step entries to progress.yaml. Auto-detects the step ID format (S-prefix or bare numbers) and assigns the next available IDs.

You still need to:
- Add the step definitions to steps.md (titles, intent, work, done-when)
- Write your findings in review.md

This script handles the mechanical progress.yaml updates.

### Usage

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/kick-back-phase/kick-back-phase.py <phase-dir> "title 1" ["title 2" ...]
```

### Arguments

- `phase-dir`: Path to the phase directory
- Remaining args: Titles for new follow-up steps (one per argument)

### Example

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/kick-back-phase/kick-back-phase.py .ushabti/phases/0005-my-phase "Fix missing test for edge case" "Update docs for new parameter"
# Output:
# Phase status: building
# Added 2 follow-up steps:
#   S010: Fix missing test for edge case
#   S011: Update docs for new parameter
```

This replaces 2-3 separate Edit calls on progress.yaml (status change + adding each step entry).
