import streamlit as st
import pandas as pd
import re

# --- PAGE CONFIG ---
st.set_page_config(page_title="Visual Calendar", layout="wide")

# --- TITLE & FULLSCREEN TOGGLE ---
st.markdown("<h1 style='font-family:Poppins'>📅 Visual Calendar</h1>", unsafe_allow_html=True)
fullscreen = st.checkbox("Expand to full screen view")
if fullscreen:
    st.markdown(
        "<style>.main .block-container {max-width: 100%; padding: 0rem 2rem;}</style>",
        unsafe_allow_html=True
    )

# --- GET SELECTION ---
selection = st.session_state.get("calendar_selection")
if not selection:
    st.error("No selection found. Please go to 'Select Season' and store your filters.")
    st.stop()

season = selection["season"]
hit = selection["hit"]
launch_type = selection["launch_type"]
cp = selection["cp"]

# --- FETCH UPLOADED FILE ---
season_data = st.session_state.get("uploaded_calendars", {}).get(season)
if not season_data:
    st.error("No calendar data found for selected season.")
    st.stop()

# --- FIND MATCHING SHEET ---
pattern = re.compile(rf"{launch_type[:3].upper()}.*{cp.upper()}", re.IGNORECASE)
matched_sheet = next((s for s in season_data if pattern.search(s)), None)

if not matched_sheet:
    st.error("No matching timeline found for the selected filters.")
    st.stop()

df = season_data[matched_sheet].fillna("").astype(str)

# --- CLEAN INDEX & HEADERS ---
df.reset_index(drop=True, inplace=True)
df.columns = ["" if col.startswith("_") else col for col in df.columns]

# --- SIMULATE MERGED CELLS ---
# Merge top repeated headers
for row in [0, 1]:
    prev = ""
    for col in range(2, len(df.columns)):
        val = df.iloc[row, col]
        if val == prev:
            df.iloc[row, col] = ""
        else:
            prev = val

# Merge left repeated labels
for col in range(2):
    prev = ""
    for row in df.index:
        val = df.iloc[row, col]
        if val == prev:
            df.iloc[row, col] = ""
        else:
            prev = val

# --- CUSTOM STYLING ---
def highlight_bold_rows(val, row_label):
    if row_label in ["GRN DATE", "Launch Sequence", "Monthly Drop Split", "LAUNCH WK", "LAUNCH DATE"]:
        return "font-weight: bold"
    return ""

def style_df(df):
    styled = df.style

    # Apply bold to key rows
    for label in ["GRN DATE", "Launch Sequence", "Monthly Drop Split", "LAUNCH WK", "LAUNCH DATE"]:
        row_mask = df.iloc[:, 1] == label
        styled = styled.set_properties(subset=pd.IndexSlice[row_mask, :], **{"font-weight": "bold"})

    # Set left col bold (row headers)
    styled = styled.set_properties(subset=pd.IndexSlice[:, :2], **{"font-weight": "bold"})

    return styled

# --- DARK BORDERS BETWEEN MONTHS ---
def add_month_borders(df):
    header = df.iloc[0]
    month_boundaries = [i for i in range(2, len(header)) if header[i] != ""]
    return month_boundaries

month_lines = add_month_borders(df)

def set_borders(styled_df):
    css = """
    <style>
    thead tr th:first-child { display: none; }
    .dataframe td, .dataframe th {
        border: 1px solid #ccc;
        padding: 8px 12px;
    }
    .dataframe thead tr:nth-child(3) th {
        border-bottom: 3px solid #444 !important;
    }
    """
    for i in month_lines:
        css += f".dataframe td:nth-child({i+1}), .dataframe th:nth-child({i+1}) {{ border-left: 2px solid #000 !important; }}"
    css += "</style>"
    st.markdown(css, unsafe_allow_html=True)

# --- FINAL RENDER ---
styled_df = style_df(df)
set_borders(styled_df)
st.dataframe(styled_df, use_container_width=True)
