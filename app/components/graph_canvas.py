from streamlit_agraph import agraph

# =========================================================
# GRAPH RENDERER
# =========================================================

def render_graph(

    nodes,

    edges,

    config
):

    selected_node = agraph(

        nodes=nodes,

        edges=edges,

        config=config
    )

    return selected_node
