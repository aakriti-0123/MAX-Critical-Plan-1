import streamlit as st
import pandas as pd
import re

st.set_page_config(layout="wide")
st.title("📅 Visual Calendar")

# 🔄 Full-screen toggle
full_screen = st.checkbox("🔳 Expand to full screen view", value=False)
if full_screen:
    st.markdown("""<style> .block-container { padding-top: 1rem; padding-left: 2rem; padding-right: 2rem; } </style>""", unsafe_allow_html=True)

# 📁 Retrieve uploaded data
uploaded = st.session_state.get("uploaded_calendars", {})
selection = st.session_state.get("calendar_selection", {})

if not uploaded or not selection:
    st.warning("Please upload calendars and complete selection.")
    st.stop()

season = selection["season"]
hit = selection["hit"]
launch_type = selection["launch_type"]
cp = selection["cp"]

excel_file = uploaded[season]
if isinstance(excel_file, dict):  # already parsed
    sheets = excel_file
else:
    try:
        sheets = pd.read_excel(excel_file, sheet_name=None, header=None)
        st.session_state["uploaded_calendars"][season] = sheets
    except:
        st.error("Couldn't read Excel file.")
        st.stop()

# 🧠 Match correct sheet
cp_tag = f"{'REGULAR CP' if launch_type == 'Regular' else 'QR'}_{cp}"
matched_sheet = None
for name in sheets:
    if cp_tag.upper() in name.upper():
        matched_sheet = name
        break

if not matched_sheet:
    st.error("No sheet found for selected CP and Launch Type.")
    st.stop()

df = sheets[matched_sheet].copy().fillna("")
header_rows = df.iloc[0:3].fillna("")
body = df.iloc[3:].fillna("")

# 🗓️ Format date columns
def format_date(val):
    try:
        val = pd.to_datetime(val)
        return val.strftime('%d-%b-%Y')
    except:
        return val if str(val).strip().lower() != "none" else ""

body = body.applymap(format_date)

# 🧱 Collapse repeated milestone labels
for col in [0, 1]:  # Group columns
    body.iloc[:, col] = body.iloc[:, col].mask(body.iloc[:, col] == body.iloc[:, col].shift())

# 🔀 Merge header + body
calendar = pd.concat([header_rows, body], ignore_index=True)

# 🧾 Generate styled HTML
def generate_calendar_html(df):
   def generate_calendar_html(df):
    html = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-family: Poppins;
        }
        td, th {
            font-size: 13px;
            border: 1px solid #ccc;
            text-align: center;
            padding: 6px;
        }
        .month { font-weight: bold; background-color: #fceeee; }
        .hit { font-weight: bold; background-color: #f9f0f0; }
        .bold { font-weight: bold; }
        .left-label { font-weight: bold; text-align: left; padding-left: 10px; }
        .divider { border-right: 2px solid #222 !important; }
    </style>
    <table>
    """

    prev_month = None
    prev_hit = None
    month_row = df.iloc[1]
    hit_row = df.iloc[2]

    for i, row in df.iterrows():
        html += "<tr>"
        for j, cell in enumerate(row):
            val = "" if pd.isna(cell) or str(cell).lower() == "none" else str(cell)

            css_class = ""
            # Blank out repeating MONTHS and HIT headers
            if i == 1:  # Month row
                if j > 1 and val == prev_month:
                    val = ""
                else:
                    prev_month = val
                css_class = "month"
            elif i == 2:  # Hit row
                if j > 1 and val == prev_hit:
                    val = ""
                else:
                    prev_hit = val
                css_class = "hit"
            elif i >= 4 and j in [0, 1]:
                css_class = "left-label"
            elif val in ["GRN DATE", "LAUNCH WK", "LAUNCH DATE", "Launch Sequence", "MONTHS", "HIT"]:
                css_class = "bold"

            # Add month divider if month changes ahead
            if i >= 1 and j > 1 and j < len(row) - 1:
                this_month = str(month_row[j])
                next_month = str(month_row[j + 1])
                if this_month != next_month:
                    css_class += " divider"

            html += f"<td class='{css_class}'>{val}</td>"
        html += "</tr>"

    html += "</table>"
    return html


# ✅ Show final calendar
calendar_html = generate_calendar_html(calendar)
st.markdown(calendar_html, unsafe_allow_html=True)
