# Multilingual Knowledge Graph Engine

A robust, multilingual graph engine designed to ingest diverse linguistic lexicons and abugida (script/phonology) data into a unified, pedagogical semantic network. 

Currently, the project is structured around the **Phase 1 Prototype**, which focuses on building the foundational semantic and structural backbone of the graph.

---

## Scripts in ./matching_game/scripts/ 

> Here is a summary of what each script in the scripts folder does:

- bathtub_distance.py: A utility script that computes the "Bathtub Distance" and similarity between two words. It calculates an orthographic similarity alongside word length. It can be imported by other scripts during game generation.
- Bathtub_distance_POC.py: An earlier Proof of Concept (POC) version of the Bathtub distance algorithm. 
- concept_semantic_similarity.py: Calculates a aggregated similarity score between two concepts. It combines WordNet topological metrics (such as the shortest path distance, shared ancestor depth, and direct hypernyms) with morphological surface similarity (using the Bathtub distance algorithm). It categorizes the final weighted score into a human-readable "difficulty band" (e.g., hard, medium, easy), which is useful for generating word-matching game mechanics. Designed for edge-weight calculation.
- generate_concept_domain.py: Responsible for mapping concepts to their broad semantic domains/categories. It reads a TSV mapping file (linking UKC concept IDs to WordNet IDs), cleans the data, uses NLTK's lexname function to resolve the high-level semantic category for each concept, resolves any missing/duplicate entries, and exports the cleaned data into a CSV table (concept_domain.csv).
- test_wn_mappings.py: An interactive debugging and testing script used to explore WordNet mapping behaviors. It loads UKC-to-WordNet mappings and prompts users to input pairs of UKC Concept IDs. It then uses NLTK to print out the exact WordNet synsets, their human-readable definitions, their closest shared ancestor (Lowest Common Hypernym), and topological distance metrics.

### Concept_semantic_similarity
#### Current Implementation
The current implementation computes one final similarity score between two concepts.

It combines:
- Bathtub Similarity score → Orthographic and length similarity (How it looks)
- path closeness → how close the two concepts are in the WordNet tree
- shared ancestor depth → how specific their shared parent is? For example: sharing “fruit” is more meaningful than sharing “thing”
- concept specificity → how specific the two concepts themselves are. Reward if they are less generic. 
- same direct hypernym → Reward if they are siblings under the same immediate parent. E.g. Apple and Bananas.

After multiple iterations, I settled the final weight as:
* 50% Bathtub Similarity score
* 20% path closeness
* 15% shared ancestor depth
* 10% concept specificity
* 5% same direct hypernym
<img width="601" height="772" alt="Screenshot 2026-05-13 at 14 41 10" src="https://github.com/user-attachments/assets/5b6ba9c6-a0be-43e3-a5dd-ce322812064d" />

