import streamlit as st
import os

st.set_page_config(page_title="MAX Critical Calendar", layout="wide")

# Inject custom CSS
with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("Assets/MAX_Logo1.png", width=140)
st.sidebar.markdown("## MAX Critical Plan App")
st.sidebar.markdown("Navigate across seasons in Calendar view.")

# Main image + overlay text (fixed height, centered)
st.markdown("""
    <div style='
        position: relative;
        text-align: center;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        height: 540px;
        overflow: hidden;
        border-radius: 12px;
    '>
        <img src="https://raw.githubusercontent.com/aakriti-0123/MAX-Critical-Plan-1/main/Assets/Picture2.pn
