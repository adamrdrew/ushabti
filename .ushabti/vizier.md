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

### Target Audience & Core Value Proposition

**CRITICAL ARCHITECTURAL PRINCIPLE** (recorded 2026-02-01):

Ushabti is designed for **experienced developers who know what they want to build and how they want to build it**.

**What Ushabti is:**
- A framework for disciplined, bounded development
- A tool for developers with clear intent and direction
- A system for maintaining rigor and documentation across phases

**What Ushabti is NOT:**
- A "getting started with development" tool
- A helping hand for uncertain developers
- A system to guide users through figuring out what to build

**Design implications:**
- Do not add features that guide developers toward decisions
- Do not add discovery or exploration features
- Do not add suggestion engines or recommendation systems
- Focus on workflow discipline, not direction-setting
- Assume developer clarity, enforce developer intent

**Reason:** User feedback confirmed that adding "helpful" features that guide developers would harm the core pattern. The value is in enforcing what experienced developers already know they want to do, not in helping them figure out what to do.

**Related:** This principle validates the recommendation against traditional plugin systems (R004) and supports skill-based preferences (HI006) because skills extend capability without eroding clarity of intent.

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

### Token Consumption Analysis (2026-02-01)

**Token consumption in Claude Code:**
- System prompts (agent definitions, CLAUDE.md) consume tokens on every message
- MCP tool definitions consume tokens even when idle
- Conversation history accumulates tokens
- File reads consume tokens
- Skills consume ~100 tokens for metadata scanning, <5k when invoked
- Prompt caching reduces costs for repeated content
- Auto-compaction summarizes history when approaching limits

**Ushabti's current token footprint:**

**Base context (loaded on every agent invocation):**
- CLAUDE.md: 88 lines (~1,300 tokens)
- Agent definition: 60-247 lines (~900-3,700 tokens depending on agent)
- using-skills catalog: 109 lines (~1,600 tokens)
- **Total base**: ~3,800-6,600 tokens per agent startup

**Skills (on-demand, metadata only until invoked):**
- 20 skills total
- Average skill size: ~25 lines (~375 tokens when loaded)
- Smallest: 8 lines (describe-ushabti)
- Largest: 109 lines (using-skills)
- Skills use ~100 tokens for metadata, full content only when invoked

**Documentation (read by agents during work):**
- .ushabti/docs/: 1185 lines total (~17,800 tokens if all loaded)
- Agents read selectively, not all at once
- Most common reads: agents.md (191 lines), phase-files.md (307 lines)

**Agent prompts:**
- Lawgiver: 152 lines (~2,300 tokens)
- Surveyor: 247 lines (~3,700 tokens) - largest agent
- Builder: 88 lines (~1,300 tokens)
- Overseer: 85 lines (~1,300 tokens)
- Scribe: 60 lines (~900 tokens) - smallest agent
- Artisan: 134 lines (~2,000 tokens)
- Vizier: 184 lines (~2,800 tokens)

**Repetitive patterns identified:**
- "Use the Skill tool to invoke" appears 18 times across agents (verbosity)
- "Agent isolation" vizier.md warning appears in all 6 non-Vizier agents (96 words × 6 = 576 words)
- CLAUDE.md duplicates content from architecture.md (agent table, phase loop, file structure)
- Ancient Egyptian flavor text adds minimal value but consumes tokens

**Key optimization opportunities:**
1. CLAUDE.md contains significant duplication with .ushabti/docs/architecture.md
2. Agent isolation warning repeated 6 times verbatim could be compressed
3. Verbose skill invocation instructions could be terser
4. using-skills catalog lists all 20 skills even when most are irrelevant
5. Agent prompts contain redundant procedural instructions

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
**Note**: Given Ushabti's target audience (experienced developers), examples should demonstrate workflow mechanics, not teach development concepts.

### R004 — Plugin System Architecture Risk (RESOLVED)

**Status**: RESOLVED via architectural clarity (2026-02-01)

**Original risk**: User considering adding "personality plugin" system that could violate core architectural principles.

**Resolution**: User confirmed that guidance-oriented features would harm core pattern. Ushabti is for experienced developers who know their intent. Plugin systems that suggest or guide would erode this clarity.

**Outcome**: Traditional plugin system rejected as architecturally inappropriate. Skill-based preferences (HI006) remain viable as they extend capability without eroding clarity.

### R005 — Token Inefficiency May Impact Cost at Scale

**Risk**: Ushabti's current token consumption patterns include duplication and verbosity that increase costs per agent invocation.

**Impact**:
- Higher costs for users running many phases
- Slower agent startup due to larger context
- Reduced context window available for actual work
- May limit Ushabti adoption in cost-sensitive environments

**Current state**:
- Base context per agent: 3,800-6,600 tokens
- CLAUDE.md + docs duplication: ~1,500 tokens wasted
- Repetitive agent isolation warnings: ~800 tokens across 6 agents
- Verbose skill catalog: ~1,600 tokens (only ~400 needed for most tasks)

**Likelihood**: High - every agent invocation pays this cost

**Severity**: Medium - functional but inefficient; compounds over time

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

**Note**: Examples should demonstrate workflow mechanics for experienced developers, not teach basic development concepts. Focus on showing how Ushabti enforces discipline, not how to think about software design.

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
### HI006 — Skill-Based Preference System

**Opportunity**: Implement agent customization through skill-based preferences rather than traditional plugins.

**Value**:
- Allows preference enforcement (OOP, functional, TDD) without architectural changes
- Enables capability extension (diagram generation) through composable skills
- Preserves file-backed state principle
- Maintains agent clarity and transparency
- Shareable skills can be distributed like current Ushabti skills
- Aligns with Ushabti's target audience: experienced developers who know what they want

**Implementation approach**:
1. Create `.ushabti/config.yaml` schema for declaring preferences
2. Add `read-config` skill for agents to access configuration
3. Create preference skills:
   - `prefer-functional/` - functional programming guidance
   - `enforce-tdd/` - TDD workflow enforcement
   - `generate-block-diagram/` - diagram generation for Overseer
4. Update Builder and Overseer to read config and invoke configured skills
5. Test on a real phase

**Design constraint**: Preference skills should enforce developer intent, not suggest or guide. They validate and verify, they do not recommend or discover.

**Risk**: Low - extends existing skill architecture, no agent boundary changes
**Effort**: Medium - requires config schema, multiple new skills, agent updates
**Impact**: High - provides customization without plugin complexity

**Priority**: Evaluate after HI002 and HI003 are complete

### HI007 — Token Efficiency Optimization

**Opportunity**: Reduce token consumption through strategic refactoring while preserving functionality and clarity.

**Value**:
- Lower cost per agent invocation (estimated 20-35% reduction)
- Faster agent startup
- More context window available for actual work
- Better scaling as codebase and skill library grow
- More competitive on cost vs. alternatives

**Target reductions:**
1. **CLAUDE.md compression**: 88 lines → ~50 lines (save ~600 tokens)
   - Remove content duplicated in architecture.md
   - Link to docs instead of repeating
   - Keep only what's needed for non-agent Claude Code usage

2. **Agent isolation compression**: 6 instances × 16 words → 1 shared reference (~400 token savings)
   - Move to skill: `describe-agent-isolation`
   - Agents reference: "Load describe-agent-isolation for constraints"
   - Single source of truth, 95% token reduction

3. **Skill invocation terseness**: 18 verbose instances → terse pattern (~300 token savings)
   - From: "Use the Skill tool to invoke describe-X for Y"
   - To: "See describe-X for Y"
   - Agent frontmatter already specifies Skill tool access

4. **using-skills optimization**: Smart catalog or lazy loading (~800 token savings)
   - Option A: Categorize skills (phase, docs, validation)
   - Option B: Two-tier catalog (common vs. specialized)
   - Most agent invocations only need 5-8 skills

5. **Remove flavor text**: Ancient Egyptian references (~100 token savings)
   - "Occasionally (rarely) you may use..." appears in 7 agents
   - Minimal value, consistent token cost
   - Can remove entirely or move to style.md

**Total estimated savings**: 2,200-2,500 tokens per agent invocation (35-40% reduction in base context)

**Implementation approach**:
1. Measure current token consumption (baseline)
2. Implement changes in priority order
3. Validate functionality with test phases
4. Measure token reduction
5. Document optimization patterns in style.md

**Tradeoffs:**
- **Clarity vs. efficiency**: Some compression may reduce immediate readability
- **Self-contained vs. referenced**: Moving content to skills adds indirection
- **Stability**: Changes affect all agents, requires careful testing

**Risk**: Medium - changes touch all agents, must preserve functionality
**Effort**: Medium - systematic refactoring with validation
**Impact**: High - meaningful cost reduction for all users

**Priority**: HIGH - cost efficiency benefits all Ushabti users

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
### Plugin System Analysis (2026-02-01)

**User proposal**: Add plugin system for agent "personalities" that could:
- Enforce paradigm preferences (OOP vs functional)
- Enforce methodology preferences (TDD)
- Extend capabilities (generate diagrams)

**Core finding**: Proposal conflates two distinct needs:
1. **Preference enforcement** - already solvable with laws/style or enhanced skill system
2. **Capability extension** - already solvable with skills

**Architectural concerns identified**:
- Traditional plugins would violate agent immutability principle
- Runtime behavior modification creates non-determinism
- Bypasses file-backed state model
- Could erode agent clarity and boundary enforcement
- Risks users bypassing proper laws/style definition

**Implementation options evaluated**:

**Option A: Skill-based preference system (RECOMMENDED)**
- Create `.ushabti/config.yaml` for preference declarations
- Implement preferences as skills agents invoke based on config
- Preserves all architectural principles
- File-backed, transparent, composable
- Skills can be shared/installed independently
- **Filed as HI006**

**Option B: Agent template system**
- Core agent logic in templates
- Personality overlays as YAML files
- Generate final agents by merging
- **Rejected**: Violates immutability, requires build step

**Option C: External plugin hooks**
- True plugin API with runtime hooks
- Maximum extensibility
- **Rejected**: Massive complexity, violates file-backed state, non-deterministic

**Option D: Enhanced style system**
- Extend `.ushabti/style.md` with structured preference declarations
- Skills verify compliance
- **Viable alternative**: Simpler than config.yaml, but less structured

**Option E: Phase-level directives**
- Individual phases declare specific constraints
- Builder reads and applies per-phase
- **Viable alternative**: Good for one-off preferences, not global configuration

**Option F: Agent variant system**
- Maintain official agent variants (builder-functional.md, overseer-visual.md)
- Users select which to use
- **Viable long-term**: Maximum transparency, high maintenance burden

**Recommendation delivered**: Do not implement traditional plugin system. Prototype skill-based preferences (Option A) if customization need is validated. Observe usage before committing to full implementation.

**Key insight**: Ushabti's strength is explicitness and clarity. Any extension mechanism must preserve these properties. Skills provide this. Plugins likely do not.

**Follow-up (2026-02-01)**: User confirmed architectural principle. Ushabti is for experienced developers who know what they want to build. Features that guide or suggest would harm the core pattern. Plugin system rejected as inappropriate for this audience. Skill-based preferences remain viable because they enforce intent without suggesting direction.

### Token Efficiency Research (2026-02-01)

Researched Claude Code token management best practices and analyzed Ushabti's consumption patterns.

**Key learnings from Anthropic documentation:**
- Skills use ~100 tokens for metadata scanning, <5k when invoked (progressive disclosure)
- CLAUDE.md loads into context at session start - should be <500 lines
- Moving instructions from CLAUDE.md to skills reduces base context
- Code intelligence plugins reduce token usage vs. text search
- Specific prompts reduce token waste vs. vague requests
- MCP tools consume tokens even when idle (threshold: 10% of context window)
- Tool search reduces tool token usage by 85%

**Ushabti-specific findings:**
- Base context: 3,800-6,600 tokens per agent (CLAUDE.md + agent + using-skills)
- CLAUDE.md is 88 lines (~1,300 tokens) with significant duplication
- Agent isolation warning appears verbatim in 6 agents (~800 tokens total)
- using-skills catalog lists all 20 skills even when irrelevant (~1,600 tokens)
- Verbose skill invocation pattern repeated 18 times (~300 tokens)
- Ancient Egyptian flavor text adds ~100 tokens across agents

**Optimization potential**: 2,200-2,500 token reduction (35-40%) without functionality loss

**Action**: Created HI007 for systematic token optimization

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
- [ECMA-404 Standard](https://www.ecma-international.org/publications-and-standards/ecma-404/)

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
- [Token-Efficient Tool Use](https://docs.claude.com/en/docs/agents-and-tools/tool-use/token-efficient-tool-use)
- [Manage Costs Effectively](https://code.claude.com/docs/en/costs)

---

_Memory is truth. Update as wisdom grows._
