# Steps

## S001: Read current Vizier agent definition

**Intent:** Understand the existing memory system documentation to identify what needs refinement.

**Work:**
- Read `agents/vizier.md` in full
- Identify the "Memory system" section and related guidance
- Note current instructions about what to store

**Done when:** Current memory system documentation is understood and baseline established.

---

## S002: Define evergreen vs. ephemeral distinction

**Intent:** Create clear, explicit guidance on what Vizier should and should not store in memory.

**Work:**
- Add or update a section in the Vizier agent definition that explicitly defines:
  - **Evergreen information** (store): Project structure, purpose, user preferences (brief), Reference Library
  - **Ephemeral information** (do not store): State, conversation logs, proposed ideas, work results, ongoing discussions
- Use clear, direct language suitable for LLM interpretation
- Ensure no contradictions with existing guidance

**Done when:** Vizier agent definition contains an explicit "Memory Boundaries" or similar section that distinguishes evergreen from ephemeral information.

---

## S003: Add prohibitions against storing state and logs

**Intent:** Prevent Vizier from treating memory as a conversation log or state tracker.

**Work:**
- Add explicit prohibitions in the Vizier agent definition:
  - Do not store conversation logs or summaries of past discussions
  - Do not store state (e.g., "user proposed X," "we discussed Y")
  - Do not store work results or outcomes
  - Do not store anything that needs to reconcile with ongoing work
- Frame prohibitions clearly and unambiguously

**Done when:** Vizier agent definition contains clear prohibitions against storing state, logs, and ephemeral information.

---

## S004: Clarify user preference storage

**Intent:** Ensure Vizier understands how to note user preferences without creating verbose logs.

**Work:**
- Add guidance on storing user preferences:
  - Store preferences briefly (e.g., "User prefers TypeScript" or "User introduced themselves as Alice")
  - Do not expand preferences into conversation summaries
  - Preferences are factual statements, not narratives
- Include examples if helpful

**Done when:** Vizier agent definition includes guidance on storing user preferences concisely.

---

## S005: Add minimal memory guidance

**Intent:** Instruct Vizier to keep memory lean and focused.

**Work:**
- Add or update guidance emphasizing:
  - Memory should be minimal and focused on background context
  - Avoid duplication of information already in docs or phases
  - Update memory only when discovering something truly worth remembering
  - Prefer references (links to files) over copying content
- Frame as a directive, not a suggestion

**Done when:** Vizier agent definition contains clear guidance to keep memory minimal and avoid bloat.

---

## S006: Review updated agent definition for contradictions

**Intent:** Ensure new guidance does not conflict with existing Vizier instructions.

**Work:**
- Read the updated `agents/vizier.md` in full
- Check for contradictions between new memory guidance and existing sections (Startup behavior, Capabilities, etc.)
- Resolve any conflicts or ambiguities

**Done when:** Vizier agent definition is internally consistent with no contradictions.

---

## S007: Validate plugin

**Intent:** Ensure changes comply with plugin requirements.

**Work:**
- Run `claude plugin validate .` from repository root
- Verify exit code is 0 (success)
- If validation fails, diagnose and fix issues

**Done when:** Plugin validation passes successfully.

---

## S008: Increment version

**Intent:** Signal that the plugin has been updated.

**Work:**
- Open `.claude-plugin/plugin.json`
- Increment the `version` field according to semantic versioning
- Save the file

**Done when:** Version field in `plugin.json` has been incremented.

---

## S009: Final validation

**Intent:** Confirm all changes are correct and complete.

**Work:**
- Run `claude plugin validate .` again
- Verify JSON syntax is valid in `plugin.json`
- Confirm `agents/vizier.md` is well-formed markdown with valid YAML front matter

**Done when:** All validation checks pass and files are well-formed.
