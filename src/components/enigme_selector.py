from io import BytesIO

import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner

from src import log


def main_enigme_selector():
    st.subheader("Sélection de l'énigme")

    if st.toggle(
        label="Scanner un QR code",
        value=False,
        help="Cibler le QR Code avec votre caméra.",
        key="toggle_scanner",
    ):
        qr_code = qrcode_scanner(key="qrcode_scanner")

        if qr_code is None:
            return

        log.debug(f"qr code found with value '{qr_code}'")

        if isinstance(qr_code, BytesIO):
            qr_code = qr_code.getvalue()

        if len(qr_code) > 1:
            st.error(
                f"Le QR code scanné renvoie la valeur'{qr_code}', ce qui n'est pas acceptable.",
                icon="❌",
            )

            return

        st.success("Le QR code a correctement été scanné !", icon="✅")

        st.session_state["puzzle_id"] = qr_code

        st.rerun()

    if st.button(label="Actualiser la page", icon=":material/refresh:", type="primary"):
        st.rerun()
