import streamlit as st
import pandas as pd

st.title("📅 Calendar View")

uploaded = st.session_state.get("uploaded_calendars", {})
selection = st.session_state.get("calendar_selection", {})

if not uploaded or not selection:
    st.warning("Please complete upload and selection first.")
    st.stop()

season = selection.get("season")
hit = selection.get("hit")
launch_type = selection.get("launch_type")
cp = selection.get("cp")

season_data = uploaded.get(season)
if not season_data:
    st.error("No data found for selected season.")
    st.stop()

# Match correct sheet
cp_tag = f"{'REGULAR CP' if launch_type == 'Regular' else 'QR'}_{cp}"
sheet_match = None
for name in season_data:
    if cp_tag.upper() in name.upper():
        sheet_match = name
        break

if not sheet_match:
    st.error("No matching timeline found for the selected filters.")
    st.stop()

df = season_data[sheet_match].copy().fillna("")

# Format date cells
for col in df.columns:
    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%d-%b-%Y').fillna(df[col])

# Collapse repeated values (simulate merged cells)
def collapse_row(row):
    prev = None
    new_row = []
    for val in row:
        if val == prev:
            new_row.append("")
        else:
            new_row.append(val)
            prev = val
    return new_row

df = df.apply(collapse_row, axis=1, result_type='expand')

# Clean headers
headers = []
for col in df.columns:
    if "Unnamed" in str(col) or pd.isna(col):
        headers.append("")
    else:
        headers.append(str(col))
df.columns = headers

# Build styled HTML table
def row_html(row):
    return "".join([
        f"<td style='border:1px solid #aaa; padding:6px; text-align:center'>{cell}</td>"
        for cell in row
    ])

table_html = "<style>table { font-family: Poppins; font-size:14px; border-collapse: collapse; }</style>"
table_html += "<table style='width:100%; background-color:#fffaf8;'>"
table_html += "<tr>" + "".join(
    f"<th style='border:2px solid #000; padding:10px; background-color:#f5e4e1'>{col}</th>" for col in df.columns
) + "</tr>"

for _, row in df.iterrows():
    table_html += "<tr>" + row_html(row) + "</tr>"

table_html += "</table>"
st.markdown(table_html, unsafe_allow_html=True)
