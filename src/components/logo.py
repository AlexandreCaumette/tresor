import pathlib

import streamlit as st


def main_logo():
    if "team_id" not in st.session_state:
        return

    team_id = st.session_state.team_id

    path_to_logo = (
        pathlib.Path(__file__).parent.parent / "assets" / f"logo_{team_id}.png"
    )

    if not path_to_logo.exists():
        return

    st.logo(image=path_to_logo, size="large")
