import streamlit as st
import re

st.title("Select Season and View Options")

uploaded = st.session_state.get("uploaded_calendars", {})
if not uploaded:
    st.warning("No calendars found. Please upload them first.")
    st.stop()

season = st.selectbox("Select Season", options=list(uploaded.keys()))
season_data = uploaded[season].get("data")

if not season_data:
    st.error("Invalid data format for season.")
    st.stop()

sheet_names = list(season_data.keys())

# HIT Detection
hit_pattern = re.compile(rf"{season}[- ]*HIT (\d+)", re.IGNORECASE)
hit_matches = sorted(set(int(m.group(1)) for name in sheet_names if (m := hit_pattern.search(name))))
hit_options = ["All"] + [f"Hit {i}" for i in hit_matches] if hit_matches else ["All"]
hit = st.selectbox("Select Hit", hit_options)

# Launch Type and CP Timeline
launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])
cp_tag = "REGULAR CP" if launch_type == "Regular" else "QR"
cp_pattern = re.compile(rf"{cp_tag}_(\d+D)", re.IGNORECASE)
available_cps = sorted(set(m.group(1) for name in sheet_names if (m := cp_pattern.search(name))))

if not available_cps:
    st.error("No CP timelines found for this launch type.")
    st.stop()

cp = st.selectbox("Select CP Timeline", available_cps)

if st.button("OK"):
    st.session_state['calendar_selection'] = {
        "season": season,
        "hit": hit,
        "launch_type": launch_type,
        "cp": cp
    }
    st.success("Selection stored.")
    st.markdown("➡️ [Go to Calendar View](./Visual_Calendar)")
