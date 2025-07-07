import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Custom CSS to remove margin/padding from main container and body
st.markdown("""
    <style>
        .block-container, .main, .css-uf99v8, .css-18e3th9 {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100vw !important;
            width: 100vw !important;
        }
        body {
            padding: 0 !important;
            margin: 0 !important;
        }
        header, footer {display: none !important;}
        /* Hide hamburger and Streamlit menu for even more width */
        #MainMenu {visibility: hidden;}
        .st-emotion-cache-1avcm0n {padding-top: 0 !important;}
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<div style='text-align:center; margin-bottom: 0.5rem; margin-top: 1rem;'>"
    "Please navigate to the tab named <b>REGULAR CP_30D</b> in the embedded sheet below."
    "</div>",
    unsafe_allow_html=True
)

sheet_urls = {
    "wn26": "https://docs.google.com/spreadsheets/d/1DioMTxZakUrLg5ZjElWo9DcxVPxcqhUN/preview",
    "ss26": "https://docs.google.com/spreadsheets/d/16XNqVsbEYVxUBvRyF9l6EgkT_p5lDvQy/preview",
    "wn25": "https://docs.google.com/spreadsheets/d/1mXSf7Kx89WZb4Off7x3tPa3Buc6QF1Dj/preview"
}

tab = st.radio(
    "Choose sheet to view",
    options=list(sheet_urls.keys()),
    format_func=lambda x: x,
    horizontal=True,
    key="sheet_radio"
)

# Use the full width and height of the viewport for the iframe
components.html(
    f"""
    <iframe 
        src="{sheet_urls[tab]}"
        style="
            position: fixed;
            top: 110px; /* Adjust depending on your radio/buttons height */
            left: 0;
            width: 100vw;
            height: 90vh;
            border: none;
            margin: 0;
            padding: 0;
            overflow: auto;
            background: #fff;"
        allowfullscreen
        loading="lazy"
    ></iframe>
    """,
    height=800,  # This is needed for Streamlit to render the component, but iframe uses viewport height
    width=1920,  # Large width for Streamlit, but iframe itself will cover 100vw
    scrolling=True,
)

# Optional: Add extra CSS to hide Streamlit's hamburger menu for a cleaner look:
st.markdown("""
    <style>
        .stDeployButton {display: none;}
    </style>
""", unsafe_allow_html=True)
