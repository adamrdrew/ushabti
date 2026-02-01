# Vizier Memory

Counsel offered. This is the working memory of the Vizier agent, tracking observations, risks, and reference material for the Ushabti project.

---

## Observations

### Project Structure
- **Type**: Claude Code plugin implementing an agent-driven development system
- **Core technologies**: Markdown, YAML, JSON (no traditional code)
- **Agent architecture**: Seven specialized agents with enforced boundaries
- **Phase-driven workflow**: Plan (Scribe) → Build (Builder) → Review (Overseer)
- **Most recent phase**: [0007-vizier-library](/Users/adam/Development/ushabti/.ushabti/phases/0007-vizier-library) - added Reference Library capability to Vizier (complete)

### Technology Stack
- **Markup languages**: Markdown (agent definitions, documentation, phase tracking), YAML (progress tracking, front matter), JSON (plugin manifest)
- **Development tools**: Git, Claude Code CLI, Bash scripts
- **Platform**: Claude Code plugin system

### Documentation System
- **Location**: [.ushabti/docs/](/Users/adam/Development/ushabti/.ushabti/docs/)
- **Created by**: Surveyor agent during onboarding
- **Maintained by**: Builder updates during implementation, Overseer verifies during review
- **Coverage**: Agents, architecture, phase files, plugin structure, skills, configuration

### Permissions Architecture (2026-02-01 Deep Investigation)

**Permission system overview:**

Claude Code permissions flow through three layers:
1. **Project-level** (`.claude/settings.json`) - committed, shared across team
2. **User-level** (`.claude/settings.local.json`) - local only, not committed
3. **Agent/Skill-level** (YAML frontmatter) - embedded in agent/skill definitions

**Current permission state:**
- `.claude/settings.json`: Contains `Bash(*)` wildcard (committed to repo)
- `.claude/settings.local.json`: Contains many specific bash permissions (not committed)
- Agent definitions: All use `permissionMode: default` with no specific permissions
- Skills: No permission configuration in frontmatter (skills don't support permissions)

**Agent permission modes available:**
- `default` - standard permission checking with prompts
- `acceptEdits` - auto-accept file edits
- `dontAsk` - auto-deny permission prompts (explicitly allowed tools still work)
- `bypassPermissions` - skip all permission checks (dangerous)
- `plan` - plan mode (read-only exploration)

**Skills requiring bash permissions (5 of 20):**
- `check-ushabti-prerequisites`: `[ -f path ]`, `[ -d path ]`, `echo`
- `find-current-phase`: `ls`, `grep`, `awk`, `basename`, `echo`, shell loops
- `find-next-phase-number`: `ls`, `sed`, `sort`, `tail`, `printf`
- `find-next-step`: `ls`, `grep`, `awk`, `basename`, `echo`, shell loops
- `get-phase-status`: `ls`, `grep`, `awk`, `basename`, `echo`, shell loops

All skill bash commands are read-only operations against the `.ushabti/` directory structure. No writes, no network access, no destructive operations.

**Permission inheritance model:**
- Agents inherit project-level permissions from settings.json
- Skills inherit permissions from the invoking context (user or agent)
- Skills themselves cannot declare permissions - this is a Claude Code platform limitation
- When an agent invokes a skill, the skill runs with the agent's permission set

**The problem:**
- User invocation: If permissions missing → user gets prompted → can approve
- Agent invocation: If permissions missing → operation fails silently → agent doesn't know why
- Current workaround: `Bash(*)` in project settings.json gives blanket approval

---

## Risks

### R001 — Overly Permissive Bash Wildcard

**Risk**: The `Bash(*)` permission in `.claude/settings.json` allows any bash command without restriction. While convenient for skills, this creates a broad security surface.

**Impact**: An agent or skill could theoretically execute destructive operations (rm, curl to external sites, etc.) without user approval.

**Root cause**: Skills cannot declare their own permissions in frontmatter. The only way to ensure skills work when invoked by agents is to grant permissions at the project level.

**Current status**: Active in `.claude/settings.json` (committed)

---

## High-Impact Work

### HI001 — Secure Permissions Configuration

**Opportunity**: Replace the `Bash(*)` wildcard with minimal, specific permissions that precisely match what skills actually need.

**Value**: Improved security posture while maintaining seamless skill execution for both user and agent contexts.

**Recommended approach**:

Since skills cannot declare permissions and agents inherit from project settings, the solution is to configure precise permissions in `.claude/settings.json` that cover all skill requirements.

**Specific bash commands needed:**
```json
{
  "permissions": {
    "allow": [
      "Bash([ -f *)",
      "Bash([ -d *)",
      "Bash(ls *)",
      "Bash(grep *)",
      "Bash(awk *)",
      "Bash(basename *)",
      "Bash(echo *)",
      "Bash(sed *)",
      "Bash(sort *)",
      "Bash(tail *)",
      "Bash(printf *)"
    ]
  }
}
```

**Alternative approaches considered:**

1. **Agent-level permissions**: Configure `permissionMode: bypassPermissions` in agent frontmatter
   - **Pros**: Removes friction for agent skill invocation
   - **Cons**: Too broad - agents could bypass permissions for non-skill operations
   - **Verdict**: Not recommended - violates principle of least privilege

2. **Skill-level allowed-tools**: Use `allowed-tools` field in skill frontmatter
   - **Pros**: Granular control per skill
   - **Cons**: `allowed-tools` restricts which tools are available, but doesn't grant permissions for specific commands
   - **Verdict**: Not applicable - doesn't solve the permission grant problem

3. **Hybrid approach**: Project-level specific permissions + agent documentation
   - **Pros**: Precise permissions, clear audit trail, works for all agents
   - **Cons**: Requires maintenance when adding new skills
   - **Verdict**: Recommended - balances security and functionality

**Implementation notes:**
- All bash commands used by skills are read-only
- Permissions can be scoped to specific command patterns (e.g., `Bash(ls .ushabti/*)` if further restriction needed)
- Document this pattern in `.ushabti/docs/` for future skill authors

---

## Notes

### Initial Startup
- Vizier.md created on 2026-02-01
- Project has 7 completed phases (0001-0007)
- All core agents operational: Lawgiver, Artisan, Surveyor, Scribe, Builder, Overseer, Vizier
- Phase 0007 just completed, adding Reference Library feature to Vizier

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
