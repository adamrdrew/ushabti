# Steps for Phase 0002: Add Surveyor Agent

## S001: Draft agent YAML front matter

**Intent:** Establish the agent metadata consistent with existing agents.

**Work:**
- Define name, description, model, color, and skills
- Use format matching other agents (e.g., scribe.md)
- Description should capture the Surveyor's purpose: onboarding existing projects through documentation

**Done when:** YAML front matter is drafted and ready for inclusion in the agent file.

---

## S002: Write Part A instructions (Setup)

**Intent:** Define how the Surveyor initializes the documentation structure.

**Work:**
- Create `.ushabti/` directory if missing
- Create `.ushabti/docs/` directory if missing
- Check for existing `index.md` and other `.md` files in `.ushabti/docs/`
- If prior survey exists, ask user for confirmation before proceeding
- Create `index.md` with specified format (project name, description, table of contents)
- Create `surveyor.md` with Observations and Plan sections

**Done when:** Part A instructions are complete with exact file formats specified.

---

## S003: Write Part B instructions (Discovery and Planning)

**Intent:** Define how the Surveyor explores the codebase and creates a documentation plan.

**Work:**
- Instruct agent to explore codebase for high-level understanding
- Define format for Observations section entries (systems, abstractions, subsystems, files)
- Define format for Plan section entries (step name, completion status, target doc, files/subsystems to cover)
- Specify that plan entries default to incomplete

**Done when:** Part B instructions specify discovery process and exact plan format.

---

## S004: Write Part C instructions (Writing Documentation)

**Intent:** Define how the Surveyor executes the documentation plan.

**Work:**
- Process plan steps in order
- For each step, create a doc in `.ushabti/docs/`
- Add table of contents entry in `index.md` for each doc created
- Define documentation content expectations (API info, system behavior, data formats, structures)
- Specify docs should be brief yet accurate
- Mark plan step complete after each doc is written

**Done when:** Part C instructions define stepwise documentation creation with index updates.

---

## S005: Write Part D instructions (Verification and Handoff)

**Intent:** Define how the Surveyor confirms completion and hands off.

**Work:**
- Verify all files in `.ushabti/docs/` have index.md entries
- Verify all plan steps in surveyor.md are marked complete
- If incomplete steps exist, return to Part C
- Increment version in `.claude-plugin/plugin.json`
- Git add and commit with message format
- Define conditional handoff:
  - No laws.md: suggest Lawgiver
  - laws.md but no style.md: suggest Artisan
  - Both present: suggest Scribe

**Done when:** Part D instructions specify verification checks, version increment, commit, and conditional handoff.

---

## S006: Define hard role boundaries

**Intent:** Ensure Surveyor stays in its lane, consistent with other agents.

**Work:**
- Surveyor does not plan Phases (Scribe does that)
- Surveyor does not implement code (Builder does that)
- Surveyor does not define laws (Lawgiver does that)
- Surveyor does not define style (Artisan does that)
- Surveyor does not review work (Overseer does that)
- Surveyor creates documentation only

**Done when:** Hard role boundaries are explicit in the agent prompt.

---

## S007: Assemble complete agent file

**Intent:** Combine all sections into `agents/surveyor.md`.

**Work:**
- Combine YAML front matter with all instruction sections
- Ensure consistent formatting (ATX headers, proper lists)
- Add procedure summary (the four-part flow)
- Include completion and handoff section

**Done when:** `agents/surveyor.md` exists with complete, well-formatted content.

---

## S008: Register agent in plugin.json

**Intent:** Make the agent discoverable by Claude Code.

**Work:**
- Add `./agents/surveyor.md` to the agents array in plugin.json
- Maintain alphabetical or logical ordering if one exists
- Increment the version field

**Done when:** plugin.json includes the new agent entry and has an incremented version.

---

## S009: Update CLAUDE.md agent table

**Intent:** Keep project documentation accurate.

**Work:**
- Add Surveyor row to the agent table in CLAUDE.md
- Purpose: "Onboard existing projects by creating documentation"
- Does NOT: "Plan, code, review, define laws, or style"

**Done when:** CLAUDE.md agent table includes Surveyor with correct description.

---

## S010: Update README.md agent documentation

**Intent:** Keep user-facing documentation accurate and complete.

**Work:**
- Add Surveyor to the agent documentation section in README.md
- Follow the existing format used for other agents (Lawgiver, Artisan, Scribe, Builder, Overseer)
- Include purpose: onboarding existing projects through documentation
- Include role boundaries: does not plan, code, review, define laws, or style

**Done when:** README.md documents the Surveyor agent alongside the other agents.

---

## S011: Validate plugin

**Intent:** Confirm the plugin is correctly configured per L07.

**Work:**
- Run `claude plugin validate .` from repository root
- Command must exit with code 0

**Done when:** Validation passes with no errors.

---

## S012: Verify acceptance criteria

**Intent:** Confirm all criteria are met before review.

**Work:**
- Check each acceptance criterion from phase.md:
  1. surveyor.md exists with valid front matter and complete prompt
  2. All four parts defined with clear instructions
  3. plugin.json includes the agent
  4. Version incremented
  5. Plugin validates
  6. CLAUDE.md updated
  7. README.md updated
  8. Hard role boundaries present
  9. Exact file formats specified

**Done when:** All nine acceptance criteria are satisfied.

---

## S013: Update progress.yaml

**Intent:** Truthfully record completion state for handoff to review.

**Work:**
- Mark all implemented steps as `implemented: true`
- List touched files for each step
- Set phase status to `review`

**Done when:** progress.yaml reflects actual work completed.
