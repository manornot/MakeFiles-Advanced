#!/bin/bash

# Extract the current origin URL
URL=$(git remote -v | grep '^origin' | grep '(fetch)' | awk '{print $2}')

# Prepare the line to insert
NEW_LINE="git remote add template $URL"

# Create a new temporary file with the new line
echo "$NEW_LINE" > temp_file.sh

# Append the original script to the new file
cat updateFromMaster.sh >> temp_file.sh

# Replace the original script with the new file
mv temp_file.sh updateFromMaster.sh

# Make the script executable
chmod +x updateFromMaster.sh
