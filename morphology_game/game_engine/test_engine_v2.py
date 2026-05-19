import pandas as pd
import json
import random

class LanguageEngine:
    def __init__(self, csv_path, fsa_path, root_col="lemmas"):
        print(f"Loading Game Data from {csv_path}...")
        self.df = pd.read_csv(csv_path)
        
        # Filter for Verbs (Part of speech 3)
        self.verbs_df = self.df[(self.df['part_of_speech'] == 3) & (self.df[root_col].notna())]
        
        # Helper function to extract the true morphological root
        def extract_nepali_root(lemma):
            lemma_str = str(lemma).split('|')[0].strip()
            # If the lemma ends in "नु" (nu), slice off the last two characters
            if lemma_str.endswith("नु"):
                return lemma_str[:-2] 
            return lemma_str
            
        self.all_roots = self.verbs_df[root_col].apply(extract_nepali_root).tolist()
        
        with open(fsa_path, 'r', encoding='utf-8') as f:
            self.fsa = json.load(f)
            
        self.pronouns = list(self.fsa['pronouns'].keys())

    def conjugate(self, root, pronoun, tense="present_continuous"):
        tense_interfix = self.fsa['tenses'].get(tense, "")
        
        prefix = self.fsa['pronouns'][pronoun].get('prefix', "")
        suffix = self.fsa['pronouns'][pronoun]['suffix']
        
        return f"{prefix}{root}{tense_interfix}{suffix}"

    def generate_question(self, target_lemma, target_pronoun, difficulty="easy"):
        target_root = target_lemma[:-2] if target_lemma.endswith("नु") else target_lemma
        
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