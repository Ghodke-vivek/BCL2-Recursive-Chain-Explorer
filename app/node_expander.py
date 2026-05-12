from streamlit_agraph import (
    Node,
    Edge
)

# =========================================================
# NODE EXPANDER
# =========================================================

class NodeExpander:

    def __init__(

        self,

        graph_index,

        node_index
    ):

        self.graph_index = graph_index

        self.node_index = node_index

    # =====================================================
    # EXPAND SINGLE NODE
    # =====================================================

    def expand_node(

        self,

        node_id,

        allowed_pathways=None
    ):

        visual_nodes = []

        visual_edges = []

        added_nodes = set()

        # =================================================
        # FETCH DIRECT NEIGHBORS
        # =================================================

        connected_edges = self.graph_index.get(

            node_id,

            []
        )

        # =================================================
        # PROCESS NEIGHBORS
        # =================================================

        for edge_data in connected_edges:

            source = str(node_id)

            target = str(

                edge_data.get(
                    "target",
                    ""
                )
            )

            interaction = str(

                edge_data.get(
                    "interaction",
                    ""
                )
            )

            pathway = str(

                edge_data.get(
                    "pathway",
                    ""
                )
            )

            # =============================================
            # PATHWAY FILTER
            # =============================================

            if (

                allowed_pathways

                and pathway not in allowed_pathways
            ):

                continue

            # =============================================
            # SOURCE NODE
            # =============================================

            if source not in added_nodes:

                visual_nodes.append(

                    Node(

                        id=source,

                        label=source,

                        size=30,

                        color="#FF4B4B"
                    )
                )

                added_nodes.add(source)

            # =============================================
            # TARGET NODE
            # =============================================

            if target not in added_nodes:

                visual_nodes.append(

                    Node(

                        id=target,

                        label=target,

                        size=22,

                        color="#4CAF50"
                    )
                )

                added_nodes.add(target)

            # =============================================
            # EDGE
            # =============================================

            visual_edges.append(

                Edge(

                    source=source,

                    target=target,

                    color="#999999"
                )
            )

        return visual_nodes, visual_edges
