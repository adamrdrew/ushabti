# Vizier Memory

Counsel offered. This is the working memory of the Vizier agent, tracking observations, risks, and reference material for the Ushabti project.

---

## Observations

### Project Structure
- **Type**: Claude Code plugin implementing an agent-driven development system
- **Core technologies**: Markdown, YAML, JSON (no traditional code)
- **Agent architecture**: Seven specialized agents with enforced boundaries
- **Phase-driven workflow**: Plan (Scribe) → Build (Builder) → Review (Overseer)
- **Most recent phase**: [0008-minimal-bash-permissions](/Users/adam/Development/ushabti/.ushabti/phases/0008-minimal-bash-permissions) - replaced Bash(*) with explicit minimal permissions (complete)

### Technology Stack
- **Markup languages**: Markdown (agent definitions, documentation, phase tracking), YAML (progress tracking, front matter), JSON (plugin manifest)
- **Development tools**: Git, Claude Code CLI, Bash scripts
- **Platform**: Claude Code plugin system

### Documentation System
- **Location**: [.ushabti/docs/](/Users/adam/Development/ushabti/.ushabti/docs/)
- **Created by**: Surveyor agent during onboarding
- **Maintained by**: Builder updates during implementation, Overseer verifies during review
- **Coverage**: Agents, architecture, phase files, plugin structure, skills, configuration
- **Completeness**: 1185 total lines across 8 docs files - comprehensive coverage

### Codebase Health (2026-02-01 Assessment)

**What's working well:**
- **Clean separation of concerns**: Seven agents with hard boundaries, no overlapping responsibilities
- **Comprehensive documentation**: 1185 lines covering all major systems
- **Security hardened**: Phase 0008 replaced Bash(*) with 11 explicit read-only permissions
- **Automation**: Pre-commit hook automatically updates skill catalog
- **Phase discipline**: All 8 phases have complete review.md files, all marked complete
- **Version management**: Plugin version properly incremented per L08
- **Agent isolation**: Vizier memory properly separated from other agents

**Current state:**
- **Laws**: 8 laws defined, all enforced (plugin compliance, file locations, manifest completeness, versioning)
- **Style**: Comprehensive style guide covering prose, markup, docs accuracy, theme usage
- **Agents**: All 7 agents operational with proper frontmatter and tools
- **Skills**: 20 skills total, 5 use bash (all read-only), catalog auto-maintained
- **Tests**: No automated test suite present (Ushabti is markup only, no traditional code to test)
- **Git hooks**: Pre-commit hook for skill catalog reconciliation (working)

---

## Risks

### R001 — Overly Permissive Bash Wildcard (RESOLVED)

**Status**: RESOLVED in Phase 0008

**Resolution**: Replaced `Bash(*)` with 11 explicit read-only command permissions. Security posture significantly improved while maintaining full functionality.

### R002 — No Automated Validation

**Risk**: Plugin manifest, agent frontmatter, and skill frontmatter are not automatically validated before commits.

**Impact**: Invalid JSON or YAML could be committed, breaking plugin loading for users. Law L01 requires `claude plugin validate .` to pass, but this is not enforced pre-commit.

**Likelihood**: Medium - humans can miss validation steps

**Current state**: Manual validation expected during Overseer review

### R003 — Missing User Onboarding Examples

**Risk**: New users may struggle to understand the complete workflow without concrete examples.

**Impact**: Reduced adoption, increased support burden, potential misuse of agents

**Current state**: README is comprehensive but abstract. No step-by-step examples of a complete Phase cycle from planning through review.

### R004 — Memory Leak from Skill Bash Commands (CRITICAL)

**Status**: ACTIVE - Critical memory leak identified

**Risk**: Skills containing embedded bash commands (using `!` backtick syntax) execute every time a skill is loaded. These commands iterate over all phase directories with multiple grep/awk operations, generating potentially unbounded output.

**Impact**: SEVERE - Claude Code memory balloons to 30GB rapidly, not gradually. User reports "fast and all at once" memory spikes.

**Root cause**: Skills with bash command injection patterns:
1. **find-current-phase** (line 11): Loops over `.ushabti/phases/*/`, runs `grep` and `awk` on each `progress.yaml`
2. **find-next-step** (line 11): Multiple `grep` and `awk` operations per phase directory with counting
3. **get-phase-status** (line 11): Loops over all phases with multiple `grep -c` operations
4. **find-next-phase-number** (line 11): Lists all phases, pipes through `sed`, `sort`, `tail`
5. **check-ushabti-prerequisites** (lines 11-14): Four file existence checks

**Why this causes memory leaks**:
- Skills are loaded at agent startup and during skill invocations
- Bash commands execute immediately when skill markdown is rendered
- Output is captured and held in memory
- With 8+ phases and multiple agents invoking skills, memory accumulates rapidly
- No cleanup mechanism between skill loads

**Severity**: CRITICAL - Makes the system unusable on projects with multiple phases

**Likelihood**: CERTAIN - Happens on every agent invocation that loads these skills

**Affected agents**: All 7 agents (all have `using-skills` skill loaded, which catalogs the problematic skills)

**Evidence**:
- `/Users/adam/Development/ushabti/skills/find-current-phase/SKILL.md:11`
- `/Users/adam/Development/ushabti/skills/find-next-step/SKILL.md:11`
- `/Users/adam/Development/ushabti/skills/get-phase-status/SKILL.md:11`
- `/Users/adam/Development/ushabti/skills/find-next-phase-number/SKILL.md:11`
- `/Users/adam/Development/ushabti/skills/check-ushabti-prerequisites/SKILL.md:11-14`

---

## High-Impact Work

### HI001 — Secure Permissions Configuration (COMPLETED)

**Status**: COMPLETED in Phase 0008

### HI002 — Pre-Commit Validation Hook

**Opportunity**: Add `claude plugin validate .` to the pre-commit hook to catch manifest errors before they're committed.

**Value**:
- Enforces Law L01 automatically
- Catches JSON syntax errors, missing files, schema violations
- Zero ongoing maintenance cost once implemented
- Prevents broken states from reaching users

**Implementation approach**:
1. Update `.githooks/pre-commit` to run `claude plugin validate .`
2. Exit with failure if validation fails
3. Document in README under Development section
4. Test with intentionally broken manifest

**Risk**: Low - validation is read-only and fast
**Effort**: Low - 10-15 lines in existing hook
**Impact**: High - prevents entire class of defects

### HI003 — Example-Driven Documentation

**Opportunity**: Add concrete, end-to-end examples showing the full workflow for a small feature.

**Value**:
- Dramatically lowers onboarding friction
- Demonstrates agent boundaries in practice
- Shows what good Phase planning looks like
- Provides template for users to follow

**Implementation approach**:
1. Create `.ushabti/docs/examples.md`
2. Walk through a complete example: "Add a new skill"
   - Scribe planning session (what phase.md and steps.md look like)
   - Builder implementation (how progress.yaml updates)
   - Overseer review (what review.md contains)
3. Show agent prompts user would actually type
4. Link from README "Getting Started" section

**Risk**: Low - documentation only, no code changes
**Effort**: Medium - requires thoughtful example selection and clear writing
**Impact**: High - addresses primary adoption barrier

### HI004 — Agent Startup Latency Reduction

**Opportunity**: Skills are loaded on-demand, but `using-skills` catalog is large (20 skills). Consider splitting catalog into categories or lazy-loading.

**Value**:
- Faster agent startup
- Reduced token usage per agent invocation
- Better scalability as skill count grows

**Implementation approach**:
1. Analyze token cost of current `using-skills/SKILL.md`
2. Consider categorizing skills (phase-management, docs, validation, etc.)
3. Agent loads category catalog, invokes category skill, then specific skill
4. Measure improvement

**Risk**: Medium - changes skill invocation pattern, affects all agents
**Effort**: Medium - requires skill reorganization and catalog split
**Impact**: Medium - optimization, not critical path issue

**Current assessment**: Not urgent. 20 skills is manageable. Revisit when skill count exceeds 30.

### HI005 — Progress.yaml Schema Validation

**Opportunity**: Add a skill or law that validates progress.yaml structure against a defined schema.

**Value**:
- Catches malformed progress files before review
- Ensures Builder updates are machine-parseable
- Prevents drift in progress.yaml format across phases

**Implementation approach**:
1. Define JSON Schema for progress.yaml structure
2. Add `validate-progress` skill that checks schema compliance
3. Builder invokes skill before marking phase status as "review"
4. Overseer invokes skill during review

**Risk**: Low - validation only, doesn't modify files
**Effort**: Medium - requires schema definition and validation logic
**Impact**: Medium - catches errors earlier, reduces review friction

### HI006 — Eliminate Skill Bash Command Injection (URGENT)

**Opportunity**: Remove all embedded bash commands from skills to fix critical memory leak.

**Value**:
- **CRITICAL**: Eliminates 30GB memory leak issue
- Prevents system from becoming unusable on projects with multiple phases
- Improves agent startup performance
- Reduces token usage per invocation

**Implementation approach**:
1. Remove all `!` backtick bash command patterns from skill files
2. Convert skills to pure documentation (explain what to check, not execute checks)
3. Agents should invoke bash commands directly via Bash tool when needed
4. Update skill documentation to describe procedures rather than execute them
5. Alternative: Move dynamic queries to agent startup procedures instead of skills

**Affected skills** (all in `/Users/adam/Development/ushabti/skills/`):
- `find-current-phase/SKILL.md:11`
- `find-next-step/SKILL.md:11`
- `get-phase-status/SKILL.md:11`
- `find-next-phase-number/SKILL.md:11`
- `check-ushabti-prerequisites/SKILL.md:11-14`

**Risk**: Low - removes problematic pattern, agents can still execute bash via Bash tool
**Effort**: Low - remove ~5 lines per skill, document procedures instead
**Impact**: CRITICAL - fixes severe memory leak, makes system usable

**Urgency**: IMMEDIATE - blocks all multi-phase usage

---

## Notes

### Initial Startup
- Vizier.md created on 2026-02-01
- Project has 8 completed phases (0001-0008)
- All core agents operational: Lawgiver, Artisan, Surveyor, Scribe, Builder, Overseer, Vizier
- Phase 0008 completed security hardening of bash permissions

### Permissions Investigation (2026-02-01)
- Examined all 20 skills for bash command usage
- Only 5 skills execute bash commands (all read-only)
- Commands used: `ls`, `grep`, `awk`, `basename`, `echo`, `sed`, `sort`, `tail`, `printf`, `[ -f ]`, `[ -d ]`
- All commands operate on `.ushabti/` directory only
- No network access, no destructive operations, no writes outside skill execution context
- Researched Claude Code permission model via official documentation
- Skills cannot declare permissions - this is a platform constraint
- Agent `permissionMode` and `allowed-tools` fields exist but don't solve the permission grant problem
- Only project-level or user-level permissions can grant bash command access

### Codebase Assessment (2026-02-01)
- Reviewed all 8 completed phases - all have proper review.md and complete status
- Examined agent definitions - all 7 agents have proper frontmatter and tools
- Reviewed documentation - comprehensive coverage across 8 files (1185 lines)
- Checked git hooks - pre-commit hook working, updates skill catalog automatically
- Assessed permissions - Phase 0008 completed security hardening
- No automated test suite (not applicable - Ushabti is markup-based, no traditional code)
- No automated validation in CI/CD (opportunity for improvement)

### Memory Leak Investigation (2026-02-01)
- User reported severe memory leaks (30GB) happening "fast and all at once"
- Investigated all skills, agent configs, and scripts for problematic patterns
- **ROOT CAUSE IDENTIFIED**: Skills with embedded bash commands using `!` backtick syntax
- These commands execute every time skills are loaded (agent startup, skill invocations)
- 5 skills iterate over phase directories with grep/awk, generating unbounded output
- Output accumulates in memory without cleanup between loads
- Memory leak severity scales with number of phases in project
- All 7 agents affected (all load `using-skills` which catalogs problematic skills)
- **RECOMMENDED FIX**: Remove all bash command injection from skills (HI006)

---

## Reference Library

Curated links to official documentation for technologies used in this project.

### Languages

**Markdown**
- [CommonMark Specification](https://spec.commonmark.org/)
- [Markdown Guide](https://www.markdownguide.org/) - Official guide

**YAML**
- [YAML Specification 1.2](https://yaml.org/spec/1.2.2/)

**JSON**
- [JSON Specification](https://www.json.org/)
- [ECMA-404 Standard](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/)

### Tools

**Git**
- [Git Official Documentation](https://git-scm.com/doc)
- [Git Reference Manual](https://git-scm.com/docs)

**Bash**
- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)

**Claude Code**
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Claude Plugin Documentation](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [Claude Code Sub-Agents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)

---

_Memory is truth. Update as wisdom grows._
