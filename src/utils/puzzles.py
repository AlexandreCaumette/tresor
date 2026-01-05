import streamlit as st

from src import log
from src.data.dict_enigmes import PUZZLES


def get_team_puzzle(puzzle_id: str) -> dict | None:
    puzzle = PUZZLES.get(puzzle_id)

    if puzzle is None:
        log.error(f"The puzzle id '{puzzle_id}' doesn't exist in the puzzles list.")

        st.error(
            "L'énigme scannée n'existe pas, contactez le roi des pirates.", icon="🚨"
        )

        return

    team_id: str = st.session_state.team_id

    team_puzzle: dict | None = puzzle.get(team_id)

    if team_puzzle is None:
        log.error(f"The puzzle id '{puzzle_id}' doesn't know the team id '{team_id}'.")

        st.error(
            "L'énigme scannée n'existe pas pour votre équipe, contactez le roi des pirates.",
            icon="🚨",
        )

        return

    team_puzzle["meta"] = puzzle["meta"]

    return team_puzzle
