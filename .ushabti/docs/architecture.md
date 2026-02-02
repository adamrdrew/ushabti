# Architecture Overview

## Overview

Ushabti is a file-backed, agent-driven development system implemented as a Claude Code plugin. All state lives in files within the repository. Development happens in bounded Phases that flow through a Plan-Build-Review loop until approved.

## Core Principles

1. **File-backed state**: All project state is stored in files under `.ushabti/`. No hidden state, no external dependencies.

2. **Bounded Phases**: Work is organized into small, reviewable units called Phases. Each Phase has explicit scope, acceptance criteria, and ordered steps.

3. **Agent specialization**: Six agents with strictly enforced role boundaries. No agent can perform another's function.

4. **Mandatory review**: No Phase is complete without Overseer approval.

## The Phase Loop

```
Plan (Scribe) --> Build (Builder) --> Review (Overseer)
                        ^                    |
                        |                    v
                        +------ refine ------+
```

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
├── laws.md           # Project invariants
├── style.md          # Project conventions
├── docs/             # Project documentation
├── tickets/          # Active tickets
│   └── .archived/    # Completed tickets
└── phases/
    └── NNNN-slug/
        ├── phase.md
        ├── steps.md
        ├── progress.yaml
        └── review.md
```

### Laws vs Style

**Laws** (`.ushabti/laws.md`): Non-negotiable invariants. Any violation fails a Phase.

**Style** (`.ushabti/style.md`): Conventions for consistency. May evolve over time. Must not contradict laws.

## Ticket System

Tickets provide a lightweight way to capture ideas for future work without immediately planning a Phase. They complement the Phase-driven workflow by preserving valuable ideas discovered during development.

### Design

- **File-backed**: Tickets are YAML files stored in `.ushabti/tickets/`
- **Simple lifecycle**: Create → derive phase → archive (no editing, no state transitions)
- **Agent-aware**: Agents can read, create, and archive tickets during their workflows

### Workflow

1. **Create**: Agent or user creates a ticket in `.ushabti/tickets/TNNNN-description.yaml`
2. **Derive**: When ready, Scribe creates a Phase from the ticket (adds `ticket: TNNNN` to phase.md)
3. **Archive**: When the derived Phase completes, Overseer moves the ticket to `.ushabti/tickets/.archived/`

### Agent Integration

- **Vizier**: Can read active tickets and offer to create tickets during conversation (sparingly)
- **Scribe**: Reads tickets when planning phases, incorporates ticket context and proposed work, adds ticket metadata to phase.md
- **Overseer**: Archives tickets when completing ticket-derived phases
- **All agents**: Tickets in `.ushabti/tickets/.archived/` are invisible and never read

### Ticket Schema

Required fields (YAML):
- `id`: Sequential ticket ID (T0001, T0002, etc.)
- `title`: Brief description
- `created`: ISO 8601 date (YYYY-MM-DD)
- `priority`: Must be `low`, `medium`, or `high`
- `context`: Why this ticket exists
- `proposed_work`: What should be done

See `describe-tickets` skill for complete schema and format details.

## Agent Architecture

Seven agents, each with a single responsibility:

| Agent | Responsibility |
|-------|---------------|
| Lawgiver | Define project invariants |
| Artisan | Define project style |
| Surveyor | Create project documentation |
| Scribe | Plan Phases |
| Builder | Implement Phases |
| Overseer | Review and approve Phases |
| Vizier | Answer questions and provide advice |

### Role Boundaries

Agents have hard boundaries:
- Scribe plans but does not code
- Builder codes but does not plan or approve
- Overseer approves but does not code or plan
- Vizier advises but does not modify files (except vizier-memory.md)

Cross-role violations are fundamental errors.

## Skill Architecture

Agents access domain knowledge through skills. Rather than preloading all content, agents:
1. Receive a skill catalog at startup (`using-skills`)
2. Invoke specific skills on-demand via the Skill tool

This keeps agent context lightweight while providing access to the full knowledge library.

## Plugin Architecture

```
.
├── .claude-plugin/plugin.json   # Plugin manifest
├── agents/                      # Agent definitions
├── skills/                      # Skill definitions
└── scripts/                     # Maintenance scripts
```

The plugin manifest registers all agents and skills with Claude Code.

## Workflow Summary

### Bootstrap (one-time)

**New project (empty directory):**
1. Run Lawgiver to define invariants (also creates minimal docs scaffold)
2. Run Artisan to define style
3. Optionally run Surveyor for comprehensive documentation
4. Proceed to development cycle

**Existing project:**
1. Run Surveyor to document existing code
2. Run Lawgiver to define invariants
3. Run Artisan to define style
4. Proceed to development cycle

### Docs Scaffold vs Comprehensive Docs

Lawgiver creates a minimal docs scaffold (`.ushabti/docs/index.md`) during bootstrap. This enables the docs loop to function immediately. The scaffold contains placeholder content and a marker indicating comprehensive documentation is needed.

Surveyor creates comprehensive documentation by exploring the codebase and generating detailed system docs. For existing projects, run Surveyor first. For new projects, the scaffold is sufficient to start — run Surveyor when there's code worth documenting.

### Development Cycle (repeating)

1. Scribe plans a Phase
2. Builder implements the Phase
3. Overseer reviews the Phase
4. If approved, return to step 1
5. If not approved, Builder addresses follow-ups
