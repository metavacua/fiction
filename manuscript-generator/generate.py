"""
This script generates a draft manuscript and its creative provenance log
based on the data in the SudoWrite Story Bible.
"""

import yaml
import os
from datetime import datetime

STORY_BIBLE_PATH = "story-bible-datamodel/example.yaml"
MANUSCRIPT_DIR = "manuscript"
PROVENANCE_TEMPLATE = {
    "creative_action": {
        "id": "",
        "timestamp": "",
        "actor": "ai",
        "type": "AIGeneratedSuggestion",
        "based_on": "Story Bible Outline",
        "copyright_status": "not_copyrightable",
        "content": ""
    }
}

def load_story_bible(filepath):
    """Loads the Story Bible YAML file."""
    print(f"Loading Story Bible from: {filepath}")
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def generate_manuscript_files(story_bible):
    """Generates manuscript and provenance files from the Story Bible."""
    if not os.path.exists(MANUSCRIPT_DIR):
        print(f"Creating manuscript directory: {MANUSCRIPT_DIR}")
        os.makedirs(MANUSCRIPT_DIR)

    chapters = story_bible.get("outline", [])
    print(f"Found {len(chapters)} chapters to generate.")

    for chapter in chapters:
        chapter_num = chapter.get("chapter_number")
        title = chapter.get("title", f"Chapter {chapter_num}").replace(" ", "-").lower()
        filename = f"{chapter_num:02d}-{title}.md"
        filepath = os.path.join(MANUSCRIPT_DIR, filename)

        # Generate manuscript content
        content = f"# {chapter.get('title', '')}\n\n{chapter.get('summary', '')}\n"

        print(f"Generating manuscript file: {filepath}")
        with open(filepath, 'w') as f:
            f.write(content)

        # Generate provenance log
        provenance_filepath = filepath.replace(".md", ".provenance.yaml")
        provenance_data = PROVENANCE_TEMPLATE.copy()
        provenance_data["creative_action"]["id"] = f"uuid-generation-{chapter_num}"
        provenance_data["creative_action"]["timestamp"] = datetime.utcnow().isoformat() + "Z"
        provenance_data["creative_action"]["content"] = content

        print(f"Generating provenance file: {provenance_filepath}")
        with open(provenance_filepath, 'w') as f:
            yaml.dump([provenance_data], f, sort_keys=False, indent=2)

def main():
    """Main function to run the manuscript generation."""
    print("Starting manuscript generation process...")
    story_bible = load_story_bible(STORY_BIBLE_PATH)
    if story_bible:
        generate_manuscript_files(story_bible)
        print("Manuscript generation process completed successfully.")
    else:
        print("Could not load story bible. Aborting.")

if __name__ == "__main__":
    main()