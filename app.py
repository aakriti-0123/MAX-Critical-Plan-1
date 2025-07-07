import streamlit as st
import os

st.set_page_config(page_title="MAX Critical Calendar", layout="wide")

# Inject custom CSS for no scroll and fixing page height
custom_css = """
<style>
body, .main, .block-container, .stApp {
    overflow: hidden !important;
    height: 100vh !important;
    min-height: 100vh !important;
    max-height: 100vh !important;
}
.stApp {
    padding: 0 !important;
}
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}
.stSidebar {
    min-height: 100vh !important;
    max-height: 100vh !important;
}
</style>
"""

# Inject custom CSS from file (theme) and additional no-scroll CSS
with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar logo
st.sidebar.image("Assets/MAX_Logo1.png", width=140)
st.sidebar.markdown("## MAX Critical Plan App")
st.sidebar.markdown("Navigate across seasons in Calendar view.")

# Main content with smaller, sharper hero image and text block
st.markdown("""
    <div style='position: relative; text-align: center; margin-top: -10px; margin-bottom: 0;'>
        <img src="https://raw.githubusercontent.com/aakriti-0123/MAX-Critical-Plan-1/main/Assets/Picture2.png" 
             alt="Fashion Hero" 
             style="width: 420px; max-width: 90vw; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.12);" />
        <div style='
            position: relative;
            background-color: rgba(255, 255, 255, 0.92);
            margin: 1.5rem auto 0 auto;
            padding: 1rem 2rem;
            border-radius: 12px;
            max-width: 520px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            display: inline-block;
        '>
            <h1 style='margin: 0; font-size: 2.2rem;'>Welcome to the MAX Critical Plan Calendar</h1>
            <p style='font-size: 1.1rem; margin-top: 0.5rem;'>
                This dashboard helps visualize apparel launch timelines across seasons, hits, and launch types.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)
