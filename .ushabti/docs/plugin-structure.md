# Plugin Structure

## Overview

Ushabti is packaged as a Claude Code plugin. This document describes the plugin structure and development workflow.

## Directory Layout

```
.
├── .claude-plugin/
│   └── plugin.json       # Plugin manifest
├── agents/               # Agent definitions
│   ├── lawgiver.md
│   ├── artisan.md
│   ├── surveyor.md
│   ├── scribe.md
│   ├── builder.md
│   └── overseer.md
├── skills/               # Skill definitions (20 skills)
│   ├── using-skills/
│   ├── describe-*/       # 14 domain knowledge skills
│   ├── check-ushabti-prerequisites/
│   ├── find-current-phase/
│   ├── find-next-phase-number/
│   ├── find-next-step/
│   └── get-phase-status/
├── .ushabti/             # Project state (not part of plugin distribution)
├── CLAUDE.md
└── README.md
```

## Plugin Manifest

Located at `.claude-plugin/plugin.json`. Registers all agents and skills.

## Agent Format

Agents are markdown files with YAML front matter:

```yaml
---
name: agent-name
description: "Description for auto-delegation"
model: sonnet
color: blue
skills:
  - using-skills
tools: Read, Edit, Write, Bash, Glob, Skill
---

[Agent prompt content]
```

Key fields:
- `skills`: Skills preloaded at startup (typically just `using-skills`)
- `tools`: Tools the agent can use (include `Skill` for on-demand skill invocation)

## Skill Format

Skills are directories containing a `SKILL.md` file:

```
skills/skill-name/
└── SKILL.md
```

SKILL.md has YAML frontmatter:

```yaml
---
name: skill-name
description: What this skill provides
user-invocable: false
---

[Skill content]
```


## Validation

Validate the plugin after changes:
```bash
claude plugin validate .
```

## Installation

```
/plugin marketplace add adamrdrew/marketplace
/plugin install ushabti@adamrdrew
```

## Development

Ushabti is developed using itself. Changes go through the Phase loop: planned by Scribe, implemented by Builder, reviewed by Overseer.

When developing the plugin locally, note that invoking Ushabti agents uses the installed plugin version, not the local repository. To test changes, reinstall the plugin from the local path.
