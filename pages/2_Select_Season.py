import streamlit as st

st.title("Select Season and View Options")
uploaded = st.session_state.get("uploaded_calendars", {})

if not uploaded:
    st.warning("No calendars found. Please upload them on the Upload page.")
    st.stop()

season = st.selectbox("Select Season", options=list(uploaded.keys()))
season_prefix = season[:2].upper()

hit_options = ["All"]
hit_options += [f"Hit {i}" for i in range(1, 8)] if season_prefix == "SS" else [f"Hit {i}" for i in range(1, 6)]
hit = st.selectbox("Select Hit", options=hit_options)

launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])
timeline_options = ["90D", "120D", "105D", "75D", "60D", "45D", "30D"] if launch_type == "Regular" else ["75D", "60D", "45D", "30D"]
cp = st.selectbox("Select CP Timeline", timeline_options)

st.session_state['calendar_selection'] = {
    "season": season,
    "hit": hit,
    "launch_type": launch_type,
    "cp": cp
}

st.success("Selection stored. Go to 'Visual Calendar' to see the result.")
