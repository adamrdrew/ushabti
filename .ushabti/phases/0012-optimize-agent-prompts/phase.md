# Phase 0012: Optimize Agent Prompts for Token Efficiency

## Intent

Reduce agent prompt token usage by approximately 1,310 tokens (~13-15%) through five targeted optimizations based on official Anthropic best practices research. This is a pure refactoring Phase—no functional changes, all agent behaviors preserved.

The optimizations remove redundancy, consolidate theming guidance, and streamline skill invocation patterns without sacrificing clarity or correctness.

## Scope

### In Scope

**Optimization 1: Remove Agent Isolation Warnings**
- Remove the `**Agent isolation**` paragraph from 6 agents: builder, scribe, overseer, lawgiver, artisan, surveyor
- Vizier retains its own isolation rules (different content, not just about vizier.md)

**Optimization 2: Move Egyptian Theming Guidance to CLAUDE.md**
- Remove theming guidance from all 7 agent files
- Add consolidated theming section to CLAUDE.md under "Agent Configuration"

**Optimization 3: Simplify Skill Invocation Patterns**
- Replace verbose "Use the Skill tool to invoke X" with concise "Invoke X" across all agents
- Approximately 18 occurrences across 7 agent files

**Optimization 4: Shorten Frontmatter Descriptions**
- Remove redundant "Use when..." clauses from all 7 agent descriptions
- Keep core purpose, remove usage examples

**Optimization 5: Consolidate Grouped Skill References**
- Convert multi-line skill lists to single-line comma-separated lists
- Example: "describe-phase-directory-structure, describe-good-phase, describe-phase-file..." on one line

### Out of Scope

- Skill file modifications
- Changes to laws.md or style.md
- Documentation file changes (except CLAUDE.md)
- Any functional changes to agent behavior
- Changes to plugin.json structure (except version increment)

## Constraints

**L01 — Claude Code Plugin Compliance**: Must run `claude plugin validate .` and pass before completion.

**L08 — Version Increment on Phase Completion**: Must increment version from 1.6.6 to 1.6.7 in plugin.json.

**Style — Clarity**: All changes must preserve clarity and precision. No ambiguity introduced.

**Style — Markdown**: Maintain ATX-style headers, proper spacing, valid YAML frontmatter.

**Refactoring Principle**: This is a pure refactoring. Every agent must behave identically after the changes.

## Acceptance Criteria

1. Agent isolation warning removed from exactly 6 agents (builder, scribe, overseer, lawgiver, artisan, surveyor)
2. Theming guidance removed from all 7 agent files
3. Theming section added to CLAUDE.md under "Agent Configuration"
4. All skill invocations use concise pattern ("Invoke X" instead of "Use the Skill tool to invoke X")
5. All frontmatter descriptions shortened (no "Use when..." clauses)
6. Grouped skill references consolidated to single-line lists where they appear
7. `claude plugin validate .` exits with success (exit code 0)
8. Version incremented from 1.6.6 to 1.6.7 in plugin.json
9. All YAML frontmatter remains valid
10. All Markdown remains valid
11. No functional changes to agent behavior

## Risks / Notes

**Low Risk**: These are mechanical refactorings based on Anthropic research. Token reduction is measured and validated.

**Validation**: Plugin validation will catch any YAML or structural errors.

**Behavioral Preservation**: Each optimization preserves the semantic meaning—only the expression changes.
