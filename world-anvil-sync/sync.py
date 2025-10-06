"""
This script will handle the synchronization of data between World Anvil
and the local SudoWrite Story Bible data model.

It will perform the following functions:
1.  Fetch the latest worldbuilding data from the World Anvil API.
2.  Parse the local story bible YAML file.
3.  Update the story bible data with the information from World Anvil.
4.  Write the updated data back to the story bible YAML file.
"""

import yaml


def get_world_anvil_data():
    """
    Fetches the latest worldbuilding data from the World Anvil API.

    This function will require an API key, which should be stored securely
    as a GitHub secret and accessed via environment variables.
    """
    print("Fetching data from World Anvil API...")
    # api_key = os.getenv("WORLD_ANVIL_API_KEY")
    # headers = {"Authorization": f"Bearer {api_key}"}
    # response = requests.get("https://www.worldanvil.com/api/v1/...", headers=headers)
    # response.raise_for_status()
    # return response.json()
    # Placeholder data for now:
    return {
        "characters": [
            {"name": "Kaelen Voss", "description": "Updated description from World Anvil."}
        ]
    }


def load_story_bible(filepath="../story-bible-datamodel/example.yaml"):
    """
    Loads the SudoWrite Story Bible data from the local YAML file.
    """
    print(f"Loading story bible from {filepath}...")
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def update_story_bible_data(story_bible, world_anvil_data):
    """
    Updates the story bible data with the new data from World Anvil.

    This is a simple merge for now. A more sophisticated implementation
    would involve more complex logic to handle conflicts and data mapping.
    """
    print("Updating story bible data...")
    # This is a naive update. A real implementation would be more robust.
    for wa_char in world_anvil_data.get("characters", []):
        for sb_char in story_bible.get("characters", []):
            if wa_char["name"] == sb_char["name"]:
                sb_char["description"] = wa_char["description"]
                print(f"Updated character: {wa_char['name']}")
    return story_bible


def save_story_bible(story_bible, filepath="../story-bible-datamodel/example.yaml"):
    """
    Saves the updated Story Bible data back to the YAML file.
    """
    print(f"Saving updated story bible to {filepath}...")
    with open(filepath, 'w') as f:
        yaml.dump(story_bible, f, sort_keys=False, indent=2)


def main():
    """
    Main function to run the synchronization process.
    """
    print("Starting World Anvil sync process...")
    world_anvil_data = get_world_anvil_data()
    story_bible_data = load_story_bible()
    updated_data = update_story_bible_data(story_bible_data, world_anvil_data)
    save_story_bible(updated_data)
    print("Sync process completed successfully.")


if __name__ == "__main__":
    main()
