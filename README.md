# 𓀀 Ushabti

<p align="center">
   <img src="images/logo.png" alt="Ushabti logo" width="360" style="max-width: 100%; height: auto;" />
</p>

<p align="center">
   <em>Your development practices have been weighed against Ma’at and found wanting. Come. Let us build.</em>
</p>

Ushabti is a lightweight, file-backed, agent-driven development system for Claude Code. It is inspired by spec-kit, but deliberately not tied to spec-driven development. Ushabti is optimized for tight iteration loops, not one-shot bootstrapping.

In ancient Egypt, ushabti were small figurines placed in tombs to do work for you in the afterlife. In this project, Ushabti are small agents that do focused work for you so you can stay at the decision layer.

## 🧱 Installation

```
/plugin marketplace add adamrdrew/marketplace
/plugin install ushabti@adamrdrew
```

### Permissions Configuration

Ushabti skills use read-only bash commands to inspect repository state (e.g., finding the current phase, checking for required files). Following the principle of least privilege, Ushabti grants only the specific commands needed.

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

These permissions grant access to common read-only commands that skills use for file inspection and text processing. If you add new skills that require additional commands, update this list accordingly.

## 𓁗 Core Idea

Development happens in Phases.

A Phase is a bounded unit of work that is:
1. Planned
2. Implemented
3. Reviewed
4. Completed (green)

Once a Phase is green, you move on. No half-finished work. No drifting scope. No invisible state.

Everything is tracked in files inside the repo, not in chat history.

## 𓁀 The Phase Loop

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

## 📜 Project Invariants

Ushabti separates what must never change from what evolves.

### ⚖️ Laws
(`.ushabti/laws.md`)

Project invariants that must always hold.

Examples:
- Architectural constraints
- Security rules
- Performance guarantees
- Forbidden patterns
- Non-negotiable principles

If a Phase violates a law, the Phase is invalid.

### 🖋️ Style
(`.ushabti/style.md`)

How the project is written and structured.

Examples:
- Directory layout
- Naming conventions
- Testing strategy
- Error handling
- Logging and observability norms

Style may evolve over time. Laws should not, except deliberately.

## 🏺 The Agents

Ushabti uses seven specialized agents, each with a narrow, enforced role.

### 🦅 Ushabti Lawgiver

Purpose: Define and maintain project laws.
- Captures invariants into `.ushabti/laws.md`
- Asks clarifying questions when invariants are ambiguous
- Does not plan work
- Does not write code

This agent establishes the immovable ground rules of the project.

### 🧱 Ushabti Artisan

Purpose: Define and maintain project style.
- Creates and updates `.ushabti/style.md`
- Ensures style does not contradict laws
- Encodes "how we build things here"

This agent shapes consistency and readability over time.

### 🐊 Ushabti Surveyor

Purpose: Onboard existing projects by creating documentation.
- Explores the codebase to understand its structure
- Creates structured documentation in `.ushabti/docs/`
- Produces an index and working document for tracking progress
- Operates in four parts: Setup, Discovery, Writing, Handoff

This agent does not plan Phases, write code, review work, or define laws or style. It creates documentation only.

The documentation Surveyor creates becomes a critical resource for other agents. Once created, these docs are consulted during planning and updated during development to stay current with the codebase.

### 📜 Ushabti Scribe

Purpose: Plan a Phase.
- Creates a new Phase directory under `.ushabti/phases/`
- Writes:
  - phase.md (intent, scope, acceptance)
  - steps.md (explicit work steps)
  - progress.yaml (machine-tracked state)
- Keeps Phases intentionally small and reviewable

The Scribe never writes production code.

### 🧱 Ushabti Builder

Purpose: Implement the Phase.
- Reads laws, style, and the Phase plan
- Implements steps in order
- Updates progress.yaml truthfully
- Adds new steps if missing work is discovered (never silently)

The Builder does not decide scope and does not declare completion.

### 👁️ Ushabti Overseer

Purpose: Review and gate the Phase.
- Verifies acceptance criteria
- Verifies laws and style compliance
- Reviews code and tests
- Adds required follow-up steps if needed
- Declares the Phase green when complete

No Phase is complete without Overseer approval.

### 🧙 Ushabti Vizier

Purpose: Advisory agent for questions and guidance.
- Answers questions about the codebase
- Evaluates technical options and tradeoffs
- Identifies risks and technical debt
- Suggests high-impact work
- Maintains memory at `.ushabti/vizier.md`
- Curates a Reference Library of official documentation for project technologies

Vizier does not plan, build, or review Phases. It does not modify code, laws, style, or documentation. If asked to make changes, Vizier offers to create a Scribe prompt instead.

## 🏛️ Repository Structure

```
.
├── .claude-plugin/
│   └── plugin.json       # Claude Code plugin manifest
├── .githooks/
│   └── pre-commit        # Auto-updates skill catalog
├── .ushabti/
│   ├── laws.md           # Project invariants
│   ├── style.md          # Project conventions
│   ├── docs/             # Project documentation (created by Surveyor)
│   └── phases/
│       └── NNNN-slug/
│           ├── phase.md
│           ├── steps.md
│           ├── progress.yaml
│           └── review.md
├── agents/               # Agent definitions
├── skills/               # Skill definitions (20 skills)
├── scripts/
│   └── reconcile-skills.sh
├── CLAUDE.md
└── README.md
```

Everything Ushabti needs to reason about the project lives inside the repo.

## 🧭 How You Use Ushabti (Typical Flow)

### 🌅 New Projects

1. Bootstrap
   - Tell Lawgiver the project invariants
   - Tell Artisan the project style preferences
   - Run Surveyor to create initial documentation
2. Start a Phase
   - Ask Scribe to plan the next Phase
3. Build
   - Hand the Phase to Builder
   - Let it implement, update progress, and update docs
4. Review
   - Hand the Phase to Overseer
   - Address follow-ups if required (including docs reconciliation)
5. Repeat
   - Once green, ask Scribe to plan the next Phase

### 🏺 Existing Projects (Onboarding)

1. Survey
   - Run Surveyor to explore and document the existing codebase
   - Surveyor creates `.ushabti/docs/` with structured documentation
2. Establish Rules
   - Run Lawgiver to capture project invariants
   - Run Artisan to define project style
3. Begin Phase Loop
   - Scribe consults the docs when planning Phases
   - Builder uses docs for context and updates them during implementation
   - Overseer verifies docs are current before marking Phases green

You stay in control of what gets built. Ushabti handles how the work is executed and tracked.

## 📜 Documentation in the Loop

The `.ushabti/docs/` directory is not just onboarding material—it's a living resource that stays current with the codebase.

### ♻️ How Docs Integrate with the Phase Loop

```
Surveyor creates docs
        ↓
┌─────────────────────────────────────────┐
│  Plan → Build → Review                  │
│    ↑       ↑       ↓                    │
│ consult  update  verify                 │
│  docs    docs    docs                   │
└─────────────────────────────────────────┘
```

- **Scribe** consults docs when planning to understand existing systems
- **Builder** uses docs for context and updates them when code changes
- **Overseer** verifies docs are reconciled before marking a Phase green

A Phase cannot be marked complete if documentation is out of sync with the code changes made during that Phase.

### 📚 What Gets Documented

Surveyor creates documentation covering:
- Architecture and system overview
- Agent purposes and boundaries
- Component and subsystem reference
- Configuration and settings
- File formats and schemas

These docs reduce discovery time for agents and provide a reliable source of truth about the repository.

## ☀️ Design Philosophy

- Iteration over ceremony
- Files over prompts
- Explicit state over vibes
- Small Phases beat big specs
- Review is mandatory, not optional

Ushabti is not trying to replace engineering judgment. It exists to amplify it without losing control.

## 🏺 Onboarding an Existing Project

Ushabti works with existing codebases, not just greenfield projects. To onboard:

1. **Install Ushabti** (see Installation above)

2. **Run Surveyor first**
   - Surveyor explores your codebase and creates structured documentation
   - This produces `.ushabti/docs/` with an index and system docs
   - Documentation is tailored to what agents need to know

3. **Establish project rules**
   - Run Lawgiver to capture invariants (what must never change)
   - Run Artisan to define style (how you build things)

4. **Start the Phase loop**
   - With docs, laws, and style in place, Scribe can plan Phases effectively
   - Agents use the docs to understand your codebase without extensive exploration

The Surveyor step is critical. Without docs, Scribe will ask you to run Surveyor before planning. The docs become the shared knowledge base that accelerates all subsequent work.

## 🏜️ Status

Ushabti is under active design.

Agent prompts, schemas, and conventions will evolve—but the core loop and roles are intentional and stable.

## 🧱 Development

Ushabti is developed using itself. All changes go through the Phase loop: planned by Scribe, implemented by Builder, reviewed by Overseer.

### Setup

After cloning, enable the git hooks:
```bash
git config core.hooksPath .githooks
```

This enables the pre-commit hook that maintains the skill catalog.

### Skills

Skills provide domain knowledge that agents invoke on-demand. Agents preload a single `using-skills` skill containing the skill catalog, then invoke specific skills via the Skill tool as needed.

To add a skill:
1. Create `skills/skill-name/SKILL.md`
2. Add to `plugin.json`
3. Commit — the hook auto-updates the catalog