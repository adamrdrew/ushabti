# Steps for Phase 0001: Update the README

## S001: Audit current README structure

**Intent:** Understand what exists before making changes.

**Work:**
- Read the entire README
- Identify all sections and their purposes
- Note duplications, contradictions, and inaccuracies

**Done when:** A clear list of issues exists (can be mental or noted in progress.yaml).

---

## S002: Consolidate installation instructions

**Intent:** Users should find one clear, correct way to install Ushabti.

**Work:**
- Remove the duplicate installation section (lines 180-215)
- Keep and correct the installation section near the top (lines 7-12)
- Ensure instructions use the marketplace approach:
  ```
  /plugin marketplace add adamrdrew/marketplace
  /plugin install ushabti@adamrdrew
  ```

**Done when:** Exactly one installation section exists with correct marketplace commands.

---

## S003: Add dogfooding statement

**Intent:** Communicate that Ushabti is developed using its own framework.

**Work:**
- Add a brief section or statement indicating that Ushabti is developed with itself
- Place this logically (near "Status" or as its own section)
- Keep it concise per style guidelines

**Done when:** The README clearly states that Ushabti is developed using itself.

---

## S004: Correct repository structure diagram

**Intent:** The diagram should match reality.

**Work:**
- Update the repository structure to reflect actual layout:
  - `.ushabti/` contains `laws.md` and `style.md` directly
  - No root-level mirrors exist
  - Include `.claude-plugin/` directory
  - Include `agents/` and `skills/` directories
- Remove references to non-existent files

**Done when:** The diagram matches the output of `ls -la` at repo root and `.ushabti/`.

---

## S005: Remove stale content

**Intent:** Eliminate outdated or redundant information.

**Work:**
- Remove any remaining references to outdated installation methods
- Remove mentions of "mirrored" files if they do not exist
- Check for any other stale claims

**Done when:** No false statements remain in the README.

---

## S006: Apply style guidelines

**Intent:** Ensure prose quality matches project standards.

**Work:**
- Review all text for clarity and brevity
- Cut filler words
- Ensure consistent formatting (ATX headers, proper lists, fenced code blocks)
- Keep lines under 120 characters where practical

**Done when:** README conforms to `.ushabti/style.md` prose and markdown conventions.

---

## S007: Verify acceptance criteria

**Intent:** Confirm the Phase is complete before review.

**Work:**
- Check each acceptance criterion from phase.md
- Verify no duplicate installation sections
- Verify dogfooding statement exists
- Verify structure diagram is accurate
- Verify no contradictions remain

**Done when:** All five acceptance criteria are satisfied.

---

## S008: Update progress.yaml

**Intent:** Truthfully record completion state.

**Work:**
- Mark all implemented steps as `implemented: true`
- List touched files
- Set phase status to `review`

**Done when:** progress.yaml reflects actual work completed.
