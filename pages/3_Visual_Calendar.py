
import streamlit as st
import pandas as pd

st.title("Launch Calendar")

season = st.session_state.get("season", "SS26")
hit = st.session_state.get("hit", "Hit 1")
calendar_type = st.session_state.get("launch_type", "Regular")

st.markdown(f"**Season:** {season} &nbsp;&nbsp; **Hit:** {hit} &nbsp;&nbsp; **Type:** {calendar_type}")

df = pd.DataFrame({
    "Milestone": [
        "Trend Presentation", "Merge Direction", "Vendor Week", "Range Build",
        "Tech Handover", "Planning Budget Handover"
    ],
    "Date": [
        "March 3, 2026", "March 10, 2026", "March 17, 2026", "March 24, 2026",
        "March 31, 2026", "April 2, 2026"
    ]
})

st.dataframe(df, use_container_width=True)
