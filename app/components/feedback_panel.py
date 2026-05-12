import streamlit as st

# =========================================================
# FEEDBACK PANEL
# =========================================================

def render_feedback_panel(

    feedback_paths
):

    if not feedback_paths:

        st.info(
            "No feedback loops detected."
        )

        return

    # =====================================================
    # DISPLAY FEEDBACK LOOPS
    # =====================================================

    for idx, feedback in enumerate(

        feedback_paths
    ):

        source = feedback.get(
            "source",
            ""
        )

        target = feedback.get(
            "target",
            ""
        )

        path = feedback.get(
            "path",
            []
        )

        length = feedback.get(
            "length",
            0
        )

        with st.expander(

            f"Feedback Loop {idx + 1}"

        ):

            st.markdown(

                f"""
                **Source Node:** `{source}`

                **Reconnects To Seed:** `{target}`

                **Path Length:** `{length}`
                """
            )

            st.markdown(
                "### Path"
            )

            st.code(
                " → ".join(path)
            )
