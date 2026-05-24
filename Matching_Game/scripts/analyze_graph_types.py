import networkx as nx
import os
import argparse

def analyze_graph(filepath):
    print(f"Loading graph from {filepath}...\n")
    try:
        G = nx.read_graphml(filepath)
    except Exception as e:
        print(f"Error loading graph: {e}")
        return

    node_types = set()
    edge_types = set()
    
    node_attributes = set()
    edge_attributes = set()
    
    weight_types = set()
    
    # Analyze nodes
    for _, data in G.nodes(data=True):
        node_attributes.update(data.keys())
        if 'type' in data:
            node_types.add(data['type'])
        elif 'node_type' in data:
            node_types.add(data['node_type'])
        elif 'label' in data and type(data['label']) == str and data['label'].isupper(): # sometimes labels are types
             pass
            
    # Analyze edges
    for u, v, data in G.edges(data=True):
        edge_attributes.update(data.keys())
        if 'type' in data:
            edge_types.add(data['type'])
        elif 'relation' in data:
            edge_types.add(data['relation'])
        elif 'edge_type' in data:
            edge_types.add(data['edge_type'])
        elif 'label' in data:
            edge_types.add(data['label'])
            
        # Collect weight keys
        for key in data.keys():
            if 'weight' in key.lower() or 'score' in key.lower() or 'similarity' in key.lower() or 'distance' in key.lower():
                weight_types.add(key)
                
    print("=== Graph Summary ===")
    print(f"Total Nodes: {G.number_of_nodes()}")
    print(f"Total Edges: {G.number_of_edges()}")
    
    print("\n=== Node Types Found ===")
    if node_types:
        for nt in sorted(node_types):
            print(f"  - {nt}")
    else:
        print("  (No explicit 'type' or 'node_type' attribute found on nodes)")
        print(f"  Available node attributes: {', '.join(sorted(node_attributes))}")
        
    print("\n=== Edge Types (Relations) Found ===")
    if edge_types:
        for et in sorted(edge_types):
            print(f"  - {et}")
    else:
        print("  (No explicit 'type', 'relation', or 'label' attribute found on edges)")
        print(f"  Available edge attributes: {', '.join(sorted(edge_attributes))}")
        
    print("\n=== Edge Weight Attributes Found ===")
    if weight_types:
        for wt in sorted(weight_types):
            print(f"  - {wt}")
    else:
        print("  (No explicit weight/score attributes found)")
        print(f"  Available edge attributes: {', '.join(sorted(edge_attributes))}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a GraphML file for node/edge types.")
    parser.add_argument("filepath", nargs="?", default=None, help="Path to GraphML file")
    
    args = parser.parse_args()
    
    if args.filepath:
        filepath = args.filepath
    else:
        # Default path relative to this script
        filepath = os.path.join(os.path.dirname(__file__), "..", "artifacts", "graph_phase3_semantics.graphml")
        
    analyze_graph(filepath)
