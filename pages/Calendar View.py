import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Mapping of toggle names to Google Sheets published embed URLs (toolbar and edit both disabled)
sheet_urls = {
    "WN26": "https://docs.google.com/spreadsheets/d/1mlpVAeyxQNPGZuQjXw5GYiC8MB9sf4YQ/edit?usp=sharing&ouid=109548826197667239183&rtpof=true&sd=true",
    "SS26": "https://docs.google.com/spreadsheets/d/1ky9jx-QVTFVmrO62KQCY1VAAN0jgjwVJ/edit?usp=sharing&ouid=109548826197667239183&rtpof=true&sd=true",
    "WN25": "https://docs.google.com/spreadsheets/d/1O64AJMJWFUOpX1KxZcQM5APwpcaTo50V/edit?usp=sharing&ouid=109548826197667239183&rtpof=true&sd=true"
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

# Embed the selected Google Sheet in published (read-only, no toolbar) mode
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
        body, html, .main, .block-container {{
            overflow: hidden !important;
        }}
    </style>
    """,
    height=900,
    width=1920,
    scrolling=False,  # disables iframe scrollbars
)

st.markdown("""
    <style>
        .main, .block-container, .stApp {{
            overflow: hidden !important;
        }}
    </style>
""", unsafe_allow_html=True)
