import networkx as nx
import pandas as pd
from pathlib import Path

CHAIN_DIR = Path("../data/expanded_chains")

G = nx.DiGraph()

all_files = list(CHAIN_DIR.glob("*.xlsx"))

for file in all_files:

    try:
        df = pd.read_excel(file)

        for _, row in df.iterrows():

            source = str(row["Source_NodeID"])
            target = str(row["Target_NodeID"])

            G.add_edge(source, target)

    except:
        pass

cycles = list(nx.simple_cycles(G))

print(f"Total feedback loops: {len(cycles)}")

for idx, cycle in enumerate(cycles[:20]):

    print(f"\nLoop {idx + 1}")
    print(" -> ".join(cycle))
