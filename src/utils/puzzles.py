import streamlit as st

from src import log
from src.data.dict_enigmes import PUZZLES


def get_puzzle(puzzle_id: str) -> dict | None:
    puzzle = PUZZLES.get(puzzle_id)

    if puzzle is None:
        log.error(f"The puzzle id '{puzzle_id}' doesn't exist in the puzzles list.")

        st.error(
            "L'énigme scannée n'existe pas, contactez le roi des pirates.", icon="🚨"
        )

        return

    return puzzle
