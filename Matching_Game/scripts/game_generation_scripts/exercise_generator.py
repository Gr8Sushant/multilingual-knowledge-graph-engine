import random
import uuid

class ExerciseGenerator:
    def __init__(self, semantic_index, script_index, max_options=4, random_seed=42):
        self.semantic_index = semantic_index
        self.script_index = script_index
        self.max_options = max_options
        self.random = random.Random(random_seed)
        
    def generate_mode1_exercises(self, lang="np"):
        """Mode 1: Transliteration to Grapheme"""
        items = []
        for trans, correct_g in self.script_index.transliteration_to_grapheme.items():
            g_lang = self.script_index.grapheme_to_lang.get(correct_g)
            if g_lang and g_lang != lang:
                continue
                
            cat = self.script_index.grapheme_to_category.get(correct_g)
            lesson = self.script_index.grapheme_to_lesson.get(correct_g)
            
            # Score and rank distractors
            distractors_with_scores = self._get_mode1_distractors(correct_g, cat, lesson, lang)
            
            if not distractors_with_scores:
                continue
                
            # Take top distractors and randomly sample to max_options - 1
            num_dist = min(len(distractors_with_scores), self.max_options - 1)
            sampled = self.random.sample(distractors_with_scores[:max(num_dist, self.max_options*2)], num_dist)
            selected_distractors = [x[0] for x in sampled]
            max_score = max([x[1] for x in sampled]) if sampled else 0
            
            if max_score >= 50:
                difficulty = "hard"
            elif max_score >= 20:
                difficulty = "medium"
            else:
                difficulty = "easy"
            
            options = [correct_g] + selected_distractors
            self.random.shuffle(options)
            
            item = {
                "item_id": f"m1_{uuid.uuid4().hex[:8]}",
                "mode": 1,
                "language": lang,
                "prompt_type": "transliteration",
                "transliteration": trans,
                "audio_path": self.script_index.grapheme_to_audio.get(correct_g),
                "audio_placeholder": "placeholders/audio.mp3" if not self.script_index.grapheme_to_audio.get(correct_g) else None,
                "internal_ipa": self.script_index.grapheme_to_ipa.get(correct_g),
                "correct_grapheme": correct_g,
                "options": options,
                "distractor_graphemes": selected_distractors,
                "lesson_id": lesson,
                "difficulty": difficulty
            }
            items.append(item)
        return items
        
    def _get_mode1_distractors(self, correct_g, category, lesson, lang):
        all_g = list(self.script_index.grapheme_to_transliteration.keys())
        scored = []
        
        # Determine if correct_g is in a confusable set
        confusable_set = set()
        for s in self.script_index.confusable_sets:
            if correct_g in s:
                confusable_set = s
                break
                
        for g in all_g:
            if g == correct_g: continue
            
            g_lang = self.script_index.grapheme_to_lang.get(g)
            if g_lang and g_lang != lang:
                continue
            
            score = 0
            if g in confusable_set:
                score += 50  # High boost for visual/phonetic confusable sets
            if category and self.script_index.grapheme_to_category.get(g) == category:
                score += 20  # Base rule: same type (consonant vs consonant)
            if lesson and self.script_index.grapheme_to_lesson.get(g) == lesson:
                score += 10
                
            scored.append((score, g))
            
        # Sort descending by score, then randomize tie-breakers
        scored.sort(key=lambda x: (x[0], self.random.random()), reverse=True)
        return [(x[1], x[0]) for x in scored]

    def generate_mode2_exercises(self, lang="np"):
        """Mode 2: English to target language"""
        items = []
        for concept_id, eng_lemmas in self.semantic_index.concept_to_english.items():
            target_lemmas = self.semantic_index.concept_to_target.get(concept_id, {}).get(lang)
            if not eng_lemmas or not target_lemmas:
                continue
                
            eng_prompt = eng_lemmas[0]
            correct_target = target_lemmas[0]
            rom_lemmas = self.semantic_index.concept_to_roman.get(concept_id)
            transliteration = rom_lemmas[0] if rom_lemmas else None
            
            # Find distractors
            distractors_with_scores = self._get_mode2_distractors(concept_id, correct_target, lang)
            if not distractors_with_scores:
                continue
                
            num_dist = min(len(distractors_with_scores), self.max_options - 1)
            sampled = self.random.sample(distractors_with_scores[:max(num_dist, self.max_options*3)], num_dist)
            selected_distractors = [{"text": x[0], "transliteration": x[2]} for x in sampled]
            max_score = max([x[1] for x in sampled]) if sampled else 0
            
            if max_score >= 40:
                difficulty = "hard"
            elif max_score >= 20:
                difficulty = "medium"
            else:
                difficulty = "easy"
            
            correct_option = {"text": correct_target, "transliteration": transliteration}
            options = [correct_option] + selected_distractors
            self.random.shuffle(options)
            
            domains = self.semantic_index.concept_to_domain.get(concept_id, [])
            
            item = {
                "item_id": f"m2_{uuid.uuid4().hex[:8]}",
                "mode": 2,
                "language": lang,
                "concept_id": concept_id,
                "english_prompt": eng_prompt,
                "correct_nepali": correct_target, # Keeping key name for compatibility
                "correct_transliteration": transliteration,
                "options": options,
                "distractor_nepali": [x["text"] for x in selected_distractors],
                "domain": domains[0] if domains else None,
                "difficulty": difficulty,
                "semantic_source": "conceptsimilarity" if len(self.semantic_index.concept_similarities.get(concept_id, {})) > 0 else "domain"
            }
            items.append(item)
        return items
        
    def _get_mode2_distractors(self, correct_concept, correct_target, lang):
        scored_concepts = []
        
        # 1. Semantic Similarity
        similarities = self.semantic_index.concept_similarities.get(correct_concept, {})
        for cid, weight in similarities.items():
            scored_concepts.append((weight * 100, cid))
            
        # 2. Domain neighbors (if few similarities)
        domains = self.semantic_index.concept_to_domain.get(correct_concept, [])
        for d in domains:
            for cid in self.semantic_index.domain_to_concepts.get(d, []):
                if cid != correct_concept and cid not in similarities:
                    scored_concepts.append((10, cid)) # lower score than direct similarity
                    
        # Sort and map to target lemmas
        scored_concepts.sort(key=lambda x: (x[0], self.random.random()), reverse=True)
        
        distractors = []
        seen = {correct_target}
        for score, cid in scored_concepts:
            target_list = self.semantic_index.concept_to_target.get(cid, {}).get(lang)
            if target_list and target_list[0] not in seen:
                rom_list = self.semantic_index.concept_to_roman.get(cid)
                rom = rom_list[0] if rom_list else None
                distractors.append((target_list[0], score, rom))
                seen.add(target_list[0])
                
        # 3. Random fallback
        if len(distractors) < self.max_options - 1:
            all_concepts = list(self.semantic_index.concept_to_target.keys())
            self.random.shuffle(all_concepts)
            for cid in all_concepts:
                if cid != correct_concept:
                    target_list = self.semantic_index.concept_to_target.get(cid, {}).get(lang)
                    if target_list and target_list[0] not in seen:
                        rom_list = self.semantic_index.concept_to_roman.get(cid)
                        rom = rom_list[0] if rom_list else None
                        distractors.append((target_list[0], 0, rom))
                        seen.add(target_list[0])
                        if len(distractors) >= self.max_options - 1:
                            break
                            
        return distractors
