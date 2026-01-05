import polars as pl
import streamlit as st


def main_page_treasure():
    st.header("👑 Récupérer le trésor")

    coordinates = st.text_input(
        label="Saisissez la solution finale de toutes les énigmes :"
    )

    if st.button(
        label="Valider la réponse",
        type="primary",
        disabled=coordinates is None or coordinates == "",
        icon=":material/check_circle:",
        help="Il faut saisir au moins 1 caractère dans le champ de saisi de texte.",
    ):
        st.space(size="small")

        if coordinates != st.secrets.solution["coordinates"]:
            st.error(
                f"La réponse '{coordinates}' n'est pas la bonne solution !", icon="❌"
            )

            return

        st.snow()

        st.success(
            "Les coordonnées du trésor sont correctes ! Vite foncez le récupérer !",
            icon="✅",
        )

        st.space(size="small")

        df = pl.DataFrame(
            {
                "LATITUDE": [float(st.secrets.solution["coordinates"].split(",")[0])],
                "LONGITUDE": [float(st.secrets.solution["coordinates"].split(",")[1])],
            }
        )

        st.map(data=df, size=5)
