import pandas as pd
from pathlib import Path
from collections import defaultdict
import pickle

CHAIN_DIR = Path("../data/expanded_chains")

all_files = list(CHAIN_DIR.glob("*.xlsx"))

graph_index = defaultdict(list)

for file in all_files:

    try:
        df = pd.read_excel(file)

        for _, row in df.iterrows():

            source = str(row["Source_NodeID"])
            target = str(row["Target_NodeID"])

            graph_index[source].append(target)

    except Exception as e:
        print(e)

with open("../cache/graph_index.pkl", "wb") as f:
    pickle.dump(graph_index, f)

print("Graph index saved.")
