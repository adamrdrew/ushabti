# Implementation Steps

## S001 — Remove Agent Isolation Warnings

**Intent**: Eliminate redundant vizier.md isolation warnings from 6 agents.

**Work**: Remove the `**Agent isolation**: You MUST ignore .ushabti/vizier.md...` paragraph from builder.md, scribe.md, overseer.md, lawgiver.md, artisan.md, and surveyor.md. Do not modify vizier.md (its isolation rules are different).

**Done when**: The 6 agents no longer contain the agent isolation paragraph. Vizier.md is unchanged.

---

## S002 — Remove Theming Guidance from All Agents

**Intent**: Eliminate theming guidance from agent files before consolidating in CLAUDE.md.

**Work**: Remove theming-related sentences from all 7 agent files. These appear as variations of "Occasionally (rarely) you may use a brief Ancient Egyptian reference..." Remove the entire sentence.

**Done when**: No agent file contains theming guidance.

---

## S003 — Add Theming Section to CLAUDE.md

**Intent**: Consolidate theming guidance in a single canonical location.

**Work**: Add a new section to CLAUDE.md under "Agent Configuration" titled "## Agent Theming Guidelines". Include consolidated guidance: "Agents may occasionally use brief Ancient Egyptian references (e.g., 'inscribe,' 'weighed and found true') when they do not reduce clarity. Clarity always takes precedence over theme."

**Done when**: CLAUDE.md contains the new theming section. The guidance is clear and concise.

---

## S004 — Simplify Skill Invocations in builder.md

**Intent**: Reduce verbose skill invocation patterns to concise format.

**Work**: Replace all instances of "Use the Skill tool to invoke X" with "Invoke X" in builder.md. Preserve the skill name and context.

**Done when**: All skill invocations in builder.md use the concise pattern. The file remains valid Markdown.

---

## S005 — Simplify Skill Invocations in scribe.md

**Intent**: Reduce verbose skill invocation patterns to concise format.

**Work**: Replace all instances of "Use the Skill tool to invoke X" with "Invoke X" in scribe.md. Preserve the skill name and context.

**Done when**: All skill invocations in scribe.md use the concise pattern. The file remains valid Markdown.

---

## S006 — Simplify Skill Invocations in overseer.md

**Intent**: Reduce verbose skill invocation patterns to concise format.

**Work**: Replace all instances of "Use the Skill tool to invoke X" with "Invoke X" in overseer.md. Preserve the skill name and context.

**Done when**: All skill invocations in overseer.md use the concise pattern. The file remains valid Markdown.

---

## S007 — Simplify Skill Invocations in lawgiver.md, artisan.md, surveyor.md, vizier.md

**Intent**: Reduce verbose skill invocation patterns to concise format.

**Work**: Replace all instances of "Use the Skill tool to invoke X" with "Invoke X" in lawgiver.md, artisan.md, surveyor.md, and vizier.md. Preserve the skill name and context.

**Done when**: All skill invocations in the 4 agent files use the concise pattern. Files remain valid Markdown.

---

## S008 — Shorten Frontmatter Descriptions

**Intent**: Remove redundant "Use when..." clauses from all agent descriptions.

**Work**: Edit the `description` field in the YAML frontmatter of all 7 agent files. Remove "Use when..." clauses and usage examples. Keep only the core purpose statement.

**Done when**: All 7 agent frontmatter descriptions are concise, contain no "Use when..." clauses, and YAML remains valid.

---

## S009 — Consolidate Grouped Skill References in scribe.md

**Intent**: Convert multi-line skill lists to single-line comma-separated format.

**Work**: In scribe.md, locate the "Reference skills" section. Convert the bulleted list of skills to a single-line comma-separated list: "Invoke describe-phase-directory-structure, describe-good-phase, describe-phase-file, describe-steps-file, describe-progress-file, describe-review-file for format details."

**Done when**: The skill list is on a single line. The section remains clear and readable.

---

## S010 — Consolidate Grouped Skill References in Other Agents

**Intent**: Convert multi-line skill lists to single-line format where applicable.

**Work**: Review builder.md, overseer.md, lawgiver.md, artisan.md, surveyor.md, and vizier.md for grouped skill references. Convert any multi-line lists to single-line comma-separated format using the same pattern as S009.

**Done when**: All grouped skill references use single-line format. Files remain clear and readable.

---

## S011 — Increment Version in plugin.json

**Intent**: Satisfy L08 requirement for version increment.

**Work**: Change the `version` field in .claude-plugin/plugin.json from "1.6.6" to "1.6.7".

**Done when**: plugin.json contains version "1.6.7". JSON remains valid.

---

## S012 — Validate Plugin

**Intent**: Ensure all changes comply with Claude Code plugin specifications.

**Work**: Run `claude plugin validate .` from the repository root. Address any validation errors.

**Done when**: `claude plugin validate .` exits with success (exit code 0).
