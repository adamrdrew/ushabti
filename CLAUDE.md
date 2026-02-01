# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What is Ushabti?

Ushabti is a file-backed, agent-driven development system for VS Code. Development happens in bounded **Phases** that are planned, implemented, reviewed, and completed. Everything is tracked in files inside the repo, not chat history.

The core loop:
```
Plan (Scribe) → Build (Builder) → Review (Overseer)
                      ↑                    ↓
                      └───── refine ───────┘
```

No Phase is complete without Overseer approval.

## Agent Roles

Seven specialized agents with strictly enforced boundaries:

| Agent | Purpose | Does NOT |
|-------|---------|----------|
| **Lawgiver** | Define project invariants in `laws.md` | Plan, code, or style |
| **Artisan** | Define conventions in `style.md` | Define laws or write code |
| **Surveyor** | Onboard existing projects by creating documentation | Plan, code, review, define laws, or style |
| **Scribe** | Plan Phases with steps and acceptance criteria | Write production code |
| **Builder** | Implement steps exactly as planned | Change scope or approve work |
| **Overseer** | Verify completion and declare Phases green | Write code or plan |
| **Vizier** | Advisory agent: answer questions, evaluate options, identify risks | Modify code, laws, style, docs, or any files except `vizier.md` |

## Canonical State Location

All Ushabti state lives under `.ushabti/`:

```
.ushabti/
├── laws.md           # Project invariants (absolute constraints)
├── style.md          # Conventions (how we build)
└── phases/
    └── NNNN-slug/    # Zero-padded sequential
        ├── phase.md      # Intent, scope, acceptance criteria
        ├── steps.md      # 5-15 ordered steps with done-when conditions
        ├── progress.yaml # Machine-tracked step status
        └── review.md     # Review findings
```

## Key Constraints

- **Laws are absolute**: Any violation fails the Phase
- **Steps are ordered**: Implement in sequence unless explicitly allowed otherwise
- **Tests are first-class**: Not implied—must be explicit steps
- **No silent changes**: Missing work must be surfaced by adding steps
- **Progress.yaml is truth**: Update truthfully after each step completion

## Progress.yaml Structure

```yaml
phase:
  id: NNNN
  slug: short-slug
  title: Title
  status: planned|building|review|complete

steps:
  - id: S001
    title: Short title
    implemented: false   # Builder sets true when done
    reviewed: false      # Only Overseer sets true
    notes: ""
    touched: []          # Files modified
```

## Typical Usage Flow

1. **Bootstrap**: Run Lawgiver to capture invariants, then Artisan for style
2. **Plan**: Scribe creates Phase directory with all required files
3. **Build**: Builder implements steps in order, updates progress.yaml
4. **Review**: Overseer verifies or adds follow-up steps
5. **Repeat**: Once green, Scribe plans next Phase

## Agent Configuration

Agent prompts are defined in:
- `.claude/agents/` — Claude Code agents
- `.github/agents/` — GitHub Copilot agents

Both contain the same core specifications with platform-specific metadata.
