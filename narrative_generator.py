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

def conjugate_verb(verb):
    """Conjugates a verb for third-person singular present tense."""
    if verb.endswith('y') and verb[-2].lower() not in 'aeiou':
        return verb[:-1] + 'ies'
    if verb.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return verb + 'es'
    return verb + 's'

def format_sentence(text):
    """Capitalizes the first letter and adds a period."""
    if not text:
        return ""
    return text[0].upper() + text[1:] + "."

def generate_narrative(protagonist_id):
    """Generates a narrative from the protagonist's point of view."""
    characters = load_yaml_files("character-notes")
    locations = load_yaml_files("world-building")
    scenes_data = load_yaml_files("manuscript")

    scenes = sorted(scenes_data.values(), key=lambda s: s.get('order', float('inf')))

    if not characters or not scenes:
        return "Error: Could not load character or scene data."
    if protagonist_id not in characters:
        return f"Error: Protagonist '{protagonist_id}' not found."

    narrative = []
    for scene in scenes:
        if protagonist_id not in [p['character_id'] for p in scene['characters_present']]:
            continue

        location = locations.get(scene['location_id'], {})
        narrative.append(f"--- {scene['name']} ---")
        narrative.append(location.get('description', ''))

        for event in scene['events']:
            actor_id = event.get('actor_id')
            actor = characters.get(actor_id, {'name': 'Someone', 'possessive_pronoun': 'their'})
            description = event.get('description', '').strip()

            is_protagonist_action = (actor_id == protagonist_id)

            # Resolve placeholders
            if '{possessive_pronoun}' in description:
                pronoun = 'my' if is_protagonist_action else actor.get('possessive_pronoun', 'their')
                description = description.replace('{possessive_pronoun}', pronoun)

            if '{target_name}' in description:
                target_id = event.get('target_id')
                target = characters.get(target_id)
                if target:
                    target_name = target['name'] if is_protagonist_action else target['name'].capitalize()
                    description = description.replace('{target_name}', target_name)

            # Generate narrative line
            sentence = ""
            if event['type'] == 'dialogue':
                if is_protagonist_action:
                    sentence = f"I said, \"{event['dialogue']}\""
                else:
                    sentence = f"{actor['name'].capitalize()} said, \"{event['dialogue']}\""
            else: # Action or Observation
                parts = description.split(' ', 1)
                verb = parts[0]
                rest = parts[1] if len(parts) > 1 else ""

                if is_protagonist_action:
                    # First-person action: "I walk over to Elara"
                    sentence = f"I {verb} {rest}".strip()
                else:
                    # Third-person event, always viewed from protagonist's POV
                    # "I saw Kiera walk over to Elara"
                    # "I saw Kiera smirk"
                    # The verb in the description remains in its base form.
                    sentence = f"I saw {actor['name'].capitalize()} {verb} {rest}".strip()

            narrative.append(format_sentence(sentence))

    return "\n\n".join(narrative)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a story from a character's perspective.")
    parser.add_argument("protagonist", help="The ID of the protagonist character (e.g., 'kiera').")
    args = parser.parse_args()

    story = generate_narrative(args.protagonist)
    print(story)