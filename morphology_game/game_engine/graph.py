import graphviz

def generate_darija_graph():
    # Initialize a left-to-right directed graph
    fsa = graphviz.Digraph('Darija_FSA', filename='darija_fsa', format='png')
    
    # Set graph attributes for a clean, presentation-ready look
    fsa.attr(rankdir='LR', size='12,6', fontname='Helvetica')
    fsa.attr('node', shape='circle', style='filled', color='lightblue', fontname='Helvetica', fontcolor='black')
    fsa.attr('edge', fontname='Helvetica', fontsize='10')

    # Define the States (Nodes)
    fsa.node('Start', shape='doublecircle', color='lightgreen')
    fsa.node('Tense', label='Tense\nSlot')
    fsa.node('Prefix', label='Prefix\nSlot')
    fsa.node('Root', label='Root\nSlot', color='gold') # Highlight the root verb slot
    fsa.node('Suffix', label='Suffix\nSlot')
    fsa.node('End', shape='doublecircle', color='lightgreen', label='Conjugated\nWord')

    # 1. Start to Tense
    fsa.edge('Start', 'Tense')

    # 2. Tense to Prefix (From tense_markers in JSON)
    fsa.edge('Tense', 'Prefix', label='ka (Present)')
    fsa.edge('Tense', 'Prefix', label='ghadi (Future)')

    # 3. Prefix to Root (From pronouns prefix in JSON)
    fsa.edge('Prefix', 'Root', label='n- (ana / 7na)')
    fsa.edge('Prefix', 'Root', label='t- (nta / nti / hiya / ntuma)')
    fsa.edge('Prefix', 'Root', label='y- (huwa / huma)')

    # 4. Root to Suffix (The Lexicon Injection)
    fsa.edge('Root', 'Suffix', label='[UKC Verb Lemma]\ne.g., kla, shreb')

    # 5. Suffix to End (From pronouns suffix in JSON)
    fsa.edge('Suffix', 'End', label='-∅ / Empty (ana / nta / huwa / hiya)')
    fsa.edge('Suffix', 'End', label='-i (nti)')
    fsa.edge('Suffix', 'End', label='-u (7na / ntuma / huma)')

    # Render the graph
    fsa.render(cleanup=True)
    print("Success! The FSA graph has been generated as 'darija_fsa.png'")

if __name__ == "__main__":
    generate_darija_graph()