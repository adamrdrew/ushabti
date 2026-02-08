# Getting Started with Ushabti

Welcome to Ushabti — a file-backed, agent-driven development system for Claude Code.

## What is Ushabti?

Ushabti transforms how you develop software with Claude Code by introducing structure, accountability, and explicit state. Instead of drifting through chat history, development happens in bounded **Phases** that are planned, built, reviewed, and completed. Everything lives in files inside your repository, not in ephemeral conversation context.

In ancient Egypt, ushabti were small figurines placed in tombs to perform work in the afterlife. In this system, Ushabti are specialized agents that handle focused work, letting you stay at the decision layer.

## Prerequisites

Before installing Ushabti, you need:

- **Claude Code**: Ushabti is a Claude Code plugin. Install Claude Code from [claude.ai/code](https://claude.ai/code)
- **A project**: Either a new repository or an existing codebase you want to develop with structured Phases

## Installation

Install Ushabti from the Claude Code plugin marketplace:

```
/plugin marketplace add adamrdrew/marketplace
/plugin install ushabti@adamrdrew
```

### Permissions Configuration

Ushabti skills use read-only bash commands to inspect repository state. Following the principle of least privilege, you need to grant specific command permissions.

Add the following to your project's `.claude/settings.json` or `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash([ -f *)",
      "Bash([ -d *)",
      "Bash(ls *)",
      "Bash(grep *)",
      "Bash(awk *)",
      "Bash(basename *)",
      "Bash(echo *)",
      "Bash(sed *)",
      "Bash(sort *)",
      "Bash(tail *)",
      "Bash(printf *)"
    ]
  }
}
```

These permissions allow Ushabti to find phases, check for required files, and inspect repository state without write access.

## The Seven Agents

Ushabti uses seven specialized agents, each with a narrow, enforced role. No agent can perform functions assigned to another.

### Ushabti Lawgiver

**Purpose**: Define and maintain project laws — the absolute invariants that must always hold.

**Use when**: You need to capture architectural constraints, security rules, performance guarantees, or forbidden patterns. Run this at project bootstrap or when core invariants change.

**Cannot**: Plan Phases, write code, or define style.

**Invocation**: `/agent lawgiver`

### Ushabti Artisan

**Purpose**: Define and maintain project style — how you build things.

**Use when**: You need to establish conventions for directory layout, naming, testing strategy, error handling, or observability. Run this during bootstrap or when conventions evolve.

**Cannot**: Define laws or write production code.

**Invocation**: `/agent artisan`

### Ushabti Surveyor

**Purpose**: Onboard existing projects by creating structured documentation.

**Use when**: You're introducing Ushabti to an existing codebase. Surveyor explores the repository and creates documentation that other agents consult during planning and development.

**Cannot**: Plan Phases, write code, review work, or define laws/style.

**Invocation**: `/agent surveyor`

### Ushabti Scribe

**Purpose**: Plan Phases with explicit steps and acceptance criteria.

**Use when**: You're ready to start a new unit of work. Scribe creates the Phase directory, writes the intent and scope, defines ordered steps, and prepares the progress tracker.

**Cannot**: Write production code or declare work complete.

**Invocation**: `/agent scribe`

### Ushabti Builder

**Purpose**: Implement Phase steps exactly as planned.

**Use when**: You have a planned Phase ready to build. Builder reads laws, style, and the plan, then implements steps in order, updating progress truthfully.

**Cannot**: Change scope, improvise beyond the plan, or approve its own work.

**Invocation**: `/agent builder`

### Ushabti Overseer

**Purpose**: Review and gate Phases. Final authority on correctness.

**Use when**: Builder has finished all steps and the Phase is ready for review. Overseer verifies acceptance criteria, checks law and style compliance, and either declares the Phase complete or adds follow-up steps.

**Cannot**: Write production code or plan new Phases.

**Invocation**: `/agent overseer`

### Ushabti Vizier

**Purpose**: Provide advisory guidance without modifying the codebase.

**Use when**: You have questions about your code, need to evaluate technical options, want to identify risks, or need suggestions for high-impact work. Vizier maintains memory but never changes code, laws, style, or docs.

**Cannot**: Modify any files except `.ushabti/vizier.md` (its memory). Cannot plan, build, or review Phases.

**Invocation**: `/agent vizier`

## The Card System

Ushabti uses Hieroglyphs-compatible cards to capture ideas, technical debt, and future work that doesn't fit into the current Phase. Cards provide a structured way to record work without bloating your current Phase or losing track of good ideas.

### What Are Cards?

Cards are directories containing a `card.md` file stored in `.ushabti/cards/{slug}/`. Each card includes:

- **id**: UUID v4 identifier (globally unique)
- **slug**: Human-readable kebab-case identifier derived from title
- **title**: Brief, descriptive name
- **created**: ISO 8601 timestamp when the card was created
- **updated**: ISO 8601 timestamp of last modification
- **priority**: low, medium, or high
- **status**: todo, backlog, in-progress, or done
- **type**: bug or feature
- **tags**: Array of categorization tags (may be empty)

The card body contains markdown sections:
- **Overview**: Why this card exists (context and motivation)
- **Requirements**: What should be done (specific acceptance criteria)

### When to Create Cards

Create cards to capture:
- **Improvement ideas** discovered during planning or implementation
- **Technical debt** that's out of scope for the current Phase
- **Feature requests** to consider later
- **Refactoring opportunities** noticed during development

Cards let you acknowledge work without derailing your current Phase.

### Card Workflow

1. **Create**: Use the `create-card` skill to generate a new card
   ```
   /skill create-card
   ```
   The skill generates a UUID, derives a slug from the title, and creates the card with proper Hieroglyphs frontmatter.

2. **List**: View cards using the `list-cards` skill
   ```
   /skill list-cards
   ```
   This shows card slugs, titles, status, priority, and type. You can filter by status (e.g., only `todo` cards).

3. **Plan Phase**: When ready to work on a card, tell Scribe to create a Phase from it
   ```
   /agent scribe
   "Create a Phase based on card improve-error-handling"
   ```
   Scribe reads the card's Overview and Requirements sections to inform Phase planning.

4. **Complete**: After the Phase completes, Overseer marks the card as done
   ```
   /skill complete-card
   ```
   This updates the card's status to `done` (cards remain in `.ushabti/cards/` but are considered closed).

### Example: Card Format

```markdown
---
created: 2026-02-08T14:30:00Z
id: 550e8400-e29b-41d4-a716-446655440000
priority: medium
slug: add-validation-to-card-creation
status: todo
tags: []
title: Add validation to card creation
type: feature
updated: 2026-02-08T14:30:00Z
---

# Overview

Currently cards can be created with invalid priority values,
which breaks the list-cards skill's filtering logic.

# Requirements

- Add priority validation to create-card skill
- Verify priority is exactly "low", "medium", or "high"
- Fail gracefully with clear error if invalid
```

This card would be saved as `.ushabti/cards/add-validation-to-card-creation/card.md`

### Example: Planning from a Card

When you're ready to work on card `add-validation-to-card-creation`:

1. Tell Scribe: "Create a Phase based on card add-validation-to-card-creation"
2. Scribe reads the card file's Overview and Requirements sections
3. The resulting `phase.md` includes metadata: `card: add-validation-to-card-creation`
4. After Overseer approves the Phase, Overseer marks the card as done (status: done)

### Tips

- **Keep cards small**: If a card describes more than one Phase of work, create multiple cards
- **Use status field**: Cards track lifecycle with status (todo → in-progress → done), not archival directories
- **Use cards during Phases**: Discovered technical debt? Create a card for it instead of scope creeping the current Phase
- **Cards are optional**: Not everything needs a card. Use them when capturing the idea is more valuable than acting on it immediately
- **Hieroglyphs compatibility**: Cards use the Hieroglyphs format, enabling future integration with the Hieroglyphs task management tool

## The Development Loop

All development in Ushabti follows a three-step cycle:

```
Plan → Build → Review
        ↑       ↓
        └── refine ──┘
```

### Plan (Scribe)

Scribe creates a Phase directory with:
- `phase.md`: Intent, scope, and acceptance criteria
- `steps.md`: Ordered implementation steps with done-when conditions
- `progress.yaml`: Machine-tracked state
- `review.md`: Review scaffold

Phases are intentionally small — 5 to 15 steps, completable in one focused session.

### Build (Builder)

Builder implements steps in the order defined by Scribe. After completing each step, Builder updates `progress.yaml` to mark it implemented and record which files were touched.

If Builder discovers missing work, it does not improvise silently — it adds new steps to the plan and proceeds.

### Review (Overseer)

Overseer verifies the Phase against acceptance criteria and checks compliance with laws and style. Overseer either:
- **Declares the Phase complete** (status: `complete`)
- **Adds follow-up steps** and sends the Phase back to Builder (status: `building`)

**No Phase is complete without Overseer approval.** This is non-negotiable.

## When to Use Each Agent

| Situation | Agent | Why |
|-----------|-------|-----|
| Starting a new project | Lawgiver → Artisan → Surveyor | Establish invariants, conventions, and baseline docs |
| Onboarding an existing project | Surveyor → Lawgiver → Artisan | Document first, then establish rules |
| Capturing ideas for later | (use cards) | Create cards for work that's not in scope right now |
| Planning the next feature | Scribe | Define the Phase with steps and acceptance criteria |
| Planning from a card | Scribe | Tell Scribe to create a Phase based on a card slug |
| Implementing a planned Phase | Builder | Execute steps as written |
| Checking if Phase is done | Overseer | Verify acceptance and gate completion |
| Asking questions | Vizier | Get guidance without modifying anything |
| Evaluating technical options | Vizier | Compare tradeoffs before planning |
| Remembering project context | Vizier | Ask Vizier to store decisions or patterns in memory |

## What Happens When

### First Time Setup (New Project)

1. **Lawgiver**: Capture project laws
2. **Artisan**: Define project style
3. **Surveyor** (optional but recommended): Create initial docs scaffold
4. **Scribe**: Plan your first Phase
5. **Builder**: Implement it
6. **Overseer**: Review and approve
7. Repeat from step 4

### First Time Setup (Existing Project)

1. **Surveyor**: Explore and document the codebase
2. **Lawgiver**: Capture project invariants
3. **Artisan**: Define project style
4. **Scribe**: Plan your first Phase (Scribe consults the docs Surveyor created)
5. **Builder**: Implement it (Builder uses docs for context)
6. **Overseer**: Review and approve (Overseer verifies docs are current)
7. Repeat from step 4

### Ongoing Development

Once bootstrap is complete, you cycle through the Plan → Build → Review loop:

1. **Plan**: Ask Scribe to plan the next Phase
2. **Build**: Hand the Phase to Builder
3. **Review**: Hand the Phase to Overseer
4. If Overseer adds follow-ups, Builder implements them and Overseer reviews again
5. Once Overseer marks the Phase complete, return to step 1

## File Structure

Ushabti creates this structure in your repository:

```
.ushabti/
├── laws.md           # Project invariants (absolute constraints)
├── style.md          # Conventions (how you build)
├── docs/             # Project documentation (created by Surveyor)
│   ├── index.md
│   └── *.md
├── cards/            # Work items (Hieroglyphs-compatible)
│   └── {slug}/
│       └── card.md
└── phases/
    └── NNNN-slug/    # Zero-padded sequential phase directories
        ├── phase.md
        ├── steps.md
        ├── progress.yaml
        └── review.md
```

Everything Ushabti needs lives in files. No hidden state. No chat-only context.

## Next Steps

- **New project?** Read [Greenfield Projects](greenfield.md)
- **Existing codebase?** Read [Brownfield Projects](brownfield.md)
- **Want advanced patterns?** See [Tips and Tricks](tips-and-tricks.md)

---

Ready to build. Let Ushabti handle the how.
