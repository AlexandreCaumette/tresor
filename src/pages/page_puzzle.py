import streamlit as st

from src.components.enigme_displayer import main_enigme_displayer
from src.components.enigme_selector import main_enigme_selector


def main_page_puzzle():
    st.header("🧩 Les énigmes du *Papa Enfonças*")

    main_enigme_selector()

    st.divider()

    if "puzzle_id" in st.session_state:
        main_enigme_displayer(puzzle_id=st.session_state.puzzle_id)
