# Project Laws

## Preamble

These laws define the absolute constraints for the Ushabti project — a file-backed, agent-driven development system implemented as a Claude Code plugin. Every Phase, implementation, and review MUST comply with these laws. Violations fail the Phase unconditionally.

The Overseer verifies compliance during review. No law may be weakened or reinterpreted without explicit user instruction to the Lawgiver.

---

## Laws

### L01 — Claude Code Plugin Compliance

- **Rule:** Ushabti MUST adhere to Claude Code plugin best practices and specifications.
- **Rationale:** Ushabti is distributed as a Claude Code plugin. Non-compliance breaks installation, discovery, or runtime behavior for users.
- **Enforcement:** Run `claude plugin validate .` from the repository root. The command MUST exit with success (exit code 0).
- **Scope:** The entire repository.
- **Exceptions:** None.

---

### L02 — Agent Location

- **Rule:** All agent definitions MUST reside in the `agents/` directory at the repository root.
- **Rationale:** A single, predictable location ensures discoverability and simplifies plugin manifest maintenance.
- **Enforcement:** No agent file (markdown with YAML front matter defining an agent) may exist outside `agents/`. Reviewers verify by inspecting the directory structure.
- **Scope:** All agent definitions.
- **Exceptions:** None.

---

### L03 — Agent File Format

- **Rule:** Agent files MUST be markdown files with YAML front matter.
- **Rationale:** Claude Code expects this format for agent definitions. Deviation breaks agent loading.
- **Enforcement:** Each file in `agents/` MUST begin with a valid YAML front matter block (delimited by `---`) followed by markdown content.
- **Scope:** All files in `agents/`.
- **Exceptions:** None.

---

### L04 — Skill Location

- **Rule:** All skill definitions MUST reside in the `skills/` directory at the repository root.
- **Rationale:** A single, predictable location ensures discoverability and simplifies plugin manifest maintenance.
- **Enforcement:** No skill directory may exist outside `skills/`. Reviewers verify by inspecting the directory structure.
- **Scope:** All skill definitions.
- **Exceptions:** None.

---

### L05 — Skill Directory Structure

- **Rule:** Each skill MUST be a directory containing a `SKILL.md` file.
- **Rationale:** This structure is required by Claude Code for skill discovery and loading.
- **Enforcement:** Every entry under `skills/` MUST be a directory, and each directory MUST contain a file named `SKILL.md`.
- **Scope:** All skills in `skills/`.
- **Exceptions:** None.

---

### L06 — Plugin Manifest Completeness

- **Rule:** Every agent and skill MUST be registered in `.claude-plugin/plugin.json`.
- **Rationale:** Unregistered agents and skills are invisible to Claude Code clients. The manifest is the source of truth for what the plugin exposes.
- **Enforcement:**
  1. Every file in `agents/` MUST have a corresponding entry in the `agents` array of `plugin.json`.
  2. Every directory in `skills/` MUST have a corresponding entry in the `skills` array of `plugin.json`.
  3. Run `claude plugin validate .` — validation MUST pass.
- **Scope:** All agents and skills.
- **Exceptions:** None.

---

### L07 — Plugin Validation on Addition

- **Rule:** Whenever a new agent or skill is added, the plugin MUST be validated before the Phase is considered complete.
- **Rationale:** Early validation catches manifest errors, missing files, and schema violations before they reach users.
- **Enforcement:**
  1. Verify JSON schema validity of `plugin.json`.
  2. Verify all file paths in `plugin.json` point to existing files or directories.
  3. Run `claude plugin validate .` from the repository root — MUST exit with success.
- **Scope:** Any Phase that adds agents or skills.
- **Exceptions:** None.

---

### L08 — Version Increment on Phase Completion

- **Rule:** The `version` field in `.claude-plugin/plugin.json` MUST be incremented when any development Phase completes.
- **Rationale:** Version changes signal to users and tooling that the plugin has been updated. Stale versions cause confusion and caching issues.
- **Enforcement:** The Overseer MUST verify that the `version` field differs from its value at Phase start before declaring a Phase complete.
- **Scope:** All Phases that modify the repository.
- **Exceptions:** Phases that make no functional changes (e.g., documentation-only updates that do not affect plugin behavior) MAY skip the version bump if explicitly noted in the Phase plan.

---

## Revision History

| Date       | Change                          |
|------------|---------------------------------|
| 2026-01-28 | Initial laws inscribed (L01-L08) |
