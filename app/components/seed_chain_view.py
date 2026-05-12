from streamlit_agraph import (
    Node,
    Edge
)

# =========================================================
# BUILD SEED CHAIN
# =========================================================

def build_seed_chain(

    seed_df,

    pathway_manager
):

    nodes = []

    edges = []

    added_nodes = set()

    # =====================================================
    # BUILD GRAPH
    # =====================================================

    for _, row in seed_df.iterrows():

        source = str(
            row["Source_NodeID"]
        )

        target = str(
            row["Target_NodeID"]
        )

        interaction = str(
            row.get(
                "Interaction",
                ""
            )
        )

        pathway = str(
            row.get(
                "Pathway_Name",
                ""
            )
        )

        color = pathway_manager.get_color(
            pathway
        )

        # =================================================
        # SOURCE NODE
        # =================================================

        if source not in added_nodes:

            nodes.append(

                Node(

                    id=source,

                    label=source,

                    size=32,

                    color=color
                )
            )

            added_nodes.add(source)

        # =================================================
        # TARGET NODE
        # =================================================

        if target not in added_nodes:

            nodes.append(

                Node(

                    id=target,

                    label=target,

                    size=32,

                    color=color
                )
            )

            added_nodes.add(target)

        # =================================================
        # EDGE
        # =================================================

        edges.append(

            Edge(

                source=source,

                target=target,

                label=interaction,

                color=color
            )
        )

    return nodes, edges
