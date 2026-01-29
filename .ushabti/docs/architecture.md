# Architecture Overview

## Overview

Ushabti is a file-backed, agent-driven development system implemented as a Claude Code plugin. All state lives in files within the repository, not in chat history. Development happens in bounded Phases that flow through a Plan-Build-Review loop until approved.

## Core Principles

1. **File-backed state**: All project state is stored in files under `.ushabti/`. No hidden state, no external dependencies.

2. **Bounded Phases**: Work is organized into small, reviewable units called Phases. Each Phase has explicit scope, acceptance criteria, and ordered steps.

3. **Agent specialization**: Six agents with strictly enforced role boundaries. No agent can perform another's function.

4. **Mandatory review**: No Phase is complete without Overseer approval. Review is a gate, not a formality.

## The Phase Loop

```
Plan (Scribe) --> Build (Builder) --> Review (Overseer)
                        ^                    |
                        |                    v
                        +------ refine ------+
```

### Flow

1. **Plan**: Scribe creates a Phase directory with intent, scope, acceptance criteria, and ordered steps.

2. **Build**: Builder implements each step in order, updating `progress.yaml` after each completion.

3. **Review**: Overseer verifies acceptance criteria, law compliance, and step completion.
   - If issues exist: Overseer adds follow-up steps and sends back to Build.
   - If complete: Overseer declares the Phase green.

4. **Repeat**: Once green, Scribe plans the next Phase.

## State Model

All Ushabti state lives under `.ushabti/`:

```
.ushabti/
├── laws.md           # Project invariants (absolute constraints)
├── style.md          # Conventions (how we build)
├── docs/             # Project documentation (created by Surveyor)
└── phases/
    └── NNNN-slug/    # Zero-padded sequential Phase directories
        ├── phase.md
        ├── steps.md
        ├── progress.yaml
        └── review.md
```

### Laws vs Style

**Laws** (`.ushabti/laws.md`):
- Non-negotiable invariants
- Any violation fails a Phase
- Only Lawgiver can modify

**Style** (`.ushabti/style.md`):
- Conventions for consistency
- May evolve over time
- Only Artisan can modify
- Must not contradict laws

## Agent Architecture

Six agents, each with a single responsibility:

| Agent | Responsibility |
|-------|---------------|
| Lawgiver | Define project invariants |
| Artisan | Define project style |
| Surveyor | Create project documentation |
| Scribe | Plan Phases |
| Builder | Implement Phases |
| Overseer | Review and approve Phases |

### Role Boundaries

Agents have hard boundaries. For example:
- Scribe plans but does not code
- Builder codes but does not plan or approve
- Overseer approves but does not code or plan

Cross-role violations are fundamental errors.

## Plugin Architecture

Ushabti is packaged as a Claude Code plugin:

```
.
├── .claude-plugin/
│   └── plugin.json       # Plugin manifest
├── agents/               # Agent definitions (markdown with YAML front matter)
└── skills/               # Skill definitions (directories with SKILL.md)
```

The plugin manifest (`plugin.json`) registers all agents and skills, making them available to Claude Code clients.

## Workflow Summary

1. **Bootstrap** (one-time):
   - Run Lawgiver to define invariants
   - Run Artisan to define style
   - Optionally run Surveyor to document existing code

2. **Development cycle** (repeating):
   - Scribe plans a Phase
   - Builder implements the Phase
   - Overseer reviews the Phase
   - If approved, return to step 1
   - If not approved, Builder addresses follow-ups

This cycle continues until all planned work is complete.
