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

### Permissions Architecture (2026-02-01 Investigation)

Skills can be invoked in two contexts:
1. **User context**: Direct invocation gets permission prompts
2. **Agent context**: Skills invoked by agents fail silently if permissions missing

**Current permission state:**
- `.claude/settings.json`: Contains `Bash(*)` wildcard (committed to repo)
- `.claude/settings.local.json`: Contains many specific bash permissions (not committed)
- Agent definitions: No permissions configured in agent YAML front matter
- Current workaround: `Bash(*)` in project settings.json

**Skills requiring bash permissions (4 of 20):**
- `check-ushabti-prerequisites`: `[ -f path ]`, `[ -d path ]`, `echo`
- `find-current-phase`: `ls`, `grep`, `awk`, `basename`, `echo`, shell loops
- `find-next-phase-number`: `ls`, `sed`, `sort`, `tail`, `printf`
- `find-next-step`: `ls`, `grep`, `awk`, `basename`, `echo`, shell loops
- `get-phase-status`: `ls`, `grep`, `awk`, `basename`, `echo`, shell loops

All skill bash commands are read-only operations against the `.ushabti/` directory structure.

---

## Risks

### R001 — Overly Permissive Bash Wildcard

**Risk**: The `Bash(*)` permission in `.claude/settings.json` allows any bash command without restriction. While convenient for skills, this creates a broad security surface.

**Impact**: An agent or skill could theoretically execute destructive operations (rm, curl to external sites, etc.) without user approval.

**Mitigation options**:
1. Replace `Bash(*)` with specific command permissions
2. Configure permissions at agent level via YAML front matter
3. Use both project-level and agent-level permissions for defense in depth

**Current status**: Active in `.claude/settings.json` (committed)

---

## High-Impact Work

### HI001 — Secure Permissions Configuration

**Opportunity**: Replace the `Bash(*)` wildcard with minimal, specific permissions that precisely match what skills actually need.

**Value**: Improved security posture while maintaining seamless skill execution for both user and agent contexts.

**Approach**: 
- Define specific bash command permissions for the 4 skills that need them
- Configure permissions at both project and agent level
- Ensure agents can invoke skills without prompts or silent failures
- Document the pattern for future skill development

---

## Notes

### Initial Startup
- Vizier.md created on 2026-02-01
- Project has 7 completed phases (0001-0007)
- All core agents operational: Lawgiver, Artisan, Surveyor, Scribe, Builder, Overseer, Vizier
- Phase 0007 just completed, adding Reference Library feature to Vizier

### Permissions Investigation (2026-02-01)
- Examined all 20 skills for bash command usage
- Only 4 skills execute bash commands (all read-only)
- Commands used: `ls`, `grep`, `awk`, `basename`, `echo`, `sed`, `sort`, `tail`, `printf`, `[ -f ]`, `[ -d ]`
- All commands operate on `.ushabti/` directory only
- No network access, no destructive operations, no writes outside skill execution context

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

---

_Memory is truth. Update as wisdom grows._
