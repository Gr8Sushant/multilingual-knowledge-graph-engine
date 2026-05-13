import pandas as pd
import pydoda
import os
import glob
import numpy as np

print("1. Loading UKC lexicons...")
df_darija = pd.read_csv('../data/darija_english_ukc_lexicon.csv')
df_viet = pd.read_csv('../data/vietnamese_english_ukc_lexicon.csv')

print("2. Extracting raw data from PyDODa with Part of Speech tracking...")
pydoda_path = os.path.dirname(pydoda.__file__)
csv_files = glob.glob(os.path.join(pydoda_path, '**', '*.csv'), recursive=True)

doda_dict = {}

for file in csv_files:
    filename = os.path.basename(file).lower()
    
    if 'verb' in filename:
        file_pos = 3 
    elif 'adjective' in filename:
        file_pos = 2 
    elif 'adverb' in filename or 'preposition' in filename:
        file_pos = 4 
    else:
        file_pos = 1 

    try:
        df_temp = pd.read_csv(file, header=None, on_bad_lines='skip')
        for _, row in df_temp.iterrows():
            valid_cols = row.dropna().tolist()
            if len(valid_cols) >= 3:
                arabizi = str(valid_cols[0]).strip()
                arabic_script = str(valid_cols[-2]).strip()
                english = str(valid_cols[-1]).strip().lower()
                
                eng_variants = [e.strip() for e in english.replace('/', ',').split(',')]
                for eng in eng_variants:
                    if eng:
                        doda_dict[(eng, file_pos)] = (arabizi, arabic_script)
    except:
        continue

print(f"   -> Successfully loaded {len(doda_dict)} unique (English, PoS) pairs!\n")


print("3. Retro-fitting Arabizi to the original Darija words...")
# Create the empty column first
if 'arabizi' not in df_darija.columns:
    df_darija['arabizi'] = pd.Series(dtype='object')

updated_count = 0
for index, row in df_darija.iterrows():
    ukc_pos = row['part_of_speech']
    eng_lemmas = [w.strip().lower() for w in str(row['english_lemmas']).split('|')]
    
    for eng_word in eng_lemmas:
        if (eng_word, ukc_pos) in doda_dict:
            arabizi, _ = doda_dict[(eng_word, ukc_pos)]
            df_darija.at[index, 'arabizi'] = arabizi
            updated_count += 1
            break # Found the match, move to next original word

print(f"   -> Added Arabizi to {updated_count} out of {len(df_darija)} original words.\n")


print("4. Finding completely new words from Vietnamese UKC...")
existing_concepts = set(df_darija['concept_id'])
missing_concepts = df_viet[~df_viet['concept_id'].isin(existing_concepts)]

new_rows = []
for _, row in missing_concepts.iterrows():
    ukc_pos = row['part_of_speech']
    eng_lemmas = [w.strip().lower() for w in str(row['english_lemmas']).split('|')]
    
    for eng_word in eng_lemmas:
        if (eng_word, ukc_pos) in doda_dict:
            arabizi, arabic_script = doda_dict[(eng_word, ukc_pos)]
            
            new_rows.append({
                'concept_id': row['concept_id'],
                'part_of_speech': ukc_pos,
                'lemmas': arabic_script,
                'arabizi': arabizi,
                'english_lemmas': row['english_lemmas'],
                'gloss': row['gloss'],
                'english_gloss': row['english_gloss']
            })
            break 

# 5. Save the Final Output
df_expanded = pd.concat([df_darija, pd.DataFrame(new_rows)], ignore_index=True)

# Rearrange columns so 'arabizi' is right next to 'lemmas' for neatness
cols = ['concept_id', 'part_of_speech', 'lemmas', 'arabizi', 'english_lemmas', 'gloss', 'english_gloss']
df_expanded = df_expanded[cols]

output_path = '../output/darija_expanded_arabizi_ukc.csv'
df_expanded.to_csv(output_path, index=False)

print("========================================")
print("🎉 SUCCESS! Full Pipeline Complete.")
print(f"🎉 Original words updated: {updated_count}")
print(f"🎉 New words added: {len(new_rows)}")
print(f"🎉 Total words in lexicon: {len(df_expanded)}")
print(f"🎉 File saved to: {output_path}")
print("========================================")