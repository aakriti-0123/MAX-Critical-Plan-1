import streamlit as st
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

season = st.selectbox("Select Season", options=list(uploaded.keys()))
season_data = uploaded[season].get("data")

if not season_data:
    st.error("Selected season data is not in the correct format.")
    st.stop()

sheet_names = list(season_data.keys())

# Detect hit sheets
hit_pattern = re.compile(rf"{season}[- ]*HIT (\d+)", re.IGNORECASE)
hit_matches = sorted(set(int(m.group(1)) for name in sheet_names if (m := hit_pattern.search(name))))
hit_options = ["All"] + [f"Hit {i}" for i in hit_matches] if hit_matches else ["All"]

hit = st.selectbox("Select Hit", options=hit_options)
launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])

# Match CP sheets
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
