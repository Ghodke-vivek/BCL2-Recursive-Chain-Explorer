import pandas as pd
import pickle

from pathlib import Path
from collections import defaultdict

# =========================================================
# DIRECTORIES
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = (
    ROOT_DIR / "data" / "processed"
)

CACHE_DIR = (
    ROOT_DIR / "cache"
)

CACHE_DIR.mkdir(
    exist_ok=True
)

# =========================================================
# FILES
# =========================================================

EDGES_FILE = (
    PROCESSED_DIR / "edges.parquet"
)

OUTPUT_FILE = (
    CACHE_DIR / "graph_index.pkl"
)

# =========================================================
# LOAD EDGES
# =========================================================

print("\nLoading edges parquet...\n")

edges_df = pd.read_parquet(
    EDGES_FILE
)

# =========================================================
# BUILD GRAPH INDEX
# =========================================================

graph_index = defaultdict(list)

for _, row in edges_df.iterrows():

    source = str(
        row["Source"]
    )

    target = str(
        row["Target"]
    )

    interaction = str(
        row.get(
            "Interaction",
            ""
        )
    )

    pathway = str(
        row.get(
            "Pathway",
            ""
        )
    )

    graph_index[source].append(

        {
            "target": target,

            "interaction": interaction,

            "pathway": pathway
        }
    )

# =========================================================
# SAVE INDEX
# =========================================================

with open(
    OUTPUT_FILE,
    "wb"
) as f:

    pickle.dump(
        dict(graph_index),
        f
    )

# =========================================================
# SUMMARY
# =========================================================

print("====================================")
print("GRAPH INDEX GENERATED")
print("====================================")

print(f"\nNodes Indexed: {len(graph_index)}")

print(f"\nSaved To:\n{OUTPUT_FILE}")

print("\n====================================")
