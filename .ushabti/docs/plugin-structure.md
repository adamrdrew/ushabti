# Plugin Structure

## Overview

Ushabti is packaged as a Claude Code plugin. This document describes the plugin structure, requirements, and how to validate and distribute the plugin.

## Directory Layout

```
.
├── .claude-plugin/
│   └── plugin.json       # Plugin manifest (required)
├── agents/               # Agent definitions
│   ├── lawgiver.md
│   ├── artisan.md
│   ├── surveyor.md
│   ├── scribe.md
│   ├── builder.md
│   └── overseer.md
├── skills/               # Skill definitions
│   ├── ushabti-core/
│   │   └── SKILL.md
│   └── phase-files/
│       └── SKILL.md
├── .ushabti/             # Project state (not part of plugin)
├── CLAUDE.md             # Claude Code guidance
└── README.md             # Project documentation
```

## Plugin Manifest

The plugin manifest lives at `.claude-plugin/plugin.json`.

### Current Manifest

```json
{
  "name": "ushabti",
  "version": "1.1.1",
  "description": "File-backed, agent-driven development system with specialized agents for planning, building, and reviewing Phases",
  "author": {
    "name": "Adam Drew",
    "email": "adamrdrew@live.com",
    "url": "https://github.com/adamrdrew/ushabti"
  },
  "repository": "https://github.com/adamrdrew/ushabti",
  "license": "MIT",
  "keywords": ["development", "agents", "phases", "planning", "review"],
  "agents": [
    "./agents/lawgiver.md",
    "./agents/artisan.md",
    "./agents/surveyor.md",
    "./agents/scribe.md",
    "./agents/builder.md",
    "./agents/overseer.md"
  ],
  "skills": [
    "./skills/ushabti-core/",
    "./skills/phase-files/"
  ]
}
```

## Agent Requirements

Per project laws (L02, L03):

- All agents must reside in `agents/`
- Agent files must be markdown with YAML front matter

### Agent File Format

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

[Agent prompt content]
```

### Front Matter Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Agent identifier |
| `description` | string | Brief purpose statement |
| `model` | string | LLM model (e.g., "sonnet") |
| `color` | string | Display color in Claude Code UI |
| `skills` | array | List of skill names the agent can access |

## Skill Requirements

Per project laws (L04, L05):

- All skills must reside in `skills/`
- Each skill must be a directory containing `SKILL.md`

### Skill Directory Format

```
skills/
└── skill-name/
    └── SKILL.md
```

The `SKILL.md` file contains markdown documentation that agents can reference.

## Manifest Completeness

Per law L06, every agent and skill must be registered in `plugin.json`:

- Every file in `agents/` needs a corresponding entry in `agents` array
- Every directory in `skills/` needs a corresponding entry in `skills` array

## Validation

Per law L07, validate the plugin when adding agents or skills.

### Validation Command

```bash
claude plugin validate .
```

Run from repository root. Must exit with success (exit code 0).

### What Validation Checks

- JSON schema validity of `plugin.json`
- All referenced agent files exist
- All referenced skill directories exist
- Agent files have valid YAML front matter
- Skill directories contain `SKILL.md`

## Version Management

Per law L08, increment the `version` field in `plugin.json` when any development Phase completes.

**Exception**: Documentation-only Phases that do not affect plugin behavior may skip the version bump if explicitly noted in the Phase plan.

### Version Format

Use semantic versioning: `MAJOR.MINOR.PATCH`

## Installation

Users install Ushabti from the marketplace:

```
/plugin marketplace add adamrdrew/marketplace
/plugin install ushabti@adamrdrew
```

## Enabling the Plugin

Once installed, enable the plugin in `.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "ushabti@adamrdrew": true
  }
}
```

## Development Notes

Ushabti is developed using itself (dogfooding). All changes go through the Phase loop:
1. Scribe plans the Phase
2. Builder implements the Phase
3. Overseer reviews the Phase

This ensures the system remains coherent and well-tested.
