import yaml
import os
import argparse

def load_yaml_files(directory):
    """Loads all YAML files from a given directory."""
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith((".yaml", ".yml")) and not filename.startswith("_"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as f:
                content = yaml.safe_load(f)
                if content and 'id' in content:
                    data[content['id']] = content
    return data

def generate_prompt(scene_id):
    """Generates a structured prompt for a specific scene."""
    characters = load_yaml_files("character-notes")
    locations = load_yaml_files("world-building")
    scenes_data = load_yaml_files("manuscript")

    if scene_id not in scenes_data:
        return f"Error: Scene '{scene_id}' not found."

    scene = scenes_data[scene_id]
    location = locations.get(scene['location_id'], {})

    prompts = []

    for protagonist in scene['characters_present']:
        protagonist_id = protagonist['character_id']
        protagonist_char = characters.get(protagonist_id, {'name': 'Unknown'})

        prompt = []
        prompt.append(f"--- PROMPT FOR: {protagonist_char['name']} ---")
        prompt.append(f"**Scene:** {scene['name']}")
        prompt.append(f"**Location:** {location.get('name', 'Unknown')} ({location.get('description', 'No description')})")
        prompt.append(f"**Point of View:** You are {protagonist_char['name']}.")
        prompt.append("\n**Events:**")

        for event in scene['events']:
            actor_id = event.get('actor_id')
            actor = characters.get(actor_id, {'name': 'Someone'})
            description = event.get('description', '').strip()

            # Resolve placeholders
            if '{target_name}' in description:
                target_id = event.get('target_id')
                target = characters.get(target_id)
                if target:
                    description = description.replace('{target_name}', target['name'])

            if '{possessive_pronoun}' in description:
                pronoun = actor.get('possessive_pronoun', 'their')
                description = description.replace('{possessive_pronoun}', pronoun)

            # Format event string
            if event['type'] == 'dialogue':
                prompt.append(f"- **Dialogue:** {actor['name']} says, \"{event['dialogue']}\"")
            else:
                prompt.append(f"- **Action:** {actor['name']} {description}.")

        prompts.append("\n".join(prompt))

    return "\n\n".join(prompts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate writing prompts for a specific scene.")
    parser.add_argument("scene_id", help="The ID of the scene to generate prompts for (e.g., '01-meeting').")
    args = parser.parse_args()

    # To find the scene file, we assume the scene_id corresponds to a file
    # This is a simplification. A real implementation might search all files.
    scene_prompts = generate_prompt(args.scene_id)
    print(scene_prompts)