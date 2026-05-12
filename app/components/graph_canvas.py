from streamlit_agraph import agraph


def render_graph(nodes, edges, config):

    return agraph(
        nodes=nodes,
        edges=edges,
        config=config
    )
