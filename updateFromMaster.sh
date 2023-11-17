

# Fetch updates from the template repository
git fetch template

# Merge updates into the current branch
git merge template/main --allow-unrelated-histories -m "Merge updates from template"
