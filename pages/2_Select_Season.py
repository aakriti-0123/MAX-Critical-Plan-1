import streamlit as st
import pandas as pd
import re

st.title("Select Season and View Options")

# Ensure calendars are uploaded
uploaded = st.session_state.get("uploaded_calendars", {})
if not uploaded:
    st.warning("No calendars found. Please upload them on the Upload page.")
    st.stop()

season = st.selectbox("Select Season", options=list(uploaded.keys()))
launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])

# Get all sheet names from uploaded file
sheet_names = list(uploaded[season].keys())
cp_regex = re.compile(r"(REGULAR CP|QR)[ _](\d+D)", re.IGNORECASE)
cp_timelines = set()

for name in sheet_names:
    match = cp_regex.search(name)
    if match:
        cp_type, cp_value = match.groups()
        if (launch_type == "Regular" and "REGULAR" in cp_type.upper()) or \
           (launch_type == "Quick Response" and "QR" in cp_type.upper()):
            cp_timelines.add(cp_value)

cp_timelines = sorted(cp_timelines, key=lambda x: int(x[:-1]))
if not cp_timelines:
    st.error("No CP timelines available for this launch type.")
    st.stop()

cp = st.selectbox("Select CP Timeline", cp_timelines)

# OK button to store selection
if st.button("OK"):
    st.session_state['calendar_selection'] = {
        "season": season,
        "launch_type": launch_type,
        "cp": cp
    }
    st.success("Selection stored successfully!")
