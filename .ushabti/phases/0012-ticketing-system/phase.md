# Phase 0012: Ticketing System

## Intent

Add a lightweight, file-backed ticketing system to Ushabti that allows agents and users to capture ideas for future work. Tickets are stored as YAML files in `.ushabti/tickets/`, can be converted into phases, and are archived when complete. This keeps all work tracking within the repository without relying on external systems.

## Scope

**In scope:**
- Directory structure: `.ushabti/tickets/` and `.ushabti/tickets/.archived/`
- Five ticket skills: describe-tickets, find-next-ticket-number, create-ticket, archive-ticket, list-tickets
- Ticket YAML schema with validation on creation
- Updates to Vizier agent to know about tickets and offer creation in conversation
- Updates to Scribe agent to support creating phases from tickets
- Updates to Overseer agent to archive tickets when derived phases complete
- Phase metadata tracking ticket origin (when applicable)
- Documentation updates to describe ticket system
- Plugin manifest registration of new skills
- Version increment

**Out of scope:**
- Ticket editing or status updates (tickets are create-only, then archived)
- Ticket prioritization logic, ranking, or automated sorting
- Ticket assignment, ownership, or multi-user workflows
- Integration with external ticketing systems (GitHub Issues, Jira, etc.)
- Ticket dependencies or relationships

## Constraints

**Laws:**
- L04: Skills must reside in `skills/`
- L05: Each skill must be a directory containing `SKILL.md`
- L06: All skills must be registered in `.claude-plugin/plugin.json`
- L07: Plugin validation must pass after adding skills
- L08: Version increment required on Phase completion

**Style:**
- YAML: 2-space indentation, valid syntax, explicit true/false
- Markdown: ATX headers, fenced code blocks with language specifiers
- Clarity: Explicit, unambiguous prose
- Brevity: Concise, no filler
- Documentation accuracy: Docs must reflect current state

## Acceptance Criteria

1. `.ushabti/tickets/` directory exists
2. `.ushabti/tickets/.archived/` directory exists
3. Five ticket skills exist as directories with `SKILL.md` files:
   - describe-tickets
   - find-next-ticket-number
   - create-ticket
   - archive-ticket
   - list-tickets
4. All five skills registered in `.claude-plugin/plugin.json`
5. Ticket YAML schema includes: id, title, created, priority, context, proposed_work
6. Ticket filename format is `TNNNN-short-description.yaml`
7. Vizier agent (`agents/vizier.md`) knows tickets exist and can offer to create them during conversation
8. Scribe agent (`agents/scribe.md`) can create phases from tickets
9. Overseer agent (`agents/overseer.md`) archives tickets when derived phases complete
10. Phase files include optional `ticket` metadata field in `phase.md` to track origin
11. Documentation updated to describe ticket system (at least one new doc file or updates to existing docs)
12. Skills are both user-invokable and model-invokable (no restrictions)
13. `claude plugin validate .` passes
14. Version incremented to 1.6.7 in `.claude-plugin/plugin.json`

## Risks / Notes

**Intentional design decisions:**
- Tickets are deliberately simple: create, derive phase from, archive. No editing, no complex state transitions.
- Archived tickets are "invisible" to agents (they don't read `.archived/`)
- Agents should offer ticket creation sparingly, only when observing genuine out-of-scope work during their duties
- Tickets complement phases, they don't replace planning or become a backlog management tool

**Related work:**
- This Phase creates the foundation for ticket-aware workflows but doesn't mandate ticket usage
- Future phases may enhance ticket discovery or reporting if needed
