import streamlit as st
import os

st.set_page_config(page_title="MAX Critical Calendar", layout="wide")

# Inject custom CSS
with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar logo
st.sidebar.image("Assets/MAX_Logo1.png", width=140)
st.sidebar.markdown("## MAX Critical Plan App")
st.sidebar.markdown("Navigate across seasons in Calendar view.")

# Main content with hero image and text block
st.markdown("""
    <div style='position: relative; text-align: center; margin-top: -30px;'>
        <img src="https://raw.githubusercontent.com/aakriti-0123/MAX-Critical-Plan-1/main/Assets/Picture2.png" 
             alt="Fashion Hero" 
             style="width: 90%; border-radius: 12px;"/>
        <div style='
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background-color: rgba(255, 255, 255, 0.85);
            padding: 1rem 2rem;
            border-radius: 12px;
            max-width: 80%;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        '>
            <h1 style='margin: 0; font-size: 2.5rem;'>Welcome to the MAX Critical Plan Calendar</h1>
            <p style='font-size: 1.2rem; margin-top: 0.5rem;'>
                This dashboard helps visualize apparel launch timelines across seasons, hits, and launch types.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)
