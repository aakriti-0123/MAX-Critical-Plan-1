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
season_file = uploaded.get(season)

# Load all sheets from the Excel file if not already done
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

# Detect hits from sheet names
hit_pattern = re.compile(rf"{season}[- ]*HIT (\d+)", re.IGNORECASE)
hit_matches = sorted(set(int(m.group(1)) for name in sheet_names if (m := hit_pattern.search(name))))
hit_options = ["All"] + [f"Hit {i}" for i in hit_matches] if hit_matches else ["All"]

hit = st.selectbox("Select Hit", options=hit_options)
launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])

# Detect CP timelines for each launch type
cp_pattern = re.compile(rf"{season}.*{'REGULAR CP' if launch_type == 'Regular' else 'QR'}_(\d+D)", re.IGNORECASE)
available_cps = sorted(set(m.group(1) for name in sheet_names if (m := cp_pattern.search(name))))

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
