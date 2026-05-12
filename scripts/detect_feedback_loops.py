import networkx as nx
import pandas as pd

from pathlib import Path

# =========================================================
# DIRECTORIES
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = (
    ROOT_DIR / "data" / "processed"
)

# =========================================================
# FILES
# =========================================================

EDGES_FILE = (
    PROCESSED_DIR / "edges.parquet"
)

# =========================================================
# LOAD EDGES
# =========================================================

print("\nLoading processed graph...\n")

edges_df = pd.read_parquet(
    EDGES_FILE
)

# =========================================================
# BUILD GRAPH
# =========================================================

G = nx.DiGraph()

for _, row in edges_df.iterrows():

    source = str(
        row["Source"]
    )

    target = str(
        row["Target"]
    )

    pathway = str(
        row.get(
            "Pathway",
            ""
        )
    )

    interaction = str(
        row.get(
            "Interaction",
            ""
        )
    )

    G.add_edge(

        source,

        target,

        pathway=pathway,

        interaction=interaction
    )

# =========================================================
# DETECT FEEDBACK LOOPS
# =========================================================

print("Detecting feedback loops...\n")

cycles = list(
    nx.simple_cycles(G)
)

# =========================================================
# SUMMARY
# =========================================================

print("====================================")
print("FEEDBACK LOOP ANALYSIS")
print("====================================")

print(f"\nTotal Loops Detected: {len(cycles)}")

# =========================================================
# DISPLAY LOOPS
# =========================================================

MAX_DISPLAY = 20

for idx, cycle in enumerate(

    cycles[:MAX_DISPLAY]
):

    print(
        f"\nLoop {idx + 1}"
    )

    print(
        " -> ".join(cycle)
    )

    print(
        f"Loop Length: {len(cycle)}"
    )

# =========================================================
# OPTIONAL EXPORT
# =========================================================

export_df = pd.DataFrame(

    {
        "Loop_ID": [

            f"LOOP_{i+1:04d}"

            for i in range(
                len(cycles)
            )
        ],

        "Path": [

            " -> ".join(cycle)

            for cycle in cycles
        ],

        "Length": [

            len(cycle)

            for cycle in cycles
        ]
    }
)

OUTPUT_FILE = (
    ROOT_DIR
    / "cache"
    / "feedback_loops.csv"
)

export_df.to_csv(

    OUTPUT_FILE,

    index=False
)

print("\n====================================")

print(
    f"Feedback loop report saved:\n"
    f"{OUTPUT_FILE}"
)

print("\n====================================")
