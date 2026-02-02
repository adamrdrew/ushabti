# Steps for Phase 0013

## S001: Add ticket directory creation to Lawgiver

**Intent**: Ensure Lawgiver creates ticket directories during bootstrap so new projects have the structure ready for ticket creation.

**Work**:
- Read `agents/lawgiver.md` to understand current bootstrap procedure
- Add ticket directory creation to the bootstrap infrastructure section
- Update the procedure to create `.ushabti/tickets/` and `.ushabti/tickets/.archived/`

**Done when**:
- Lawgiver bootstrap procedure includes creating both ticket directories
- Instructions are clear and placed appropriately in the bootstrap section
- Markdown syntax remains valid

## S002: Add ticket directory creation to Surveyor

**Intent**: Ensure Surveyor creates ticket directories during Part A setup so onboarded projects have the structure ready.

**Work**:
- Read `agents/surveyor.md` to understand Part A setup procedure
- Add ticket directory creation to Part A steps
- Place after `.ushabti/docs/` creation to maintain logical ordering

**Done when**:
- Surveyor Part A includes creating both ticket directories
- Instructions are sequenced logically with other directory creation
- Markdown syntax remains valid

## S003: Add defensive directory creation to create-ticket skill

**Intent**: Provide fallback directory creation in case bootstrap or onboarding didn't run or directories were accidentally deleted.

**Work**:
- Read `skills/create-ticket/SKILL.md`
- Add mkdir step to creation procedure before writing ticket file
- Use `mkdir -p .ushabti/tickets` to ensure directory exists without error if already present

**Done when**:
- Creation procedure includes defensive mkdir before file write
- Command uses `-p` flag for idempotency
- Placement makes logical sense in the procedure flow

## S004: Add defensive directory check to find-next-ticket-number skill

**Intent**: Prevent find command failure when ticket directory doesn't exist.

**Work**:
- Read `skills/find-next-ticket-number/SKILL.md`
- Add directory existence check to bash command or create directory if missing
- Ensure command handles missing directory gracefully

**Done when**:
- Bash command handles missing `.ushabti/tickets/` directory without error
- Returns T0001 when directory doesn't exist or is empty
- Logic is clear and maintainable

## S005: Add defensive directory creation to archive-ticket skill

**Intent**: Ensure `.archived/` subdirectory exists before attempting to move tickets into it.

**Work**:
- Read `skills/archive-ticket/SKILL.md`
- Add mkdir step to archive procedure before moving ticket file
- Use `mkdir -p .ushabti/tickets/.archived` for idempotency

**Done when**:
- Archive procedure includes defensive mkdir before mv command
- Command uses `-p` flag
- Procedure flow remains clear

## S006: Document ticket system in README.md

**Intent**: Make users aware the ticket system exists and provide high-level overview.

**Work**:
- Read current README.md structure
- Add ticket system section after Agents section, before Repository Structure
- Include brief description of purpose and basic usage
- Keep concise and link to detailed docs

**Done when**:
- Ticket system has dedicated section in README
- Description explains what tickets are and when to use them
- Integration with existing content is natural
- Markdown syntax is valid

## S007: Add ticket workflow to getting-started.md

**Intent**: Educate users on how tickets integrate with the Phase loop.

**Work**:
- Read current getting-started.md structure
- Add ticket system section after agent descriptions
- Explain ticket creation, ticket-to-phase workflow, and archival
- Include example usage

**Done when**:
- getting-started.md includes ticket system overview
- Workflow explanation is clear and complete
- Examples help users understand practical usage
- Fits naturally with existing content

## S008: Update greenfield.md to mention tickets

**Intent**: Show greenfield users when and how to use tickets during new project setup.

**Work**:
- Read greenfield.md bootstrap workflow
- Add brief mention of tickets as optional step after Surveyor
- Explain that tickets can capture future work ideas during bootstrap

**Done when**:
- greenfield.md mentions tickets in appropriate location
- Explanation clarifies tickets are optional and when to use them
- Integration doesn't disrupt existing workflow narrative

## S009: Update brownfield.md to mention tickets

**Intent**: Show brownfield users when and how tickets fit into onboarding workflow.

**Work**:
- Read brownfield.md onboarding workflow
- Add brief mention of tickets after Surveyor completes
- Explain using tickets to capture technical debt or improvement ideas identified during survey

**Done when**:
- brownfield.md mentions tickets in appropriate location
- Explanation fits naturally with onboarding narrative
- Clarifies practical use case for tickets in brownfield context

## S010: Increment version in plugin.json

**Intent**: Satisfy L08 requirement to increment version on Phase completion.

**Work**:
- Read `.claude-plugin/plugin.json`
- Increment version field according to semantic versioning
- Update version field only, no other changes

**Done when**:
- Version field in plugin.json is incremented
- JSON syntax remains valid
- No other fields are modified

## S011: Verify all changes

**Intent**: Confirm all modifications maintain syntactic validity and logical correctness.

**Work**:
- Validate all modified markdown files render correctly
- Verify YAML syntax in modified agent front matter
- Verify JSON syntax in plugin.json
- Spot-check that directory creation logic is correct and idempotent

**Done when**:
- All markdown files are syntactically valid
- All YAML is valid
- plugin.json is valid JSON
- Directory creation logic reviewed and confirmed correct
