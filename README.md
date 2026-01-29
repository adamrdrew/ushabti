# Ushabti

Ushabti is a lightweight, file-backed, agent-driven development system for Claude Code. It is inspired by spec-kit, but deliberately not tied to spec-driven development. Ushabti is optimized for tight iteration loops, not one-shot bootstrapping.

In ancient Egypt, ushabti were small figurines placed in tombs to do work for you in the afterlife. In this project, Ushabti are small agents that do focused work for you so you can stay at the decision layer.

## Installation

```
/plugin marketplace add adamrdrew/marketplace
/plugin install ushabti@adamrdrew
```

## Core Idea

Development happens in Phases.

A Phase is a bounded unit of work that is:
1. Planned
2. Implemented
3. Reviewed
4. Completed (green)

Once a Phase is green, you move on. No half-finished work. No drifting scope. No invisible state.

Everything is tracked in files inside the repo, not in chat history.

## The Phase Loop

```
Plan → Build → Review
        ↑       ↓
        └── refine ──┘
```

- Planning produces a Phase folder on disk
- Building modifies code and updates progress
- Review either:
  - declares the Phase complete, or
  - adds concrete follow-up steps and sends it back to Build

There is no implicit “done.” A Phase is done only when the Reviewer marks it green.

## Project Invariants

Ushabti separates what must never change from what evolves.

### Laws
(`.ushabti/laws.md`)

Project invariants that must always hold.

Examples:
- Architectural constraints
- Security rules
- Performance guarantees
- Forbidden patterns
- Non-negotiable principles

If a Phase violates a law, the Phase is invalid.

### Style
(`.ushabti/style.md`)

How the project is written and structured.

Examples:
- Directory layout
- Naming conventions
- Testing strategy
- Error handling
- Logging and observability norms

Style may evolve over time. Laws should not, except deliberately.

## The Agents

Ushabti uses five specialized agents, each with a narrow, enforced role.

### Ushabti Lawgiver

Purpose: Define and maintain project laws.
- Captures invariants into `.ushabti/laws.md`
- Asks clarifying questions when invariants are ambiguous
- Does not plan work
- Does not write code

This agent establishes the immovable ground rules of the project.

### Ushabti Artisan

Purpose: Define and maintain project style.
- Creates and updates `.ushabti/style.md`
- Ensures style does not contradict laws
- Encodes "how we build things here"

This agent shapes consistency and readability over time.

### Ushabti Surveyor

Purpose: Onboard existing projects by creating documentation.
- Explores the codebase to understand its structure
- Creates structured documentation in `.ushabti/docs/`
- Produces an index and working document for tracking progress
- Operates in four parts: Setup, Discovery, Writing, Handoff

This agent does not plan Phases, write code, review work, or define laws or style. It creates documentation only.

### Ushabti Scribe

Purpose: Plan a Phase.
- Creates a new Phase directory under `.ushabti/phases/`
- Writes:
  - phase.md (intent, scope, acceptance)
  - steps.md (explicit work steps)
  - progress.yaml (machine-tracked state)
- Keeps Phases intentionally small and reviewable

The Scribe never writes production code.

### Ushabti Builder

Purpose: Implement the Phase.
- Reads laws, style, and the Phase plan
- Implements steps in order
- Updates progress.yaml truthfully
- Adds new steps if missing work is discovered (never silently)

The Builder does not decide scope and does not declare completion.

### Ushabti Overseer

Purpose: Review and gate the Phase.
- Verifies acceptance criteria
- Verifies laws and style compliance
- Reviews code and tests
- Adds required follow-up steps if needed
- Declares the Phase green when complete

No Phase is complete without Overseer approval.

## Repository Structure

```
.
├── .claude-plugin/
│   └── plugin.json       # Claude Code plugin manifest
├── .ushabti/
│   ├── laws.md           # Project invariants
│   ├── style.md          # Project conventions
│   └── phases/
│       └── NNNN-slug/
│           ├── phase.md
│           ├── steps.md
│           ├── progress.yaml
│           └── review.md
├── agents/               # Agent definitions (markdown with YAML front matter)
├── skills/               # Skill definitions (directories with SKILL.md)
├── CLAUDE.md
└── README.md
```

Everything Ushabti needs to reason about the project lives inside the repo.

## How You Use Ushabti (Typical Flow)

1. Bootstrap
   - Tell Lawgiver the project invariants
   - Tell Artisan the project style preferences
2. Start a Phase
   - Ask Scribe to plan the next Phase
3. Build
   - Hand the Phase to Builder
   - Let it implement and update progress
4. Review
   - Hand the Phase to Overseer
   - Address follow-ups if required
5. Repeat
   - Once green, ask Scribe to plan the next Phase

You stay in control of what gets built. Ushabti handles how the work is executed and tracked.

## Design Philosophy

- Iteration over ceremony
- Files over prompts
- Explicit state over vibes
- Small Phases beat big specs
- Review is mandatory, not optional

Ushabti is not trying to replace engineering judgment. It exists to amplify it without losing control.

## Status

Ushabti is under active design.

Agent prompts, schemas, and conventions will evolve—but the core loop and roles are intentional and stable.

## Development

Ushabti is developed using itself. All changes go through the Phase loop: planned by Scribe, implemented by Builder, reviewed by Overseer.