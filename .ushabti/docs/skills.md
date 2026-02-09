# Skills Reference

## Overview

Skills provide domain knowledge that agents can access on-demand. Rather than preloading all knowledge into each agent, Ushabti uses a catalog-based approach: agents receive a skill manifest at startup and invoke individual skills as needed via the Skill tool.

## Skill Architecture

```
┌──────────────────────────────────────────────┐
│  using-skills (preloaded at agent startup)   │
│  ├── How to invoke skills via Skill tool     │
│  └── Catalog of all available skills         │
└──────────────────────────────────────────────┘
                     │
                     ▼
         Agent calls Skill(skill-name)
                     │
                     ▼
         Skill content loaded on-demand
```

This approach minimizes startup context while giving agents access to the full skill library.

## Skill Categories

### Meta Skill

**using-skills** — Teaches agents how to invoke skills and lists all available skills with descriptions. Preloaded into all agents at startup.

### Domain Knowledge Skills

These skills provide reference information about Ushabti concepts:

| Skill | Purpose |
|-------|---------|
| describe-ushabti | Core concepts and development lifecycle |
| describe-canonical-locations | File locations for laws, style, phases, docs |
| describe-laws-and-style | Distinction between invariants and conventions |
| describe-agent-roles | Agent responsibilities and boundaries |
| describe-required-inputs | Mandatory files agents must read |
| describe-questions-policy | Guidelines for asking clarifying questions |
| describe-phase-loop | Plan-Build-Review cycle and handoffs |
| describe-phase-directory-structure | Phase directory layout and naming |
| describe-phase-file | phase.md format and sections |
| describe-steps-file | steps.md format and ordering |
| describe-progress-file | progress.yaml structure and field ownership |
| describe-review-file | review.md format and sections |
| describe-good-phase | Phase sizing and anti-patterns |
| describe-docs-system | Documentation maintenance requirements |

### Orchestration Skills

These skills automate multi-agent workflows:

| Skill | Purpose |
|-------|---------|
| ir-kat | Execute a full Scribe → Builder → Overseer phase cycle. User-invocable. Accepts a PHASE_PROMPT via `$ARGUMENTS` (inline text or file path). Includes retry loop (max 3 kickbacks before declaring blocked). |

### Utility Skills

These skills provide dynamic information about project state:

| Skill | Purpose |
|-------|---------|
| check-ushabti-prerequisites | Verify required files exist |
| find-current-phase | Locate active phase by status |
| find-next-phase-number | Calculate next sequential phase ID |
| find-next-step | Find next unimplemented step |
| get-phase-status | Check phase workflow position |

Utility skills use dynamic context injection to provide live project state when invoked.

## Skill Invocation

Agents invoke skills using the Skill tool:

```
Skill(describe-progress-file)
```

The skill content is loaded into the agent's context at that moment, keeping it fresh and avoiding lost-in-middle effects during long-running sessions.

## Skill Directory Structure

Each skill is a directory containing a SKILL.md file:

```
skills/
├── using-skills/
│   └── SKILL.md
├── describe-ushabti/
│   └── SKILL.md
├── find-current-phase/
│   └── SKILL.md
└── ...
```

## Skill Maintenance

The `using-skills` catalog is automatically maintained by a pre-commit hook. When skill files change, `scripts/reconcile-skills.sh` updates the catalog to reflect current skill names and descriptions.

## Adding New Skills

1. Create a directory under `skills/` (e.g., `skills/new-skill/`)
2. Create `SKILL.md` with YAML frontmatter (name, description) and content
3. Add the skill to `plugin.json`
4. Commit — the pre-commit hook updates the `using-skills` catalog automatically
