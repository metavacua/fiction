#!/bin/bash

# A script to compile a multi-chapter manuscript from Markdown files into a single .docx file using Pandoc.

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
MANUSCRIPT_DIR="manuscript"
OUTPUT_DIR="dist"
OUTPUT_FILENAME="manuscript.docx" # The name of the final compiled file

# --- Script ---

echo "Starting manuscript build process..."

# Check if Pandoc is installed
if ! command -v pandoc &> /dev/null
then
    echo "Error: pandoc is not installed. Please install it to use this script."
    exit 1
fi

# Find all markdown files in the manuscript directory, sorted numerically/alphabetically.
# Using `ls` here is safe because we control the filenames and don't expect special characters.
# The shell will expand the wildcard `*` in alphabetical order.
CHAPTERS=("$MANUSCRIPT_DIR"/*.md)

# Check if any manuscript files were found
if [ ! -e "${CHAPTERS[0]}" ]; then
    echo "Error: No manuscript files (.md) found in the '${MANUSCRIPT_DIR}' directory."
    echo "Please make sure your chapters are in the format '01-chapter-one.md', '02-chapter-two.md', etc."
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

OUTPUT_FILE="${OUTPUT_DIR}/${OUTPUT_FILENAME}"

# Inform the user about the files being compiled
echo "Found ${#CHAPTERS[@]} chapter(s). They will be compiled in the following order:"
for chapter in "${CHAPTERS[@]}"; do
    echo "  - $(basename "$chapter")"
done

# Convert the files. Pandoc can take multiple input files and will concatenate them in order.
echo "Compiling manuscript into ${OUTPUT_FILE}..."
pandoc "${CHAPTERS[@]}" -o "$OUTPUT_FILE"

echo "Build complete! Your compiled manuscript is ready at ${OUTPUT_FILE}"