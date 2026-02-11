---
name: approve-phase
description: Approve a phase — sets status to complete, marks all steps reviewed, updates linked card. Use when declaring a phase green.
user-invocable: false
---

## Approve Phase

Single command to perform all mechanical state transitions when declaring a phase green:

1. Sets phase status to `complete` in progress.yaml
2. Marks all steps `reviewed: true` in progress.yaml
3. If phase.md has a `card:` field, updates the card's status to `done` with current timestamp

You still need to write your review decision in review.md separately — that's creative content this script doesn't touch.

### Usage

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/approve-phase/approve-phase.py <phase-dir>
```

### Arguments

- `phase-dir`: Path to the phase directory (e.g., `.ushabti/phases/0005-my-phase`)

### Example

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/approve-phase/approve-phase.py .ushabti/phases/0009-tag-reconciler
# Output:
# Phase status: complete
# All steps: reviewed
# Card 'tag-reconciler': marked done
```

This replaces 4-5 separate Edit calls (status update + marking each step reviewed + card read + card update).
