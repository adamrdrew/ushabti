# Steps — Phase 0005

## S001 — Define the minimal docs scaffold format

**Intent**: Establish what the minimal docs scaffold contains so Lawgiver can create it consistently.

**Work**:
- Define the content for a minimal `.ushabti/docs/index.md` that:
  - Provides enough structure for the docs loop to recognize docs exist
  - Clearly indicates that comprehensive documentation is needed
  - Recommends running Surveyor for full project documentation
- Document this format in a new section of the Lawgiver agent file

**Done when**: The minimal scaffold format is defined and documented in Lawgiver's agent file.

---

## S002 — Update Lawgiver to create docs scaffold

**Intent**: Make Lawgiver responsible for creating the minimal docs infrastructure when bootstrapping.

**Work**:
- Add a new section to `agents/lawgiver.md` under "Procedure" that instructs Lawgiver to:
  1. Create `.ushabti/` directory if it doesn't exist
  2. Create `.ushabti/docs/` directory if it doesn't exist
  3. Create `.ushabti/docs/index.md` with the minimal scaffold (defined in S001) if it doesn't exist
- The scaffold creation happens during law writing, before the handoff to Artisan
- Lawgiver should only create the scaffold if docs don't already exist (preserve existing docs)

**Done when**: Lawgiver's agent file contains instructions to create the docs scaffold during bootstrap.

---

## S003 — Update Artisan handoff logic

**Intent**: Ensure Artisan correctly recommends Surveyor when docs are minimal (scaffold only) vs. comprehensive.

**Work**:
- Review Artisan's current completion logic (line 122-124 in `agents/artisan.md`)
- Update the handoff recommendation to distinguish between:
  - No docs → recommend Surveyor
  - Scaffold-only docs (index.md exists but has minimal content or a scaffold marker) → recommend Surveyor
  - Comprehensive docs (multiple files, substantive content) → recommend Scribe
- The check can be simple: if only `index.md` exists in `.ushabti/docs/` or if `index.md` contains the scaffold marker text, recommend Surveyor

**Done when**: Artisan's handoff logic distinguishes between scaffold and comprehensive docs.

---

## S004 — Update check-ushabti-prerequisites skill

**Intent**: Reflect the new bootstrap flow in the prerequisites skill.

**Work**:
- Update `skills/check-ushabti-prerequisites/SKILL.md` to:
  - Note that Lawgiver creates the minimal docs scaffold
  - Update the "Recommended Bootstrap Order" to clarify that Surveyor is for comprehensive documentation, not initial scaffold
  - Update the "Required Files by Agent" table to show Lawgiver creates docs scaffold

**Done when**: The prerequisites skill accurately documents the new bootstrap flow.

---

## S005 — Update project documentation

**Intent**: Keep `.ushabti/docs/` current with the new Lawgiver behavior.

**Work**:
- Update `.ushabti/docs/agents.md` to document:
  - Lawgiver's new responsibility for creating the docs scaffold
  - The distinction between scaffold docs and comprehensive docs
  - The updated bootstrap flow
- Update `.ushabti/docs/architecture.md` if it contains bootstrap flow information

**Done when**: Project documentation reflects the new Lawgiver behavior and bootstrap flow.

---

## S006 — Validate plugin and increment version

**Intent**: Ensure plugin compliance and proper versioning per L07 and L08.

**Work**:
- Run `claude plugin validate .` from repository root
- Fix any validation errors
- Increment the `version` field in `.claude-plugin/plugin.json`

**Done when**: Plugin validates successfully and version is incremented.

---

## S007 — Manual verification test

**Intent**: Verify the fix works for the new-project bootstrap scenario.

**Work**:
- Document a test procedure that can be run manually:
  1. In a clean directory (simulated new project), invoke Lawgiver
  2. Verify `.ushabti/docs/index.md` is created with scaffold content
  3. Invoke Artisan
  4. Verify Artisan recommends Surveyor for comprehensive docs
  5. Invoke Scribe
  6. Verify Scribe does not fail due to missing docs (scaffold is sufficient)
- This test procedure should be added as a note in the review.md for Overseer

**Done when**: Test procedure is documented and can be executed to verify the fix.
