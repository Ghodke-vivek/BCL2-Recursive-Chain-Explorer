import random
import json

pathways = [
    "Neurotrophin signaling pathway",
    "PI3K-Akt signaling pathway",
    "Apoptosis"
]

colors = {}

for pathway in pathways:

    colors[pathway] = "#%06x" % random.randint(0, 0xFFFFFF)

with open("../app/assets/pathway_colors.json", "w") as f:

    json.dump(colors, f, indent=4)

print("Pathway colors generated.")
