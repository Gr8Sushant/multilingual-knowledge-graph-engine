import pandas as pd
import json
import random

class LanguageEngine:
    def __init__(self, csv_path, fsa_path, root_col="lemmas"):
        print(f"Loading Game Data from {csv_path}...")
        self.df = pd.read_csv(csv_path)
        
        # Filter for Verbs (Part of speech 3)
        self.verbs_df = self.df[(self.df['part_of_speech'] == 3) & (self.df[root_col].notna())]
        
        # Urdu and Nepali have roots like "دم لینا | سانس لینا". We just want the first one.
        self.all_roots = self.verbs_df[root_col].apply(lambda x: str(x).split('|')[0].strip()).tolist()
        
        with open(fsa_path, 'r', encoding='utf-8') as f:
            self.fsa = json.load(f)
            
        self.pronouns = list(self.fsa['pronouns'].keys())

    def conjugate(self, root, pronoun, tense="present"):
        tense_marker = self.fsa['tense_markers'].get(tense, "")
        prefix = self.fsa['pronouns'][pronoun]['prefix']
        suffix = self.fsa['pronouns'][pronoun]['suffix']
        
        # Build the word! Add spaces for Urdu auxiliary verbs.
        if " " in suffix:  # e.g., Urdu "تا ہوں"
            parts = suffix.split(" ")
            return f"{tense_marker}{prefix}{root}{parts[0]} {parts[1]}"
        
        return f"{tense_marker}{prefix}{root}{suffix}"

    def generate_question(self, target_root, target_pronoun, difficulty="easy"):
        correct_answer = self.conjugate(target_root, target_pronoun)
        distractors = set()
        
        if difficulty == "easy":
            while len(distractors) < 3:
                random_root = random.choice(self.all_roots)
                if random_root != target_root:
                    distractors.add(self.conjugate(random_root, target_pronoun))
        elif difficulty == "hard":
            while len(distractors) < 3:
                wrong_pronoun = random.choice(self.pronouns)
                if wrong_pronoun != target_pronoun:
                    distractors.add(self.conjugate(target_root, wrong_pronoun))

        options = list(distractors) + [correct_answer]
        random.shuffle(options)
        
        return {
            "root": target_root,
            "pronoun": target_pronoun,
            "correct_answer": correct_answer,
            "options": options,
            "difficulty": difficulty
        }