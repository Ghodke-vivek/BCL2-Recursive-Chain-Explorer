import streamlit as st

# =========================================================
# NODE PANEL
# =========================================================

def render_node_panel(

    selected_node,

    node_index
):

    st.markdown(
        f"### Selected Node"
    )

    st.code(
        selected_node
    )

    # =====================================================
    # CHAIN MEMBERSHIP
    # =====================================================

    connected_chains = node_index.get(

        selected_node,

        []
    )

    st.markdown(
        "### Connected Chains"
    )

    st.write(
        len(connected_chains)
    )

    # =====================================================
    # DISPLAY CHAINS
    # =====================================================

    if connected_chains:

        with st.expander(
            "View Chain IDs"
        ):

            for chain_id in connected_chains:

                st.write(
                    chain_id
                )

    else:

        st.info(
            "No connected chains found."
        )
