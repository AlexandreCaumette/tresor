import streamlit as st

from src.data.dict_enigmes import PUZZLES


def main_page_admin():
    st.header("🛡️ Vue administrateur")

    puzzle_id = st.selectbox(
        label="Sélectionner l'id de l'énigme :", options=PUZZLES.keys(), index=0
    )

    puzzle = PUZZLES[puzzle_id]

    st.divider()

    with st.expander(label="Cachette :", icon=":material/info:"):
        st.write(
            f"L'énigme est cachée dans **:red[{puzzle.get('category')}]** au niveau de **:orange[{puzzle.get('place')}]**."
        )

        st.write(
            f'L\'indice pour trouvre la cachette : ***:blue["{puzzle.get("place_hint")}"]***'
        )

    with st.expander(label="Question :", icon=":material/quiz:"):
        st.write(puzzle.get("question", ""))

    with st.expander(label="Réponse :", icon=":material/input:"):
        st.write(f'La réponse à l\'énigme est : **:green["{puzzle.get("answer")}"]**')

    with st.expander(label="L'aide :", icon=":material/help:"):
        st.write(
            f"Epreuve pour obtenir une assistance : **:blue[{puzzle.get('help')}]**"
        )

        st.text("Aide pour comprendre l'énigme :")

        st.markdown(puzzle.get("puzzle_hint"))

    with st.expander(
        label="Coordonnées par équipe :", icon=":material/globe_location_pin:"
    ):
        for id in range(1, 4):
            team_id = f"team_{id}"

            st.write(f'- Equipe {team_id} : **:green["{puzzle.get(team_id)}"]**')
