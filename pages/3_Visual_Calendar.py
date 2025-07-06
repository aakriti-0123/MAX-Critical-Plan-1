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

# --- FETCH CALENDAR DATA ---
season_data = st.session_state.get("uploaded_calendars", {}).get(season)
if not season_data:
    st.error("No calendar data found for selected season.")
    st.stop()

# --- FIND MATCHING SHEET ---
launch_key = "REGULAR" if launch_type == "Regular" else "QR"
pattern = re.compile(rf"{launch_key}.*_{cp}", re.IGNORECASE)
sheet_name = next((s for s in season_data if pattern.search(s)), None)
if not sheet_name:
    st.error("No matching timeline found for the selected filters.")
    st.stop()

df = season_data[sheet_name].fillna("").astype(str)

# --- FORMAT DATE COLUMNS TO SHOW DD-MMM ONLY ---
for col in df.columns[2:]:  # Skip row headers
    try:
        parsed = pd.to_datetime(df[col], errors='coerce')
        df[col] = parsed.dt.strftime('%d-%b').where(parsed.notna(), df[col])
    except Exception:
        continue

df.reset_index(drop=True, inplace=True)

# --- CLEAN HEADERS ---
df.columns = ["" if isinstance(col, str) and col.startswith("_") else col for col in df.columns]

# --- SIMULATE MERGED CELLS ---
def merge_repeats(df, axis=0, rows_or_cols=None):
    df_copy = df.copy()
    if rows_or_cols is None:
        rows_or_cols = [0, 1] if axis == 0 else [0, 1]

    if axis == 0:
        for row in rows_or_cols:
            prev = None
            for col in range(2, df.shape[1]):
                curr = df.iloc[row, col]
                if curr == prev:
                    df_copy.iloc[row, col] = ""
                else:
                    prev = curr
    else:
        for col in rows_or_cols:
            prev = None
            for row in df.index:
                curr = df.iloc[row, col]
                if curr == prev:
                    df_copy.iloc[row, col] = ""
                else:
                    prev = curr
    return df_copy

df = merge_repeats(df, axis=0)
df = merge_repeats(df, axis=1)

# --- DETECT MONTH BOUNDARIES ---
def detect_month_boundaries(df):
    first_row = df.iloc[0, 2:]
    boundaries = [i + 2 for i, val in enumerate(first_row) if val != ""]
    return boundaries

month_boundaries = detect_month_boundaries(df)

# --- STYLING FUNCTION ---
def style_calendar(df):
    def bold_rows(row):
        bold_labels = ["GRN DATE", "Launch Sequence", "Monthly Drop Split", "LAUNCH WK", "LAUNCH DATE"]
        return ['font-weight: bold' if row[1] in bold_labels else '' for _ in row]

    styled = df.style.apply(bold_rows, axis=1)
    styled = styled.set_properties(subset=pd.IndexSlice[:, :2], **{"font-weight": "bold"})

    # Inject custom CSS
    css = """
    <style>
    thead tr th:first-child { display: none; }

    .dataframe td, .dataframe th {
        font-size: 12px;
        font-family: 'Poppins', sans-serif;
        border: 1px solid #ddd;
        padding: 4px 6px;
        white-space: nowrap;
        min-width: 85px;
        max-width: 85px;
        width: 85px;
    }
    """

    for col_idx in month_boundaries:
        css += f""".dataframe th:nth-child({col_idx+1}),
                   .dataframe td:nth-child({col_idx+1}) {{
                       border-left: 2px solid black !important;
                   }}"""

    css += "</style>"
    st.markdown(css, unsafe_allow_html=True)
    return styled

# --- DISPLAY FINAL CALENDAR ---
st.dataframe(style_calendar(df), use_container_width=True)
