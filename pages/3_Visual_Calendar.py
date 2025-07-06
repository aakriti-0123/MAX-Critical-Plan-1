import streamlit as st
import pandas as pd

st.title("Calendar View")

uploaded = st.session_state.get("uploaded_calendars", {})
selection = st.session_state.get("calendar_selection", {})

if not uploaded or not selection:
    st.warning("Please upload files and complete selection.")
    st.stop()

season = selection.get("season")
hit = selection.get("hit")
launch_type = selection.get("launch_type")
cp = selection.get("cp")

season_data = uploaded[season].get("data")
if not season_data:
    st.error("Season data not loaded.")
    st.stop()

# Build matching sheet(s)
sheet_matches = []
for name, df in season_data.items():
    if f"{cp_tag := ('REGULAR CP' if launch_type == 'Regular' else 'QR')}_{cp}" in name:
        if hit == "All" or f"{season} - HIT {hit.split()[-1]}" in name:
            sheet_matches.append((name, df))

if not sheet_matches:
    st.error("No matching timeline found for selection.")
    st.stop()

# Display matched calendars
for name, df in sheet_matches:
    st.markdown(f"### 📄 {name}")
    df = df.fillna("")

    # Format date columns
    for col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime('%d-%b-%Y').fillna(df[col])

    # Collapse repeated values across rows
    def collapse_row(row):
        prev = None
        return ["" if val == prev else val for val in row]

    df = df.apply(collapse_row, axis=1, result_type="expand")

    # Clean column headers
    headers = []
    for col in df.columns:
        headers.append("" if "Unnamed" in str(col) or pd.isna(col) else str(col))
    df.columns = headers

    # HTML Table
    def row_html(row):
        return "".join([
            f"<td style='border:1px solid #999; padding:8px; text-align:center'>{cell}</td>"
            for cell in row
        ])

    table_html = "<style>table, th, td { font-family: Poppins; font-size:14px; border-collapse: collapse; }</style>"
    table_html += "<table style='width:100%; background-color:#fffaf8;'>"
    table_html += "<tr>" + "".join(
        f"<th style='border:2px solid #999; padding:10px; background-color:#f5e4e1'>{col}</th>" for col in df.columns
    ) + "</tr>"

    for _, row in df.iterrows():
        table_html += "<tr>" + row_html(row) + "</tr>"

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)
