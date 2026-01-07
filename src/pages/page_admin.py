import streamlit as st

from src.data.dict_enigmes import PUZZLES


def main_page_admin():
    st.header("🛡️ Vue administrateur")

    puzzle_id = st.selectbox(
        label="Sélectionner l'id de l'énigme :", options=PUZZLES.keys(), index=0
    )

    puzzle = PUZZLES[puzzle_id]

    st.subheader(f"Visualisation de l'énigme n°{puzzle_id}")

    st.text("Les méta-données de l'énigme :")

    st.write(puzzle.get("meta", {}))

    st.divider()

    for team_id in range(1, 4):
        st.text(f"L'énigme pour l'équipe {team_id} :")

        team_puzzle = puzzle.get(f"team_{team_id}", {})

        with st.expander(label="Question :"):
            st.write(team_puzzle.get("question", ""))

        with st.expander(label="Réponse :"):
            st.write(team_puzzle.get("answer", ""))

        with st.expander(label="Coordonnées :"):
            st.write(team_puzzle.get("coordinate", ""))

        st.divider()
