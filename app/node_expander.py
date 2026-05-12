from app.graph_loader import (
    load_all_graph_data
)

def get_connected_nodes(G, node_id):

    incoming = list(G.predecessors(node_id))
    outgoing = list(G.successors(node_id))

    return {
        "incoming": incoming,
        "outgoing": outgoing,
    }
