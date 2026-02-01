# Agent Reference

## Overview

Ushabti uses six specialized agents, each with a narrow, enforced role. Agents have hard boundaries: they cannot perform functions assigned to other agents.

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

## Skill Access

All agents preload the `using-skills` skill at startup, which provides:
- Instructions on using the Skill tool
- A catalog of all available skills

Agents invoke skills on-demand during execution:
```
Skill(describe-progress-file)
```

This keeps agent startup lightweight while providing access to the full skill library.

## Lawgiver

**File**: `agents/lawgiver.md`

**Purpose**: Capture and maintain project invariants (laws).

**Tools**: Read, Edit, Write, Bash, Glob, Skill

**Inputs**: `.ushabti/laws.md` (if exists), user-provided constraints

**Outputs**: `.ushabti/laws.md`

**Handoff**: Recommends Artisan for style definition.

## Artisan

**File**: `agents/artisan.md`

**Purpose**: Define and maintain project style conventions.

**Tools**: Read, Edit, Write, Bash, Glob, Skill

**Inputs**: `.ushabti/laws.md` (mandatory), `.ushabti/style.md` (if exists), repository structure

**Outputs**: `.ushabti/style.md`

**Handoff**: Recommends Surveyor (if no docs) or Scribe.

## Surveyor

**File**: `agents/surveyor.md`

**Purpose**: Onboard existing projects by creating structured documentation.

**Tools**: Read, Edit, Write, Bash, Glob, Grep, Skill

**Procedure**:
1. Setup: Create `.ushabti/docs/`, `index.md`, `surveyor.md`
2. Discovery: Explore codebase, record observations, create plan
3. Writing: Create documentation files per plan
4. Handoff: Verify completeness, commit, recommend next agent

**Outputs**: `.ushabti/docs/` with index and system documentation

**Handoff**: Recommends Lawgiver, Artisan, or Scribe depending on what exists.

## Scribe

**File**: `agents/scribe.md`

**Purpose**: Plan Phases with steps and acceptance criteria.

**Tools**: Read, Edit, Write, Bash, Glob, Skill

**Inputs**: `.ushabti/laws.md`, `.ushabti/style.md`, existing phases, user's goal

**Outputs**:
- `.ushabti/phases/NNNN-slug/phase.md`
- `.ushabti/phases/NNNN-slug/steps.md`
- `.ushabti/phases/NNNN-slug/progress.yaml`
- `.ushabti/phases/NNNN-slug/review.md`

**Handoff**: Hands off to Builder.

## Builder

**File**: `agents/builder.md`

**Purpose**: Implement Phase steps exactly as planned.

**Tools**: Read, Edit, Write, Bash, Glob, Grep, LSP, Skill

**Inputs**: `.ushabti/laws.md`, `.ushabti/style.md`, Phase directory, relevant code

**Outputs**: Implemented code, updated `progress.yaml`

**Handoff**: Hands off to Overseer when all steps complete.

## Overseer

**File**: `agents/overseer.md`

**Purpose**: Review and gate Phases. Final authority on Phase correctness.

**Tools**: Read, Edit, Write, Bash, Glob, Grep, LSP, Skill

**Inputs**: `.ushabti/laws.md`, `.ushabti/style.md`, Phase directory, changed code/tests

**Outputs**: Updated `progress.yaml`, `review.md`, follow-up steps if needed

**Decision outcomes**:
- **Green**: Phase complete, status set to `complete`
- **Needs work**: Follow-up steps added, status set to `building`, hands back to Builder

## Agent File Format

```yaml
---
name: agent-name
description: "Brief description for auto-delegation"
model: sonnet
color: blue
skills:
  - using-skills
tools: Read, Edit, Write, Bash, Glob, Skill
---

[Agent prompt content]
```

**Front matter fields**:
- `name`: Agent identifier
- `description`: Purpose statement (used for auto-delegation)
- `model`: LLM model to use
- `color`: Display color in Claude Code
- `skills`: Skills to preload (typically just `using-skills`)
- `tools`: Tools the agent can use
