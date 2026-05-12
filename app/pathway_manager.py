import random


def generate_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


def build_pathway_colors(pathways):

    pathway_colors = {}

    for pathway in pathways:
        pathway_colors[pathway] = generate_color()

    return pathway_colors
