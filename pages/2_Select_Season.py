import streamlit as st
import pandas as pd
import re

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

# Select season
season = st.selectbox("Select Season", options=list(uploaded.keys()))
season_file = uploaded.get(season)

# Load all sheets for the season if not already parsed
if isinstance(season_file, dict):
    season_data = season_file
else:
    try:
        season_data = pd.read_excel(season_file, sheet_name=None)
        st.session_state['uploaded_calendars'][season] = season_data
    except Exception as e:
        st.error(f"Failed to read Excel file: {e}")
        st.stop()

sheet_names = list(season_data.keys())

# Detect launch type and available CP timelines
launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])
cp_prefix = "REGULAR CP" if launch_type == "Regular" else "QR"

available_cp = [sheet for sheet in sheet_names if sheet.upper().startswith(cp_prefix)]
cp_timelines = sorted(re.findall(r"(\d+D)", " ".join(available_cp)))

if not cp_timelines:
    st.error("No CP timelines available for this launch type.")
    st.stop()

cp = st.selectbox("Select CP Timeline", cp_timelines)

# Detect HITs from the selected CP sheet
cp_sheet_name = f"{cp_prefix}_{cp}"
hit_row = season_data[cp_sheet_name].iloc[2].dropna().astype(str).tolist()
hit_names = [hit for hit in hit_row if f"{season}" in hit and "HIT" in hit.upper()]
hit_numbers = sorted(set(re.findall(r"HIT\s*(\d+)", " ".join(hit_names))))
hit_options = ["All"] + [f"Hit {i}" for i in hit_numbers]

hit = st.selectbox("Select Hit", hit_options)

# Save selection
if st.button("OK"):
    st.session_state['calendar_selection'] = {
        "season": season,
        "hit": hit,
        "launch_type": launch_type,
        "cp": cp
    }
    st.success("Selection stored.")
    st.markdown("➡️ [Go to Calendar View](Visual_Calendar)")
