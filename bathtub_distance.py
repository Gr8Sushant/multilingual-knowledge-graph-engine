from typing import List, Tuple
import argparse
import sys
import regex


def split_graphemes(text: str) -> List[str]:
    """
    Split a string into Unicode grapheme clusters.
    This is better than plain character splitting for scripts like Devanagari.
    """
    return regex.findall(r"\X", text)


def longest_common_prefix_graphemes(g1: List[str], g2: List[str]) -> int:
    """
    Count matching grapheme clusters from the start.
    """
    match_length = 0
    for a, b in zip(g1, g2):
        if a == b:
            match_length += 1
        else:
            break
    return match_length


def longest_common_suffix_graphemes(g1: List[str], g2: List[str]) -> int:
    """
    Count matching grapheme clusters from the end.
    """
    match_length = 0
    for a, b in zip(reversed(g1), reversed(g2)):
        if a == b:
            match_length += 1
        else:
            break
    return match_length


def boundary_similarity(w1: str, w2: str) -> float:
    """
    Boundary similarity rewards shared prefix + suffix structure.
    It is capped by the length of the shorter word.
    """
    g1 = split_graphemes(w1.strip())
    g2 = split_graphemes(w2.strip())

    n = len(g1)
    m = len(g2)

    if n == 0 or m == 0:
        raise ValueError("Input words must be non-empty.")

    prefix = longest_common_prefix_graphemes(g1, g2)
    suffix = longest_common_suffix_graphemes(g1, g2)

    return min(prefix + suffix, min(n, m)) / min(n, m)


def length_similarity(w1: str, w2: str) -> float:
    """
    Length similarity rewards similar grapheme length.
    """
    g1 = split_graphemes(w1.strip())
    g2 = split_graphemes(w2.strip())

    n = len(g1)
    m = len(g2)

    if n == 0 or m == 0:
        raise ValueError("Input words must be non-empty.")

    return 1.0 - abs(n - m) / max(n, m)


def bathtub_similarity(
    w1: str,
    w2: str,
    alpha: float = 0.80,
    beta: float = 0.20,
) -> float:
    """
    Weighted combination of boundary similarity and length similarity.
    Returns a similarity in [0, 1].
    """
    if not w1 or not w2:
        raise ValueError("w1 and w2 must be non-empty strings.")

    if alpha < 0 or beta < 0:
        raise ValueError("alpha and beta must be non-negative.")

    if alpha + beta == 0:
        raise ValueError("alpha + beta must be positive.")

    b = boundary_similarity(w1, w2)
    l = length_similarity(w1, w2)

    return (alpha * b + beta * l) / (alpha + beta)


def bathtub_distance(
    w1: str,
    w2: str,
    alpha: float = 0.80,
    beta: float = 0.20,
) -> float:
    """
    Distance version of bathtub similarity.
    Returns a distance in [0, 1].
    """
    return 1.0 - bathtub_similarity(w1, w2, alpha=alpha, beta=beta)


def compare_words(w1: str, w2: str) -> Tuple[float, float]:
    """
    Convenience wrapper returning (similarity, distance).
    """
    similarity = bathtub_similarity(w1, w2)
    distance = 1.0 - similarity
    return similarity, distance


def main():
    parser = argparse.ArgumentParser(
        description="Compute Bathtub Distance and Similarity between two words."
    )
    parser.add_argument("w1", nargs="?", type=str, help="First word")
    parser.add_argument("w2", nargs="?", type=str, help="Second word")
    args = parser.parse_args()

    if args.w1 and args.w2:
        sim, dist = compare_words(args.w1, args.w2)
        print(f"Words: {args.w1} / {args.w2}")
        print(f"Similarity: {sim:.4f}")
        print(f"Distance: {dist:.4f}")
    elif args.w1 or args.w2:
        print("Error: Please provide both w1 and w2 parameters.")
        sys.exit(1)
    else:
        examples = [
            ("distance", "différence"),
            ("main", "pain"),
            ("lampe", "palme"),
            ("ma", "má"),
            ("शित्तल्", "पित्तल्"),
            ("Krankenwagen", "Krankenhaus"),
        ]

        for w1, w2 in examples:
            sim, dist = compare_words(w1, w2)
            print(f"Words: {w1} / {w2}")
            print(f"Similarity: {sim:.4f}")
            print(f"Distance: {dist:.4f}")
            print()


if __name__ == "__main__":
    main()