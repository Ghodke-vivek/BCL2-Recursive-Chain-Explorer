import streamlit as st

from styles import PAGE_STYLE

from graph_loader import (
    load_all_graph_data
)

from pathway_manager import (
    PathwayColorManager
)

from feedback_detector import (
    FeedbackDetector
)

from node_expander import (
    NodeExpander
)

from layout_manager import (
    get_graph_config
)

from components.graph_canvas import (
    render_graph
)

from components.seed_chain_view import (
    build_seed_chain
)

from components.feedback_panel import (
    render_feedback_panel
)

from components.node_panel import (
    render_node_panel
)

from components.pathway_legend import (
    render_pathway_legend
)

from utils import (
    load_excel
)

from config import (
    SEED_FILE
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="BCL2 Recursive Chain Explorer",

    layout="wide",

    initial_sidebar_state="expanded"
)

# =========================================================
# APPLY CSS
# =========================================================

st.markdown(
    PAGE_STYLE,
    unsafe_allow_html=True
)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data(show_spinner=True)

def cached_graph_data():

    return load_all_graph_data()

graph_data = cached_graph_data()

nodes_df = graph_data["nodes"]

edges_df = graph_data["edges"]

all_chains = graph_data["chains"]

node_index = graph_data["node_index"]

pathway_index = graph_data["pathway_index"]

# =========================================================
# LOAD SEED NETWORK
# =========================================================

seed_df = load_excel(
    SEED_FILE
)

# =========================================================
# PATHWAY COLORS
# =========================================================

pathway_manager = PathwayColorManager()

# =========================================================
# FEEDBACK DETECTOR
# =========================================================

feedback_detector = FeedbackDetector(
    edges_df=edges_df
)

# =========================================================
# NODE EXPANDER
# =========================================================

node_expander = NodeExpander(

    edges_df=edges_df,

    node_index=node_index,

    chains=all_chains
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title(
    "BCL2 Recursive Explorer"
)

st.sidebar.markdown("---")

# =========================================================
# SEED NODES
# =========================================================

seed_nodes = sorted(

    set(
        seed_df["Source_NodeID"]
    ).union(

        set(
            seed_df["Target_NodeID"]
        )
    )
)

selected_seed_node = st.sidebar.selectbox(

    "Select Seed Chain Node",

    seed_nodes
)

# =========================================================
# EXPANSION DEPTH
# =========================================================

max_depth = st.sidebar.slider(

    "Expansion Depth",

    min_value=1,

    max_value=10,

    value=3
)

# =========================================================
# FEEDBACK TOGGLE
# =========================================================

show_feedback = st.sidebar.checkbox(

    "Enable Feedback Loop Detection",

    value=True
)

# =========================================================
# PATHWAY FILTER
# =========================================================

available_pathways = sorted(

    edges_df["Pathway"]
    .dropna()
    .unique()
)

selected_pathways = st.sidebar.multiselect(

    "Filter Pathways",

    available_pathways,

    default=available_pathways
)

# =========================================================
# TITLE
# =========================================================

st.title(
    "BCL2 Recursive Chain Network Explorer"
)

st.markdown(
    """
    Interactive visualization of recursive pathway expansion,
    seed-chain branching, and feedback loop architecture.
    """
)

# =========================================================
# BUILD SEED CHAIN
# =========================================================

seed_nodes_graph, seed_edges_graph = build_seed_chain(

    seed_df=seed_df,

    pathway_manager=pathway_manager
)

# =========================================================
# NODE EXPANSION
# =========================================================

expanded_nodes, expanded_edges = node_expander.expand_node(

    selected_seed_node,

    max_depth=max_depth,

    allowed_pathways=selected_pathways
)

# =========================================================
# MERGE ALL NODES + EDGES
# =========================================================

all_nodes = (
    seed_nodes_graph
    + expanded_nodes
)

all_edges = (
    seed_edges_graph
    + expanded_edges
)

# =========================================================
# REMOVE DUPLICATE NODES
# =========================================================

unique_nodes = {}

for node in all_nodes:

    unique_nodes[node.id] = node

all_nodes = list(
    unique_nodes.values()
)

# =========================================================
# REMOVE DUPLICATE EDGES
# =========================================================

unique_edges = {}

for edge in all_edges:

    edge_key = (

        edge.source,

        edge.target,

        edge.label
    )

    unique_edges[edge_key] = edge

all_edges = list(
    unique_edges.values()
)

# =========================================================
# FEEDBACK DETECTION
# =========================================================

feedback_paths = []

if show_feedback:

    feedback_paths = (

        feedback_detector
        .detect_feedback_loops(

            selected_seed_node
        )
    )

# =========================================================
# GRAPH CONFIG
# =========================================================

graph_config = get_graph_config()

# =========================================================
# MAIN LAYOUT
# =========================================================

left_col, right_col = st.columns(
    [4, 1]
)

# =========================================================
# GRAPH PANEL
# =========================================================

with left_col:

    st.subheader(
        "Recursive Network Graph"
    )

    render_graph(

        nodes=all_nodes,

        edges=all_edges,

        config=graph_config
    )

# =========================================================
# RIGHT PANEL
# =========================================================

with right_col:

    st.subheader(
        "Node Information"
    )

    render_node_panel(

        selected_seed_node,

        node_index
    )

    st.markdown("---")

    st.subheader(
        "Pathway Legend"
    )

    render_pathway_legend(
        pathway_manager
    )

    st.markdown("---")

    if show_feedback:

        st.subheader(
            "Feedback Loops"
        )

        render_feedback_panel(
            feedback_paths
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(

    "BCL2 Recursive Chain Explorer | "
    "Pathway-Specific Recursive "
    "Network Visualization"
)
