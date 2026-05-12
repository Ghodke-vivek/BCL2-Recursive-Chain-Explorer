import streamlit as st


def render_node_panel(node_data):

    st.sidebar.subheader("Selected Node")

    st.sidebar.write(node_data)
