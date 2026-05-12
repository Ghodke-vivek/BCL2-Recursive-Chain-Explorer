import streamlit as st

# =========================================================
# PATHWAY LEGEND
# =========================================================

def render_pathway_legend(

    color_manager
):

    pathway_colors = (

        color_manager
        .get_all_colors()
    )

    if not pathway_colors:

        st.info(
            "No pathway colors available."
        )

        return

    st.markdown(
        "### Pathway Colors"
    )

    # =====================================================
    # DISPLAY PATHWAYS
    # =====================================================

    for pathway, color in sorted(

        pathway_colors.items()
    ):

        st.markdown(

            f"""
            <div style="
                display:flex;
                align-items:center;
                margin-bottom:6px;
            ">

                <div style="
                    width:16px;
                    height:16px;
                    border-radius:50%;
                    background:{color};
                    margin-right:10px;
                    border:1px solid white;
                "></div>

                <div style="
                    font-size:14px;
                ">
                    {pathway}
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )
