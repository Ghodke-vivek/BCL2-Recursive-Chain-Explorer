import networkx as nx

# =========================================================
# FEEDBACK DETECTOR
# =========================================================

class FeedbackDetector:

    def __init__(self, edges_df):

        self.edges_df = edges_df

        self.graph = self._build_graph()

    # =====================================================
    # BUILD NETWORKX GRAPH
    # =====================================================

    def _build_graph(self):

        G = nx.DiGraph()

        for _, row in self.edges_df.iterrows():

            source = str(
                row["Source_NodeID"]
            )

            target = str(
                row["Target_NodeID"]
            )

            G.add_edge(
                source,
                target
            )

        return G

    # =====================================================
    # DETECT FEEDBACK LOOPS
    # =====================================================

    def detect_feedback_loops(
        self,
        seed_node
    ):

        feedback_paths = []

        for node in self.graph.nodes:

            if node == seed_node:
                continue

            try:

                path = nx.shortest_path(

                    self.graph,

                    source=node,

                    target=seed_node
                )

                if len(path) > 1:

                    feedback_paths.append(

                        {
                            "source": node,

                            "target": seed_node,

                            "path": path,

                            "length": len(path)
                        }
                    )

            except nx.NetworkXNoPath:

                continue

            except nx.NodeNotFound:

                continue

        return feedback_paths
