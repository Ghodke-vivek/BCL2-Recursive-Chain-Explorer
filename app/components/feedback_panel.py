import streamlit as st


def render_feedback_panel(feedback_paths):

    st.sidebar.subheader("Feedback Loops")

    if not feedback_paths:
        st.sidebar.info("No feedback loops detected")
        return

    for idx, path in enumerate(feedback_paths):

        st.sidebar.write(f"Loop {idx + 1}")
        st.sidebar.write(" → ".join(path))
