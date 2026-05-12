import networkx as nx

from streamlit_agraph import (
    Node,
    Edge
)

from app.pathway_manager import (
    PathwayColorManager
)


def build_graph(df):

    G = nx.DiGraph()

    for _, row in df.iterrows():

        source = str(row["Source_NodeID"])
        target = str(row["Target_NodeID"])

        G.add_node(source)
        G.add_node(target)

        G.add_edge(
            source,
            target,
            relation_id=row.get("RelationID", ""),
            interaction=row.get("Interaction", ""),
            pathway=row.get("Pathway_ID", ""),
            pathway_name=row.get("Pathway_Name", ""),
        )

    return G
