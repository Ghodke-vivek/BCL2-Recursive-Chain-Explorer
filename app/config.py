from pathlib import Path

# =========================================================
# ROOT
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

# =========================================================
# DATA DIRECTORIES
# =========================================================

DATA_DIR = ROOT_DIR / "data"

SEED_DIR = DATA_DIR / "seed_network"

CHAIN_DIR = DATA_DIR / "expanded_chains"

METADATA_DIR = DATA_DIR / "metadata"

PROCESSED_DIR = DATA_DIR / "processed"

CACHE_DIR = ROOT_DIR / "cache"

# =========================================================
# SEED FILE
# =========================================================

SEED_FILE = (
    SEED_DIR
    / "BCL2_UPSTREAM_Neurotrophin_signaling_pathway.xlsx"
)

# =========================================================
# PROCESSED GRAPH FILES
# =========================================================

NODES_FILE = (
    PROCESSED_DIR
    / "nodes.parquet"
)

EDGES_FILE = (
    PROCESSED_DIR
    / "edges.parquet"
)

CHAINS_FILE = (
    PROCESSED_DIR
    / "all_chains.pkl.gz"
)

NODE_INDEX_FILE = (
    PROCESSED_DIR
    / "node_index.pkl"
)

PATHWAY_INDEX_FILE = (
    PROCESSED_DIR
    / "pathway_index.pkl"
)

# =========================================================
# ASSETS
# =========================================================

ASSETS_DIR = ROOT_DIR / "app" / "assets"

CSS_FILE = (
    ASSETS_DIR
    / "custom.css"
)

PATHWAY_COLOR_FILE = (
    ASSETS_DIR
    / "pathway_colors.json"
)

# =========================================================
# CORE SETTINGS
# =========================================================

BCL2_NODE_ID = "N00142"

APP_TITLE = (
    "BCL2 Recursive Chain Explorer"
)

LAYOUT_DIRECTION = "LR"

MAX_EXPANSION_DEPTH = 10
