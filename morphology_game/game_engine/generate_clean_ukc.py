import pandas as pd
import sys


# =====================================================================
# Look at the first row of your verbs.csv file. Type the exact column headers here:
DARIJA_COL_NAME = "verb_darija"   # e.g., "darija", "Root", "verb_darija"
ENGLISH_COL_NAME = "verb_english" # e.g., "english", "Translation", "verb_english"
# =====================================================================

print("1. Loading Datasets...")
try:
    doda_verbs = pd.read_csv('verbs.csv')
except FileNotFoundError:
    print("❌ ERROR: Could not find 'verbs.csv'. Make sure it is in the same folder.")
    sys.exit()

try:
    ukc_data = pd.read_csv('ukc_english_lexicon.csv')
except FileNotFoundError:
    print("❌ ERROR: Could not find 'ukc_english_lexicon.csv'. Make sure it is in the same folder.")
    sys.exit()

# Safety Check: Verify the column names exist to prevent KeyErrors!
if DARIJA_COL_NAME not in doda_verbs.columns or ENGLISH_COL_NAME not in doda_verbs.columns:
    print(f"\n❌ KEY ERROR: The script could not find columns named '{DARIJA_COL_NAME}' or '{ENGLISH_COL_NAME}'.")
    print(f"Here are the columns actually inside your verbs.csv file: {list(doda_verbs.columns)}")
    print("Please update the CONFIGURATION section at the top of this script to match one of those exact names!")
    sys.exit()

print("2. Filtering UKC Database & Purging Pseudo-Verbs...")
# Filter UKC to ONLY Verbs (POS = 3)
ukc_verbs = ukc_data[ukc_data['part_of_speech'] == 3]

# The blacklist of pseudo-verbs
pseudo_verbs = ['3nd', 'khass', 'fi', 'bgha', 'ban']

# Filter out the pseudo-verbs
doda_verbs = doda_verbs[~doda_verbs[DARIJA_COL_NAME].isin(pseudo_verbs)]

perfect_matches = []
ambiguous_matches = []

print("3. Cross-Referencing with UKC Concept IDs...")
for index, row in doda_verbs.iterrows():
    # Safely extract and clean the text
    darija_root = str(row[DARIJA_COL_NAME]).strip()
    english_lemma = str(row[ENGLISH_COL_NAME]).lower().strip()

    # Skip empty rows or NaN values
    if pd.isna(row[DARIJA_COL_NAME]) or pd.isna(row[ENGLISH_COL_NAME]) or darija_root == 'nan' or english_lemma == 'nan':
        continue

    # Look up the English word in the filtered UKC verbs dataset
    ukc_matches = ukc_verbs[ukc_verbs['lemma'].str.lower() == english_lemma]
    match_count = len(ukc_matches)

    if match_count == 1:
        # PERFECT MATCH
        concept_id = ukc_matches.iloc[0]['concept_id']
        perfect_matches.append({
            'concept_id': concept_id, 
            'arabizi': darija_root, 
            'english_lemmas': english_lemma,
            'part_of_speech': 3
        })
        
    elif match_count > 1:
        # AMBIGUOUS MATCH
        for _, ukc_row in ukc_matches.iterrows():
            ambiguous_matches.append({
                'darija_root': darija_root,
                'english_lemma': english_lemma,
                'possible_concept_id': ukc_row['concept_id'],
                'ukc_definition': ukc_row.get('gloss', 'No definition available') 
            })

print("4. Saving Results...")
if perfect_matches:
    pd.DataFrame(perfect_matches).to_csv('darija_ukc_perfect.csv', index=False)
    print(f"✅ SUCCESS: Saved {len(perfect_matches)} perfect verbs ready for the game to 'darija_ukc_perfect.csv'")
else:
    print("⚠️ No perfect matches found.")

if ambiguous_matches:
    pd.DataFrame(ambiguous_matches).to_csv('darija_ukc_ambiguous_review.csv', index=False)
    unique_ambiguous = len(set([x['darija_root'] for x in ambiguous_matches]))
    print(f"⚠️ Sent {unique_ambiguous} ambiguous verbs for manual review to 'darija_ukc_ambiguous_review.csv'")

print("Script Complete!")