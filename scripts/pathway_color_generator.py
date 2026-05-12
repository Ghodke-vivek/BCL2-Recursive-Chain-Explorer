import json
import random

from pathlib import Path

# =========================================================
# OUTPUT FILE
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

OUTPUT_FILE = (
    ROOT_DIR
    / "app"
    / "assets"
    / "pathway_colors.json"
)

# =========================================================
# ALL PATHWAYS
# =========================================================

pathways = [

    "EGFR tyrosine kinase inhibitor resistance",

    "Endocrine resistance",

    "Platinum drug resistance",

    "NF-kappa B signaling pathway",

    "HIF-1 signaling pathway",

    "Sphingolipid signaling pathway",

    "p53 signaling pathway",

    "Autophagy - animal",

    "Protein processing in endoplasmic reticulum",

    "PI3K-Akt signaling pathway",

    "Apoptosis",

    "Apoptosis - multiple species",

    "Necroptosis",

    "Adrenergic signaling in cardiomyocytes",

    "Hedgehog signaling pathway",

    "Focal adhesion",

    "NOD-like receptor signaling pathway",

    "JAK-STAT signaling pathway",

    "Neurotrophin signaling pathway",

    "Cholinergic synapse",

    "Estrogen signaling pathway",

    "Parathyroid hormone synthesis, secretion and action",

    "AGE-RAGE signaling pathway in diabetic complications",

    "Amyotrophic lateral sclerosis",

    "Pathways of neurodegeneration - multiple diseases",

    "Shigellosis",

    "Salmonella infection",

    "Toxoplasmosis",

    "Tuberculosis",

    "Hepatitis B",

    "Measles",

    "Herpes simplex virus 1 infection",

    "Epstein-Barr virus infection",

    "Human immunodeficiency virus 1 infection",

    "Pathways in cancer",

    "MicroRNAs in cancer",

    "Chemical carcinogenesis - receptor activation",

    "Colorectal cancer",

    "Prostate cancer",

    "Small cell lung cancer",

    "Gastric cancer",

    "Lipid and atherosclerosis",

    "Fluid shear stress and atherosclerosis"
]

# =========================================================
# GENERATE COLORS
# =========================================================

colors = {}

used_colors = set()

# =========================================================
# SAFE COLOR GENERATOR
# =========================================================

def generate_unique_color():

    while True:

        color = "#%06x" % random.randint(
            0x222222,
            0xFFFFFF
        )

        if color not in used_colors:

            used_colors.add(color)

            return color

# =========================================================
# ASSIGN COLORS
# =========================================================

for pathway in pathways:

    colors[pathway] = generate_unique_color()

# =========================================================
# SAVE JSON
# =========================================================

with open(
    OUTPUT_FILE,
    "w"
) as f:

    json.dump(
        colors,
        f,
        indent=4
    )

# =========================================================
# SUMMARY
# =========================================================

print("====================================")
print("PATHWAY COLORS GENERATED")
print("====================================")

print(
    f"\nTotal Pathways: {len(colors)}"
)

print(
    f"\nSaved To:\n{OUTPUT_FILE}"
)

print("\n====================================")
