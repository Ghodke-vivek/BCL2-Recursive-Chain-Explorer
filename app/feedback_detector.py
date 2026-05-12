import networkx as nx

def detect_feedback_paths(G, seed_nodes):

    feedback_edges = []

    for node in G.nodes:

        for seed_node in seed_nodes:

            if node == seed_node:
                continue

            try:

                path = nx.shortest_path(
                    G,
                    source=node,
                    target=seed_node,
                )

                if len(path) > 1:

                    feedback_edges.append(
                        {
                            "source": node,
                            "target": seed_node,
                            "path": path,
                        }
                    )

            except:
                pass

    return feedback_edges
