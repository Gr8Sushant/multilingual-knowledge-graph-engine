import re
import sys
from pathlib import Path

import nltk
import pandas as pd
from nltk.corpus import wordnet as wn


def ensure_wordnet():
    resources = ["wordnet", "omw-1.4"]
    for resource in resources:
        try:
            nltk.data.find(f"corpora/{resource}")
        except LookupError:
            nltk.download(resource, quiet=True)


def normalize_column_name(name):
    return re.sub(r"[^a-z0-9]+", "", str(name).strip().lower())


def find_column(df, aliases, required_tokens=None):
    normalized_to_original = {
        normalize_column_name(column): column for column in df.columns
    }

    for alias in aliases:
        alias_norm = normalize_column_name(alias)
        if alias_norm in normalized_to_original:
            return normalized_to_original[alias_norm]

    if required_tokens:
        for norm_name, original_name in normalized_to_original.items():
            if all(token in norm_name for token in required_tokens):
                return original_name

    return None


def is_missing(value):
    if value is None:
        return True
    if pd.isna(value):
        return True
    text = str(value).strip()
    return text == "" or text.lower() in {"nan", "none", "null"}


def load_tsv(path):
    df = pd.read_csv(
        path,
        sep="\t",
        dtype=str,
        encoding="utf-8",
        keep_default_na=False,
    )

    concept_col = find_column(
        df,
        aliases=[
            "concept_id",
            "conceptid",
            "concept id",
            "ukc_concept_id",
            "ukcconceptid",
        ],
        required_tokens=["concept", "id"],
    )

    wn30_col = find_column(
        df,
        aliases=[
            "wn30_id",
            "wn30id",
            "wn30 id",
            "wordnet_id",
            "wordnetid",
            "wordnet 3.0 id",
            "wn_id",
            "wnid",
            "synset",
            "synset_id",
            "synsetid",
            "wn30",
        ],
        required_tokens=["wn30", "id"],
    )

    if concept_col is None:
        raise ValueError(
            f"Could not detect a concept_id column. Available columns: {list(df.columns)}"
        )

    if wn30_col is None:
        raise ValueError(
            f"Could not detect a wn30_id column. Available columns: {list(df.columns)}"
        )

    normalized_df = df.rename(
        columns={
            concept_col: "concept_id",
            wn30_col: "wn30_id",
        }
    ).copy()

    normalized_df["concept_id"] = normalized_df["concept_id"].astype(str).str.strip()
    normalized_df["wn30_id"] = normalized_df["wn30_id"].astype(str).str.strip()

    return normalized_df[["concept_id", "wn30_id"]]


def resolve_synset(wn30_id):
    if is_missing(wn30_id):
        return None

    text = str(wn30_id).strip()

    try:
        return wn.synset(text)
    except Exception:
        pass

    compact = text.replace(" ", "")

    patterns = [
        r"^(?:eng-30-)?(\d{8})-([nvars])$",
        r"^([nvars])-(\d{8})$",
        r"^(\d{8})([nvars])$",
    ]

    for pattern in patterns:
        match = re.match(pattern, compact, flags=re.IGNORECASE)
        if not match:
            continue

        groups = match.groups()
        if groups[0].isdigit():
            offset_str, pos = groups[0], groups[1].lower()
        else:
            pos, offset_str = groups[0].lower(), groups[1]

        try:
            return wn.synset_from_pos_and_offset(pos, int(offset_str))
        except Exception:
            return None

    parts = compact.split("-")
    if len(parts) >= 2:
        for i in range(len(parts) - 1):
            left = parts[i]
            right = parts[i + 1]
            if left.isdigit() and len(left) == 8 and len(right) == 1 and right.lower() in "nvars":
                try:
                    return wn.synset_from_pos_and_offset(right.lower(), int(left))
                except Exception:
                    return None

    return None


def resolve_domain(wn30_id):
    synset = resolve_synset(wn30_id)
    if synset is None:
        return "unknown"

    try:
        return synset.lexname()
    except Exception:
        return "unknown"


def build_concept_domain_table(df):
    total_rows = len(df)
    unique_concepts_found = df.loc[
        ~df["concept_id"].apply(is_missing), "concept_id"
    ].nunique()

    concept_map = {}
    unresolved_rows = 0

    for row in df.itertuples(index=False):
        concept_id = "" if is_missing(row.concept_id) else str(row.concept_id).strip()
        wn30_id = "" if is_missing(row.wn30_id) else str(row.wn30_id).strip()

        if not concept_id:
            unresolved_rows += 1
            continue

        domain = resolve_domain(wn30_id)
        if domain == "unknown":
            unresolved_rows += 1

        candidate = {
            "concept_id": concept_id,
            "wn30_id": wn30_id,
            "domain": domain,
        }

        existing = concept_map.get(concept_id)

        if existing is None:
            concept_map[concept_id] = candidate
            continue

        existing_known = existing["domain"] != "unknown"
        candidate_known = candidate["domain"] != "unknown"

        if not existing_known and candidate_known:
            concept_map[concept_id] = candidate
        elif (
            not existing["wn30_id"]
            and candidate["wn30_id"]
            and existing["domain"] == "unknown"
        ):
            concept_map[concept_id] = candidate

    result_df = pd.DataFrame(
        concept_map.values(),
        columns=["concept_id", "wn30_id", "domain"],
    )

    if not result_df.empty:
        result_df = result_df.sort_values("concept_id").reset_index(drop=True)

    domains_resolved = int((result_df["domain"] != "unknown").sum()) if not result_df.empty else 0

    summary = {
        "total_rows_read": total_rows,
        "unique_concepts_found": int(unique_concepts_found),
        "domains_resolved": domains_resolved,
        "unresolved_rows": int(unresolved_rows),
    }

    return result_df, summary


def main():
    ensure_wordnet()

    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("ukc_wn30_mappings (1).tsv")
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("concept_domain.csv")

    df = load_tsv(input_path)
    concept_domain_df, summary = build_concept_domain_table(df)

    concept_domain_df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"total rows read: {summary['total_rows_read']}")
    print(f"unique concepts found: {summary['unique_concepts_found']}")
    print(f"domains resolved: {summary['domains_resolved']}")
    print(f"unresolved rows: {summary['unresolved_rows']}")


if __name__ == "__main__":
    main()