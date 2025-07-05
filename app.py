
import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="MAX Critical Plan", layout="wide")

with st.sidebar:
    logo_path = Path("assets/MAX Logo.png")
    if logo_path.exists():
        logo = Image.open(logo_path)
        st.image(logo, width=120)
    st.markdown("## MAX Critical Calendar")

st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&family=Poppins&display=swap');</style>", unsafe_allow_html=True)
st.markdown(open("styles/custom.css").read(), unsafe_allow_html=True)
