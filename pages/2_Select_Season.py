import streamlit as st

st.markdown("<h1 style='font-family:Poppins,sans-serif;'>📋 Select Season and View Options</h1>", unsafe_allow_html=True)

uploaded = st.session_state.get("uploaded_calendars", {})

if not uploaded:
    st.markdown(
        "<div style='padding:1rem; background-color:#fff0f0; border-radius:10px; color:#b30000;'>"
        "<strong>⚠️ No calendars found.</strong> Please upload them on the Upload page."
        "</div>", unsafe_allow_html=True)
    st.stop()

# --- Step 1: Season Dropdown ---
season = st.selectbox("Select Season", options=list(uploaded.keys()))
season_prefix = season[:2].upper()

# --- Step 2: Auto-Detect Hits from Sheet Names ---
available_sheets = uploaded[season].keys()
hit_names = set()
for name in available_sheets:
    if season in name and "HIT" in name:
        parts = name.split("HIT")
        if len(parts) > 1 and parts[1].strip()[0].isdigit():
            hit_number = parts[1].strip().split()[0]
            hit_names.add(f"Hit {hit_number}")

hit_options = ["All"] + sorted(hit_names, key=lambda x: int(x.split()[1]) if x != "All" else -1)
hit = st.selectbox("Select Hit", options=hit_options)

# --- Step 3: Launch Type and Dynamic CP Dropdown ---
launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])

# Detect available CP timelines
available_cp = []
for sheet in available_sheets:
    if launch_type == "Regular" and sheet.startswith("CP_"):
        available_cp.append(sheet.replace("CP_", ""))
    elif launch_type == "Quick Response" and sheet.startswith("QR_"):
        available_cp.append(sheet.replace("QR_", ""))

if not available_cp:
    st.error(f"❌ No {launch_type} CP timelines found for {season}.")
    st.stop()

cp = st.selectbox("Select CP Timeline", sorted(available_cp, reverse=True))

# --- Step 4: OK Button ---
if st.button("✅ OK / Apply Selection", use_container_width=True):
    st.session_state['calendar_selection'] = {
        "season": season,
        "hit": hit,
        "launch_type": launch_type,
        "cp": cp
    }
    st.markdown(
        "<div style='padding:1rem; background-color:#e6f4ea; border-radius:10px; color:#007000;'>"
        "✅ <strong>Selection stored.</strong> Go to 'Visual Calendar' to see the result."
        "</div>", unsafe_allow_html=True)
