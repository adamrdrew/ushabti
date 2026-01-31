#!/bin/bash

# reconcile-skills.sh
# Updates skills/using-skills/SKILL.md with a catalog of all available skills

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$REPO_ROOT/skills"
USING_SKILLS_FILE="$SKILLS_DIR/using-skills/SKILL.md"

# Check that using-skills exists
if [ ! -f "$USING_SKILLS_FILE" ]; then
    echo "Error: $USING_SKILLS_FILE not found"
    exit 1
fi

# Create a temp file for the new content
TEMP_FILE=$(mktemp)

# Copy everything up to and including "# Available Skills" line
while IFS= read -r line; do
    echo "$line" >> "$TEMP_FILE"
    if [ "$line" = "# Available Skills" ]; then
        break
    fi
done < "$USING_SKILLS_FILE"

# Add a blank line after the header
echo "" >> "$TEMP_FILE"

# Track if we've added any skills (for separator logic)
first_skill=true

# Iterate through each skill directory
for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")

    # Skip using-skills itself
    if [ "$skill_name" = "using-skills" ]; then
        continue
    fi

    skill_file="$skill_dir/SKILL.md"

    # Skip if SKILL.md doesn't exist
    if [ ! -f "$skill_file" ]; then
        echo "Warning: No SKILL.md in $skill_dir, skipping"
        continue
    fi

    # Extract name and description from frontmatter
    # Read the file and parse YAML frontmatter between --- markers
    in_frontmatter=false
    name=""
    description=""

    while IFS= read -r line; do
        if [ "$line" = "---" ]; then
            if [ "$in_frontmatter" = true ]; then
                # End of frontmatter
                break
            else
                # Start of frontmatter
                in_frontmatter=true
                continue
            fi
        fi

        if [ "$in_frontmatter" = true ]; then
            # Extract name
            if [[ "$line" =~ ^name:\ *(.*) ]]; then
                name="${BASH_REMATCH[1]}"
            fi
            # Extract description
            if [[ "$line" =~ ^description:\ *(.*) ]]; then
                description="${BASH_REMATCH[1]}"
                # Remove surrounding quotes if present
                description="${description#\"}"
                description="${description%\"}"
                description="${description#\'}"
                description="${description%\'}"
            fi
        fi
    done < "$skill_file"

    # Only add if we found both name and description
    if [ -n "$name" ] && [ -n "$description" ]; then
        # Add separator before all but first skill
        if [ "$first_skill" = true ]; then
            first_skill=false
        else
            echo "" >> "$TEMP_FILE"
            echo "---" >> "$TEMP_FILE"
            echo "" >> "$TEMP_FILE"
        fi

        echo "name: $name" >> "$TEMP_FILE"
        echo "description: $description" >> "$TEMP_FILE"
    else
        echo "Warning: Could not extract name/description from $skill_file"
    fi
done

# Replace the original file with the new content
mv "$TEMP_FILE" "$USING_SKILLS_FILE"

echo "Successfully updated $USING_SKILLS_FILE"
