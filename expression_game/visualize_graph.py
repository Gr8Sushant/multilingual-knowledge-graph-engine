import pandas as pd
from pyvis.network import Network
import networkx as nx

def generate_interactive_graph(csv_path="expressions (2).csv"):
    print(f"Loading data from {csv_path}...")
    df = pd.read_csv(csv_path).fillna("")
    df.columns = df.columns.str.strip().str.lower()

    # Initialize Pyvis Network (Dark Mode looks highly academic/professional)
    net = Network(height="900px", width="100%", bgcolor="#222222", font_color="white", directed=True)
    net.force_atlas_2based(gravity=-50) # Gives the graph an organic, sprawling layout

    added_nodes = set()
    languages = ['darija', 'urdu', 'nepali', 'vietnamese']
    lang_colors = {'darija': '#e67e22', 'urdu': '#e74c3c', 'nepali': '#9b59b6', 'vietnamese': '#f1c40f'}

    print("Building nodes and edges...")

    for index, row in df.iterrows():
        cat = row['category']
        trigger = row['trigger_event']
        temporal = row['temporal_position']

        # 1. The T-Box: Macro Category Nodes (Blue)
        if cat and cat not in added_nodes:
            net.add_node(cat, label=cat, color="#3498db", size=35, title="Macro Category (T-Box)")
            added_nodes.add(cat)

        # 2. The T-Box: Micro Trigger Nodes (Green)
        if trigger and trigger not in added_nodes:
            # Hovering over this shows the generic global scenario
            net.add_node(trigger, label=trigger, color="#2ecc71", size=25, title=f"Global Scenario:\n{row['scenarios']}")
            added_nodes.add(trigger)
            # Edge linking Category -> Trigger (Labeled with temporal position)
            net.add_edge(cat, trigger, label=temporal, color="#7f8c8d")

        # 3. The A-Box: Language Expression Nodes
        for lang in languages:
            expr = row[lang].strip()
            if expr:
                # Use a unique ID to handle polyfunctional words (like L7amdullah appearing multiple times)
                node_id = f"{expr}_{lang}_{index}"
                scenario_override = row.get(f"{lang}_scenario", "").strip()
                
                # Build the hover-tooltip data
                tooltip = f"Language: {lang.capitalize()}\nLiteral: {row['literal_translation']}"
                
                # 4. The Axiom Override (Highlighting asymmetric nuances)
                if scenario_override:
                    tooltip += f"\n\n🚨 AXIOM OVERRIDE:\n{scenario_override}"
                    edge_color = "#e74c3c" # Red edge means it breaks the generic rule
                else:
                    edge_color = "#95a5a6" # Grey edge means it perfectly aligns with the generic rule

                # Add Expression Node
                net.add_node(node_id, label=f"{expr}\n({lang[:3].upper()})", color=lang_colors[lang], size=15, title=tooltip)
                
                # Connect Trigger -> Expression
                net.add_edge(trigger, node_id, color=edge_color)

    # Save and output the interactive HTML file
    output_file = "pragmatic_knowledge_graph.html"
    net.write_html(output_file)
    print(f"\n✅ Success! Graph generated.")
    print(f"Open '{output_file}' in your web browser to interact with it.")

if __name__ == "__main__":
    generate_interactive_graph()