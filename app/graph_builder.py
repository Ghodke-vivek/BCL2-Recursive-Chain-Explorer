import networkx as nx

from streamlit_agraph import (
    Node,
    Edge
)

from pathway_manager import (
    PathwayColorManager
)

# =========================================================
# GRAPH BUILDER
# =========================================================

class GraphBuilder:

    def __init__(

        self,

        nodes_df,

        edges_df,

        pathway_manager
    ):

        self.nodes_df = nodes_df

        self.edges_df = edges_df

        self.pathway_manager = pathway_manager

        self.graph = self._build_networkx_graph()

    # =====================================================
    # BUILD NETWORKX GRAPH
    # =====================================================

    def _build_networkx_graph(self):

        G = nx.DiGraph()

        for _, row in self.edges_df.iterrows():

            source = str(
                row["Source"]
            )

            target = str(
                row["Target"]
            )

            pathway = str(
                row.get("Pathway", "")
            )

            interaction = str(
                row.get("Interaction", "")
            )

            relation_id = str(
                row.get("RelationID", "")
            )

            G.add_node(source)

            G.add_node(target)

            G.add_edge(

                source,

                target,

                pathway=pathway,

                interaction=interaction,

                relation_id=relation_id
            )

        return G

    # =====================================================
    # BUILD VISUAL GRAPH
    # =====================================================

    def build_visual_graph(

        self,

        selected_pathways=None
    ):

        nodes = []

        edges = []

        added_nodes = set()

        for _, row in self.edges_df.iterrows():

            pathway = str(
                row.get("Pathway", "")
            )

            if (
                selected_pathways
                and pathway not in selected_pathways
            ):

                continue

            source = str(
                row["Source"]
            )

            target = str(
                row["Target"]
            )

            interaction = str(
                row.get("Interaction", "")
            )

            color = self.pathway_manager.get_color(
                pathway
            )

            # =============================================
            # SOURCE NODE
            # =============================================

            if source not in added_nodes:

                nodes.append(

                    Node(

                        id=source,

                        label=source,

                        size=20,

                        color=color
                    )
                )

                added_nodes.add(source)

            # =============================================
            # TARGET NODE
            # =============================================

            if target not in added_nodes:

                nodes.append(

                    Node(

                        id=target,

                        label=target,

                        size=20,

                        color=color
                    )
                )

                added_nodes.add(target)

            # =============================================
            # EDGE
            # =============================================

            edges.append(

                Edge(

                    source=source,

                    target=target,

                    label=interaction,

                    color=color
                )
            )

        return nodes, edges
