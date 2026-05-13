from streamlit_agraph import agraph

# =========================================================
# GRAPH RENDERER
# =========================================================

def render_graph(nodes, edges, config):

    selected_node = agraph(
        nodes=nodes,
        edges=edges,
        config=config
    )

    # ensure string output
    if selected_node is not None:
        selected_node = str(selected_node)

    return selected_node
