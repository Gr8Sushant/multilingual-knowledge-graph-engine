import csv
import pickle
import networkx as nx

def build_graph():
    G = nx.MultiDiGraph()

    # --- Load alphabet nodes ---
    with open('urdu_alphabet_data - urdu_alphabet_data.csv', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            nid = f"letter_{row['Character']}"
            G.add_node(nid,
                node_type=row['Type'],        # Vowel / Consonant / Diacritic
                character=row['Character'],
                ipa=row['IPA'],
                transliteration=row['Transliteration'],
                audio=row['Audio'],
                additional_form=row['Additional_Form']
            )

    # --- Load words + concepts from all 4 languages ---
    languages = {
        'urdu':       'urdu_english_ukc_lexicon.csv',
        'darija':     'darija_english_ukc_lexicon.csv',
        'nepali':     'nepali_english_ukc_lexicon.csv',
        'vietnamese': 'vietnamese_english_ukc_lexicon.csv',
    }

    for lang, path in languages.items():
        with open(path, encoding='utf-8') as f:
            for row in csv.DictReader(f):
                cid = row['concept_id']
                concept_nid = f"concept_{cid}"

                # add concept node if not exists
                if not G.has_node(concept_nid):
                    G.add_node(concept_nid,
                        node_type='concept',
                        concept_id=cid,
                        english=row['english_lemmas'],
                        english_gloss=row['english_gloss']
                    )

                # store preferred lemma per language (first lemma from UKC lexicon)
                preferred = row['lemmas'].split('|')[0].strip()
                node = G.nodes[concept_nid]
                if not node.get(f'preferred_{lang}'):
                    node[f'preferred_{lang}'] = preferred

                # add word node per language
                for lemma in row['lemmas'].split('|'):
                    lemma = lemma.strip()
                    if not lemma:
                        continue
                    word_nid = f"word_{lang}_{lemma}"
                    G.add_node(word_nid,
                        node_type='word',
                        language=lang,
                        lemma=lemma,
                        gloss=row['gloss'],
                        pos=row['part_of_speech']
                    )
                    # word -> concept
                    G.add_edge(word_nid, concept_nid, rel='means')
                    # concept -> word
                    G.add_edge(concept_nid, word_nid, rel='has_word', language=lang)

                    # word -> letter edges (urdu only, for alphabet games)
                    if lang == 'urdu':
                        for char in lemma:
                            letter_nid = f"letter_{char}"
                            if G.has_node(letter_nid):
                                G.add_edge(word_nid, letter_nid, rel='contains')

    # --- Load WN30 mappings ---
    with open('ukc_wn30_mappings - ukc_wn30_mappings.csv', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            concept_nid = f"concept_{row['UKC_local_concept_id']}"
            wn_nid = f"wn30_{row['WN_30_id']}"
            if not G.has_node(wn_nid):
                G.add_node(wn_nid, node_type='wn30', wn30_id=row['WN_30_id'])
            if G.has_node(concept_nid):
                G.add_edge(concept_nid, wn_nid, rel='maps_to')

    # --- Load domain + imagenet info ---
    with open('imagenet_words.csv', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            concept_nid = f"concept_{row['concept_id']}"
            # convert wn30 id format: 02403454-n -> n02403454
            raw_wn = row['wn30_id']
            parts = raw_wn.split('-')
            imagenet_id = parts[1] + parts[0] if len(parts) == 2 else raw_wn
            if G.has_node(concept_nid):
                G.nodes[concept_nid]['domain'] = row['domain']
                G.nodes[concept_nid]['imagenet_id'] = imagenet_id

    print(f"Graph built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G


def save_graph(G, path='urdu_game_graph.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(G, f)
    print(f"Saved to {path}")


def load_graph(path='urdu_game_graph.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    G = build_graph()
    save_graph(G)
