from collections import defaultdict
from .graph_builder import rel_is, norm_type, norm_value

NEPALI_LOOKALIKES = [
    {"क", "फ"},  # ka, pha
    {"ख", "रव"}, # kha, ra+va
    {"ग", "श"},  # ga, sha
    {"घ", "ध"},  # gha, dha
    {"च", "ज"},  # cha, ja
    {"ट", "ठ", "ड", "ढ"}, # retroflex
    {"त", "न"},  # ta, na
    {"प", "ष", "य"}, # pa, sha (retroflex), ya
    {"ब", "व"},  # ba, wa
    {"भ", "म"},  # bha, ma
    {"र", "स"},  # ra, sa
]

def get_edges(G, u, v, reverse=False):
    if reverse:
        edge_data = G.get_edge_data(v, u)
    else:
        edge_data = G.get_edge_data(u, v)
        
    if not edge_data:
        return []
        
    if G.is_multigraph():
        return list(edge_data.values())
    else:
        return [edge_data]

class ScriptIndex:
    def __init__(self, G):
        self.G = G
        self.transliteration_to_grapheme = {}
        self.grapheme_to_transliteration = {}
        self.grapheme_to_category = {}
        self.grapheme_to_lesson = {}
        self.category_to_graphemes = defaultdict(list)
        self.lesson_to_graphemes = defaultdict(list)
        self.grapheme_to_audio = {}
        self.grapheme_to_ipa = {}
        self.grapheme_to_lang = {}
        self.confusable_sets = NEPALI_LOOKALIKES
        self._build_indexes()

    def _build_indexes(self):
        for node, data in self.G.nodes(data=True):
            t = norm_type(data.get("type") or data.get("labelV"))
            if t == "grapheme":
                g = data.get("grapheme") or data.get("label") or node
                if g.startswith("g_"):
                    g = data.get("grapheme") # Fallback to attr
                    
                lang = data.get("language")
                if lang:
                    self.grapheme_to_lang[g] = lang
                
                # Find associated transliteration, phoneme, audio
                for neighbor in self.G.predecessors(node):
                    edges = get_edges(self.G, neighbor, node)
                    for edge_data in edges:
                        if rel_is(edge_data, "phoneme_written_as"):
                            p_data = self.G.nodes[neighbor]
                            ipa = p_data.get("ipa")
                            if ipa:
                                self.grapheme_to_ipa[g] = ipa
                                # Fallback: use IPA as transliteration for languages like VN that lack explicit translit nodes
                                if lang == "vn":
                                    self.transliteration_to_grapheme[ipa] = g
                                    self.grapheme_to_transliteration[g] = ipa
                            
                            # Find transliteration from phoneme
                            for p_neighbor in self.G.successors(neighbor):
                                p_edges = get_edges(self.G, neighbor, p_neighbor)
                                for p_edge_data in p_edges:
                                    if rel_is(p_edge_data, "phoneme_transliterated_as"):
                                        t_data = self.G.nodes[p_neighbor]
                                        trans = t_data.get("transliteration") or t_data.get("label") or p_neighbor
                                        if trans.startswith("t_"):
                                            trans = t_data.get("transliteration")
                                            
                                        # Fallback to IPA if transliteration is '-'
                                        if trans == "-":
                                            trans = self.grapheme_to_ipa.get(g)
                                            
                                        if trans:
                                            self.transliteration_to_grapheme[trans] = g
                                            self.grapheme_to_transliteration[g] = trans
                                            
                        if rel_is(edge_data, "audio_represents"):
                            a_data = self.G.nodes[neighbor]
                            self.grapheme_to_audio[g] = a_data.get("path") or a_data.get("placeholder")
                                    
                for neighbor in self.G.successors(node):
                    edges = get_edges(self.G, node, neighbor)
                    for edge_data in edges:
                        if rel_is(edge_data, "grapheme_to_category"):
                            cat = self.G.nodes[neighbor].get("id") or neighbor
                            self.grapheme_to_category[g] = cat
                            self.category_to_graphemes[cat].append(g)
                        elif rel_is(edge_data, "grapheme_to_lesson"):
                            lesson = self.G.nodes[neighbor].get("id") or neighbor
                            self.grapheme_to_lesson[g] = lesson
                            self.lesson_to_graphemes[lesson].append(g)

class SemanticIndex:
    def __init__(self, G):
        self.G = G
        self.concept_to_english = defaultdict(list)
        self.concept_to_target = defaultdict(lambda: defaultdict(list))
        self.concept_to_roman = defaultdict(list)
        self.concept_to_domain = defaultdict(list)
        self.domain_to_concepts = defaultdict(list)
        self.concept_similarities = defaultdict(dict)
        self._build_indexes()

    def _build_indexes(self):
        for node, data in self.G.nodes(data=True):
            t = norm_type(data.get("type") or data.get("labelV"))
            if t == "concept":
                concept_id = data.get("id") or node
                
                # Outgoing edges for domains, synsets, similarity
                for neighbor in self.G.successors(node):
                    edges = get_edges(self.G, node, neighbor)
                    for ed in edges:
                        if rel_is(ed, "belongs_to_domain"):
                            domain_id = self.G.nodes[neighbor].get("id") or neighbor
                            self.concept_to_domain[concept_id].append(domain_id)
                            self.domain_to_concepts[domain_id].append(concept_id)
                        elif rel_is(ed, "concept_similarity"):
                            target_concept = self.G.nodes[neighbor].get("id") or neighbor
                            weight = ed.get("weight", 0.5)
                            if isinstance(weight, str):
                                try: weight = float(weight)
                                except: weight = 0.5
                            self.concept_similarities[concept_id][target_concept] = weight
                            self.concept_similarities[target_concept][concept_id] = weight # Make symmetric
                    
                    # check bidirectional similarity just in case
                    edges_rev = get_edges(self.G, node, neighbor, reverse=True)
                    for ed in edges_rev:
                        if rel_is(ed, "concept_similarity"):
                            target_concept = self.G.nodes[neighbor].get("id") or neighbor
                            weight = ed.get("weight", 0.5)
                            if isinstance(weight, str):
                                try: weight = float(weight)
                                except: weight = 0.5
                            self.concept_similarities[concept_id][target_concept] = weight
                            self.concept_similarities[target_concept][concept_id] = weight

                # Incoming edges for lemmas
                for neighbor in self.G.predecessors(node):
                    edges = get_edges(self.G, neighbor, node)
                    for ed in edges:
                        if rel_is(ed, "english_label_for"):
                            lemma = self.G.nodes[neighbor].get("lemma") or self.G.nodes[neighbor].get("label") or neighbor
                            if lemma.startswith("eng_"): lemma = self.G.nodes[neighbor].get("lemma")
                            self.concept_to_english[concept_id].append(lemma)
                        elif rel_is(ed, "target_label_for"):
                            n_data = self.G.nodes[neighbor]
                            lemma = n_data.get("lemma") or n_data.get("label") or neighbor
                            if lemma.startswith("nep_"): lemma = n_data.get("lemma")
                            lang = n_data.get("language", "np")
                            self.concept_to_target[concept_id][lang].append(lemma)
                            
                            # Find romanised lemma from the target lemma
                            for rom_neighbor in self.G.successors(neighbor):
                                rom_edges = get_edges(self.G, neighbor, rom_neighbor)
                                for rom_ed in rom_edges:
                                    if rel_is(rom_ed, "romanised_as"):
                                        rom_lemma = self.G.nodes[rom_neighbor].get("lemma") or self.G.nodes[rom_neighbor].get("label") or rom_neighbor
                                        if rom_lemma.startswith("rom_"): rom_lemma = self.G.nodes[rom_neighbor].get("lemma")
                                        self.concept_to_roman[concept_id].append(rom_lemma)
