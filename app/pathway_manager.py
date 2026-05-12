import json
import random

from config import (
    PATHWAY_COLOR_FILE
)

# =========================================================
# PATHWAY COLOR MANAGER
# =========================================================

class PathwayColorManager:

    def __init__(self):

        self.pathway_colors = (

            self._load_pathway_colors()
        )

    # =====================================================
    # LOAD PATHWAY COLORS
    # =====================================================

    def _load_pathway_colors(self):

        try:

            with open(
                PATHWAY_COLOR_FILE,
                "r"
            ) as f:

                colors = json.load(f)

            return colors

        except Exception as e:

            print(
                f"Error loading pathway colors: {e}"
            )

            return {}

    # =====================================================
    # GENERATE RANDOM COLOR
    # =====================================================

    def generate_color(self):

        return "#%06x" % random.randint(
            0,
            0xFFFFFF
        )

    # =====================================================
    # GET PATHWAY COLOR
    # =====================================================

    def get_color(

        self,

        pathway_name
    ):

        if pathway_name in self.pathway_colors:

            return self.pathway_colors[
                pathway_name
            ]

        # ================================================
        # GENERATE NEW COLOR IF MISSING
        # ================================================

        new_color = self.generate_color()

        self.pathway_colors[
            pathway_name
        ] = new_color

        return new_color

    # =====================================================
    # GET ALL PATHWAY COLORS
    # =====================================================

    def get_all_colors(self):

        return self.pathway_colors
