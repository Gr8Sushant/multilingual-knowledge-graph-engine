from flask import Flask, jsonify, request, render_template
from engine import LanguageEngine
import random

app = Flask(__name__)

# Load all three languages!
engines = {
    "darija": LanguageEngine("../data/darija_expanded_arabizi_ukc.csv", "fsa_darija.json", root_col="arabizi"),
    "urdu": LanguageEngine("../data/urdu_english_ukc_lexicon.csv", "fsa_urdu.json", root_col="lemmas"),
    "nepali": LanguageEngine("../data/nepali_english_ukc_lexicon.csv", "fsa_nepali.json", root_col="lemmas")
}

# The SRS Database now tracks languages separately: srs_db["urdu"]["root_word"]
srs_db = {"darija": {}, "urdu": {}, "nepali": {}}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/get_question', methods=['GET'])
def get_question():
    language = request.args.get('lang', 'darija')
    engine = engines[language]
    
    target_root = random.choice(engine.all_roots)
    target_pronoun = random.choice(engine.pronouns)
    
    if target_root not in srs_db[language]:
        srs_db[language][target_root] = {"level": "easy", "times_correct": 0}
        
    current_difficulty = srs_db[language][target_root]["level"]
    question_data = engine.generate_question(target_root, target_pronoun, current_difficulty)
    
    return jsonify(question_data)

@app.route('/api/update_srs', methods=['POST'])
def update_srs():
    data = request.json
    language = data.get('lang')
    root = data.get('root')
    was_correct = data.get('correct')
    
    if language in srs_db and root in srs_db[language]:
        if was_correct:
            srs_db[language][root]["times_correct"] += 1
            srs_db[language][root]["level"] = "hard"
        else:
            srs_db[language][root]["times_correct"] = 0
            srs_db[language][root]["level"] = "easy"
            
    print(f"SRS Update [{language}] -> Verb: {root} | New Level: {srs_db[language][root]['level']}")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)