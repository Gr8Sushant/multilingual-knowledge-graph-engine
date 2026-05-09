import csv
import sys
from dataclasses import dataclass
from typing import Optional, Dict, Tuple

from bathtub_distance import bathtub_similarity

try:
    import nltk
    from nltk.corpus import wordnet as wn
except ImportError:
    print("Hey there! you need to install nltk first")
    sys.exit(1)


@dataclass
class SemanticSimilarityFeatures:
    """
    A data class to store the various metrics computed between two concepts.
    This includes both WordNet topological metrics (path distance, depths) 
    and morphological metrics (surface similarity).
    """
    shortest_path_distance: Optional[int]
    shared_ancestor_depth: Optional[int]
    concept1_depth: Optional[int]
    concept2_depth: Optional[int]
    same_direct_hypernym: bool = False
    surface_similarity: float = 0.0


def ensure_wordnet():
    try:
        wn.synsets("dog")
    except LookupError:
        nltk.download("wordnet", quiet=True)
        nltk.download("omw-1.4", quiet=True)


def clamp01(x: float) -> float:
    """
    Clamps a floating-point value to be strictly within the range [0.0, 1.0].
    """
    return max(0.0, min(1.0, x))


def normalize_path_similarity(distance: Optional[int], max_distance: int = 12) -> float:
    """
    Normalizes the shortest path distance between two synsets into a similarity score (0 to 1).
    Shorter distances yield higher similarity scores. Distances beyond `max_distance` are penalized.
    """
    if distance is None:
        return 0.0
    return clamp01(1.0 - (distance / max_distance))


def normalize_depth(depth: Optional[int], max_depth: int = 20) -> float:
    """
    Normalizes the depth of a synset into a score (0 to 1).
    Deeper nodes in the WordNet hierarchy are considered more specific and yield higher scores.
    """
    if depth is None:
        return 0.0
    return clamp01(depth / max_depth)


def semantic_similarity_weight(
    f: SemanticSimilarityFeatures,
    max_path_distance: int = 12,
    max_depth: int = 20,
    w_surface: float = 0.50,
    w_path: float = 0.20,
    w_shared_depth: float = 0.15,
    w_specificity: float = 0.10,
    w_direct_hypernym: float = 0.05
) -> float:
    """
    Computes a final weighted semantic similarity score by linearly combining:
    1. Shortest path distance (normalized)
    2. Depth of the Lowest Common Hypernym (shared ancestor)
    3. Average depth (specificity) of the two concepts
    4. A bonus if they share an immediate parent
    5. The morphological Bathtub distance (surface similarity) of their strings
    
    Returns a final score clamped between 0.0 and 1.0.
    """
    path_sim = normalize_path_similarity(f.shortest_path_distance, max_path_distance)
    shared_depth_sim = normalize_depth(f.shared_ancestor_depth, max_depth)

    # Specificity is the average normalized depth of the two concepts
    c1 = normalize_depth(f.concept1_depth, max_depth)
    c2 = normalize_depth(f.concept2_depth, max_depth)
    specificity = (c1 + c2) / 2.0

    direct_hypernym_bonus = 1.0 if f.same_direct_hypernym else 0.0
    surface_sim = clamp01(f.surface_similarity)

    # Combine weighted factors
    score = (
        w_path * path_sim
        + w_shared_depth * shared_depth_sim
        + w_specificity * specificity
        + w_direct_hypernym * direct_hypernym_bonus
        + w_surface * surface_sim
    )
    return clamp01(score)


def difficulty_band(score: float) -> str:
    """
    Categorizes a numeric similarity score [0.0 - 1.0] into a human-readable difficulty label.
    Higher similarity often translates to harder distinction for language models/systems.
    """
    if score >= 0.80:
        return "hard"
    elif score >= 0.60:
        return "medium-hard"
    elif score >= 0.40:
        return "medium"
    elif score >= 0.20:
        return "easy"
    return "very-easy"


def load_mappings(tsv_path: str) -> Dict[str, str]:
    """
    Loads UKC Concept ID to WordNet 3.0 ID mappings from a TSV file.
    It checks various possible column headers to accommodate different versions of the file.
    """
    ukc_to_wn = {}
    print("loading the mappings")

    with open(tsv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")

        for row in reader:
            if not row:
                continue

            wn_id = row.get("WN_30_id")
            ukc_id = row.get("UKC_local_concept_id")

            if wn_id and ukc_id:
                ukc_to_wn[str(ukc_id).strip()] = str(wn_id).strip()

    return ukc_to_wn


def load_lemmas(csv_path: str) -> Dict[str, str]:
    """
    Loads UKC Concept ID to Nepali Lemmas mapping from the Lexicon CSV file.
    This allows us to fetch the actual Nepali word strings to compute orthographic similarity.
    """
    ukc_to_lemmas = {}
    print("loading the lemmas")

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            concept_id = row.get("concept_id")
            lemmas = row.get("lemmas")

            if concept_id and lemmas:
                ukc_to_lemmas[str(concept_id).strip()] = str(lemmas).strip()

    return ukc_to_lemmas


def split_lemma_field(lemmas_str: str):
    """
    Splits a pipe or semicolon-separated string of lemmas into a list of individual lemma strings.
    """
    if not lemmas_str:
        return []

    normalized = lemmas_str.replace(";", "|").replace(",", "|")
    return [part.strip() for part in normalized.split("|") if part.strip()]


def get_max_bathtub_similarity(lemmas_str1: str, lemmas_str2: str) -> float:
    """
    Computes the maximum Bathtub surface similarity between all possible lemma pairs 
    for two given concepts. Since a concept may have multiple synonymous lemmas, 
    we find the pair that looks the most orthographically similar.
    """
    if not lemmas_str1 or not lemmas_str2:
        return 0.0

    lemmas1 = split_lemma_field(lemmas_str1)
    lemmas2 = split_lemma_field(lemmas_str2)

    max_sim = 0.0
    for l1 in lemmas1:
        for l2 in lemmas2:
            try:
                # Compare each lemma combination using Bathtub logic
                sim = bathtub_similarity(l1, l2)
                if sim > max_sim:
                    max_sim = sim
            except Exception:
                pass

    return max_sim


def get_synset_from_wn_id(wn_id: str):
    """
    Retrieves an NLTK WordNet Synset object from a WordNet ID string (e.g., '00001740-n').
    The ID is parsed into an offset and a Part-Of-Speech (POS) tag.
    """
    if "-" not in wn_id:
        return None

    offset_str, pos = wn_id.split("-", 1)
    try:
        return wn.synset_from_pos_and_offset(pos, int(offset_str))
    except Exception:
        return None


def get_deepest_lch(synset1, synset2):
    """
    Finds the Lowest Common Hypernym (LCH) between two synsets.
    If multiple common hypernyms exist, it returns the one deepest in the WordNet hierarchy 
    (the most specific shared ancestor).
    """
    common_hypernyms = synset1.lowest_common_hypernyms(synset2)
    if not common_hypernyms:
        return None
    return max(common_hypernyms, key=lambda s: s.max_depth())


def same_direct_hypernym(synset1, synset2) -> bool:
    """
    Checks if two synsets share at least one immediate parent (hypernym).
    This indicates they are direct siblings in the conceptual graph.
    """
    hypers1 = set(synset1.hypernyms())
    hypers2 = set(synset2.hypernyms())
    return len(hypers1.intersection(hypers2)) > 0


def build_features(
    synset1,
    synset2,
    surface_similarity: float = 0.0
) -> Tuple[SemanticSimilarityFeatures, Optional[object]]:
    """
    Compiles all topological and morphological metrics into a SemanticSimilarityFeatures object.
    It computes the shared ancestor, path distance, depths, and stores the provided surface similarity.
    """
    lch = get_deepest_lch(synset1, synset2)
    path_distance = synset1.shortest_path_distance(synset2)

    features = SemanticSimilarityFeatures(
        shortest_path_distance=path_distance,
        shared_ancestor_depth=lch.max_depth() if lch else None,
        concept1_depth=synset1.max_depth(),
        concept2_depth=synset2.max_depth(),
        same_direct_hypernym=same_direct_hypernym(synset1, synset2),
        surface_similarity=surface_similarity
    )
    return features, lch


def print_result(
    id1: str,
    id2: str,
    synset1,
    synset2,
    lch,
    features: SemanticSimilarityFeatures,
    lemmas1: str = "",
    lemmas2: str = ""
):
    """
    Outputs the final computed semantic similarity and all intermediate metrics to the console.
    """
    score = semantic_similarity_weight(features)
    wn_path_sim = synset1.path_similarity(synset2)

    print(f"\nUKC Concept 1: {id1} (Lemmas: {lemmas1})")
    print(f"UKC Concept 2: {id2} (Lemmas: {lemmas2})")

    print(f"\nSynset 1: {synset1.name()} ({synset1.definition()})")
    print(f"Synset 2: {synset2.name()} ({synset2.definition()})")

    if lch:
        print(f"Lowest Common Hypernym: {lch.name()} ({lch.definition()})")
    else:
        print("Lowest Common Hypernym: None")

    print(f"Same Direct Hypernym: {features.same_direct_hypernym}")
    print(f"Shortest Path Distance: {features.shortest_path_distance}")
    print(f"WordNet Path Similarity: {wn_path_sim}")
    print(f"Depth of Shared Ancestor: {features.shared_ancestor_depth}")
    print(f"Depth of Concept 1: {features.concept1_depth}")
    print(f"Depth of Concept 2: {features.concept2_depth}")
    print(f"Surface Similarity Bonus (Bathtub): {features.surface_similarity:.4f}")

    print(f"\nSemantic Similarity Weight: {score:.4f}")
    print(f"Suggested Difficulty Band: {difficulty_band(score)}")


def main():
    """
    Main interactive loop.
    1. Ensures datasets are downloaded.
    2. Loads ID mappings and Lemmas into memory.
    3. Prompts the user for pairs of UKC Concept IDs.
    4. Computes and prints their semantic similarity and morphological similarity.
    """
    ensure_wordnet()

    ukc_to_wn = load_mappings("ukc_wn30_mappings (1).tsv")
    ukc_to_lemmas = load_lemmas("nepali_english_ukc_lexicon_transliterated.csv")

    while True:
        id1 = input("\nEnter first UKC Concept ID (or 'q' to quit): ").strip()
        if id1.lower() == "q":
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

        if synset1.pos() != "n" or synset2.pos() != "n":
            print("Warning: this weighting is mainly designed for noun hierarchies.")

        lemmas1 = ukc_to_lemmas.get(id1, "")
        lemmas2 = ukc_to_lemmas.get(id2, "")

        surface_sim = 0.0
        # Compute maximum Bathtub similarity if both concepts have Nepali lemmas
        if lemmas1 and lemmas2:
            surface_sim = get_max_bathtub_similarity(lemmas1, lemmas2)

        features, lch = build_features(
            synset1,
            synset2,
            surface_similarity=surface_sim
        )

        print_result(id1, id2, synset1, synset2, lch, features, lemmas1, lemmas2)


if __name__ == "__main__":
    main()