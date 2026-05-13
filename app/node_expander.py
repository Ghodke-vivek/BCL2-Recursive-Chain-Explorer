from collections import defaultdict
from streamlit_agraph import Node, Edge

# =========================================================
# NODE EXPANDER
# =========================================================

class NodeExpander:

    def __init__(self, edges_df, node_index, chains):

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

            source = str(row["Source"])
            target = str(row["Target"])

            lookup[source].append(row)
            lookup[target].append(row)

        return lookup

    # =====================================================
    # EXPAND NODE (CURRENT DFS VERSION)
    # =====================================================

    def expand_node(self, node_id, max_depth=2, allowed_pathways=None):

        visited = set()
        visual_nodes = []
        visual_edges = []
        added_nodes = set()

        def dfs(current_node, depth):

            if depth > max_depth:
                return

            if current_node in visited:
                return

            visited.add(current_node)

            for row in self.edge_lookup.get(current_node, []):

                source = str(row["Source"])
                target = str(row["Target"])
                pathway = str(row.get("Pathway", ""))

                if allowed_pathways and pathway not in allowed_pathways:
                    continue

                # NODE COLORS
                color_source = "#FF4B4B" if source == node_id else "#4CAF50"
                color_target = "#2196F3"

                if source not in added_nodes:
                    visual_nodes.append(
                        Node(id=source, label=source, size=20, color=color_source)
                    )
                    added_nodes.add(source)

                if target not in added_nodes:
                    visual_nodes.append(
                        Node(id=target, label=target, size=20, color=color_target)
                    )
                    added_nodes.add(target)

                # 🔴 EDGE WITHOUT LABEL
                visual_edges.append(
                    Edge(
                        source=source,
                        target=target,
                        label="",   # CLEAN GRAPH
                        color="#555555"
                    )
                )

                if source != current_node:
                    dfs(source, depth + 1)

                if target != current_node:
                    dfs(target, depth + 1)

        dfs(node_id, 0)

        return visual_nodes, visual_edges
