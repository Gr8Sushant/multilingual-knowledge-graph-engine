import pandas as pd
import random

class ExpressionEngine:
    def __init__(self, csv_path="expressions (2).csv"):
        # Load the refined 14-column CSV
        self.df = pd.read_csv(csv_path)
        
        # Clean column names
        self.df.columns = self.df.columns.str.strip().str.lower()
        
        # Fill NaNs with empty strings to prevent parsing errors
        self.df = self.df.fillna("")
        
        # SRS Tracker: { user_id: { usage_id: {"streak": int, "mode": "easy"|"hard"} } }
        self.srs = {}

    def get_question(self, language="darija", user_id="demo_user"):
        lang = language.lower()
        scenario_override_col = f"{lang}_scenario"

        # 1. SKIP LOGIC: Filter out rows where the requested language is blank
        if lang not in self.df.columns:
            return {"error": f"Language '{lang}' column not found in CSV."}
            
        valid_df = self.df[self.df[lang] != ""]
        
        if valid_df.empty:
            return {"error": f"No valid data available for {language}."}

        # 2. Pick a random target USAGE
        target_row = valid_df.sample(1).iloc[0]
        usage_id = target_row['usage_id']
        target_cat = target_row['category']
        target_trigger = target_row['trigger_event']
        correct_answer = target_row[lang].strip()

        # 3. SUBSUMPTION FALLBACK (The Dynamic Prompt Logic)
        lang_specific_scenario = target_row.get(scenario_override_col, "").strip()
        if lang_specific_scenario:
            # The language deviates from the global norm; use the specific nuance
            display_prompt = f"({lang.capitalize()} Nuance): {lang_specific_scenario}"
        else:
            # The language perfectly aligns with the global pragmatic norm
            display_prompt = target_row['scenarios'].strip()

        # 4. SRS Tracking (Tracked by USAGE, not by word, for polyfunctional mastery)
        if user_id not in self.srs:
            self.srs[user_id] = {}
        if usage_id not in self.srs[user_id]:
            self.srs[user_id][usage_id] = {"streak": 0, "mode": "easy"}
            
        current_mode = self.srs[user_id][usage_id]["mode"]

        # 5. Semantic Distractor Generation
        distractors = set()
        all_lang_expressions = valid_df[lang].unique().tolist()

        if current_mode == "easy":
            # EASY: Pick expressions from entirely different MACRO categories
            wrong_df = valid_df[valid_df['category'] != target_cat]
        else:
            # HARD: Same MACRO category, but different MICRO trigger_event or temporal position
            wrong_df = valid_df[(valid_df['category'] == target_cat) & 
                                (valid_df['trigger_event'] != target_trigger) & 
                                (valid_df[lang] != correct_answer)]

        # Extract the wrong labels
        if not wrong_df.empty:
            wrong_exprs = wrong_df[lang].unique().tolist()
            for exp in wrong_exprs:
                if exp.strip() != correct_answer:
                    distractors.add(exp.strip())

        # Failsafe Padding
        while len(distractors) < 3 and len(all_lang_expressions) > 1:
            rand_exp = random.choice(all_lang_expressions).strip()
            if rand_exp != correct_answer:
                distractors.add(rand_exp)

        options = list(distractors)[:3] + [correct_answer]
        random.shuffle(options)

        # Build Explanation using literal translation and temporal rules
        explanation_html = f"<b>Literal Meaning:</b> {target_row['literal_translation']}<br>"
        explanation_html += f"<b>Timing:</b> {target_row['temporal_position']}<br>"
        explanation_html += f"<b>Category:</b> {target_cat}"

        return {
            "situation_id": usage_id,
            "situation_english": display_prompt,
            "correct_answer": correct_answer,
            "options": options,
            "metadata": {
                "literal": target_row['literal_translation'],
                "timing": target_row['temporal_position'].replace("_", " ").lower(), # Cleans up text like POST_ACTION
                "category": target_cat.replace("_", " ").title() # Cleans up text like GREETING_REPLY
            },
            "mode": current_mode
        }

    def update_srs(self, user_id, scenario_id, is_correct):
        if user_id not in self.srs:
            self.srs[user_id] = {}
        if scenario_id not in self.srs[user_id]:
            self.srs[user_id][scenario_id] = {"streak": 0, "mode": "easy"}

        profile = self.srs[user_id][scenario_id]
        
        if is_correct:
            profile["streak"] += 1
            if profile["streak"] >= 3 and profile["mode"] == "easy":
                profile["mode"] = "hard"
                profile["streak"] = 0
                print(f"--> [PROMOTION] Usage {scenario_id} advanced to HARD Mode.")
        else:
            profile["streak"] = 0
            if profile["mode"] == "hard":
                profile["mode"] = "easy"
                print(f"--> [DEMOTION] Usage {scenario_id} dropped to EASY Mode.")

        self.srs[user_id][scenario_id] = profile
        return profile