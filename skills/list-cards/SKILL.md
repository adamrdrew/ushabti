# List Cards

Scan and list all Hieroglyphs-compatible cards in `.ushabti/cards/`, with optional filtering by status or other criteria.

## When to Use

Use this skill when:
- You need to see all available work items
- Looking for cards in a specific state (e.g., only `todo` cards)
- Determining which cards to plan next
- Checking card priorities and types

## Card Location

Cards are stored in:
```
.ushabti/cards/{slug}/card.md
```

Each card is a directory containing a `card.md` file with YAML frontmatter and markdown body.

## Scanning Cards

To find all cards:

```bash
find .ushabti/cards -name "card.md" -type f
```

This returns paths like:
```
.ushabti/cards/improve-error-handling/card.md
.ushabti/cards/add-user-guide/card.md
```

## Parsing Frontmatter

Extract frontmatter fields using tools like `yq`, `awk`, or manual parsing.

Example with `awk` to extract specific fields:

```bash
# Extract title
awk '/^---$/{flag=!flag;next}flag && /^title:/{print $0}' card.md

# Extract status
awk '/^---$/{flag=!flag;next}flag && /^status:/{print $0}' card.md
```

Example with `sed` and `grep`:

```bash
# Get frontmatter section (between --- delimiters)
sed -n '/^---$/,/^---$/p' card.md | grep -v '^---$'
```

## Listing Format

Display cards in a clear, scannable format. Include at minimum:
- Slug (identifier)
- Title (human-readable)
- Status (lifecycle state)
- Priority (urgency level)

Example output:

```
Cards in .ushabti/cards/:

  improve-error-handling
    Title: Improve error handling
    Status: todo
    Priority: medium
    Type: feature

  fix-validation-bug
    Title: Fix validation bug
    Status: in-progress
    Priority: high
    Type: bug
```

## Status Filtering

Filter cards by status field to focus on specific work states.

Common filters:
- **Open work**: status is `todo`, `backlog`, or `in-progress`
- **Closed work**: status is `done`
- **Actionable work**: status is `todo` or `in-progress`

Example filtering for `todo` cards only:

```bash
for card in .ushabti/cards/*/card.md; do
  status=$(awk '/^---$/{flag=!flag;next}flag && /^status:/{print $2}' "$card")
  if [ "$status" = "todo" ]; then
    slug=$(basename $(dirname "$card"))
    title=$(awk '/^---$/{flag=!flag;next}flag && /^title:/{sub(/^title: /, ""); print}' "$card")
    echo "$slug: $title"
  fi
done
```

## Field Extraction Examples

Extract specific fields from a card:

```bash
card_path=".ushabti/cards/example-card/card.md"

# Extract all frontmatter as YAML
sed -n '1,/^---$/p' "$card_path" | sed '1d;$d'

# Extract title
sed -n '/^---$/,/^---$/p' "$card_path" | grep '^title:' | sed 's/^title: //'

# Extract status
sed -n '/^---$/,/^---$/p' "$card_path" | grep '^status:' | sed 's/^status: //'

# Extract priority
sed -n '/^---$/,/^---$/p' "$card_path" | grep '^priority:' | sed 's/^priority: //'

# Extract type
sed -n '/^---$/,/^---$/p' "$card_path" | grep '^type:' | sed 's/^type: //'

# Extract slug
sed -n '/^---$/,/^---$/p' "$card_path" | grep '^slug:' | sed 's/^slug: //'
```

## Filtering by Priority

List only high-priority cards:

```bash
for card in .ushabti/cards/*/card.md; do
  priority=$(sed -n '/^---$/,/^---$/p' "$card" | grep '^priority:' | sed 's/^priority: //')
  if [ "$priority" = "high" ]; then
    slug=$(basename $(dirname "$card"))
    title=$(sed -n '/^---$/,/^---$/p' "$card" | grep '^title:' | sed 's/^title: //')
    echo "$slug: $title (priority: high)"
  fi
done
```

## Filtering by Type

List only bugs:

```bash
for card in .ushabti/cards/*/card.md; do
  type=$(sed -n '/^---$/,/^---$/p' "$card" | grep '^type:' | sed 's/^type: //')
  if [ "$type" = "bug" ]; then
    slug=$(basename $(dirname "$card"))
    title=$(sed -n '/^---$/,/^---$/p' "$card" | grep '^title:' | sed 's/^title: //')
    echo "$slug: $title (type: bug)"
  fi
done
```

## Empty Results

If no cards exist, `.ushabti/cards/` may be empty or contain no `card.md` files. Handle gracefully:

```bash
cards=(.ushabti/cards/*/card.md)
if [ "${cards[0]}" = ".ushabti/cards/*/card.md" ]; then
  echo "No cards found in .ushabti/cards/"
fi
```

## Notes

- Cards with `status: done` are closed but not removed (unlike the old ticket archival system)
- The `find` command is more reliable than globbing for complex directory structures
- Always verify `.ushabti/cards/` directory exists before scanning
- Card slugs are unique identifiers—no two cards should have the same slug
