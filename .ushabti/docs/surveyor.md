# Surveyor Working Document

## Observations

### Ushabti System (Core)

- **Type:** system
- **Location:** Repository root, `.ushabti/`
- **Purpose:** A file-backed, agent-driven development system implemented as a Claude Code plugin. Development happens in bounded Phases that are planned, implemented, reviewed, and completed.
- **Key files:** `README.md`, `CLAUDE.md`, `.claude-plugin/plugin.json`
- **Dependencies:** Claude Code (as host platform)

### Agent System

- **Type:** system
- **Location:** `agents/`
- **Purpose:** Six specialized agents with strictly enforced role boundaries that handle different aspects of the development workflow.
- **Key files:**
  - `agents/lawgiver.md` — defines project invariants
  - `agents/artisan.md` — defines project style
  - `agents/surveyor.md` — onboards existing projects via documentation
  - `agents/scribe.md` — plans Phases
  - `agents/builder.md` — implements Phases
  - `agents/overseer.md` — reviews and approves Phases
- **Dependencies:** Skills (ushabti-core, phase-files)

### Skills System

- **Type:** system
- **Location:** `skills/`
- **Purpose:** Shared knowledge modules that agents reference. Provides context about Ushabti concepts and Phase file structures.
- **Key files:**
  - `skills/ushabti-core/SKILL.md` — core concepts (laws vs style, Phase loop, agent boundaries)
  - `skills/phase-files/SKILL.md` — Phase file formats and conventions
- **Dependencies:** None

### Phase System

- **Type:** system
- **Location:** `.ushabti/phases/`
- **Purpose:** Tracks bounded units of work through planning, building, and review. Each Phase has its own directory with standardized files.
- **Key files:**
  - `phase.md` — intent, scope, acceptance criteria
  - `steps.md` — ordered implementation steps
  - `progress.yaml` — machine-tracked state
  - `review.md` — review findings
- **Dependencies:** laws.md, style.md

### Configuration System

- **Type:** subsystem
- **Location:** `.ushabti/`, `.claude-plugin/`, `.claude/`
- **Purpose:** Project invariants (laws), conventions (style), plugin manifest, and Claude Code settings.
- **Key files:**
  - `.ushabti/laws.md` — 8 laws governing plugin compliance, file locations, formats
  - `.ushabti/style.md` — prose, markup, documentation, and theme conventions
  - `.claude-plugin/plugin.json` — plugin manifest (name, version, agents, skills)
  - `.claude/settings.json` — enabled plugins
  - `.claude/settings.local.json` — local permissions
- **Dependencies:** None

## Plan

### Step 1: Architecture Overview

- **Status:** complete
- **Target doc:** architecture.md
- **Covers:** High-level system architecture, the Phase loop, agent workflow, file-backed state model
- **Notes:** Foundational document that explains how Ushabti works

### Step 2: Agent Reference

- **Status:** complete
- **Target doc:** agents.md
- **Covers:** All six agents (Lawgiver, Artisan, Surveyor, Scribe, Builder, Overseer), their purposes, boundaries, inputs, outputs
- **Notes:** Comprehensive reference for understanding agent responsibilities

### Step 3: Skills Reference

- **Status:** complete
- **Target doc:** skills.md
- **Covers:** ushabti-core skill, phase-files skill, how skills are structured and used
- **Notes:** Documents the shared knowledge modules

### Step 4: Phase Files Reference

- **Status:** complete
- **Target doc:** phase-files.md
- **Covers:** Phase directory structure, phase.md format, steps.md format, progress.yaml schema, review.md format
- **Notes:** Technical reference for Phase file formats

### Step 5: Configuration Reference

- **Status:** complete
- **Target doc:** configuration.md
- **Covers:** laws.md structure, style.md structure, plugin.json schema, Claude settings files
- **Notes:** Reference for all configuration files

### Step 6: Plugin Structure

- **Status:** complete
- **Target doc:** plugin-structure.md
- **Covers:** Claude Code plugin requirements, directory layout, manifest format, validation
- **Notes:** Documents how Ushabti is packaged as a plugin
