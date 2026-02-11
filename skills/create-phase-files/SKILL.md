---
name: create-phase-files
description: Create a phase directory with all required files in one call. Use instead of separate mkdir + Write calls when creating a new phase.
user-invocable: false
---

## Create Phase Files

Creates the phase directory and writes all phase files (phase.md, steps.md, progress.yaml, review.md) from a single stdin input with section delimiters.

### Usage

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/create-phase-files/create-phase-files.py <phase-dir> <<'PHASE_CONTENT'
===PHASE===
<phase.md content>
===STEPS===
<steps.md content>
===PROGRESS===
<progress.yaml content>
===REVIEW===
<review.md scaffold>
PHASE_CONTENT
```

### Arguments

- `phase-dir`: Path for the new phase directory (e.g., `.ushabti/phases/0005-my-phase`)
- stdin: File contents separated by `===PHASE===`, `===STEPS===`, `===PROGRESS===`, `===REVIEW===` delimiters

### Required sections

- `===PHASE===` -> phase.md
- `===STEPS===` -> steps.md
- `===PROGRESS===` -> progress.yaml

### Optional sections

- `===REVIEW===` -> review.md (scaffold for Overseer)

### Example

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/create-phase-files/create-phase-files.py .ushabti/phases/0010-add-auth <<'PHASE_CONTENT'
===PHASE===
# Phase 0010: Add Auth
card: add-auth

## Intent
Add authentication to the API.

## Scope
**In scope**: JWT token validation, middleware
**Out of scope**: OAuth providers

## Constraints
- L09: Sandi Metz principles

## Acceptance criteria
- All protected endpoints require valid JWT
- Invalid tokens return 401

## Risks / notes
None identified.

===STEPS===
# Steps

## S001: Create auth middleware

**Intent:** Validate JWT tokens on protected routes.

**Work:**
- Create middleware function
- Verify token signature and expiry
- Attach user context to request

**Done when:** Middleware rejects invalid tokens with 401.

===PROGRESS===
phase:
  id: 0010
  slug: add-auth
  title: Add Auth
  status: planned

steps:
  - id: S001
    title: Create auth middleware
    implemented: false
    reviewed: false
    notes: ""
    touched: []

===REVIEW===
# Review: Phase 0010 — Add Auth

*Awaiting review.*
PHASE_CONTENT
```

This replaces mkdir + 3-4 separate Write calls with a single Bash invocation.
