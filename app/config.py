from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"
SEED_DIR = DATA_DIR / "seed_network"
CHAIN_DIR = DATA_DIR / "expanded_chains"
METADATA_DIR = DATA_DIR / "metadata"
CACHE_DIR = ROOT_DIR / "cache"

SEED_FILE = SEED_DIR / "BCL2_UPSTREAM_Neurotrophin_signaling_pathway.xlsx"

BCL2_NODE_ID = "N00142"

APP_TITLE = "BCL2 Recursive Chain Explorer"

LAYOUT_DIRECTION = "LR"
