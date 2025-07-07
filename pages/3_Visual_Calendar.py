import streamlit as st
import streamlit.components.v1 as components

# Google Sheet URLs (use /preview for embed)
sheet_urls = {
    "wn26": "https://docs.google.com/spreadsheets/d/1DioMTxZakUrLg5ZjElWo9DcxVPxcqhUN/preview",
    "ss26": "https://docs.google.com/spreadsheets/d/16XNqVsbEYVxUBvRyF9l6EgkT_p5lDvQy/preview",
    "wn25": "https://docs.google.com/spreadsheets/d/1mXSf7Kx89WZb4Off7x3tPa3Buc6QF1Dj/preview"
}

# Remove Streamlit padding
st.markdown("""
    <style>
    .block-container {
        padding: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Optional: Tab instruction
st.markdown(
    "<div style='text-align:center; padding: 1rem;
