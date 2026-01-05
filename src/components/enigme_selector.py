import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner

from src import log


def main_enigme_selector():
    st.subheader("Sélection de l'énigme")

    if st.toggle(
        label="Scanner un QR code",
        value=False,
        help="Cibler le QR Code avec votre caméra.",
    ):
        log.info("Searching for a qr code.")

        qr_code = qrcode_scanner(key="qrcode_scanner")

        if qr_code is None:
            return

        log.info(f"qr code found with value '{qr_code}'")

        qr_code_value = qr_code.getvalue()

        if len(qr_code_value) > 1:
            st.error(
                f"Le QR code scanné renvoie la valeur'{qr_code_value}', ce qui n'est pas acceptable.",
                icon="❌",
            )

            return

        st.success("Le QR code a correctement été scanné !", icon="✅")

        st.session_state["puzzle_id"] = qr_code

        st.rerun()
