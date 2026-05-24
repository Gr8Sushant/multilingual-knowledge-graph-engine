from flask import Flask, jsonify, request, render_template
from engine import LanguageEngine
import random

app = Flask(__name__)

# Load all three languages
engines = {
    "darija": LanguageEngine("../data/darija_expanded_arabizi_ukc.csv", "fsa_darija.json", root_col="arabizi"),
    "urdu": LanguageEngine("../data/urdu_english_ukc_lexicon.csv", "fsa_urdu.json", root_col="lemmas"),
    "nepali": LanguageEngine("../data/nepali_english_ukc_lexicon.csv", "fsa_nepali.json", root_col="lemmas")
}

# Track mastery by PRONOUN concepts across languages
srs_db = {"darija": {}, "urdu": {}, "nepali": {}}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/get_question', methods=['GET'])
def get_question():
    language = request.args.get('lang', 'darija')
    requested_diff = request.args.get('difficulty', 'auto') 
    engine = engines[language]
    
    # 1. Grammar-First Selection Logic: Focus on mastering pronouns
    seen_pronouns = list(srs_db[language].keys())
    if len(seen_pronouns) > 0 and random.random() < 0.3:
        target_pronoun = random.choice(seen_pronouns)
    else:
        target_pronoun = random.choice(engine.pronouns)
        
    # Verbs are selected at random from the UKC lexicon to test the pattern dynamically
    target_root = random.choice(engine.all_roots)
    
    # Initialize pronoun tracking if it's the user's first time seeing it
    if target_pronoun not in srs_db[language]:
        srs_db[language][target_pronoun] = {"level": "easy", "times_correct": 0}
        
    # Determine difficulty level
    if requested_diff == 'auto':
        current_difficulty = srs_db[language][target_pronoun]["level"]
    else:
        current_difficulty = requested_diff
        
    question_data = engine.generate_question(target_root, target_pronoun, current_difficulty)
    return jsonify(question_data)

@app.route('/api/update_srs', methods=['POST'])
def update_srs():
    data = request.json
    language = data.get('lang')
    pronoun = data.get('pronoun')  # Grading tracks the grammar token!
    was_correct = data.get('correct')
    
    if language in srs_db and pronoun in srs_db[language]:
        if was_correct:
            srs_db[language][pronoun]["times_correct"] += 1
            srs_db[language][pronoun]["level"] = "hard"
        else:
            srs_db[language][pronoun]["times_correct"] = 0
            srs_db[language][pronoun]["level"] = "easy"
            
    return jsonify({"status": "success", "srs_data": srs_db[language]})

if __name__ == "__main__":
    app.run(debug=True, port=5000)