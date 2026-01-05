import streamlit as st

from src import log
from src.components.login import main_login
from src.components.place_hint import main_place_hint
from src.data.ordre_enigmes import ORDRE
from src.utils.puzzles import get_team_puzzle


def main_presentation():
    st.subheader("Présentation de la chasse au trésor")

    body = """
    Bienvenu jeunes aventuriers téméraires et audacieux.

    🏰 Vous venez de mettre un pied sur la sinistrement célèbre Arche de la Garenne-Colombes,
    connue pour ses nauséabondes odeurs de chausson d'escalade, ou ses incessants cris d'animaux
    sauvage (*"bibi ! keke ! bibi ! puta carmen !!!"*).

    🏴‍☠️ Vous cherchez mon trésor ? Je vous le laisse si vous voulez ! Trouvez-le ! Je l'ai laissé quelque part dans ce quartier !

    ⌛ Mais ne tardez pas, d'autres pirates sont également en chemin et essayeront de vous devancer...
    """

    st.markdown(body=body)


def main_explications():
    st.subheader("Explications et règles du jeu")

    body = f"""
    Bonjour équipe **:orange[{st.session_state.team_name}]** !

    La chasse au trésor est composée de **9 énigmes**, chaque énigme résolue vous apportera
    la localisation de l'énigme suivante, ainsi qu'une partie de la localisation du trésor.

    Pour éviter que les équipes ne trichent, chaque énigme sera énoncée
    en 3 version différentes, avec 3 réponses différentes.

    Une fois arrivé sur le lieu d'une énigme, utilisez la page *"Enigme"* pour scanner le QR code de l'énigme.

    Les morceaux de la localisation du trésor ne seront pas sauvegardés dans cette interface, :red[à vous
    de les noter].

    L'équipe qui remportera le trésor sera la première arrivée à la localisation finale, et avec la
    localisation exacte notée.

    En cas de difficulté, contactez le **:green[grand roi des pirates de l'Arche]** via messenger.
    """

    st.markdown(body=body)


def main_page_home():
    st.header("🏡 Accueil")

    main_presentation()

    log.info("Displaying home page.")

    team_id: str = st.session_state.get("team_id", None)

    if team_id is None:
        st.divider()

        main_login()

        return

    st.divider()

    main_explications()

    st.divider()

    first_puzzle_id = ORDRE.get(team_id, [])[0]
    puzzle = get_team_puzzle(puzzle_id=first_puzzle_id)

    main_place_hint(puzzle=puzzle)
