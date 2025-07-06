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

# 1. Load uploaded Excel files
uploaded = st.session_state.get("uploaded_calendars", {})
if not uploaded:
    st.warning("No calendars found. Please upload them on the Upload page.")
    st.stop()

# 2. Season Selection
season = st.selectbox("Select Season", options=list(uploaded.keys()))
season_file = uploaded[season]

# 3. Load all sheets from the Excel file if not already loaded
if isinstance(season_file, dict):
    season_data = season_file
else:
    try:
        season_data = pd.read_excel(season_file, sheet_name=None, header=None)
        st.session_state['uploaded_calendars'][season] = season_data
    except Exception as e:
        st.error(f"Failed to read Excel file: {e}")
        st.stop()

# 4. Extract Hit values from row 2 of each sheet (index 1)
hit_set = set()
for df in season_data.values():
    try:
        row2 = df.iloc[1, 2:]  # Row 2, excluding first two columns
        hit_matches = row2[row2.astype(str).str.contains(rf"{season}\s*-\s*HIT\s+\d+", case=False, na=False)]
        for val in hit_matches.dropna().unique():
            match = re.search(r"HIT\s+(\d+)", str(val), re.IGNORECASE)
            if match:
                hit_set.add(f"Hit {match.group(1)}")
    except Exception:
        continue

hit_options = ["All"] + sorted(hit_set, key=lambda x: int(x.split()[-1])) if hit_set else ["All"]
hit = st.selectbox("Select Hit", options=hit_options)

# 5. Launch Type selection
launch_type = st.radio("Launch Type", ["Regular", "Quick Response"])

# 6. CP timeline detection from sheet names
sheet_names = list(season_data.keys())
cp_regex = re.compile(r"(REGULAR CP|QR)[ _](\d+D)", re.IGNORECASE)
cp_timelines = set()

for name in sheet_names:
    match = cp_regex.search(name)
    if match:
        cp_type, cp_value = match.groups()
        if (launch_type == "Regular" and "REGULAR" in cp_type.upper()) or \
           (launch_type == "Quick Response" and "QR" in cp_type.upper()):
            cp_timelines.add(cp_value)

cp_timelines = sorted(cp_timelines, key=lambda x: int(x[:-1]))  # Sort like 30D, 60D
if not cp_timelines:
    st.error("No CP timelines available for this launch type.")
    st.stop()

cp = st.selectbox("Select CP Timeline", cp_timelines)

# 7. OK button and confirmation
if st.button("OK"):
    st.session_state['calendar_selection'] = {
        "season": season,
        "hit": hit,
        "launch_type": launch_type,
        "cp": cp
    }
    st.success("Selection stored.")
