import pandas as pd
import networkx as nx
import uuid
import json
import matplotlib.pyplot as plt
import os
from networkx.readwrite import json_graph

# Ensure output folders exist
os.makedirs("graph_export/artifacts", exist_ok=True)

print("1. Reading Database...")
db_df = pd.read_excel("db_pronouns_social-adressing_v1.xlsx", sheet_name="input_nodes")
db_df = db_df[~db_df['adressing relation'].str.contains("child", na=False)] 
db_df['language'] = db_df['language'].fillna('Unknown').astype(str).str.strip().str.title()

G_plugged = nx.DiGraph() 
attribute_nodes = set()

def add_attribute_node(graph, node_id, category):
    if node_id not in attribute_nodes:
        graph.add_node(node_id, type="attribute", category=category)
        attribute_nodes.add(node_id)

def process_and_build_graph(row):
    relation = str(row['adressing relation']).lower()
    note = str(row['any note?']).lower()
    
    # Layer Definitions
    if "younger" in relation: broad_age = "Younger"
    elif "same age" in relation: broad_age = "Same Age"
    else: broad_age = "Older" 
        
    if "senior" in relation or "grandparent" in relation: specific_age = "Grandparents' gen"
    elif "middle-age" in relation or "parents" in relation: specific_age = "Parents' gen"
    elif "older" in relation: specific_age = "Older (same gen)"
    elif "younger" in relation: specific_age = "Younger (same gen)"
    else: specific_age = "Exactly same age"
        
    addr_options = ["Male", "Female"]
    if "you as male" in note or "bhai" in note or "uncle" in relation or "uncle" in note or ("male" in note and "female" not in note): 
        addr_options = ["Male"]
    elif "you as female" in note or "baji" in note or "apa" in note or "aunt" in relation or "aunty" in note or "khala" in note or ("female" in note): 
        addr_options = ["Female"]

    social_options = ["Neutral"]
    if "casual" in note or "informal" in note: social_options = ["Informal"]
    elif "formal" in note or "polite" in note or "respect" in note: social_options = ["Formal"]
        
    spk_options = ["Male spk", "Female spk"]
    if "i/me as male" in note: spk_options = ["Male spk"]
    elif "i/me as female" in note: spk_options = ["Female spk"]

    paths = []
    for addr in addr_options:
        for social in social_options:
            for spk in spk_options:
                path_str = f"{broad_age} - {specific_age} - {addr} - {social} - {spk}"
                paths.append(path_str)
                
                G_plugged.add_node(path_str, type="schema_path")
                add_attribute_node(G_plugged, f"Age: {broad_age}", "Broad Age")
                add_attribute_node(G_plugged, f"Gen: {specific_age}", "Specific Gen")
                add_attribute_node(G_plugged, f"Target: {addr}", "Addressee Gender")
                add_attribute_node(G_plugged, f"Context: {social}", "Social Context")
                add_attribute_node(G_plugged, f"Spk: {spk}", "Speaker Gender")
                
                G_plugged.add_edge(path_str, f"Age: {broad_age}", type="HAS_BROAD_AGE")
                G_plugged.add_edge(path_str, f"Gen: {specific_age}", type="HAS_SPECIFIC_GEN")
                G_plugged.add_edge(path_str, f"Target: {addr}", type="HAS_TARGET")
                G_plugged.add_edge(path_str, f"Context: {social}", type="HAS_CONTEXT")
                G_plugged.add_edge(path_str, f"Spk: {spk}", type="HAS_SPEAKER")
    return paths

# 🌟 CRITICAL: THIS LOOP WAS MISSING!
print("2. Building Instances...")
for index, row in db_df.iterrows():
    target_paths = process_and_build_graph(row)
    
    term_i = str(row['terms (i/me)']).strip() if pd.notna(row['terms (i/me)']) else ""
    term_you = str(row['terms (you)']).strip() if pd.notna(row['terms (you)']) else ""
    lang = row['language']
    
    if term_i == "" and term_you == "": continue
    if "no word" in term_i.lower() or "no word" in term_you.lower(): continue
        
    instance_id = f"Instance_{uuid.uuid4().hex[:6]}"
    label = f"{lang}: {term_i}/{term_you}"
    
    G_plugged.add_node(instance_id, type="instance", language=lang, term_i=term_i, term_you=term_you, label=label)
    
    for path in target_paths:
        G_plugged.add_edge(path, instance_id, type="HAS_PRONOUN")

# Embed Penalty Rules
penalty_rules = { "Broad Age": 5, "Specific Gen": 4, "Addressee": 3, "Context": 2, "Speaker": 1 }
G_plugged.graph['scoring_rules'] = penalty_rules

# Export Artifacts
print("3. Exporting Artifacts...")
nodes_export = [{"id": n, **data} for n, data in G_plugged.nodes(data=True)]
pd.DataFrame(nodes_export).to_csv("graph_export/artifacts/nodes.csv", index=False)
edges_export = [{"source": u, "target": v, **data} for u, v, data in G_plugged.edges(data=True)]
pd.DataFrame(edges_export).to_csv("graph_export/artifacts/edges.csv", index=False)

plugged_data = json_graph.node_link_data(G_plugged)
with open("graph_export/graph_data.js", "w", encoding="utf-8") as f:
    f.write("var myGraphData = " + json.dumps(plugged_data, indent=4) + ";")

print("✅ build_graph.py completed successfully.")