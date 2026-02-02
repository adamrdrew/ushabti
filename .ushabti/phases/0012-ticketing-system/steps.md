# Implementation Steps

## S001: Create ticket directory structure

**Intent**: Establish the file system locations for tickets and archived tickets.

**Work**:
- Create `.ushabti/tickets/` directory
- Create `.ushabti/tickets/.archived/` directory
- Verify both directories exist and are empty

**Done when**:
- `.ushabti/tickets/` directory exists
- `.ushabti/tickets/.archived/` directory exists
- Both directories are confirmed via filesystem check

## S002: Create describe-tickets skill

**Intent**: Provide reference documentation on the ticket system, schema, and workflows.

**Work**:
- Create `skills/describe-tickets/` directory
- Create `skills/describe-tickets/SKILL.md` with:
  - YAML frontmatter (name: describe-tickets, description: ticket system overview)
  - Ticket YAML schema definition with all fields (id, title, created, priority, context, proposed_work)
  - Ticket filename format (TNNNN-short-description.yaml)
  - Directory locations (.ushabti/tickets/, .ushabti/tickets/.archived/)
  - Workflow explanation (create, derive phase, archive)
  - Agent responsibilities for ticket awareness

**Done when**:
- `skills/describe-tickets/SKILL.md` exists with valid YAML frontmatter
- Skill content documents schema, format, locations, and workflows
- File is valid Markdown

## S003: Create find-next-ticket-number skill

**Intent**: Provide logic to determine the next sequential ticket ID.

**Work**:
- Create `skills/find-next-ticket-number/` directory
- Create `skills/find-next-ticket-number/SKILL.md` with:
  - YAML frontmatter (name: find-next-ticket-number, description: calculate next ticket ID)
  - Bash command to find the highest existing ticket number
  - Logic to handle empty ticket directory (start at T0001)
  - Example output showing sequential numbering

**Done when**:
- `skills/find-next-ticket-number/SKILL.md` exists with valid YAML frontmatter
- Skill provides working bash command for ticket ID discovery
- File is valid Markdown

## S004: Create create-ticket skill

**Intent**: Provide instructions for creating new tickets with proper validation.

**Work**:
- Create `skills/create-ticket/` directory
- Create `skills/create-ticket/SKILL.md` with:
  - YAML frontmatter (name: create-ticket, description: create new ticket with validation)
  - Step-by-step ticket creation procedure
  - YAML schema validation requirements
  - Filename generation logic (TNNNN-short-description.yaml)
  - Priority validation (must be low, medium, or high)
  - Example ticket creation with all required fields

**Done when**:
- `skills/create-ticket/SKILL.md` exists with valid YAML frontmatter
- Skill documents creation procedure with validation
- File is valid Markdown

## S005: Create archive-ticket skill

**Intent**: Provide instructions for moving tickets to archived state.

**Work**:
- Create `skills/archive-ticket/` directory
- Create `skills/archive-ticket/SKILL.md` with:
  - YAML frontmatter (name: archive-ticket, description: archive completed tickets)
  - Archive procedure (move from .ushabti/tickets/ to .ushabti/tickets/.archived/)
  - When to archive (phase completion for ticket-derived phases)
  - Filesystem operation details

**Done when**:
- `skills/archive-ticket/SKILL.md` exists with valid YAML frontmatter
- Skill documents archive procedure and timing
- File is valid Markdown

## S006: Create list-tickets skill

**Intent**: Provide instructions for discovering and listing open tickets.

**Work**:
- Create `skills/list-tickets/` directory
- Create `skills/list-tickets/SKILL.md` with:
  - YAML frontmatter (name: list-tickets, description: list open tickets)
  - Bash command to list all tickets in .ushabti/tickets/
  - Exclusion of archived tickets (don't list .archived/)
  - Output format guidance

**Done when**:
- `skills/list-tickets/SKILL.md` exists with valid YAML frontmatter
- Skill provides working bash command for ticket listing
- File is valid Markdown

## S007: Register ticket skills in plugin manifest

**Intent**: Make all five ticket skills discoverable to Claude Code.

**Work**:
- Read `.claude-plugin/plugin.json`
- Add all five ticket skill paths to the `skills` array:
  - `./skills/describe-tickets/`
  - `./skills/find-next-ticket-number/`
  - `./skills/create-ticket/`
  - `./skills/archive-ticket/`
  - `./skills/list-tickets/`
- Maintain alphabetical ordering within the skills array
- Ensure JSON remains valid

**Done when**:
- All five ticket skills registered in `.claude-plugin/plugin.json`
- JSON file is syntactically valid
- Skills array maintains consistent formatting

## S008: Update Vizier agent for ticket awareness

**Intent**: Enable Vizier to know about tickets, consult them, and offer to create them during conversations.

**Work**:
- Read `agents/vizier.md`
- Add ticket awareness to capabilities section:
  - Vizier can read tickets in .ushabti/tickets/
  - Vizier ignores archived tickets in .ushabti/tickets/.archived/
  - Vizier can offer to create tickets when good ideas for future work arise
- Add guidance on when to offer ticket creation (sparingly, only for genuine future work ideas)
- Add ticket creation to the "when to suggest action" section

**Done when**:
- `agents/vizier.md` documents ticket awareness in capabilities
- Guidance on ticket creation timing is explicit
- Vizier knows to ignore .archived/ tickets
- Agent definition remains valid Markdown with YAML frontmatter

## S009: Update Scribe agent for phase-from-ticket workflow

**Intent**: Enable Scribe to create phases derived from tickets and record the origin.

**Work**:
- Read `agents/scribe.md`
- Add ticket-aware planning to procedure:
  - When user references a ticket, Scribe reads the ticket YAML
  - Scribe uses ticket context and proposed_work to inform phase planning
  - Scribe adds `ticket: TNNNN` field to phase.md metadata when phase derives from a ticket
- Add guidance on incorporating ticket information into phase intent and scope

**Done when**:
- `agents/scribe.md` documents ticket-aware planning procedure
- Instruction to add ticket field to phase.md when applicable
- Agent definition remains valid Markdown with YAML frontmatter

## S010: Update Overseer agent for ticket archival

**Intent**: Enable Overseer to archive tickets when their derived phases complete.

**Work**:
- Read `agents/overseer.md`
- Add ticket archival to "declaring a Phase green" section:
  - When completing a phase, check phase.md for `ticket` field
  - If ticket field exists, move the ticket file from .ushabti/tickets/ to .ushabti/tickets/.archived/
  - Log the archival action in review findings
- Add guidance that this is part of the completion checklist

**Done when**:
- `agents/overseer.md` documents ticket archival procedure
- Archival is integrated into phase completion workflow
- Agent definition remains valid Markdown with YAML frontmatter

## S011: Update phase.md template format

**Intent**: Document the optional ticket metadata field for phase files.

**Work**:
- Read `skills/describe-phase-file/SKILL.md`
- Add documentation for optional `ticket` field in phase.md frontmatter or metadata section
- Specify format: `ticket: TNNNN` (references the ticket ID)
- Clarify this field is optional and only present when phase derives from a ticket

**Done when**:
- `skills/describe-phase-file/SKILL.md` documents the ticket metadata field
- Format and optionality are clear
- File remains valid Markdown with YAML frontmatter

## S012: Update documentation with ticket system

**Intent**: Ensure project documentation reflects the new ticket system.

**Work**:
- Read `.ushabti/docs/index.md` to determine documentation structure
- Identify the appropriate doc file to update (likely architecture.md or create new tickets.md)
- Add ticket system documentation covering:
  - Purpose and design (lightweight, file-backed, create-archive lifecycle)
  - Directory structure and file format
  - Agent responsibilities (Vizier awareness, Scribe derivation, Overseer archival)
  - Workflow: capture idea → create ticket → derive phase → archive on completion
- Update index.md if a new doc file is created

**Done when**:
- Ticket system is documented in `.ushabti/docs/`
- Documentation includes purpose, structure, format, and workflows
- Index updated if new file created
- All doc files remain valid Markdown

## S013: Update using-skills catalog

**Intent**: Ensure the using-skills skill catalog includes all five new ticket skills.

**Work**:
- Run `scripts/reconcile-skills.sh` to automatically update the using-skills catalog
- Verify that all five ticket skills appear in the catalog with correct names and descriptions
- Ensure catalog formatting is consistent

**Done when**:
- `skills/using-skills/SKILL.md` includes all five ticket skills
- Skill names and descriptions are accurate
- Catalog remains valid Markdown

## S014: Validate plugin and increment version

**Intent**: Ensure plugin validation passes and satisfy L08 requirement.

**Work**:
- Run `claude plugin validate .` from repository root
- Verify command exits with success (exit code 0)
- Read `.claude-plugin/plugin.json`
- Increment `version` field from 1.6.6 to 1.6.7
- Ensure JSON remains valid
- Re-run validation to confirm version change doesn't break validation

**Done when**:
- `claude plugin validate .` passes
- Version incremented to 1.6.7
- JSON file is syntactically valid
- Plugin validation still passes after version increment

## S015: Verify acceptance criteria

**Intent**: Confirm all acceptance criteria from phase.md are satisfied.

**Work**:
- Check all directories exist (.ushabti/tickets/, .ushabti/tickets/.archived/)
- Verify all five skills exist with proper structure
- Confirm all skills registered in plugin.json
- Verify ticket schema matches specification
- Confirm agent updates are complete (Vizier, Scribe, Overseer)
- Verify documentation updates are complete
- Confirm plugin validation passes
- Verify version is 1.6.7

**Done when**:
- All 14 acceptance criteria from phase.md pass verification
- Any deficiencies are identified for follow-up
