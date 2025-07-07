import streamlit as st
import streamlit.components.v1 as components

# Sheet URLs (use /preview for a cleaner embed)
sheet_urls = {
    "wn26": "https://docs.google.com/spreadsheets/d/1DioMTxZakUrLg5ZjElWo9DcxVPxcqhUN/preview",
    "ss26": "https://docs.google.com/spreadsheets/d/16XNqVsbEYVxUBvRyF9l6EgkT_p5lDvQy/preview",
    "wn25": "https://docs.google.com/spreadsheets/d/1mXSf7Kx89WZb4Off7x3tPa3Buc6QF1Dj/preview"
}

st.markdown(
    "<div style='text-align:center; margin-bottom: 1rem;'>"
    "Please navigate to the tab named <b>REGULAR CP_30D</b> in the embedded sheet below."
    "</div>",
    unsafe_allow_html=True
)

# Tab selection using Streamlit's radio buttons
tab = st.radio(
    "Choose sheet to view",
    options=list(sheet_urls.keys()),
    format_func=lambda x: x,
    horizontal=True
)

# Embed the selected sheet, expand as much as possible
components.html(
    f"""
    <iframe 
        src="{sheet_urls[tab]}"
        style="
            width: 100vw; 
            height: 85vh; 
            border: none; 
            margin: 0; 
            padding: 0; 
            overflow: auto;
            background: #fff;"
        allowfullscreen
        loading="lazy"
    ></iframe>
    """,
    height=700,  # Streamlit container height (adjust as needed)
    width=None,  # Use all available width
    scrolling=True,
)
