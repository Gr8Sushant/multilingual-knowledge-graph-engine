import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def build_and_visualize_graph(csv_path):
    print("Loading Data for Visualization...")
    # Load the data as before
    df = pd.read_csv(csv_path)
    # Clean the data as before
    df.columns = df.columns.str.strip().str.lower()
    df = df.rename(columns={'expression': 'darija'})
    df = df.fillna("")

    # --- SIMPLIFICATION STEP ---
    # Select exactly 4 key expressions to visualize
    # Make sure these are lowercase and exist in your CSV
    expressions_to_keep = ['bismillah', 'l7amdullah', 'inshallah', 'tbark llah']
    
    # Filter the DataFrame to keep only rows with these four expressions
    df = df[df['darija'].str.lower().isin(expressions_to_keep)]
    print(f"Graph simplified: now visualizing {len(df)} specific expressions.")
    # ---------------------------

    # Create a new Graph
    G = nx.Graph()

    # This part remains the same, but iterates only over the 4 filtered rows
    node_colors = []
    
    # 1. Add Category Nodes (The Hubs)
    categories = df['category'].unique()
    for cat in categories:
        if cat:  # Avoid empty categories
            G.add_node(cat, type='category')

    # 2. Add Situation Nodes and Edges
    for index, row in df.iterrows():
        category = row['category']
        situation = f"SIT_{index}: {row['correct_cultural_scenario'][:30]}..." # Truncate for readability
        darija_exp = row.get('darija', '')
        urdu_exp = row.get('urdu', '')

        if category:
            # Add Situation Node
            G.add_node(situation, type='situation')
            # Connect Situation to Category
            G.add_edge(category, situation)

            # 3. Add Expression Nodes (The Leaves)
            if darija_exp:
                exp_node = f"Darija: {darija_exp}"
                G.add_node(exp_node, type='expression')
                G.add_edge(situation, exp_node)
            
            if urdu_exp:
                exp_node = f"Urdu: {urdu_exp}"
                G.add_node(exp_node, type='expression')
                G.add_edge(situation, exp_node)

    # Assign colors based on node type
    for node, data in G.nodes(data=True):
        if data.get('type') == 'category':
            node_colors.append('skyblue')
        elif data.get('type') == 'situation':
            node_colors.append('lightgreen')
        elif data.get('type') == 'expression':
            node_colors.append('salmon')
        else:
            node_colors.append('gray')

    # Draw the Graph
    plt.figure(figsize=(16, 10))
    plt.title("Expression Master: Ontology Graph Visualization (Simplified)", fontsize=16, fontweight='bold')
    
    # Use a spring layout for an organic look
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    
    nx.draw(G, pos, 
            with_labels=True, 
            node_color=node_colors, 
            node_size=3000, 
            font_size=8, 
            font_weight='bold', 
            edge_color='gray', 
            width=1.5,
            edgecolors='black')

    # Create a custom legend
    import matplotlib.patches as mpatches
    cat_patch = mpatches.Patch(color='skyblue', label='Category (e.g., Food)')
    sit_patch = mpatches.Patch(color='lightgreen', label='Situation (e.g., Before Eating)')
    exp_patch = mpatches.Patch(color='salmon', label='Expression (e.g., Bismillah)')
    plt.legend(handles=[cat_patch, sit_patch, exp_patch], loc='upper right')

    print("Rendering Graph... Close the window to exit.")
    plt.show()

if __name__ == "__main__":
    build_and_visualize_graph("expressions.csv")

