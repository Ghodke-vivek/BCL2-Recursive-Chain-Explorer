from streamlit_agraph import Config

# =========================================================
# GRAPH CONFIG
# =========================================================

def get_graph_config():

    config = Config(

        width="100%",

        height=900,

        directed=True,

        physics=True,

        hierarchical=True,

        nodeHighlightBehavior=True,

        highlightColor="#F7A7A6",

        collapsible=True
    )

    return config
