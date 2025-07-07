import streamlit as st
import os

st.set_page_config(page_title="MAX Critical Calendar", layout="wide")

# Inject theme
with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar logo
st.sidebar.image("Assets/MAX_Logo1.png", width=140)
st.sidebar.markdown("## MAX Critical Plan App")
st.sidebar.markdown("Navigate across seasons in Calendar view.")

# Main content block: smaller image + text side by side
st.markdown("""
    <div style='
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 3rem;
        margin-top: 2rem;
        padding: 0 2rem;
        flex-wrap: wrap;
    '>
        <img src="https://raw.githubusercontent.com/aakriti-0123/MAX-Critical-Plan-1/main/Assets/Picture2.png"
             alt="MAX Campaign"
             style="max-width: 480px; height: auto; border-radius: 14px;"/>

        <div style='
            max-width: 500px;
            text-align: left;
        '>
            <h1 style='margin: 0; font-size: 2.2rem;'>Welcome to the MAX Critical Plan Calendar</h1>
            <p style='margin-top: 0.75rem; font-size: 1.1rem; line-height: 1.6;'>
                Visualize apparel launch timelines across seasons, hits, and launch types in one stylish view.
                Navigate easily and stay ahead of critical milestones.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)
