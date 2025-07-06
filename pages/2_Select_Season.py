import streamlit as st
import re
import pandas as pd

st.title("Select Season and View Options")
st.markdown("""
    <style>
        .stButton button {
            background-color: #f2dcdc;
            color: black;
            font-weight: 600;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            border: 1px solid #e6b8b8;
        }
    </style>
""", unsafe_allow_html=True)

uploaded = st.session_state.get("uploaded_calendars", {})
if not uploaded:
    st.warning("No calendars found. Please upload them on the Upload page.")
    st.stop()

season = st.selectbox("Select Season", options=list(uploaded.keys()))

# Ensure uploaded[season] is a dict of sheet_name: DataFrame
if isinstance(uploaded[season], dict):
    sheet_names = list(uploaded[season].keys())
else:
    sheet_names = []

# Detect hits and CP types from sheet names
hit_pattern = re.compile(rf"{season}[- ]*HIT (\d+)", re.IGNORECASE)
hit_matches = sorted(set(int(m.group(1)) for name in sheet_names if (m := hit_pattern.search(name))))
hit_options = ["All"] + [f"Hit {i}" for i in hit_matches]

# Detect CP timelines for each launch type
def extract_cp_sheets(launch_type):
    if launch_type == "Regular":
        cp_pattern = re.compile(rf"{season}.*REGULAR CP_(\d+D)", re.IGNORECASE)
    else:
        cp_pattern = re.compile(rf"{season}.*QR_(\d+D)", re.IGNORECASE)
    return sorted(set(m.group(1) for name in sheet_names if (m := cp_pattern.search(name))))

hit = st.selectbox("Select Hit", options=hit_options)
launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])
available_cps = extract_cp_sheets(launch_type)

if not available_cps:
    st.error("No CP timelines available for this launch type.")
    st.stop()

cp = st.selectbox("Select CP Timeline", available_cps)

if st.button("OK"):
    st.session_state['calendar_selection'] = {
        "season": season,
        "hit": hit,
        "launch_type": launch_type,
        "cp": cp
    }
    st.success("Selection stored. Go to 'Visual Calendar' to see the result.")
