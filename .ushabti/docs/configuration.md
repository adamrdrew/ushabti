# Configuration Reference

## Overview

Ushabti uses several configuration files for project constraints, conventions, and plugin registration. This document details the structure and purpose of each.

## Configuration Files

| File | Purpose | Managed By |
|------|---------|------------|
| `.ushabti/laws.md` | Project invariants | Lawgiver |
| `.ushabti/style.md` | Project conventions | Artisan |
| `.claude-plugin/plugin.json` | Plugin manifest | Manual or Builder |
| `.claude/settings.json` | Plugin enablement | Claude Code |
| `.claude/settings.local.json` | Local permissions | Claude Code |

## laws.md

**Location**: `.ushabti/laws.md`

**Purpose**: Defines non-negotiable invariants that must hold across all Phases, implementations, and refactors.

### Structure

```markdown
# Project Laws

## Preamble

Short statement describing the purpose of these laws and how they are enforced.

## Laws

### L01 — Short descriptive name

- **Rule:** Clear, testable invariant
- **Rationale:** Why this invariant exists
- **Enforcement:** How a reviewer verifies compliance
- **Scope:** Where it applies (optional)
- **Exceptions:** Explicit exceptions, or "None"

### L02 — ...

## Revision History

| Date | Change |
|------|--------|
| YYYY-MM-DD | Description |
```

### Guidelines

- Laws must be specific, verifiable, and unambiguous
- Use MUST / MUST NOT / SHOULD language
- Avoid vague statements ("clean," "simple," "nice")
- Merge overlapping laws instead of duplicating

### Current Laws (Ushabti)

| ID | Name | Summary |
|----|------|---------|
| L01 | Claude Code Plugin Compliance | Plugin must pass validation |
| L02 | Agent Location | Agents must be in `agents/` |
| L03 | Agent File Format | Agents use markdown with YAML front matter |
| L04 | Skill Location | Skills must be in `skills/` |
| L05 | Skill Directory Structure | Skills are directories with `SKILL.md` |
| L06 | Plugin Manifest Completeness | All agents/skills registered in manifest |
| L07 | Plugin Validation on Addition | Validate plugin when adding agents/skills |
| L08 | Version Increment on Phase Completion | Bump version when Phase completes |

## style.md

**Location**: `.ushabti/style.md`

**Purpose**: Defines conventions that govern how the system is built. Style may evolve; laws should not.

### Structure

```markdown
# Project Style Guide

## Purpose

What this style guide is for and how it is used.

## Prose Conventions

Guidelines for written content.

## Markup Conventions

Guidelines for YAML, JSON, Markdown.

## Documentation Accuracy

Requirements for keeping docs current.

## Project Structure

Directory layout preferences.

## Theme

Thematic elements (for Ushabti: Ancient Egyptian references).

## Review Checklist

Concrete items reviewers should check.

## Revision History

| Date | Change |
|------|--------|
| YYYY-MM-DD | Description |
```

### Guidelines

- Be explicit and actionable
- Prefer examples over abstractions
- Style must not contradict laws
- Keep concise but complete

## plugin.json

**Location**: `.claude-plugin/plugin.json`

**Purpose**: Plugin manifest that registers Ushabti with Claude Code.

### Schema

```json
{
  "name": "ushabti",
  "version": "1.0.0",
  "description": "Brief description",
  "author": {
    "name": "Author Name",
    "email": "email@example.com",
    "url": "https://github.com/user/repo"
  },
  "repository": "https://github.com/user/repo",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"],
  "agents": [
    "./agents/agent-name.md"
  ],
  "skills": [
    "./skills/skill-name/"
  ]
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Plugin identifier |
| `version` | Yes | Semantic version (incremented per L08) |
| `description` | Yes | Brief purpose statement |
| `author` | Yes | Author information object |
| `repository` | No | Source repository URL |
| `license` | No | License identifier |
| `keywords` | No | Searchable tags |
| `agents` | Yes | Array of agent file paths |
| `skills` | Yes | Array of skill directory paths |

### Validation

Run `claude plugin validate .` from repository root to verify:
- JSON schema validity
- All referenced files exist
- Agent and skill formats are correct

## Claude Settings

### settings.json

**Location**: `.claude/settings.json`

**Purpose**: Enables plugins for the repository.

```json
{
  "enabledPlugins": {
    "ushabti@author": true
  }
}
```

### settings.local.json

**Location**: `.claude/settings.local.json`

**Purpose**: Local permissions (not committed or varies per user).

```json
{
  "permissions": {
    "allow": [
      "Bash(command:*)",
      "Bash(another-command:*)"
    ]
  }
}
```

Permissions control what Bash commands Claude Code can execute without user confirmation.
