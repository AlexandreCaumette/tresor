import streamlit as st


def main_place_hint(puzzle: dict | None):
    if puzzle is None:
        return

    hint = puzzle.get("meta", {}).get("place_hint", "")

    st.text("🔎 Indice pour trouver la prochaine énigme :")

    with st.container(border=True):
        st.markdown(body=f'*"{hint}"*')
