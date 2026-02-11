---
name: boot-overseer
description: Bootstrap phase context for Overseer. Provides phase under review with full file contents and card metadata.
---

# Phase Bootstrap

Run the command below to get the active phase context. This replaces reading phase.md, steps.md, progress.yaml, and review.md individually. Use this to orient, then proceed to verifying the actual code and tests.

```
python3 ${CLAUDE_PLUGIN_ROOT}/skills/boot-overseer/boot.py
```
