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

# Main hero image with overlay text
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
        <img src="https://raw.githubusercontent.com/aakriti-0123/MAX-Critical-Plan-1/main/Assets/Picture2.png"
             alt="Fashion"
             style="width: 100%; height: 100%; object-fit: cover;"/>

        <div style='
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background-color: rgba(255,255,255,0.88);
            padding: 1rem 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        '>
            <h2 style='margin: 0; font-size: 1.8rem;'>Welcome to the MAX Critical Plan Calendar</h2>
            <p style='margin-top: 0.5rem; font-size: 1rem;'>
                Visualize apparel launch timelines across seasons, hits, and launch types.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)
