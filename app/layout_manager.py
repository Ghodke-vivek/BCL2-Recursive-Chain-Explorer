from streamlit_agraph import Config

# =========================================================
# GRAPH CONFIGURATION
# =========================================================

def get_graph_config():

    return Config(

        width="100%",

        height=900,

        directed=True,

        physics=True,

        hierarchical=True,

        nodeHighlightBehavior=True,

        highlightColor="#F7A7A6",

        collapsible=True,

        staticGraph=False,

        staticGraphWithDragAndDrop=False,

        node={

            "labelProperty": "label"
        },

        link={

            "labelProperty": "label",

            "renderLabel": True
        },

        hierarchical={

            "enabled": True,

            "direction": "LR",

            "sortMethod": "directed",

            "shakeTowards": "roots",

            "levelSeparation": 180,

            "nodeSpacing": 200,

            "treeSpacing": 250
        },

        physics={

            "enabled": True,

            "hierarchicalRepulsion": {

                "centralGravity": 0.0,

                "springLength": 180,

                "springConstant": 0.01,

                "nodeDistance": 220,

                "damping": 0.09
            },

            "solver": "hierarchicalRepulsion"
        }
    )
