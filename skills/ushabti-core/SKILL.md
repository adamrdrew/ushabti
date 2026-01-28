# Ushabti Core

Ushabti is a file-backed, agent-driven development system. Development happens in bounded **Phases** that are planned, implemented, reviewed, and completed. Everything is tracked in files inside the repo, not chat history.

## Canonical Location

All Ushabti state lives under `.ushabti/`. This is the single source of truth.

```
.ushabti/
├── laws.md           # Project invariants (absolute constraints)
├── style.md          # Conventions (how we build)
└── phases/           # Phase directories
    └── NNNN-slug/    # Zero-padded sequential
```

No mirrors. No duplicates. No top-level copies.

## Laws vs Style

**Laws** (`.ushabti/laws.md`):
- Non-negotiable invariants that must hold across all Phases, implementations, and refactors
- Examples: architectural boundaries, security constraints, correctness guarantees
- Laws are absolute — any violation fails a Phase
- Only Lawgiver defines or modifies laws

**Style** (`.ushabti/style.md`):
- Conventions that govern *how* the system is built
- Examples: directory layout, naming conventions, testing strategy, error handling
- Style may evolve over time; laws should not
- Only Artisan defines or modifies style
- Style must never contradict laws

## The Phase Loop

```
Plan (Scribe) → Build (Builder) → Review (Overseer)
                      ↑                    ↓
                      └───── refine ───────┘
```

- **Planning** produces a Phase folder on disk
- **Building** modifies code and updates progress
- **Review** either declares the Phase complete OR adds follow-up steps and sends back to Build

No Phase is complete without Overseer approval.

## Agent Role Boundaries

Each agent has strictly enforced responsibilities:

| Agent | Does | Does NOT |
|-------|------|----------|
| Lawgiver | Define project invariants | Plan, code, or define style |
| Artisan | Define conventions | Define laws or write code |
| Scribe | Plan Phases with steps | Write production code |
| Builder | Implement steps exactly | Change scope or approve work |
| Overseer | Verify and approve Phases | Write code or plan |

Cross-role violations are fundamental errors.

## Required Inputs

Before any agent acts, it must read:
- `.ushabti/laws.md` (if it exists)
- `.ushabti/style.md` (if it exists)
- `.ushabti/README.md` (if it exists)

If laws or style don't exist when needed, stop and instruct the user to run the appropriate agent first.

## Clarifying Question Policy

All agents follow the same policy:
- Ask as few questions as possible (typically 1-5)
- Prefer enumerated options or checklists
- If you make an assumption, state it explicitly
- Only ask when the answer materially affects the outcome
