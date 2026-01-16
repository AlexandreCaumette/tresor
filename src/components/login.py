import streamlit as st

from src import log


def main_login():
    st.subheader("Connexion à votre équipe")

    team_name = st.text_input(
        label="Saisissez votre nom d'équipe :",
        type="default",
        placeholder="La team Rocket",
        icon=":material/account_circle:",
    )

    if st.button(
        label="Ouvrir l'équipe",
        disabled=team_name is None,
        type="primary",
        icon=":material/login:",
    ):
        if team_name not in st.secrets.connection.team_names:
            log.error(f"The team name '{team_name}' is not part of the secrets.")

            st.error(
                f"L'identifiant saisi **'{team_name}'** n'est pas correct !", icon="🚨"
            )

            return

        st.success(f"Bienvenu à bord équipe {team_name} !", icon="✅")

        team_id = st.secrets.connection.team_names.index(team_name) + 1

        st.session_state["team_id"] = f"team_{team_id}"
        st.session_state["team_name"] = team_name

        st.rerun()
