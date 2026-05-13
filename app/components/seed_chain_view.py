from streamlit_agraph import Node, Edge

# =========================================================
# BUILD SEED CHAIN
# =========================================================

def build_seed_chain(seed_df, pathway_manager):

    nodes = []
    edges = []
    added_nodes = set()

    for _, row in seed_df.iterrows():

        source = str(row["Source_NodeID"])
        target = str(row["Target_NodeID"])
        pathway = str(row.get("Pathway_Name", ""))

        color = pathway_manager.get_color(pathway)

        if source not in added_nodes:
            nodes.append(
                Node(id=source, label=source, size=32, color=color)
            )
            added_nodes.add(source)

        if target not in added_nodes:
            nodes.append(
                Node(id=target, label=target, size=32, color=color)
            )
            added_nodes.add(target)

        # 🔴 EDGE WITHOUT LABEL
        edges.append(
            Edge(
                source=source,
                target=target,
                label="",   # CLEAN GRAPH
                color=color
            )
        )

    return nodes, edges
