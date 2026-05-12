import pandas as pd
import pickle
import gzip

from app.config import (
    PROCESSED_DIR
)

# =========================================================
# FILE PATHS
# =========================================================

NODES_FILE = (
    PROCESSED_DIR / "nodes.parquet"
)

EDGES_FILE = (
    PROCESSED_DIR / "edges.parquet"
)

CHAINS_FILE = (
    PROCESSED_DIR / "all_chains.pkl.gz"
)

NODE_INDEX_FILE = (
    PROCESSED_DIR / "node_index.pkl"
)

PATHWAY_INDEX_FILE = (
    PROCESSED_DIR / "pathway_index.pkl"
)

# =========================================================
# LOAD NODES
# =========================================================

def load_nodes():

    print("Loading nodes...")

    return pd.read_parquet(
        NODES_FILE
    )

# =========================================================
# LOAD EDGES
# =========================================================

def load_edges():

    print("Loading edges...")

    return pd.read_parquet(
        EDGES_FILE
    )

# =========================================================
# LOAD CHAINS
# =========================================================

def load_chains():

    print("Loading chains...")

    with gzip.open(
        CHAINS_FILE,
        "rb"
    ) as f:

        chains = pickle.load(f)

    return chains

# =========================================================
# LOAD NODE INDEX
# =========================================================

def load_node_index():

    print("Loading node index...")

    with open(
        NODE_INDEX_FILE,
        "rb"
    ) as f:

        node_index = pickle.load(f)

    return node_index

# =========================================================
# LOAD PATHWAY INDEX
# =========================================================

def load_pathway_index():

    print("Loading pathway index...")

    with open(
        PATHWAY_INDEX_FILE,
        "rb"
    ) as f:

        pathway_index = pickle.load(f)

    return pathway_index

# =========================================================
# LOAD EVERYTHING
# =========================================================

def load_all_graph_data():

    nodes_df = load_nodes()

    edges_df = load_edges()

    chains = load_chains()

    node_index = load_node_index()

    pathway_index = load_pathway_index()

    return {

        "nodes": nodes_df,

        "edges": edges_df,

        "chains": chains,

        "node_index": node_index,

        "pathway_index": pathway_index

    }
