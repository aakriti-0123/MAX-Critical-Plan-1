import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Mapping of toggle names to sheet URLs
sheet_urls = {
    "wn26": "https://docs.google.com/spreadsheets/d/1DioMTxZakUrLg5ZjElWo9DcxVPxcqhUN/preview",
    "ss26": "https://docs.google.com/spreadsheets/d/16XNqVsbEYVxUBvRyF9l6EgkT_p5lDvQy/preview",
    "wn25": "https://docs.google.com/spreadsheets/d/1mXSf7Kx89WZb4Off7x3tPa3Buc6QF1Dj/preview"
}

# Show a radio button at the top of the app for toggling
selected_sheet = st.radio(
    "Choose sheet to view",
    options=list(sheet_urls.keys()),
    horizontal=True,
)

st.markdown(
    "<div style='text-align:center; margin: 1rem 0;'>"
    "Please navigate to the tab named <b>REGULAR CP_30D</b> in the embedded sheet below."
    "</div>",
    unsafe_allow_html=True
)

# Embed the selected Google Sheet
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
            overflow: auto;
            background: #fff;"
        allowfullscreen
        loading="lazy"
    ></iframe>
    """,
    height=800,
    width=1920,
    scrolling=True,
)
