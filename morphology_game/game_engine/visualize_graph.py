import networkx as nx
import matplotlib.pyplot as plt

# 1. Initialize the Graph
G = nx.Graph()

target = "kanskn (I live)"
vocab_distractors = ["kanl3b (I play)", "kann3s (I sleep)", "kanktb (I write)"]
grammar_distractors = ["katskn (You live)", "kayskn (He lives)", "kaysknu (They live)"]

# 2. Add Nodes
G.add_node(target)
for w in vocab_distractors + grammar_distractors:
    G.add_node(w)

# 3. Add Edges (Morphological Distance)
for w in vocab_distractors:
    G.add_edge(target, w, weight=1, label="Root Change")
for w in grammar_distractors:
    G.add_edge(target, w, weight=1, label="Pronoun Change")

# 4. Plot the Graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42) # physics layout

# Draw Nodes
nx.draw_networkx_nodes(G, pos, nodelist=[target], node_size=3000, node_color='lightgreen')
nx.draw_networkx_nodes(G, pos, nodelist=vocab_distractors, node_size=2000, node_color='lightblue')
nx.draw_networkx_nodes(G, pos, nodelist=grammar_distractors, node_size=2000, node_color='salmon')

# Draw Edges & Labels
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Morphological Graph Distance (Target: skn)")
plt.axis("off")
plt.savefig("morphological_graph.png")
print("Graph saved as morphological_graph.png!")