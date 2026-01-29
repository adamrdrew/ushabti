# Skills Reference

## Overview

Skills are shared knowledge modules that agents reference. They provide context about Ushabti concepts without defining agent behavior. Skills live in `skills/` as directories, each containing a `SKILL.md` file.

## Skill Structure

Each skill is a directory under `skills/`:

```
skills/
├── ushabti-core/
│   └── SKILL.md
└── phase-files/
    └── SKILL.md
```

The `SKILL.md` file contains markdown documentation that agents can read for context.

## Available Skills

### ushabti-core

**Location**: `skills/ushabti-core/SKILL.md`

**Purpose**: Provides core Ushabti concepts that all agents need to understand.

**Contents**:
- Canonical location of Ushabti state (`.ushabti/`)
- Laws vs Style distinction
- The Phase loop (Plan, Build, Review)
- Agent role boundaries table
- Required inputs for agents
- Clarifying question policy

**Used by**: All agents

### phase-files

**Location**: `skills/phase-files/SKILL.md`

**Purpose**: Provides detailed reference for Phase file formats and conventions.

**Contents**:
- Phase directory structure
- `phase.md` format (intent, scope, constraints, acceptance criteria, risks)
- `steps.md` format (title, intent, work, done-when)
- `progress.yaml` schema (phase metadata, step tracking)
- `review.md` format (summary, verified, issues, follow-ups, decision)
- What makes a good Phase
- Status transitions

**Used by**: Scribe (planning), Builder (implementing), Overseer (reviewing)

## How Skills Are Used

Agents declare skill dependencies in their YAML front matter:

```yaml
---
name: scribe
skills:
  - ushabti-core
  - phase-files
---
```

When an agent runs, it has access to the content of its declared skills. This provides shared context without duplicating information across agent definitions.

## Skill Registration

Skills must be registered in `.claude-plugin/plugin.json`:

```json
{
  "skills": [
    "./skills/ushabti-core/",
    "./skills/phase-files/"
  ]
}
```

Per Law L04, all skill definitions must reside in `skills/`. Per Law L05, each skill must be a directory containing a `SKILL.md` file. Per Law L06, every skill must be registered in the plugin manifest.

## Adding New Skills

To add a new skill:

1. Create a directory under `skills/` (e.g., `skills/new-skill/`)
2. Create `SKILL.md` inside the directory
3. Add the skill to the `skills` array in `.claude-plugin/plugin.json`
4. Run `claude plugin validate .` to verify
5. Update agent front matter to include the new skill where needed
