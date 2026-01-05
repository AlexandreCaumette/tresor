import streamlit as st

from src.components.logo import main_logo
from src.pages.page_home import main_page_home
from src.pages.page_puzzle import main_page_puzzle
from src.pages.page_treasure import main_page_treasure


def main():
    st.set_page_config(
        layout="centered", page_icon="🗺️", page_title="Chasse au trésor de l'Arche"
    )

    st.title("🛶 La chasse au trésor perdu de l'Arche")

    main_logo()

    page_login = st.Page(
        page=main_page_home,
        title="Accueil",
        icon="🏡",
        url_path="accueil",
        default=True,
    )

    page_puzzle = st.Page(
        page=main_page_puzzle, title="Enigme", icon="🧩", url_path="enigme"
    )

    page_treasure = st.Page(
        page=main_page_treasure, title="Trésor", icon="👑", url_path="tresor"
    )

    pages = [page_login]

    if "team_id" in st.session_state:
        pages.append(page_puzzle)

    if st.session_state.get("status", None) == "terminated":
        pages.append(page_treasure)

    current_page = st.navigation(pages=pages)

    current_page.run()


if __name__ == "__main__":
    main()
