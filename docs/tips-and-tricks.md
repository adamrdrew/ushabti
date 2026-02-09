# Tips and Tricks

Advanced patterns and non-obvious techniques for effective Ushabti usage.

## Vizier: Your Advisory Agent

Vizier is the only agent that doesn't participate in the Phase loop. It's purely advisory — answering questions, evaluating options, identifying risks, and maintaining memory.

### Pattern: Evaluate Before Planning

Before asking Scribe to plan a Phase, consult Vizier to explore the problem space.

```
/agent vizier
```

> "I need to add user authentication. What are the tradeoffs between JWT tokens and session-based auth for a FastAPI application?"

Vizier evaluates options without committing to a plan. Once you've decided on an approach, ask Scribe to plan the Phase.

**Why this works**: Scribe plans execution. Vizier explores possibilities. Separate exploration from commitment.

### Pattern: Ask Vizier to Remember Context

Vizier maintains memory at `.ushabti/vizier.md`. Use this to capture decisions, patterns, or context that should persist across sessions.

```
/agent vizier
```

> "Remember: we decided to use PostgreSQL with asyncpg for the database layer because SQLAlchemy's async support wasn't mature enough at the time. We may revisit this in 6 months."

Later sessions can reference this memory:

> "What did we decide about database libraries?"

**Why this works**: Agents don't have conversation history across sessions. Vizier's memory file provides continuity.

### Pattern: Use Vizier to Identify High-Impact Work

After Surveyor creates documentation, ask Vizier to analyze it and suggest priorities.

```
/agent vizier
```

> "Review the documentation in `.ushabti/docs/` and suggest the three highest-impact improvements we could make to this codebase."

Vizier can spot technical debt, missing capabilities, or integration opportunities that make valuable Phases.

**Why this works**: Vizier sees the whole picture without execution pressure. Let it guide your roadmap.

### Pattern: Vizier as a Sounding Board

Use Vizier to pressure-test ideas before committing to a Phase.

```
/agent vizier
```

> "I'm thinking about refactoring the authentication middleware to support multiple auth schemes. What risks or complications should I consider?"

Vizier identifies edge cases, backwards compatibility concerns, and implementation pitfalls.

**Why this works**: It's cheaper to discover problems during exploration than during implementation.

### Vizier's Reference Library

Vizier can curate and maintain a Reference Library of official documentation URLs for technologies your project uses. This ensures agents have access to canonical information sources.

```
/agent vizier
```

> "Add FastAPI's official documentation and PostgreSQL's async driver docs to the reference library."

Vizier stores these in `.ushabti/vizier.md` and can consult them when answering questions.

**Why this works**: Agents' training data may be outdated. Reference libraries keep Vizier's advice current.

## Documentation Integration

The `.ushabti/docs/` directory is not static onboarding material — it's a living resource that evolves with your code.

### Pattern: Consult Docs Before Every Phase

Even if you think you know your codebase, skim the docs before planning a Phase. Surveyor may have documented nuances you forgot.

**Example**: You're planning a Phase to add caching. Check `architecture.md` — you might discover an existing caching layer you didn't remember.

### Pattern: Update Docs Proactively

If you notice during implementation that docs are stale or incomplete, don't wait. Builder can add a step to reconcile them.

**Example**: While implementing, you discover a configuration option that isn't documented. Add a step: "Update `configuration.md` to document the new cache timeout setting."

### Pattern: Docs as Handoff Documentation

When onboarding new team members (human or AI), point them to `.ushabti/docs/` first. It captures what Surveyor learned about the codebase in a structured, navigable format.

**Why this works**: Docs are written for agents, which means they're explicit, unambiguous, and comprehensive. Humans benefit too.

## Phase Sizing and Scoping

### Pattern: Split When Unsure

If you're unsure whether a goal fits in one Phase, ask Scribe to plan it. Scribe will push back if it's too large and suggest a split.

**Example**: "Plan a Phase to add user authentication" might get split into:
- Phase 1: JWT token generation and validation
- Phase 2: Login/logout endpoints
- Phase 3: Middleware integration

**Why this works**: Scribe is trained to keep Phases small. Trust its judgment.

### Pattern: Acceptance Criteria Drive Scope

When prompting Scribe, include acceptance criteria. This helps Scribe bound the Phase correctly.

**Example**:

> "Plan a Phase to add caching. Acceptance criteria:
> - Cache GET requests for public endpoints
> - Cache TTL configurable via environment variable
> - Cache hit/miss metrics exposed via /metrics endpoint
> Done when all three criteria are met, not more."

**Why this works**: Explicit acceptance criteria prevent scope creep.

### Pattern: Defer Non-Critical Work

If Builder discovers missing work that's not critical to the Phase's acceptance criteria, don't add it as a step. Note it in Vizier's memory and plan it as a future Phase.

**Example**: While implementing caching, Builder notices unrelated logging gaps. Don't add logging steps to the caching Phase. Ask Vizier to remember it for later.

**Why this works**: Keeps Phases focused. Prevents one Phase from ballooning into three.

## Skills and Introspection

Ushabti agents have access to 20+ skills that provide domain knowledge on-demand. Users can invoke these too.

### Available Skills

Invoke skills using the Skill tool in any conversation with an agent:

```
Skill(skill-name)
```

**Useful skills for users:**
- `describe-ushabti`: Core concepts and lifecycle
- `describe-agent-roles`: Agent responsibilities and boundaries
- `describe-phase-loop`: Plan-Build-Review cycle
- `find-current-phase`: Locate the active phase directory
- `get-phase-status`: Check current phase status
- `describe-laws-and-style`: Distinction between laws and style
- `describe-docs-system`: Documentation maintenance requirements
- `describe-progress-file`: Progress.yaml structure and field ownership

### Pattern: Invoke Skills to Understand State

If you're unsure which Phase is active or what its status is, invoke a skill:

```
/agent vizier
Skill(find-current-phase)
Skill(get-phase-status)
```

Vizier will use the skills to answer your question with current state.

**Why this works**: Skills provide ground truth about repository state without manual file inspection.

### Pattern: Learn Conventions On-Demand

If you forget the format for a Phase file or step definition, invoke the relevant skill:

```
Skill(describe-phase-file)
Skill(describe-steps-file)
```

**Why this works**: Skills are the canonical reference. Use them instead of guessing.

## Progress Tracking and Transparency

### Pattern: Read progress.yaml Between Steps

Builder updates `progress.yaml` after every step. If you want to monitor progress, read this file.

```yaml
steps:
  - id: S001
    title: Add caching configuration
    implemented: true
    reviewed: false
    notes: "Added CACHE_TTL env var with default 300s"
    touched:
      - src/config.py
      - tests/test_config.py
```

**Why this works**: You see exactly what's done, what's pending, and what files were modified. No guessing.

### Pattern: Check Touched Files for Context

The `touched` list in `progress.yaml` shows which files each step modified. Use this to understand the scope of changes without reading diffs.

**Why this works**: Touched files give you a map of what changed during the Phase.

## Working with Laws and Style

### Pattern: Evolve Style, Not Laws

If you discover a convention you want to change, update `.ushabti/style.md`, not `.ushabti/laws.md`. Laws are invariants. Style evolves.

**Example**: You decide to switch from `unittest` to `pytest`. This is a style change, not a law change.

**Why this works**: Laws signal "this must never change." Style signals "this is how we do it now."

### Pattern: Add Laws Sparingly

Only add a law if violating it would break the project fundamentally. Most constraints are style, not laws.

**Example**:
- Law: "No SQL injection vulnerabilities" ✓
- Style: "Use parameterized queries" ✓
- Law: "All functions must have docstrings" ✗ (this is style)

**Why this works**: Too many laws make the project rigid. Laws should protect invariants, not encode preferences.

### Pattern: Audit Laws During Review

When Overseer reviews a Phase, it checks law compliance. If a law is repeatedly in tension with development, revisit whether it's truly an invariant or should be style instead.

**Why this works**: Laws that conflict with practical development should be demoted to style or removed.

## Builder and Overseer Dynamics

### Pattern: Don't Skip Overseer

Even if Builder says "all steps implemented," run Overseer. Builder cannot approve its own work.

**Why this works**: Overseer is the gatekeeper. It verifies acceptance criteria, checks compliance, and catches issues Builder might miss.

### Pattern: Read review.md After Overseer Runs

Overseer writes findings to `review.md`. Even if the Phase is green, read this file. Overseer may note observations, minor issues, or suggestions for future work.

**Why this works**: Overseer's insights help you improve future Phases.

### Pattern: Let Overseer Add Steps

If Overseer finds missing work, it will add steps and send the Phase back to Builder. Don't fight this. Trust the process.

**Why this works**: Overseer catches gaps. Addressing them before declaring the Phase complete prevents technical debt.

## Iteration and Momentum

### Pattern: Plan One Phase Ahead, Not Five

Don't over-plan. Plan the next Phase, complete it, then plan the next. Ushabti optimizes for iteration, not prediction.

**Why this works**: Requirements change. Early plans become stale. Plan just-in-time.

### Pattern: Small Phases Compound

A Phase with 5 steps completed today beats a Phase with 20 steps that drags across a week. Keep Phases small.

**Why this works**: Small Phases provide faster feedback, clearer progress, and less context switching.

### Pattern: Use the Loop to Build Intuition

The first few Phases will feel slow and ceremonial. Stick with it. By Phase 5, the loop becomes intuitive and the overhead disappears.

**Why this works**: Discipline up front creates speed later. The loop teaches you to think in bounded units of work.

## Automated Phase Loops with Ir-Kat

### Pattern: One-Shot Phase Execution

Use the `ir-kat` skill to run a complete Plan → Build → Review cycle without manual handoffs between agents.

```
/ir-kat Build a REST API for user management with JWT authentication
```

Ir-kat creates a task list, invokes Scribe to plan, Builder to implement, and Overseer to review. If the Overseer kicks back, ir-kat feeds the review to Builder and resubmits — up to 3 cycles before declaring the phase blocked.

**Why this works**: Eliminates the manual `/agent scribe` → `/agent builder` → `/agent overseer` handoff. Useful when you trust the process and want to let it run.

### Pattern: File-Based Prompts for Complex Phases

For detailed prompts with acceptance criteria, write a PHASE_PROMPT file and pass it to ir-kat:

```
/ir-kat /path/to/PHASE_PROMPT.md
```

**Why this works**: Complex prompts are easier to write, review, and iterate on as files than as inline text.

### Pattern: Watch for Kickback Deflation

When the Overseer kicks back and the Builder fixes, the Builder tends to prioritise "pass the review" over "preserve the original intent." After multiple review cycles, the output may be more conservative than intended. If this happens, review the final result and consider whether a fresh phase with a more specific prompt would produce better results.

**Why this works**: Awareness of this dynamic helps you calibrate when to let ir-kat retry versus when to intervene manually.

## Commit Strategy

### Pattern: Commit Per Phase

When Overseer declares a Phase complete, commit all changes with a message referencing the Phase:

```bash
git add .
git commit -m "Complete Phase 0003: Add request ID tracing

- Added request_id middleware
- Updated all API responses to include request_id
- Added tracing to logs

Phase: .ushabti/phases/0003-request-tracing"
```

**Why this works**: Phases are logical units of work. One Phase = one commit provides a clean, navigable history.

### Pattern: Don't Commit Mid-Phase

Avoid committing incomplete Phases. Wait until Overseer approves.

**Why this works**: Every commit represents a complete, reviewed unit of work. No half-finished states in history.

## Emergency Escape Hatches

### Pattern: Add Steps If the Plan is Wrong

If Builder discovers the plan is fundamentally flawed, it will add steps to `steps.md` to correct course. This is expected.

**Why this works**: Plans are fallible. Builder can adapt without breaking the loop.

### Pattern: Stop and Replan If Scope Explodes

If a Phase balloons in scope (Builder keeps adding steps), stop. Ask Scribe to replan it as multiple smaller Phases.

**Why this works**: Runaway Phases are a signal that the original scope was too large. Fix it by splitting.

## Vizier Memory as Project Knowledge Base

Vizier's memory file (`.ushabti/vizier.md`) can serve as a lightweight knowledge base for project-specific decisions, patterns, and context.

### Pattern: Seed Vizier with Architectural Decisions

After making a significant architectural choice, ask Vizier to document it:

```
/agent vizier
```

> "Remember: we chose to use a message queue for async tasks because we need reliable delivery and retry semantics. We evaluated Celery and Dramatiq, and chose Dramatiq for its simpler setup and better async support."

**Why this works**: Future Phases can reference this context without re-litigating the decision.

### Pattern: Document "Why" in Vizier, "What" in Docs

Use `.ushabti/docs/` for "what exists" and `.ushabti/vizier.md` for "why we chose this."

**Example**:
- Docs: "The API uses Dramatiq for background tasks."
- Vizier: "We chose Dramatiq over Celery because we needed better async support and simpler configuration."

**Why this works**: Docs describe the system. Vizier captures reasoning.

---

These patterns emerge from real usage. Experiment. Adapt. Let the loop teach you what works.
