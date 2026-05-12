import pandas as pd
import pickle
import gzip

from app.config import (

```
NODES_FILE,

EDGES_FILE,

CHAINS_FILE,

NODE_INDEX_FILE,

PATHWAY_INDEX_FILE,

GRAPH_INDEX_FILE
```

)

# =========================================================

# VALIDATE FILES

# =========================================================

def validate_required_files():

```
required_files = [

    NODES_FILE,

    EDGES_FILE,

    CHAINS_FILE,

    NODE_INDEX_FILE,

    PATHWAY_INDEX_FILE,

    GRAPH_INDEX_FILE
]

missing = []

for file in required_files:

    if not file.exists():

        missing.append(str(file))

if missing:

    raise FileNotFoundError(

        "\nMissing required files:\n\n"
        + "\n".join(missing)
    )
```

# =========================================================

# LOAD NODES

# =========================================================

def load_nodes():

```
print("Loading nodes...")

return pd.read_parquet(
    NODES_FILE
)
```

# =========================================================

# LOAD EDGES

# =========================================================

def load_edges():

```
print("Loading edges...")

return pd.read_parquet(
    EDGES_FILE
)
```

# =========================================================

# LOAD CHAINS

# =========================================================

def load_chains():

```
print("Loading chains...")

with gzip.open(
    CHAINS_FILE,
    "rb"
) as f:

    chains = pickle.load(f)

return chains
```

# =========================================================

# LOAD NODE INDEX

# =========================================================

def load_node_index():

```
print("Loading node index...")

with open(
    NODE_INDEX_FILE,
    "rb"
) as f:

    node_index = pickle.load(f)

return node_index
```

# =========================================================

# LOAD PATHWAY INDEX

# =========================================================

def load_pathway_index():

```
print("Loading pathway index...")

with open(
    PATHWAY_INDEX_FILE,
    "rb"
) as f:

    pathway_index = pickle.load(f)

return pathway_index
```

# =========================================================

# LOAD GRAPH INDEX

# =========================================================

def load_graph_index():

```
print("Loading graph adjacency index...")

with open(
    GRAPH_INDEX_FILE,
    "rb"
) as f:

    graph_index = pickle.load(f)

return graph_index
```

# =========================================================

# LOAD EVERYTHING

# =========================================================

def load_all_graph_data():

```
validate_required_files()

nodes_df = load_nodes()

edges_df = load_edges()

chains = load_chains()

node_index = load_node_index()

pathway_index = load_pathway_index()

graph_index = load_graph_index()

return {

    "nodes": nodes_df,

    "edges": edges_df,

    "chains": chains,

    "node_index": node_index,

    "pathway_index": pathway_index,

    "graph_index": graph_index
}
```
