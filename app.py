import streamlit as st
import os

st.set_page_config(page_title="MAX Critical Path Calendar", layout="wide")

# Custom CSS for no scroll, compact layout, and bigger logo alignment
custom_css = """
<style>
body, .main, .block-container, .stApp {
    overflow: hidden !important;
    height: 100vh !important;
    min-height: 100vh !important;
    max-height: 100vh !important;
    background: #fcf7f5 !important;
}
.stApp {
    padding: 0 !important;
}
.block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
}
.stSidebar {
    min-height: 100vh !important;
    max-height: 100vh !important;
}
#max-main-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    height: 100vh;
}
.max-hero-img {
    width: 320px;
    max-width: 85vw;
    border-radius: 18px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12);
    margin-top: 1.5vh;
    margin-bottom: 1vh;
}
.max-hero-text {
    background-color: rgba(255, 255, 255, 0.96);
    padding: 1.2rem 1.5rem;
    border-radius: 18px;
    max-width: 430px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin: 0 auto;
    text-align: center;
}
.max-hero-text h1 {
    font-size: 1.7rem;
    margin: 0 0 0.6rem 0;
}
.max-hero-text p {
    font-size: 1rem;
    margin: 0;
}
/* Sidebar logo and text alignment */
#max-sidebar-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
}
#max-sidebar-header img {
    width: 220px !important;
    max-width: 80%;
    display: block;
    margin-bottom: 0.5rem;
}
#max-sidebar-header .sidebar-title {
    font-size: 1.35rem;
    font-weight: 700;
    margin: 0.3rem 0 0.4rem 0;
    text-align: center;
}
#max-sidebar-header .sidebar-desc {
    font-size: 1rem;
    text-align: center;
}
</style>
"""

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar logo and info with bigger logo and aligned text
st.sidebar.markdown("""
<div id="max-sidebar-header">
    <img src="https://raw.githubusercontent.com/aakriti-0123/MAX-Critical-Plan-1/main/Assets/MAX_Logo2.png" alt="MAX Logo"/>
    <div class="sidebar-title">MAX Critical Path App</div>
    <div class="sidebar-desc">Navigate across seasons in Calendar view.</div>
</div>
""", unsafe_allow_html=True)

# Main content
st.markdown("""
<div id="max-main-content">
    <img class="max-hero-img" src="https://raw.githubusercontent.com/aakriti-0123/MAX-Critical-Plan-1/main/Assets/Picture2.png" alt="Fashion Hero"/>
    <div class="max-hero-text">
        <h1>Welcome to the MAX Critical Path Calendar</h1>
        <p>
            This dashboard helps visualize apparel launch timelines across seasons, hits, and launch types.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
