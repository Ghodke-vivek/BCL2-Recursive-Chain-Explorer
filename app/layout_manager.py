from streamlit_agraph import Config

# =========================================================
# GRAPH CONFIG
# =========================================================

def get_graph_config():

    return Config(

        width="100%",
        height=900,

        directed=True,

        # ❗ MUST be False for stable hierarchy
        physics=False,

        # ✅ REQUIRED FOR CLICK DETECTION
        nodeHighlightBehavior=True,
        highlightColor="#F7A7A6",

        # ❗ DO NOT use both hierarchical=True and layout={}
        # Use ONLY layout block

        layout={
            "hierarchical": {
                "enabled": True,
                "direction": "RL",   # RIGHT → LEFT
                "sortMethod": "directed",
                "nodeSpacing": 150,
                "levelSeparation": 200
            }
        }
    )
