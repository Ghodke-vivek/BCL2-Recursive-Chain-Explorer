import pandas as pd
import pickle
import gzip

from pathlib import Path

# =========================================================
# INPUT DIRECTORY
# =========================================================

CHAIN_DIR = Path(
    r"G:\NETWORK_BCL2\1. Network Files\1. Network Files\Neurotrophin_Upstream_Expanded_Network_2"
)

# =========================================================
# OUTPUT DIRECTORY
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = (
    ROOT_DIR / "data" / "processed"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# =========================================================
# FILES
# =========================================================

NODES_FILE = (
    OUTPUT_DIR / "nodes.parquet"
)

EDGES_FILE = (
    OUTPUT_DIR / "edges.parquet"
)

CHAINS_FILE = (
    OUTPUT_DIR / "all_chains.pkl.gz"
)

NODE_INDEX_FILE = (
    OUTPUT_DIR / "node_index.pkl"
)

PATHWAY_INDEX_FILE = (
    OUTPUT_DIR / "pathway_index.pkl"
)

# =========================================================
# LOAD CHAIN FILES
# =========================================================

chain_files = sorted(
    CHAIN_DIR.glob("*.xlsx")
)

print("====================================")
print("BCL2 CHAIN PREPROCESSING")
print("====================================")

print(
    f"\nTotal chain files: "
    f"{len(chain_files)}"
)

# =========================================================
# STORAGE
# =========================================================

all_chains = {}

master_nodes = []

master_edges = []

# =========================================================
# PROCESS FILES
# =========================================================

for idx, file in enumerate(chain_files):

    try:

        df = pd.read_excel(
            file
        ).fillna("")

        chain_id = file.stem

        # ================================================
        # STORE CHAIN
        # ================================================

        all_chains[chain_id] = df.to_dict(
            orient="records"
        )

        # ================================================
        # PROCESS ROWS
        # ================================================

        for _, row in df.iterrows():

            source = str(
                row["Source_NodeID"]
            ).strip()

            target = str(
                row["Target_NodeID"]
            ).strip()

            pathway = str(
                row.get(
                    "Pathway_Name",
                    ""
                )
            ).strip()

            interaction = str(
                row.get(
                    "Interaction",
                    ""
                )
            ).strip()

            relation_id = str(
                row.get(
                    "RelationID",
                    ""
                )
            ).strip()

            # ============================================
            # SOURCE NODE
            # ============================================

            master_nodes.append(

                {
                    "NodeID": source,

                    "ChainID": chain_id,

                    "Pathway": pathway
                }
            )

            # ============================================
            # TARGET NODE
            # ============================================

            master_nodes.append(

                {
                    "NodeID": target,

                    "ChainID": chain_id,

                    "Pathway": pathway
                }
            )

            # ============================================
            # EDGE
            # ============================================

            master_edges.append(

                {
                    "Source": source,

                    "Target": target,

                    "ChainID": chain_id,

                    "Pathway": pathway,

                    "Interaction": interaction,

                    "RelationID": relation_id
                }
            )

        print(

            f"[{idx+1}/{len(chain_files)}] "

            f"Processed: {file.name}"
        )

    except Exception as e:

        print(
            f"\nERROR: {file.name}"
        )

        print(e)

# =========================================================
# DATAFRAMES
# =========================================================

print("\nBuilding dataframes...")

nodes_df = pd.DataFrame(
    master_nodes
).drop_duplicates()

edges_df = pd.DataFrame(
    master_edges
).drop_duplicates()

# =========================================================
# SAVE PARQUET
# =========================================================

print("\nSaving parquet files...")

nodes_df.to_parquet(
    NODES_FILE,
    index=False
)

edges_df.to_parquet(
    EDGES_FILE,
    index=False
)

# =========================================================
# SAVE COMPRESSED CHAINS
# =========================================================

print("\nCompressing chain database...")

with gzip.open(
    CHAINS_FILE,
    "wb"
) as f:

    pickle.dump(
        all_chains,
        f
    )

# =========================================================
# NODE INDEX
# =========================================================

print("\nBuilding node index...")

node_index = {}

for node in nodes_df["NodeID"].unique():

    subset = nodes_df[
        nodes_df["NodeID"] == node
    ]

    node_index[node] = sorted(

        subset["ChainID"]
        .unique()
    )

with open(
    NODE_INDEX_FILE,
    "wb"
) as f:

    pickle.dump(
        node_index,
        f
    )

# =========================================================
# PATHWAY INDEX
# =========================================================

print("\nBuilding pathway index...")

pathway_index = {}

for pathway in edges_df["Pathway"].unique():

    subset = edges_df[
        edges_df["Pathway"] == pathway
    ]

    pathway_index[pathway] = sorted(

        subset["ChainID"]
        .unique()
    )

with open(
    PATHWAY_INDEX_FILE,
    "wb"
) as f:

    pickle.dump(
        pathway_index,
        f
    )

# =========================================================
# SUMMARY
# =========================================================

print("\n====================================")
print("PREPROCESSING COMPLETE")
print("====================================")

print(
    f"\nChains Serialized: "
    f"{len(all_chains)}"
)

print(
    f"\nUnique Nodes: "
    f"{len(nodes_df)}"
)

print(
    f"\nUnique Edges: "
    f"{len(edges_df)}"
)

print("\nGenerated Files:")

print(f"\n1. {NODES_FILE.name}")

print(f"2. {EDGES_FILE.name}")

print(f"3. {CHAINS_FILE.name}")

print(f"4. {NODE_INDEX_FILE.name}")

print(f"5. {PATHWAY_INDEX_FILE.name}")

print("\n====================================")
