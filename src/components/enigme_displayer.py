import streamlit as st

from src import log
from src.components.place_hint import main_place_hint
from src.data import ordre_enigmes
from src.data.dict_enigmes import PUZZLES
from src.utils.puzzles import get_puzzle


def get_next_puzzle(puzzle_id: str) -> dict | None:
    # On récupère l'id de l'équipe dans le session state.
    team_id: str = st.session_state.team_id

    # On récupère l'ordre des énigmes pour cette équipe.
    team_puzzles_order = ordre_enigmes.ORDRE.get(team_id, [])

    # On identifie l'indice de l'énigme actuelle dans l'ordre des énigmes.
    current_index = team_puzzles_order.index(puzzle_id)

    # On incrémente cet indice pour trouver la prochaine énigme.
    next_puzzle_index = current_index + 1

    # Si le prochain indice est en dehors de la liste, alors toutes les énigmes ont été résolues.
    if next_puzzle_index >= len(team_puzzles_order):
        log.info("Dernier puzzle atteint, plus d'énigme à résoudre.")

        return None

    # Sinon on récupère l'id de l'énigme suivante.
    next_puzzle_id = team_puzzles_order[next_puzzle_index]

    # Puis on récupère cette énigme.
    next_puzzle = PUZZLES.get(next_puzzle_id, {})

    return next_puzzle


def main_enigme_displayer(puzzle_id: str):
    st.subheader(f"Enigme n°{puzzle_id}")

    puzzle = get_puzzle(puzzle_id=puzzle_id)

    if not isinstance(puzzle, dict):
        return

    st.text("Voici l'énoncé de l'énigme à résoudre :")

    with st.container(border=True):
        question = puzzle.get("question", "")

        st.markdown(question)

    st.space(size="small")

    with st.expander(
        label="Besoin d'un coup de pouce (le roi des pirates doit être présent 🏴‍☠️)",
        icon="❓",
        expanded=False,
    ):
        st.markdown(puzzle.get("help"))

    st.space(size="small")

    answer = st.text_input(
        label="Saisissez la réponse à l'énigme :",
        help="Texte en minuscule, avec les tirets remplacés par des espaces, si possible sans article défini.",
    )

    if st.button(
        label="Valider la réponse",
        type="primary",
        disabled=answer is None or answer == "",
        icon=":material/check_circle:",
        help="Il faut saisir au moins 1 caractère dans le champ de saisi de texte.",
    ):
        answer = (
            answer.lower().replace("-", " ").replace(" de ", " ").replace(" du ", " ")
        )

        if answer != puzzle.get("answer"):
            st.error(
                f"La réponse proposée **'{answer}'** n'est pas correcte !", icon="❌"
            )

            return

        st.success(f"La réponse proposée **'{answer}'** est correcte !", icon="✅")

        st.info(
            f"🗺️ Voici la récompense : **'{puzzle.get(st.session_state.team_id)}'** 📍"
        )

        st.divider()

        st.subheader("Enigme suivante")

        next_puzzle = get_next_puzzle(puzzle_id=puzzle_id)

        log.info(f"Prochaine énigme : {next_puzzle}")

        if next_puzzle is None:
            st.balloons()

            st.text(
                "Vous êtes arrivés au bout des énigmes. Une nouvelle page est apparue dans la barre de navigation 👑",
            )

            st.session_state["status"] = "terminated"

            st.rerun()

            return

        main_place_hint(puzzle=next_puzzle)
