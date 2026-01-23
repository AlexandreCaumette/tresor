from io import BytesIO

import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner


def main_enigme_selector():
    st.subheader("Sélection de l'énigme")

    if "toggle_scanner" not in st.session_state:
        st.session_state["toggle_scanner"] = False

    if st.button(label="Actualiser la page", icon=":material/refresh:", type="primary"):
        st.rerun()

    if st.toggle(
        label="Scanner un QR code",
        value=st.session_state.toggle_scanner,
        help="Cibler le QR Code avec votre caméra.",
    ):
        qr_code = qrcode_scanner(key="qrcode_scanner")

        if qr_code is None:
            return

        if isinstance(qr_code, BytesIO):
            qr_code = qr_code.getvalue()

        if len(qr_code) > 1:
            st.error(
                f"Le QR code scanné renvoie la valeur'{qr_code}', ce qui n'est pas acceptable.",
                icon="❌",
            )

            return

        st.success(
            "Le QR code a correctement été scanné ! Actualiser la page.", icon="✅"
        )

        st.session_state["puzzle_id"] = qr_code

        st.session_state.toggle_scanner = False

        st.rerun()

        return
