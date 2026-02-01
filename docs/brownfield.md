# Brownfield Projects with Ushabti

This guide walks through onboarding Ushabti onto an existing codebase.

## Overview

When introducing Ushabti to an existing project, you start differently than with greenfield work. The key insight: **documentation comes first**. Before you can effectively plan Phases or establish laws and style, agents need to understand what already exists.

This is where Surveyor shines.

## Why Surveyor First?

Existing codebases have structure, patterns, constraints, and conventions already in place. Trying to define laws and style without understanding the current state leads to:
- Laws that conflict with existing architecture
- Style guides that ignore established conventions
- Plans that don't account for existing systems

Surveyor explores your codebase systematically and creates documentation that captures:
- What exists
- How it's structured
- What patterns are already in use
- Where complexity lives

This documentation becomes the foundation for all subsequent work.

## Step-by-Step Workflow

### 1. Install Ushabti

Install the plugin and configure permissions in your existing repository:

```
/plugin marketplace add adamrdrew/marketplace
/plugin install ushabti@adamrdrew
```

Add permissions to `.claude/settings.json` or `.claude/settings.local.json`:

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

### 2. Run Surveyor

Start by running Surveyor to explore and document your codebase.

```
/agent surveyor
```

**What Surveyor does:**

1. **Setup**: Creates `.ushabti/` and `.ushabti/docs/` directories
2. **Discovery**: Explores the repository structure, identifies major systems and components
3. **Writing**: Creates documentation files describing architecture, components, configuration, and more
4. **Handoff**: Verifies completeness and recommends next steps

**What you provide**: Surveyor may ask clarifying questions about the project's purpose, key systems, or areas of focus. Answer these to help Surveyor create more useful documentation.

**Output**: `.ushabti/docs/` populated with:
- `index.md`: Table of contents
- `architecture.md`: High-level system overview
- Component documentation (API routes, database models, services, etc.)
- Configuration documentation
- Any other domain-specific docs Surveyor deems useful

**Time commitment**: Surveyor's exploration can take a while for large codebases. Let it run. The documentation it creates will save significant time in every subsequent Phase.

### 3. Run Lawgiver

Once you have documentation, establish your project's laws — the invariants that must hold.

```
/agent lawgiver
```

**What to tell Lawgiver:**

Review your existing codebase and identify absolute constraints:
- Architectural rules already in place (e.g., "API layer never imports from database models directly")
- Security requirements (e.g., "all authentication goes through the auth service")
- Performance guarantees (e.g., "database queries must use connection pooling")
- Technology constraints (e.g., "Python 3.9+", "PostgreSQL only")
- Patterns that must not be violated (e.g., "no raw SQL strings, use query builder")

**Important**: Laws should reflect reality. If your existing code uses global state, don't make "no global state" a law unless you plan to refactor it. Laws that conflict with existing code create unresolvable Phases.

**Example prompt:**

> "This is an existing Django REST API. Capture these laws:
> - Python 3.9 minimum (existing deployment constraint)
> - All database access must go through Django ORM (existing pattern)
> - API keys stored in environment variables only (security requirement)
> - All endpoints require authentication except /health (existing behavior)
> - No synchronous database calls in async views (performance rule)"

**Output**: `.ushabti/laws.md`

### 4. Run Artisan

Define your project's style conventions — how you build things.

```
/agent artisan
```

**What to tell Artisan:**

Identify the conventions your codebase already follows (or should follow going forward):
- Directory structure patterns
- Naming conventions for files, classes, functions
- Testing patterns (where tests live, how they're organized)
- Error handling conventions
- Logging patterns
- Code formatting tools (if any)

**Example prompt:**

> "Define style for the Django project. Existing conventions:
> - Apps live in `apps/` directory
> - One test file per view file: `test_views.py` mirrors `views.py`
> - Use `snake_case` for all Python identifiers
> - All API errors use `APIException` subclasses with structured messages
> - Tests use pytest, not Django's built-in test framework
> - Existing code uses `black` and `flake8` (continue this)
> - Migrations must have descriptive names, not auto-generated ones"

**Output**: `.ushabti/style.md`

### 5. Begin the Phase Loop

With docs, laws, and style in place, you're ready to start planning Phases.

```
/agent scribe
```

**What's different from greenfield:**
- Scribe consults the documentation Surveyor created to understand existing systems
- Laws reflect reality, not aspirations
- Style captures existing patterns, ensuring new code fits the codebase
- Phases often involve modifying existing code, not just adding new features

**Example first Phase:**

> "Plan a Phase to add request ID tracing to all API endpoints. This should integrate with the existing logging setup documented in `.ushabti/docs/configuration.md`."

Scribe will:
- Read the docs to understand current logging configuration
- Check laws for constraints
- Check style for logging conventions
- Plan steps that work with the existing codebase

### 6. Build and Review

The Plan → Build → Review loop works identically to greenfield:

```
/agent builder   # Implements the Phase
/agent overseer  # Reviews and approves
```

**Key difference**: Builder will:
- Consult `.ushabti/docs/` to understand existing systems before modifying them
- Update docs when changes affect documented systems
- Follow existing patterns (captured in style) when adding new code

Overseer will:
- Verify docs are updated to reflect code changes
- Ensure new code integrates cleanly with existing systems
- Check that laws and style are maintained

## How Docs Integrate with the Loop

The documentation Surveyor creates is not static. It's a living resource that stays current:

```
Surveyor creates initial docs
        ↓
┌─────────────────────────────────────────┐
│  Plan → Build → Review                  │
│    ↑       ↑       ↓                    │
│ consult  update  verify                 │
│  docs    docs    docs                   │
└─────────────────────────────────────────┘
```

- **Scribe** reads docs to understand what exists before planning
- **Builder** updates docs when code changes affect documented systems
- **Overseer** verifies docs are reconciled before declaring a Phase complete

A Phase cannot be marked complete if documentation is out of sync with the code.

## Common Concerns

### "Will this disrupt my existing workflow?"

No. Ushabti operates entirely within `.ushabti/` and does not modify your existing files unless you plan a Phase to do so. You control the pace of adoption.

### "Do I have to refactor everything to match laws and style?"

No. Laws and style should reflect your current reality (with room for incremental improvement). If your existing code uses patterns you want to keep, encode those as style. If you want to evolve away from them, plan Phases to do so gradually.

### "What if my codebase is huge?"

Surveyor is designed for large codebases. It explores systematically and creates high-level documentation. You don't need to document every function — just the systems and patterns agents need to understand.

### "Can I adopt Ushabti incrementally?"

Yes. Start with one area of your codebase. Run Surveyor, establish laws and style, and plan Phases for just that subsystem. As you gain confidence, expand scope.

### "What if the docs get stale?"

The Phase loop prevents this. Overseer will not approve a Phase if docs are out of sync with code changes. This makes documentation maintenance a built-in part of development, not an afterthought.

## Example: Onboarding an Existing Django API

### Step 1: Survey
```
/agent surveyor
```
Surveyor explores the Django project and documents:
- App structure and purposes
- Model schemas and relationships
- API endpoints and authentication
- Configuration and settings
- Deployment setup

### Step 2: Laws
```
/agent lawgiver
```
Capture invariants:
- Python 3.9+
- Django ORM only (no raw SQL)
- API keys in environment variables
- Authentication required except `/health`

### Step 3: Style
```
/agent artisan
```
Define conventions:
- Apps in `apps/` directory
- pytest for testing
- `black` and `flake8` for formatting
- Structured API error responses

### Step 4: First Phase
```
/agent scribe
```
"Plan a Phase to add structured logging with request IDs to all API views."

Scribe consults the docs, sees how views are currently structured, and plans steps that integrate with existing code.

### Step 5: Build and Review
```
/agent builder
/agent overseer
```
Builder implements, updating docs as needed. Overseer verifies and approves.

### Result
You now have structured logging integrated cleanly with your existing codebase. Docs are current. Laws and style are established. You're ready to plan the next Phase.

## Tips for Brownfield Success

### Trust Surveyor's Process
Surveyor's exploration phase can feel slow. Let it run. The documentation saves time in every subsequent Phase.

### Be Honest About Laws
Don't create aspirational laws that conflict with existing code. If you want to change something, make it a style convention and plan Phases to evolve toward it.

### Start with High-Impact Areas
Don't try to onboard your entire codebase at once. Pick a subsystem, run the bootstrap, and iterate. Expand scope as you build confidence.

### Use Vizier Before Planning
Ask Vizier to review the docs Surveyor created and suggest high-impact work:

```
/agent vizier
```

> "Review the documentation and suggest the most valuable first Phase for this project."

Vizier can identify technical debt, integration points, or missing capabilities that make good starting targets.

### Keep Early Phases Small
Your first few Phases should be tiny. Get comfortable with the loop before tackling complex work.

## Next Steps

- Review [Tips and Tricks](tips-and-tricks.md) for advanced patterns
- See [Getting Started](getting-started.md) for agent reference

---

Ushabti meets you where you are. Document first. Evolve deliberately.
