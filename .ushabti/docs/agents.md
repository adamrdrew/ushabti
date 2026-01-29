# Agent Reference

## Overview

Ushabti uses six specialized agents, each with a narrow, enforced role. Agents have hard boundaries: they cannot perform functions assigned to other agents. This separation ensures clarity and prevents scope drift.

All agent definitions live in `agents/` as markdown files with YAML front matter.

## Agent Summary

| Agent | Purpose | Cannot Do |
|-------|---------|-----------|
| Lawgiver | Define project invariants | Plan, code, or style |
| Artisan | Define project style | Define laws or write code |
| Surveyor | Create project documentation | Plan, code, review, define laws/style |
| Scribe | Plan Phases | Write production code |
| Builder | Implement Phases | Change scope or approve work |
| Overseer | Review and approve Phases | Write code or plan |

## Lawgiver

**File**: `agents/lawgiver.md`

**Purpose**: Capture and maintain project invariants (laws).

**Responsibilities**:
- Extract invariant constraints from the user
- Resolve ambiguity with minimal clarifying questions
- Write or update `.ushabti/laws.md`

**Inputs**:
- `.ushabti/laws.md` (if it exists)
- User-provided constraints

**Outputs**:
- `.ushabti/laws.md`

**Handoff**: Recommends Artisan for style definition.

## Artisan

**File**: `agents/artisan.md`

**Purpose**: Define and maintain project style conventions.

**Responsibilities**:
- Create and update `.ushabti/style.md`
- Ensure style does not contradict laws
- Encode "how we build things here"

**Inputs**:
- `.ushabti/laws.md` (mandatory)
- `.ushabti/style.md` (if it exists)
- Repository structure and existing code

**Outputs**:
- `.ushabti/style.md`

**Handoff**: Recommends Scribe to plan next Phase.

## Surveyor

**File**: `agents/surveyor.md`

**Purpose**: Onboard existing projects by creating structured documentation.

**Responsibilities**:
- Explore the codebase to understand its structure
- Create documentation in `.ushabti/docs/`
- Produce an index and working document for tracking progress

**Procedure**:
1. **Setup**: Create `.ushabti/docs/`, `index.md`, `surveyor.md`
2. **Discovery**: Explore codebase, record observations, create documentation plan
3. **Writing**: Create documentation files per plan
4. **Handoff**: Verify completeness, commit, recommend next agent

**Inputs**:
- Repository files and structure
- Existing `.ushabti/docs/` content (if resuming)

**Outputs**:
- `.ushabti/docs/index.md`
- `.ushabti/docs/surveyor.md`
- Documentation files per plan

**Handoff**: Recommends Lawgiver, Artisan, or Scribe depending on what exists.

## Scribe

**File**: `agents/scribe.md`

**Purpose**: Plan Phases with steps and acceptance criteria.

**Responsibilities**:
- Create Phase directories under `.ushabti/phases/`
- Write `phase.md`, `steps.md`, `progress.yaml`, `review.md` (scaffold)
- Keep Phases intentionally small and reviewable

**Inputs**:
- `.ushabti/laws.md`
- `.ushabti/style.md`
- Existing Phase directories
- User's stated goal

**Outputs**:
- `.ushabti/phases/NNNN-slug/phase.md`
- `.ushabti/phases/NNNN-slug/steps.md`
- `.ushabti/phases/NNNN-slug/progress.yaml`
- `.ushabti/phases/NNNN-slug/review.md`

**Handoff**: Hands off to Builder for implementation.

## Builder

**File**: `agents/builder.md`

**Purpose**: Implement Phase steps exactly as planned.

**Responsibilities**:
- Implement each step in order
- Follow laws and style without exception
- Update `progress.yaml` truthfully
- Add new steps if missing work is discovered (never silently)

**Inputs**:
- `.ushabti/laws.md`
- `.ushabti/style.md`
- Phase directory (`phase.md`, `steps.md`, `progress.yaml`)
- Relevant existing code

**Outputs**:
- Implemented code/files per steps
- Updated `progress.yaml`

**Handoff**: Hands off to Overseer for review when all steps complete.

## Overseer

**File**: `agents/overseer.md`

**Purpose**: Review and gate Phases. Final authority on Phase correctness.

**Responsibilities**:
- Verify acceptance criteria are satisfied
- Verify laws and style compliance
- Review code and tests
- Add follow-up steps if issues found
- Declare Phase green when complete

**Inputs**:
- `.ushabti/laws.md`
- `.ushabti/style.md`
- Phase directory (all files)
- Code and tests changed during Phase

**Outputs**:
- Updated `progress.yaml` (reviewed flags, status)
- Updated `review.md` (findings and decision)
- Follow-up steps in `steps.md` (if needed)

**Decision outcomes**:
- **Green**: Phase complete, status set to `complete`, all steps marked reviewed
- **Needs work**: Follow-up steps added, status set to `building`, hands back to Builder

## Agent File Format

All agents use markdown with YAML front matter:

```markdown
---
name: agent-name
description: "Brief description"
model: sonnet
color: blue
skills:
  - ushabti-core
  - phase-files
---

[Agent prompt content in markdown]
```

**Front matter fields**:
- `name`: Agent identifier
- `description`: Brief purpose statement
- `model`: LLM model to use
- `color`: Display color in Claude Code
- `skills`: List of skills the agent can access

## Skills Dependency

Most agents depend on two skills:
- `ushabti-core`: Core concepts (laws vs style, Phase loop, agent boundaries)
- `phase-files`: Phase file formats and conventions

These skills provide shared context that agents reference during operation.
