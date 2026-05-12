import streamlit as st


def render_pathway_legend(color_manager):

    st.sidebar.subheader("Pathway Colors")

    for pathway, color in color_manager.pathway_colors.items():

        st.sidebar.markdown(
            f"<span style='color:{color}'>⬤</span> {pathway}",
            unsafe_allow_html=True
        )
