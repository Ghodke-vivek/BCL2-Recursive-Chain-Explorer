import streamlit as st

from styles import PAGE_STYLE

from graph_loader import load_chain_files
from graph_builder import GraphBuilder
from pathway_manager import PathwayColorManager
from feedback_detector import FeedbackDetector
from node_expander import NodeExpander
from layout_manager import get_graph_config

from components.graph_canvas import render_graph
from components.seed_chain_view import build_seed_chain
from components.feedback_panel import render_feedback_panel
from components.node_panel import render_node_panel
from components.pathway_legend import render_pathway_legend

from utils import load_excel
from config import SEED_FILE

from streamlit_agraph import Node, Edge

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="BCL2 Recursive Chain Explorer",
    layout="wide"
)

st.markdown(PAGE_STYLE, unsafe_allow_html=True)

st.title("BCL2 Recursive Chain Explorer")

# =========================================================
# LOAD SEED NETWORK
# =========================================================

seed_df = load_excel(SEED_FILE)

seed_nodes, seed_edges = build_seed_chain(seed_df)

# =========================================================
# LOAD ALL CHAIN FILES
# =========================================================

chain_dataframes = load_chain_files()

# =========================================================
# BUILD GRAPH
# =========================================================

builder = GraphBuilder()

for df in chain_dataframes:
    builder.add_dataframe(df)

G = builder.get_graph()

# =========================================================
# MANAGERS
# =========================================================

color_manager = PathwayColorManager()

seed_node_ids = set(seed_df["Source_NodeID"])
seed_node_ids.update(seed_df["Target_NodeID"])

feedback_detector = FeedbackDetector(
    G,
    seed_node_ids
)

node_expander = NodeExpander(G)

# =========================================================
# GRAPH OBJECTS
# =========================================================

nodes = seed_nodes.copy()
edges = seed_edges.copy()

# =========================================================
# USER INTERACTION
# =========================================================

selected_node = render_graph(
    nodes,
    edges,
    get_graph_config()
)

# =========================================================
# NODE EXPANSION
# =========================================================

if selected_node:

    st.sidebar.success(f"Selected Node: {selected_node}")

    connected = node_expander.get_connected_nodes(
        selected_node
    )

    render_node_panel(connected)

    feedback_paths = feedback_detector.find_feedback_paths(
        selected_node
    )

    render_feedback_panel(feedback_paths)

    additional_nodes = []
    additional_edges = []

    # -----------------------------------------------------
    # Incoming Nodes
    # -----------------------------------------------------

    for node in connected["incoming"]:

        additional_nodes.append(
            Node(
                id=node,
                label=node,
                size=25,
                color="#00c853"
            )
        )

        additional_edges.append(
            Edge(
                source=node,
                target=selected_node,
                color="#00c853"
            )
        )
    # -----------------------------------------------------
    # Outgoing Nodes
    # -----------------------------------------------------

    for node in connected["outgoing"]:


        additional_nodes.append(
            Node(
                id=node,
                label=node,
                size=25,
                color="#ff9800"
            )
        )

        additional_edges.append(
            Edge(
                source=selected_node,
                target=node,
                color="#ff9800"
            )
        )

    nodes.extend(additional_nodes)
    edges.extend(additional_edges)

    render_graph(
        nodes,
        edges,
        get_graph_config()
    )

  
