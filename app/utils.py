import hashlib
import pandas as pd

# =========================================================
# CREATE UNIQUE EDGE ID
# =========================================================

def create_edge_id(

    source,

    target,

    relation_id
):

    return hashlib.md5(

        f"{source}_{target}_{relation_id}"
        .encode()

    ).hexdigest()

# =========================================================
# LOAD EXCEL FILE
# =========================================================

def load_excel(file_path):

    try:

        df = pd.read_excel(
            file_path
        ).fillna("")

        return df

    except Exception as e:

        raise Exception(

            f"Error loading Excel file:\n"
            f"{file_path}\n\n"
            f"{e}"
        )

# =========================================================
# SAFE STRING
# =========================================================

def safe_str(value):

    if pd.isna(value):

        return ""

    return str(value).strip()

# =========================================================
# REMOVE DUPLICATES
# =========================================================

def remove_duplicate_nodes(nodes):

    unique = {}

    for node in nodes:

        unique[node.id] = node

    return list(
        unique.values()
    )

# =========================================================
# REMOVE DUPLICATE EDGES
# =========================================================

def remove_duplicate_edges(edges):

    unique = {}

    for edge in edges:

        key = (

            edge.source,

            edge.target,

            edge.label
        )

        unique[key] = edge

    return list(
        unique.values()
    )
