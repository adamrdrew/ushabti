# Phase 0010: Vizier Memory Refinement

## Intent

Refine the Vizier agent's memory system to store only evergreen background information, preventing memory bloat from conversation logs and state tracking.

Currently, Vizier stores too much detail in `.ushabti/vizier.md`, including conversation logs, proposed ideas, and work state. This violates the intended design: Vizier's memory should contain only background context needed to inform future conversations, not a log of past interactions or drifting state.

This Phase clarifies what Vizier should and should not store, ensuring memory remains lean and relevant.

## Scope

**In scope:**
- Update Vizier agent definition to distinguish evergreen vs. ephemeral information
- Add explicit prohibitions against storing state, conversation logs, or work results
- Instruct Vizier to keep notes minimal and focused on background context
- Clarify that user preferences should be noted briefly (not verbosely)

**Out of scope:**
- Modifying existing `.ushabti/vizier.md` files (user responsibility to clean up if needed)
- Changing the Reference Library concept or structure
- Altering other agents or their memory systems
- Creating automated memory cleanup or pruning mechanisms

## Constraints

**Laws:**
- L01: Claude Code plugin compliance
- L02-L03: Agent location and format
- L06-L07: Plugin manifest completeness and validation
- L08: Version increment on completion

**Style:**
- Clarity and brevity in documentation
- No contradictions
- Documentation must reflect current state

## Acceptance Criteria

1. **Memory boundaries clarified:** Vizier agent definition explicitly distinguishes between evergreen information (store) and ephemeral information (do not store)
2. **Prohibitions documented:** Agent definition explicitly prohibits storing state, conversation logs, proposed ideas, or work results
3. **Minimal guidance added:** Vizier is instructed to keep memory concise and focused on background context only
4. **User preference handling:** Vizier understands user preferences should be noted briefly (e.g., "User prefers X"), not as verbose conversation logs
5. **Plugin validation passes:** `claude plugin validate .` exits successfully
6. **Version incremented:** `version` field in `.claude-plugin/plugin.json` is bumped

## Risks / Notes

**Risk:** Existing `.ushabti/vizier.md` files may contain bloated content from prior conversations. This Phase does not automatically clean those up—users must manually prune if desired.

**Note:** This change is about **preventing future bloat**, not remediating past bloat. The agent's behavior changes, but existing memory files are untouched.

**Deferred:** Automated memory pruning or size limits could be added in a future Phase if needed, but are not required for this improvement.
