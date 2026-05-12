import pandas as pd
from pathlib import Path

CHAIN_DIR = Path("../data/expanded_chains")

all_files = list(CHAIN_DIR.glob("*.xlsx"))

print(f"Total chain files: {len(all_files)}")

combined = []

for file in all_files:

    try:
        df = pd.read_excel(file)
        df["CHAIN_FILE"] = file.name
        combined.append(df)

    except Exception as e:
        print(f"Error: {file.name} -> {e}")

if combined:

    merged = pd.concat(combined)

    output = "../data/processed/all_chains_combined.xlsx"

    merged.to_excel(output, index=False)

    print(f"Saved: {output}")
