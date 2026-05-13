import csv
import sys

# Importing NLTK's WordNet to interact with the WordNet lexical database, it provides
# predefined functions to fetch synsets, calculate similarities, and traverse hierarchies.
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
    """
    This function converts these WordNet string IDs into an actual NLTK Synset object.
    I use the predefined `wn.synset_from_pos_and_offset` function, which lets me grab the exact WordNet node 
    by splitting the ID into its offset ('02084071') and part of speech ('n' for noun).
    """
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
        
        # Checking if both of the IDs I entered exist in my mappings dictionary.
        if id1 not in ukc_to_wn or id2 not in ukc_to_wn:
            print("Error: One or both Concept IDs not found.")
            continue
            
        #  convert the raw IDs into NLTK Synset objects so we can use WordNet's built-in functions.
        synset1 = get_synset_from_wn_id(ukc_to_wn[id1])
        synset2 = get_synset_from_wn_id(ukc_to_wn[id2])
        
        if not synset1 or not synset2:
            print("Error: Could not retrieve synsets.")
            continue
            
        # 1. Exact Synsets (and their definitions)
        # Using .name() and .definition() functions to print out human-readable descriptions of the synsets.
        print(f"\nSynset 1: {synset1.name()} ({synset1.definition()})")
        print(f"Synset 2: {synset2.name()} ({synset2.definition()})")
        
        # 2. Lowest Common Hypernym
        # Using the .lowest_common_hypernyms() function to find the closest shared ancestor node between the two synsets.
        common_hypernyms = synset1.lowest_common_hypernyms(synset2)
        lch = common_hypernyms[0] if common_hypernyms else None
        
        if lch:
            print(f"Lowest Common Hypernym: {lch.name()} ({lch.definition()})")
        else:
            print("Lowest Common Hypernym: None")
            
        # 3. Shortest Path Distance
        # Using the .shortest_path_distance() function to see exactly how many edges separate the two nodes in the WordNet graph.
        path_distance = synset1.shortest_path_distance(synset2)
        print(f"Shortest Path Distance: {path_distance}")
        
        # 4. Depth of Shared Ancestor
        # The .max_depth() function tells how deep this shared ancestor is in the hierarchy, which helps measure similarity.
        lch_depth = lch.max_depth() if lch else "N/A"
        print(f"Depth of Shared Ancestor: {lch_depth}")
        
        # 5. Depth of each individual Concept
        # The .max_depth() function also tells how deep the individual concepts are, which helps determine how specific they are.
        print(f"Depth of Concept 1: {synset1.max_depth()}")
        print(f"Depth of Concept 2: {synset2.max_depth()}")

if __name__ == "__main__":
    main()
