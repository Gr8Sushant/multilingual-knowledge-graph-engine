import pandas as pd
import json
import random

class LanguageEngine:
    def __init__(self, csv_path, fsa_path, root_col="lemmas"):
        print(f"Loading Game Data from {csv_path}...")
        self.root_col = root_col
        self.df = pd.read_csv(csv_path)
        
        # Filter for Verbs (Part of speech 3)
        self.verbs_df = self.df[(self.df['part_of_speech'] == 3) & (self.df[root_col].notna())]
        
        with open(fsa_path, 'r', encoding='utf-8') as f:
            self.fsa = json.load(f)
            
        self.pronouns = list(self.fsa['pronouns'].keys())
        self.infinitive_marker = self.fsa.get("infinitive_marker", "")
        
        # Create a dictionary to map the cleaned root directly to its English translation!
        self.root_to_english = {}
        for _, row in self.verbs_df.iterrows():
            # 1. Extract and clean the root
            lemma_str = str(row[self.root_col]).split('|')[0].strip()
            if self.infinitive_marker and lemma_str.endswith(self.infinitive_marker):
                clean_root = lemma_str[:-len(self.infinitive_marker)]
            else:
                clean_root = lemma_str
            
            # 2. Extract the English translation (taking the first one if there are multiple)
            eng_lemma = str(row.get('english_lemmas', 'Unknown')).split('|')[0].strip()
            
            self.root_to_english[clean_root] = eng_lemma
            
        self.all_roots = list(self.root_to_english.keys())

    def conjugate(self, root, pronoun, tense="present"):
        pattern = self.fsa.get("pattern", "{tense_marker}{prefix}{root}{suffix}")
        
        tense_marker = self.fsa.get('tense_markers', {}).get(tense, "")
        prefix = self.fsa['pronouns'][pronoun].get('prefix', "")
        suffix = self.fsa['pronouns'][pronoun].get('suffix', "")
        
        # Build the word using the universal pattern!
        result = pattern.format(
            tense_marker=tense_marker, 
            prefix=prefix, 
            root=root, 
            suffix=suffix
        )
        
        # Handle Urdu spacing rule
        if " " in suffix:  
            parts = suffix.split(" ")
            return f"{result.replace(suffix, parts[0])} {parts[1]}"
            
        return result

    def generate_question(self, target_root, target_pronoun, difficulty="easy"):
        # FETCH THE ENGLISH TRANSLATIONS HERE!
        english_verb = self.root_to_english.get(target_root, "Unknown")
        # Grabs the "english" key from the JSON, or falls back to the pronoun itself
        english_pronoun = self.fsa['pronouns'][target_pronoun].get('english', target_pronoun)

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
        
        # Failsafe: if we don't have exactly 4 options, pad with random ones
        while len(options) < 4:
            random_root = random.choice(self.all_roots)
            options.append(self.conjugate(random_root, target_pronoun))
            options = list(set(options))
            
        random.shuffle(options)
        
        # Now we successfully return the English UI data!
        return {
            "english_translation": english_verb,
            "english_pronoun": english_pronoun,
            "root": target_root,
            "pronoun": target_pronoun,
            "correct_answer": correct_answer,
            "options": options,
            "difficulty": difficulty
        }