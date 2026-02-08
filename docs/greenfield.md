# Greenfield Projects with Ushabti

This guide walks through starting a brand new project from scratch using Ushabti.

## Overview

When building a new project with Ushabti, you begin by establishing the foundation — laws, style, and initial documentation — before entering the Phase loop. This bootstrap process sets up the structure that guides all future development.

## Step-by-Step Workflow

### 1. Create Your Repository

Start with a new repository. It can be completely empty or have basic scaffolding (README, license, etc.).

```bash
mkdir my-new-project
cd my-new-project
git init
```

### 2. Install Ushabti

Install the Ushabti plugin and configure permissions:

```
/plugin marketplace add adamrdrew/marketplace
/plugin install ushabti@adamrdrew
```

Add permissions to `.claude/settings.json`:

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

### 3. Bootstrap: Lawgiver

Run Lawgiver first to capture your project's invariants — the absolute constraints that must always hold.

```
/agent lawgiver
```

**What to tell Lawgiver:**
- Architectural constraints (e.g., "no circular dependencies between modules")
- Security requirements (e.g., "all API keys must be in environment variables")
- Performance guarantees (e.g., "all API responses must return within 200ms")
- Forbidden patterns (e.g., "no global mutable state")
- Technology constraints (e.g., "Python 3.11+", "no database ORMs")

**Example prompt:**

> "This is a new REST API in Python using FastAPI. Laws:
> - Python 3.11 or later required
> - All dependencies must be pinned with exact versions
> - No global mutable state
> - All secrets must come from environment variables
> - API responses must include request IDs for tracing
> - Tests must not touch external services without explicit mocks"

**Output**: Lawgiver creates `.ushabti/laws.md` and a minimal docs scaffold at `.ushabti/docs/index.md`.

### 4. Bootstrap: Artisan

Run Artisan next to define how you build things — your style conventions.

```
/agent artisan
```

**What to tell Artisan:**
- Directory structure preferences
- Naming conventions (files, functions, variables)
- Testing strategy (where tests live, how they're named, coverage expectations)
- Error handling patterns
- Logging and observability conventions
- Code formatting and linting tools

**Example prompt:**

> "Define style for the FastAPI project. Conventions:
> - Use `src/` for application code, `tests/` for tests
> - One test file per source file: `test_<module>.py`
> - Use `snake_case` for all Python identifiers
> - Errors should include structured context via `structlog`
> - All public functions must have docstrings
> - Use `black` for formatting, `ruff` for linting
> - Test coverage must be 80% or higher"

**Output**: Artisan creates `.ushabti/style.md`.

### 5. Bootstrap: Surveyor (Optional)

For greenfield projects, Surveyor is optional at this stage since there's minimal code to document. However, running Surveyor establishes the docs structure early.

```
/agent surveyor
```

Surveyor will explore your repository (even if mostly empty) and create initial documentation describing what exists. This gives you a baseline docs structure that grows with your project.

**Output**: Enhanced `.ushabti/docs/` with project-specific documentation.

**When to skip**: If your repository is truly empty, you can skip Surveyor initially and run it after your first few Phases have added structure.

### 5a. Capture Ideas with Cards (Optional)

During bootstrap, you may identify future work that's not essential for the first Phase. Create cards to capture these ideas:

```
/skill create-card
```

Cards let you record improvement ideas, technical debt, or nice-to-have features without bloating your first Phase. Examples:
- "Add request rate limiting"
- "Implement background job processing"
- "Create admin dashboard"

Later, when planning Phases, you can tell Scribe to create a Phase based on a card slug. See [Getting Started](getting-started.md) for detailed card workflow.

### 6. Plan Your First Phase

Now that laws and style are established, ask Scribe to plan your first Phase of actual work.

```
/agent scribe
```

**Example prompt:**

> "Plan a Phase to set up the initial FastAPI project structure with configuration, logging, and a health check endpoint."

**What Scribe does:**
- Consults `.ushabti/laws.md` and `.ushabti/style.md`
- Consults `.ushabti/docs/` if available
- Creates a Phase directory: `.ushabti/phases/0001-initial-setup/`
- Writes `phase.md` with intent, scope, and acceptance criteria
- Writes `steps.md` with ordered implementation steps
- Creates `progress.yaml` to track step completion
- Creates `review.md` scaffold

**Keep Phases small**: Scribe aims for 5–15 steps. If your goal is large, Scribe will scope it down or suggest splitting into multiple Phases.

### 7. Build the Phase

Hand the Phase to Builder to implement it.

```
/agent builder
```

Builder reads laws, style, docs, and the Phase plan, then:
- Implements steps in order
- Updates `progress.yaml` after each step
- Updates documentation if code changes affect documented systems
- Adds new steps if missing work is discovered

**You don't need to watch**: Builder is autonomous. You can check in periodically or wait until it hands off to Overseer.

### 8. Review the Phase

When Builder completes all steps, hand the Phase to Overseer.

```
/agent overseer
```

Overseer verifies:
- All acceptance criteria are met
- Laws are not violated
- Style is followed
- Tests pass (if applicable)
- Documentation is current

**Overseer's decision**:
- **Green**: Phase is complete. Overseer sets status to `complete` in `progress.yaml`.
- **Needs work**: Overseer adds follow-up steps to `steps.md`, sets status to `building`, and hands back to Builder.

**No skipping review**: You must run Overseer. A Phase is not done until Overseer declares it complete.

### 9. Iterate

Once Overseer marks the Phase complete, you're ready to plan the next one.

```
/agent scribe
```

Repeat the loop:
- **Plan** (Scribe)
- **Build** (Builder)
- **Review** (Overseer)
- Repeat

## Example: First Three Phases

Here's what a typical greenfield startup might look like:

### Bootstrap
- Run Lawgiver: Establish Python version, security rules, architectural constraints
- Run Artisan: Define directory structure, testing conventions, code style
- Run Surveyor: Optional at this stage (or run after Phase 0001)

### Phase 0001: Project Setup
- Initialize Python project with `pyproject.toml`
- Set up `black`, `ruff`, `pytest`
- Create `src/` and `tests/` directories
- Add health check endpoint
- Add basic logging

### Phase 0002: Database Layer
- Add SQLAlchemy models for core entities
- Create Alembic migrations
- Add connection pooling configuration
- Write integration tests

### Phase 0003: Authentication
- Implement JWT token generation and validation
- Add authentication middleware
- Create login/logout endpoints
- Add user fixtures for testing

Each Phase is scoped small enough to complete in one focused session. Each builds on the previous. Laws and style guide every decision.

## Tips for Greenfield Success

### Start Small
Don't try to define every law and style convention upfront. Capture the essentials during bootstrap and let Artisan add conventions as you discover them.

### Use Vizier Early
Before planning your first Phase, ask Vizier questions:

```
/agent vizier
```

> "What's a good first Phase for a new FastAPI project? What foundational pieces should I prioritize?"

Vizier can help you sequence work effectively.

### Keep Phases Focused
Resist the urge to plan large Phases. Scribe will push back, but you can help by framing work narrowly:
- "Add user authentication" → Too broad
- "Add JWT token generation and validation" → Better

### Trust the Loop
The Plan → Build → Review loop feels slow at first, but it compounds. Each Phase builds on a solid foundation. No hidden state. No drifting scope.

### Document as You Go
Builder updates docs when code changes affect documented systems. This keeps `.ushabti/docs/` current without extra effort. Trust the process.

### Use Cards to Defer Non-Essential Work
When you discover good ideas that aren't critical for the current Phase, create cards instead of expanding scope. This keeps Phases focused while ensuring ideas aren't lost.

## Common Pitfalls

### Skipping Review
Do not skip Overseer. Even if Builder says "all steps complete," you must run Overseer. It's the gatekeeper.

### Over-planning
Don't plan five Phases ahead. Plan one, build it, review it, then plan the next. Ushabti optimizes for iteration, not prediction.

### Treating Laws as Style
Laws are invariants. Style is conventions. If something might evolve, it's style. If it must never change, it's a law. Keep them separate.

### Ignoring Builder's New Steps
If Builder adds steps during implementation, read them. Builder discovered something. Understand what and why.

## Next Steps

- Review [Tips and Tricks](tips-and-tricks.md) for advanced patterns
- Understand [Brownfield onboarding](brownfield.md) if you later need to integrate existing code

---

Build deliberately. Iterate quickly. Keep Phases small. Let Ushabti handle the rest.
