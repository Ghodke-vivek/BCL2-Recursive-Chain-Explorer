import networkx as nx

# =========================================================
# FEEDBACK DETECTOR
# =========================================================

class FeedbackDetector:

    def __init__(

        self,

        edges_df
    ):

        self.edges_df = edges_df

        self.graph = self._build_graph()

    # =====================================================
    # BUILD GRAPH
    # =====================================================

    def _build_graph(self):

        G = nx.DiGraph()

        for _, row in self.edges_df.iterrows():

            source = str(
                row["Source"]
            )

            target = str(
                row["Target"]
            )

            pathway = str(
                row.get(
                    "Pathway",
                    ""
                )
            )

            interaction = str(
                row.get(
                    "Interaction",
                    ""
                )
            )

            G.add_edge(

                source,

                target,

                pathway=pathway,

                interaction=interaction
            )

        return G

    # =====================================================
    # DETECT FEEDBACK LOOPS
    # =====================================================

    def detect_feedback_loops(

        self,

        selected_seed_node
    ):

        feedback_paths = []

        for node in self.graph.nodes():

            if node == selected_seed_node:
                continue

            try:

                if nx.has_path(

                    self.graph,

                    node,

                    selected_seed_node
                ):

                    path = nx.shortest_path(

                        self.graph,

                        source=node,

                        target=selected_seed_node
                    )

                    if len(path) > 1:

                        feedback_paths.append(

                            {
                                "source": node,

                                "target": selected_seed_node,

                                "path": path,

                                "length": len(path)
                            }
                        )

            except Exception:

                continue

        return feedback_paths
