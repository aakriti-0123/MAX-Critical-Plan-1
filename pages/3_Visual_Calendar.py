import streamlit as st
import pandas as pd
from io import BytesIO
import re

st.set_page_config(layout="wide")
st.title("📅 Visual Calendar")

# Fullscreen toggle
fullscreen = st.checkbox("Expand to full screen view")

calendar_selection = st.session_state.get("calendar_selection", None)
uploaded = st.session_state.get("uploaded_calendars", {})

if not calendar_selection or not uploaded:
    st.error("Please complete the selection first.")
    st.stop()

season = calendar_selection["season"]
hit = calendar_selection["hit"]
launch_type = calendar_selection["launch_type"]
cp = calendar_selection["cp"]

# Load Excel data
season_file = uploaded.get(season)
if not season_file:
    st.error("No matching calendar file found.")
    st.stop()

if isinstance(season_file, BytesIO):
    season_data = pd.read_excel(season_file, sheet_name=None, header=None)
    st.session_state['uploaded_calendars'][season] = season_data
else:
    season_data = season_file

# Sheet name filter
pattern = f"{launch_type.upper().replace(' ', '_')}_{cp.upper()}"
matching_sheets = [name for name in season_data.keys() if pattern in name.upper()]
if not matching_sheets:
    st.error("No matching timeline found for the selected filters.")
    st.stop()

sheet = season_data[matching_sheets[0]]
sheet = sheet.fillna("")

# Remove time stamp from datetime entries
for col in sheet.columns:
    sheet[col] = sheet[col].apply(lambda x: x.strftime("%d-%b-%Y") if isinstance(x, pd.Timestamp) else x)

# Simulate merged cells by replacing repeated values with ""
def collapse_duplicates(df):
    df = df.copy()
    for row in range(1, len(df)):
        for col in range(len(df.columns)):
            if df.iat[row, col] == df.iat[row - 1, col]:
                df.iat[row, col] = ""
    return df

sheet = collapse_duplicates(sheet)

# Identify bold rows
bold_keywords = ["GRN DATE", "LAUNCH DATE", "LAUNCH WK", "Launch Sequence", "Monthly Drop Split"]
bold_rows = [i for i, row in sheet.iterrows() if any(str(cell).strip().upper() in [kw.upper() for kw in bold_keywords] for cell in row)]

# Identify top header rows for column merging
top_headers = sheet.iloc[0:2].fillna("")
column_labels = []

for col in sheet.columns:
    level1 = str(top_headers.iat[0, col]).strip()
    level2 = str(top_headers.iat[1, col]).strip()
    header = f"<b>{level1}<br>{level2}</b>" if level1 or level2 else ""
    column_labels.append(header)

# Format left header column
merged_left_labels = sheet.iloc[:, 0].copy()
for i in range(1, len(merged_left_labels)):
    if merged_left_labels[i] == merged_left_labels[i - 1]:
        merged_left_labels[i] = ""

# Format row labels bold if needed
row_labels = sheet.iloc[:, 1].copy()
for i in range(len(row_labels)):
    if i in bold_rows:
        row_labels[i] = f"<b>{row_labels[i]}</b>"
    elif pd.isna(row_labels[i]):
        row_labels[i] = ""

# Format cell content
body_data = sheet.iloc[:, 2:]
styled_cells = []

for i in range(body_data.shape[0]):
    row = []
    is_bold = i in bold_rows
    for j in range(body_data.shape[1]):
        val = str(body_data.iat[i, j]).strip()
        val = f"<b>{val}</b>" if is_bold and val else val
        row.append(val or "")
    styled_cells.append(row)

# Assemble final HTML table
table_html = """
<style>
.calendar-table {{
    width: 100%;
    border-collapse: collapse;
    font-family: 'Poppins', sans-serif;
    font-size: 14px;
}}
.calendar-table th, .calendar-table td {{
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
}}
.calendar-table th {{
    background-color: #fceeee;
    font-weight: bold;
}}
.dark-border {{
    border-right: 3px solid #999 !important;
}}
.left-merge {{
    border-left: 3px solid #999 !important;
}}
</style>
<table class="calendar-table">
    <thead>
        <tr>
            <th class="left-merge">Launch &<br>GRN Dates</th>
            <th></th>
"""

# Determine vertical dividers (every 5 columns for month change)
month_breaks = []
for i, label in enumerate(column_labels):
    if any(month in label.upper() for month in ["JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "JAN", "FEB", "MAR", "APR", "MAY", "JUN"]):
        month_breaks.append(i)

for i, col_label in enumerate(column_labels):
    border_class = "dark-border" if i in month_breaks else ""
    table_html += f'<th class="{border_class}">{col_label}</th>'
table_html += "</tr></thead><tbody>"

# Fill in rows
for i in range(len(sheet)):
    table_html += "<tr>"
    left_cell = merged_left_labels[i]
    row_label = row_labels[i]
    table_html += f"<td>{left_cell}</td><td>{row_label}</td>"

    for j, val in enumerate(styled_cells[i]):
        border_class = "dark-border" if j in month_breaks else ""
        table_html += f'<td class="{border_class}">{val}</td>'
    table_html += "</tr>"

table_html += "</tbody></table>"

# Show table
if fullscreen:
    st.markdown(f"<div style='overflow-x:auto;'>{table_html}</div>", unsafe_allow_html=True)
else:
    st.markdown(table_html, unsafe_allow_html=True)
