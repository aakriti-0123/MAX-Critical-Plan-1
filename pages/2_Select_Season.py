import streamlit as st
import pandas as pd
import re

st.title("Select Season and View Options")

uploaded = st.session_state.get("uploaded_calendars", {})

if not uploaded:
    st.warning("No calendars found. Please upload them on the Upload page.")
    st.stop()

# --- Step 1: Select season ---
season = st.selectbox("Select Season", list(uploaded.keys()))
season_file = uploaded[season]

# If already parsed, don't re-read
if isinstance(season_file, dict):
    season_data = season_file
else:
    try:
        season_data = pd.read_excel(season_file, sheet_name=None)
        st.session_state["uploaded_calendars"][season] = season_data  # cache it
    except Exception as e:
        st.error(f"Error reading Excel: {e}")
        st.stop()
except Exception as e:
    st.error(f"Error reading Excel: {e}")
    st.stop()

sheet_names = list(season_data.keys())

# --- Step 3: Launch Type ---
launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])

# --- Step 4: CP Timelines available ---
if launch_type == "Regular":
    cp_prefix = "REGULAR CP_"
else:
    cp_prefix = "QR_"

cp_sheets = [s for s in sheet_names if s.upper().startswith(cp_prefix.upper())]
cp_options = [s.split("_")[-1] for s in cp_sheets]

if not cp_options:
    st.error("No CP timelines available for this launch type.")
    st.stop()

cp = st.selectbox("Select CP Timeline", cp_options)
selected_sheet = f"{cp_prefix}{cp}"

# --- Step 5: Detect hits from selected sheet ---
try:
    df = season_data[selected_sheet]
    if df.shape[0] < 2:
        st.warning("Selected sheet doesn't have enough rows to detect hits.")
        hit_options = ["All"]
    else:
        first_row = df.iloc[0, 2:]  # Skip first 2 columns
        hit_matches = [m.group(1) for m in [re.search(r"HIT (\d+)", str(val)) for val in first_row] if m]
        hits = sorted(set(hit_matches), key=int)
        hit_options = ["All"] + [f"Hit {h}" for h in hits]
except Exception as e:
    st.error(f"Error detecting hits: {e}")
    hit_options = ["All"]

# --- Step 6: Show hit dropdown ---
hit = st.selectbox("Select Hit", options=hit_options)

# --- Step 7: Store selection ---
if st.button("OK"):
    st.session_state['calendar_selection'] = {
        "season": season,
        "hit": hit,
        "launch_type": launch_type,
        "cp": cp
    }
    st.success("Selection stored.")
