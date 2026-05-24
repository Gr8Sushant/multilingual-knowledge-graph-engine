====================================================
  UKC MULTILINGUAL VOCABULARY GAME
  Language Learning with Knowledge Graphs
====================================================

WHAT THIS PROJECT DOES
-----------------------
A vocabulary learning game that shows an image and asks
the player to pick the correct word in one of 4 languages:
Urdu, Darija (Moroccan Arabic), Nepali, or Vietnamese.

All words come from the UKC (Universal Knowledge Core)
lexicons, connected through a knowledge graph. The graph
links concepts across languages using WordNet 3.0 synset IDs.


FILES EXPLAINED
---------------

graph_builder.py
  Reads all 4 language CSV files and builds a knowledge graph.
  Each concept node stores the word in each language.
  Run this once to create urdu_game_graph.pkl.

game.py
  The actual game. Loads the graph, shows images from the
  15/ folder, and displays word options from the graph.
  Distractors are selected from the same visual category.

urdu_game_graph.pkl
  The pre-built graph file. If this exists you do not need
  to run graph_builder.py again.

15/ folder
  Contains all game images organized by category:
  animals/, birds/, bread/, clothing/, fruits/,
  furniture/, building/, profession/, people/,
  dairy/, accessories/, body parts/, transport/

urdu_english_ukc_lexicon.csv
darija_english_ukc_lexicon.csv
nepali_english_ukc_lexicon.csv
vietnamese_english_ukc_lexicon.csv
  UKC lexicon files — one per language.
  Each row is a concept with its words in that language.

ukc_wn30_mappings - ukc_wn30_mappings.csv
  Maps UKC concept IDs to WordNet 3.0 synset IDs.
  This is how concepts connect to ImageNet categories.

imagenet_words.csv
  The subset of concepts used in the game with their
  ImageNet synset IDs and domain labels.

concept_domain.csv
  Maps concept IDs to semantic domains (noun.animal,
  noun.artifact etc.) from WordNet.

urdu_alphabet_data - urdu_alphabet_data.csv
  Urdu alphabet with IPA, transliteration and audio file names.
  Used as nodes in the graph for letter-level connections.


HOW TO RUN
----------

1. Install dependencies:
   pip install networkx pillow

2. Build the graph (only needed once):
   python graph_builder.py

3. Run the game:
   python game.py

4. In the game:
   - Select a language from the dropdown (top left)
   - An image appears — pick the correct word from 4 options
   - Green = correct, Red = wrong
   - Score is tracked top right
   - Click Next to continue


KNOWN LIMITATIONS
-----------------
- Some UKC Urdu words are dialectal or Sanskrit-origin
  (e.g. حکیم for doctor, دہقان for farmer). This is a
  data quality issue in the UKC lexicon, not a code issue.
- Darija and Vietnamese have fewer concepts in UKC so
  some questions may show fewer than 4 options.
- Images were sourced manually and are AI-generated.


PROJECT STRUCTURE
-----------------
The graph connects:

  ImageNet image
       |
  imagenet_id (e.g. n02403454)
       |
  UKC concept node  -----> WordNet 3.0 synset
       |
  preferred word in each language (from UKC lexicon)
