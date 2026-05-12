from pathlib import Path

from config import (
    CSS_FILE
)

# =========================================================
# LOAD CSS
# =========================================================

def load_css():

    try:

        with open(
            CSS_FILE,
            "r"
        ) as f:

            css = f.read()

        return f"<style>{css}</style>"

    except Exception as e:

        print(
            f"Error loading CSS: {e}"
        )

        return "<style></style>"

# =========================================================
# PAGE STYLE
# =========================================================

PAGE_STYLE = load_css()
