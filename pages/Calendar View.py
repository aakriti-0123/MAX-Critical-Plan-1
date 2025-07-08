import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Mapping of toggle names to sheet URLs (use /edit if possible to preserve frozen rows/columns)
sheet_urls = {
    "WN26": "https://docs.google.com/spreadsheets/d/1DioMTxZakUrLg5ZjElWo9DcxVPxcqhUN/edit?usp=sharing",
    "SS26": "https://docs.google.com/spreadsheets/d/16XNqVsbEYVxUBvRyF9l6EgkT_p5lDvQy/edit?usp=sharing",
    "WN25": "https://docs.google.com/spreadsheets/d/1mXSf7Kx89WZb4Off7x3tPa3Buc6QF1Dj/edit?usp=sharing"
}

selected_sheet = st.radio(
    "Choose sheet to view",
    options=list(sheet_urls.keys()),
    horizontal=True,
)

st.markdown(
    "<div style='text-align:center; margin: 1rem 0;'>"
    "Please use the sheet below to navigate to the desired regular/quick launch calendar view."
    "</div>",
    unsafe_allow_html=True
)

# Embed the selected Google Sheet in 'edit' mode for frozen row/column support
components.html(
    f"""
    <iframe 
        src="{sheet_urls[selected_sheet]}"
        style="
            width: 100vw; 
            height: 90vh; 
            border: none; 
            margin: 0; 
            padding: 0; 
            background: #fff;
        "
        allowfullscreen
        loading="lazy"
    ></iframe>
    <style>
        /* Make the main body non-scrollable */
        body, html, .main, .block-container {{
            overflow: hidden !important;
        }}
    </style>
    """,
    height=900,
    width=1920,
    scrolling=False,  # disables iframe scrollbars
)

# Force Streamlit's own scrollbars off as well
st.markdown("""
    <style>
        .main, .block-container, .stApp {{
            overflow: hidden !important;
        }}
    </style>
""", unsafe_allow_html=True)
