from collections import defaultdict

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

        edges_df,

        node_index,

        chains
    ):

        self.edges_df = edges_df

        self.node_index = node_index

        self.chains = chains

        self.edge_lookup = self._build_edge_lookup()

    # =====================================================
    # BUILD EDGE LOOKUP
    # =====================================================

    def _build_edge_lookup(self):

        lookup = defaultdict(list)

        for _, row in self.edges_df.iterrows():

            source = str(
                row["Source"]
            )

            target = str(
                row["Target"]
            )

            lookup[source].append(row)

            lookup[target].append(row)

        return lookup

    # =====================================================
    # EXPAND NODE
    # =====================================================

    def expand_node(

        self,

        node_id,

        max_depth=3,

        allowed_pathways=None
    ):

        visited = set()

        visual_nodes = []

        visual_edges = []

        added_nodes = set()

        # =================================================
        # DFS RECURSION
        # =================================================

        def dfs(

            current_node,

            depth
        ):

            if depth > max_depth:

                return

            if current_node in visited:

                return

            visited.add(current_node)

            connected_edges = self.edge_lookup.get(

                current_node,

                []
            )

            for row in connected_edges:

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

                # =========================================
                # PATHWAY FILTER
                # =========================================

                if (
                    allowed_pathways
                    and pathway not in allowed_pathways
                ):

                    continue

                # =========================================
                # NODE COLOR
                # =========================================

                color = "#4CAF50"

                if source == node_id:

                    color = "#FF4B4B"

                # =========================================
                # SOURCE NODE
                # =========================================

                if source not in added_nodes:

                    visual_nodes.append(

                        Node(

                            id=source,

                            label=source,

                            size=20,

                            color=color
                        )
                    )

                    added_nodes.add(source)

                # =========================================
                # TARGET NODE
                # =========================================

                if target not in added_nodes:

                    visual_nodes.append(

                        Node(

                            id=target,

                            label=target,

                            size=20,

                            color="#2196F3"
                        )
                    )

                    added_nodes.add(target)

                # =========================================
                # EDGE
                # =========================================

                visual_edges.append(

                    Edge(

                        source=source,

                        target=target,

                        label=interaction,

                        color="#999999"
                    )
                )

                # =========================================
                # RECURSIVE EXPANSION
                # =========================================

                if source != current_node:

                    dfs(
                        source,
                        depth + 1
                    )

                if target != current_node:

                    dfs(
                        target,
                        depth + 1
                    )

        # =================================================
        # START DFS
        # =================================================

        dfs(
            node_id,
            0
        )

        return visual_nodes, visual_edges
