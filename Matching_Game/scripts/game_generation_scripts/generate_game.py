import os
import json
import sys

# Ensure the script can find the modules when run from the script directory or project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from scripts.game_generation_scripts.graph_builder import GraphGameBuilder
from scripts.game_generation_scripts.indexes import ScriptIndex, SemanticIndex
from scripts.game_generation_scripts.exercise_generator import ExerciseGenerator

# Configuration
# Assuming we run this from the Matching_Game directory. If run from the script dir, adjust.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTIFACTS_DIR = os.path.join(BASE_DIR, 'artifacts')
UI_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ui')
INPUT_GRAPH_PATH = os.path.join(ARTIFACTS_DIR, 'graph_phase3_semantics.graphml')
MAX_OPTIONS = 4
RANDOM_SEED = 42

def main():
    print(f"Base Directory: {BASE_DIR}")
    print(f"Artifacts Directory: {ARTIFACTS_DIR}")
    
    # 1. Load Graph
    builder = GraphGameBuilder(ARTIFACTS_DIR, INPUT_GRAPH_PATH)
    G = builder.load_or_build()

    # 2. Build Indices
    print("Building Script Index...")
    script_index = ScriptIndex(G)
    print(f"Indexed {len(script_index.transliteration_to_grapheme)} transliteration mappings.")

    print("Building Semantic Index...")
    semantic_index = SemanticIndex(G)
    print(f"Indexed {len(semantic_index.concept_to_english)} concept to English mappings.")

    # 3. Detect Available Languages
    # We collect languages from mode 1 (script index) and mode 2 (semantic index)
    languages = set()
    for g_lang in script_index.grapheme_to_lang.values():
        if g_lang:
            languages.add(g_lang)
            
    for concept_targets in semantic_index.concept_to_target.values():
        for t_lang in concept_targets.keys():
            languages.add(t_lang)
            
    # Default languages if detection is empty for some reason
    if not languages:
        languages = {"np", "vn", "ur", "dr"}
        
    print(f"Detected Languages: {languages}")

    # 4. Generate Exercises
    generator = ExerciseGenerator(semantic_index, script_index, MAX_OPTIONS, RANDOM_SEED)

    print("Generating Mode 1 Exercises...")
    mode1_items = []
    for lang in languages:
        items = generator.generate_mode1_exercises(lang)
        mode1_items.extend(items)
    print(f"Generated {len(mode1_items)} Mode 1 items across {len(languages)} languages.")

    print("Generating Mode 2 Exercises...")
    mode2_items = []
    for lang in languages:
        items = generator.generate_mode2_exercises(lang)
        mode2_items.extend(items)
    print(f"Generated {len(mode2_items)} Mode 2 items across {len(languages)} languages.")

    all_items = mode1_items + mode2_items
    
    # 5. Export to JSON (for records) and JS (for UI)
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)
    os.makedirs(UI_DIR, exist_ok=True)
    
    # Export raw json
    json_path = os.path.join(ARTIFACTS_DIR, 'game_items_all.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)
    print(f"Exported raw JSON to {json_path}")
    
    # Export JS for the UI to consume without a web server
    js_path = os.path.join(UI_DIR, 'game_data.js')
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write("const gameData = ")
        json.dump(all_items, f, indent=2, ensure_ascii=False)
        f.write(";\n")
    print(f"Exported JS data to {js_path}")
    
    print("Game generation complete! You can now open ui/index.html to play.")

if __name__ == "__main__":
    main()
