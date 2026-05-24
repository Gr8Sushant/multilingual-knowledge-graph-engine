import os
import networkx as nx
import pandas as pd

REL_ALIASES = {
    "english_label_for": {"english_label_for", "englishlabelfor"},
    "target_label_for": {"target_label_for", "targetlabelfor"},
    "romanised_as": {"romanised_as", "romanisedas"},
    "mapped_to_synset": {"mapped_to_synset", "mappedtosynset"},
    "belongs_to_domain": {"belongs_to_domain", "belongstodomain"},
    "concept_similarity": {"concept_similarity", "conceptsimilarity"},
    "phoneme_written_as": {"phoneme_written_as", "phonemewrittenas"},
    "phoneme_transliterated_as": {"phoneme_transliterated_as", "phonemetransliteratedas"},
    "audio_represents": {"audio_represents", "audiorepresents"},
    "lesson_contains_item": {"lesson_contains_item", "lessoncontainsitem"},
    "grapheme_to_category": {"grapheme_to_category", "graphemetocategory"},
    "grapheme_to_lesson": {"grapheme_to_lesson", "graphemetolesson"},
}

def norm_relation(r):
    if not isinstance(r, str):
        return str(r)
    return r.lower().replace("_", "").replace("-", "")

def rel_is(edge_data, canonical_name):
    r = norm_relation(edge_data.get("relation") or edge_data.get("label"))
    return r in REL_ALIASES.get(canonical_name, {canonical_name, norm_relation(canonical_name)})

def norm_value(v):
    if pd.isna(v):
        return None
    return str(v).strip()

def norm_type(t):
    if not isinstance(t, str):
        return str(t)
    return t.lower()

class GraphGameBuilder:
    def __init__(self, artifacts_dir, input_graph_path=None):
        self.artifacts_dir = artifacts_dir
        self.input_graph_path = input_graph_path or os.path.join(artifacts_dir, 'graph_phase3_semantics.graphml')
        self.graph = None

    def load_or_build(self):
        if os.path.exists(self.input_graph_path):
            print(f"Loading existing graph from {self.input_graph_path}...")
            self.graph = nx.read_graphml(self.input_graph_path)
            print(f"Loaded graph with {self.graph.number_of_nodes()} nodes and {self.graph.number_of_edges()} edges.")
        else:
            print("Graph artifact not found. Building fallback starter graph.")
            self.graph = self._build_fallback_graph()
        return self.graph

    def _build_fallback_graph(self):
        G = nx.MultiDiGraph()
        # Mock concepts
        G.add_node("c1", type="concept", id="c1")
        G.add_node("eng_name", type="lemma_eng", lemma="name")
        G.add_node("nep_name", type="lemma_lang", lemma="नाम")
        G.add_node("rom_name", type="lemma_roman", lemma="naam")
        G.add_node("syn_name", type="synset", id="syn_name")
        G.add_node("dom_general", type="domain", id="dom_general")

        G.add_edge("eng_name", "c1", relation="englishlabelfor")
        G.add_edge("nep_name", "c1", relation="targetlabelfor")
        G.add_edge("rom_name", "c1", relation="romanisedas")
        G.add_edge("c1", "syn_name", relation="mappedtosynset")
        G.add_edge("c1", "dom_general", relation="belongstodomain")

        G.add_node("c2", type="concept", id="c2")
        G.add_node("eng_house", type="lemma_eng", lemma="house")
        G.add_node("nep_house", type="lemma_lang", lemma="घर")
        G.add_node("rom_house", type="lemma_roman", lemma="ghar")
        G.add_edge("eng_house", "c2", relation="englishlabelfor")
        G.add_edge("nep_house", "c2", relation="targetlabelfor")
        G.add_edge("rom_house", "c2", relation="romanisedas")
        G.add_edge("c2", "dom_general", relation="belongstodomain")

        G.add_edge("c1", "c2", relation="conceptsimilarity", weight=0.5)

        # Mock script
        G.add_node("g_ka", type="grapheme", grapheme="क")
        G.add_node("t_ka", type="transliteration", transliteration="ka")
        G.add_node("p_ka", type="phoneme", ipa="kʌ")
        G.add_edge("p_ka", "g_ka", relation="phonemewrittenas")
        G.add_edge("p_ka", "t_ka", relation="phonemetransliteratedas")

        G.add_node("g_kha", type="grapheme", grapheme="ख")
        G.add_node("t_kha", type="transliteration", transliteration="kha")
        G.add_node("p_kha", type="phoneme", ipa="kʰʌ")
        G.add_edge("p_kha", "g_kha", relation="phonemewrittenas")
        G.add_edge("p_kha", "t_kha", relation="phonemetransliteratedas")

        G.add_node("g_ga", type="grapheme", grapheme="ग")
        G.add_node("t_ga", type="transliteration", transliteration="ga")
        G.add_node("p_ga", type="phoneme", ipa="gʌ")
        G.add_edge("p_ga", "g_ga", relation="phonemewrittenas")
        G.add_edge("p_ga", "t_ga", relation="phonemetransliteratedas")
        
        G.add_node("g_gha", type="grapheme", grapheme="घ")
        G.add_node("t_gha", type="transliteration", transliteration="gha")
        G.add_node("p_gha", type="phoneme", ipa="gʱʌ")
        G.add_edge("p_gha", "g_gha", relation="phonemewrittenas")
        G.add_edge("p_gha", "t_gha", relation="phonemetransliteratedas")

        # categories
        G.add_node("cat_consonant", type="script_category", id="consonant")
        for n in ["g_ka", "g_kha", "g_ga", "g_gha"]:
            G.add_edge(n, "cat_consonant", relation="graphemetocategory")
            G.add_edge(n, "lesson_1", relation="graphemetolesson")
            
        G.add_node("lesson_1", type="lesson", id="lesson_1")
        
        # Audio placeholder
        G.add_node("a_ka", type="audio", path="placeholders/ka.mp3")
        G.add_edge("a_ka", "g_ka", relation="audiorepresents")

        return G
