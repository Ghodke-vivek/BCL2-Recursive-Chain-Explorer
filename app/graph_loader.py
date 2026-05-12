import pandas as pd
from pathlib import Path


def load_seed_network(seed_file):
    return pd.read_excel(seed_file).fillna("")


def load_chain_files(chain_dir):

    all_dfs = []

    chain_files = list(Path(chain_dir).glob("*.xlsx"))

    for file in chain_files:

        try:
            df = pd.read_excel(file).fillna("")
            df["Chain_File"] = file.name
            all_dfs.append(df)

        except Exception as e:
            print(f"Error loading {file}: {e}")

    if len(all_dfs) == 0:
        return pd.DataFrame()

    return pd.concat(all_dfs, ignore_index=True)
