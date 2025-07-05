
import streamlit as st

st.title("Select Calendar")

season_options = ["SS26", "WN25", "WN26"]
season = st.selectbox("Season", season_options)

is_ss = season.startswith("SS")
hit_options = ["All"] + [f"Hit {i}" for i in range(1, 8)] if is_ss else ["All"] + [f"Hit {i}" for i in range(1, 6)]
hit = st.selectbox("Hit", hit_options)

launch_type = st.selectbox("Launch Type", ["Regular", "Quick Response"])

cp_options = ["CP_90D", "CP_120D", "CP_105D", "CP_75D", "CP_60D", "CP_45D", "CP_30D"] if launch_type == "Regular" else ["QR_75D", "QR_60D", "QR_45D", "QR_30D"]
cp_selected = st.selectbox("Calendar Plan Type", cp_options)

if st.button("Generate Calendar"):
    st.session_state["season"] = season
    st.session_state["hit"] = hit
    st.session_state["launch_type"] = launch_type
    st.session_state["cp_type"] = cp_selected
    st.success("Selections saved. Please go to 'Calendar' page.")
