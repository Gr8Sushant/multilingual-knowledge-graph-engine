import csv
import sys

try:
    import nltk
    from nltk.corpus import wordnet as wn
except ImportError:
    print("you need to install nltk first")
    sys.exit(1)

def ensure_wordnet():
    try:
        wn.synsets('dog')
    except LookupError:
        nltk.download('wordnet', quiet=True)
        nltk.download('omw-1.4', quiet=True)

def load_mappings(tsv_path):
    ukc_to_wn = {}
    print("loading the mappings")
    with open(tsv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader, None) # skip header
        for row in reader:
            if len(row) >= 2:
                wn_id, ukc_id = row[0], row[1]
                ukc_to_wn[ukc_id] = wn_id
    return ukc_to_wn

def get_synset_from_wn_id(wn_id):
    if '-' not in wn_id:
        return None
    offset_str, pos = wn_id.split('-')
    try:
        return wn.synset_from_pos_and_offset(pos, int(offset_str))
    except Exception:
        return None

def main():
    ensure_wordnet()
    ukc_to_wn = load_mappings("../data/ukc_wn30_mappings (1).tsv")
    
    while True:
        id1 = input("\nEnter first UKC Concept ID (or 'q' to quit): ").strip()
        if id1.lower() == 'q':
            break
        id2 = input("Enter second UKC Concept ID: ").strip()
        
        if id1 not in ukc_to_wn or id2 not in ukc_to_wn:
            print("Error: One or both Concept IDs not found.")
            continue
            
        synset1 = get_synset_from_wn_id(ukc_to_wn[id1])
        synset2 = get_synset_from_wn_id(ukc_to_wn[id2])
        
        if not synset1 or not synset2:
            print("Error: Could not retrieve synsets.")
            continue
            
        # 1. Exact Synsets (and their definitions)
        print(f"\nSynset 1: {synset1.name()} ({synset1.definition()})")
        print(f"Synset 2: {synset2.name()} ({synset2.definition()})")
        
        # 2. Lowest Common Hypernym
        common_hypernyms = synset1.lowest_common_hypernyms(synset2)
        lch = common_hypernyms[0] if common_hypernyms else None
        
        if lch:
            print(f"Lowest Common Hypernym: {lch.name()} ({lch.definition()})")
        else:
            print("Lowest Common Hypernym: None")
            
        # 3. Shortest Path Distance
        path_distance = synset1.shortest_path_distance(synset2)
        print(f"Shortest Path Distance: {path_distance}")
        
        # 4. Depth of Shared Ancestor
        lch_depth = lch.max_depth() if lch else "N/A"
        print(f"Depth of Shared Ancestor: {lch_depth}")
        
        # 5. Depth of each individual Concept
        print(f"Depth of Concept 1: {synset1.max_depth()}")
        print(f"Depth of Concept 2: {synset2.max_depth()}")

if __name__ == "__main__":
    main()
