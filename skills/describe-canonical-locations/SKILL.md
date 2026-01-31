---
name: describe-canonical-locations
description: File locations for laws, style, phases, and docs. Load when locating or creating Ushabti state files.
user-invocable: false
---

## Canonical Location

All Ushabti state lives under `.ushabti/`. This is the single source of truth.

```
.ushabti/
├── laws.md           # Project invariants (absolute constraints)
├── style.md          # Conventions (how we build)
└── phases/           # Phase directories
    └── NNNN-slug/    # Zero-padded sequential
└── docs/             # Docs directory
    └── *.md          # Docuemntation on project systems
    └── index.md      # Index of all project documentation
```

No mirrors. No duplicates. No top-level copies.