import streamlit as st
import os

st.set_page_config(page_title="MAX Critical Calendar", layout="wide")

# Inject custom CSS
with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.image("Assets/MAX_Logo.png", width=180)
st.sidebar.markdown("## MAX Critical Plan App")
st.sidebar.markdown("Navigate across seasons in Calendar view.")

st.title("Welcome to the MAX Critcal Plan Calendar")
st.markdown("This dashboard helps visualize apparel launch timelines across seasons, hits, and launch types.")
