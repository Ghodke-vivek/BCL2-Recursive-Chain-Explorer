from streamlit_agraph import Config

# =========================================================
# GRAPH CONFIG
# =========================================================

def get_graph_config():

    return Config(

        width="100%",
        height=900,

        directed=True,

        # IMPORTANT: disable physics for stable layout
        physics=False,

        # REQUIRED for click detection
        nodeHighlightBehavior=True,
        highlightColor="#F7A7A6",

        # CLEAN UI
        collapsible=False,

        # HIERARCHICAL RIGHT → LEFT
        layout={
            "hierarchical": {
                "enabled": True,
                "direction": "RL",
                "sortMethod": "directed",
                "nodeSpacing": 150,
                "levelSeparation": 200
            }
        }
    )
