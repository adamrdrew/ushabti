---
name: describe-ushabti
description: "Core Ushabti concepts, agent roles, Phase lifecycle, and file-backed state model. Use when starting any Ushabti workflow, orienting to the framework, or explaining how the system works."
user-invocable: false
---

# Ushabti

Ushabti is a file-backed, agent-driven development system for Claude Code. Development happens in bounded **Phases** that are planned, implemented, reviewed, and completed. Everything is tracked in files inside the repo, not chat history.

## Core Loop

```
Plan (Scribe) → Build (Builder) → Review (Overseer)
                      ↑                    ↓
                      └───── refine ───────┘
```

No Phase is complete without Overseer approval. If the Overseer identifies issues, the Phase returns to the Builder with concrete follow-up steps.

## Seven Specialized Agents

| Agent | Purpose | Boundary |
|-------|---------|----------|
| **Lawgiver** | Define project invariants in `.ushabti/laws.md` | Does not plan, code, or style |
| **Artisan** | Define conventions in `.ushabti/style.md` | Does not define laws or write code |
| **Surveyor** | Onboard existing projects by creating documentation in `.ushabti/docs/` | Does not plan, code, review, or define laws/style |
| **Scribe** | Plan Phases with steps and acceptance criteria | Does not write production code |
| **Builder** | Implement steps exactly as planned, update `progress.yaml` | Does not change scope or approve work |
| **Overseer** | Verify completion and declare Phases green | Does not write code or plan |
| **Vizier** | Advisory — answer questions, evaluate options, identify risks | Does not modify code, laws, style, docs, or any files except `vizier.md` |

## Canonical State Location

All Ushabti state lives under `.ushabti/`:

```
.ushabti/
├── laws.md           # Project invariants (absolute constraints)
├── style.md          # Conventions (how we build)
├── docs/             # Project documentation (created by Surveyor)
├── cards/            # Work items (Hieroglyphs-compatible)
└── phases/
    └── NNNN-slug/    # Zero-padded sequential
        ├── phase.md      # Intent, scope, acceptance criteria
        ├── steps.md      # Ordered work steps with done-when conditions
        ├── progress.yaml # Machine-tracked step status
        └── review.md     # Review findings
```

## Key Principles

- **Laws are absolute**: Any violation fails the Phase
- **Steps are ordered**: Implement in sequence unless explicitly allowed otherwise
- **Tests are first-class**: Must be explicit steps, not implied
- **No silent changes**: Missing work must be surfaced by adding steps
- **Progress.yaml is truth**: Updated truthfully after each step completion
- **Documentation stays current**: Phases cannot complete if docs are out of sync with code