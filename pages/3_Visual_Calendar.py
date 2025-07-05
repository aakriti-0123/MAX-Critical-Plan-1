import streamlit as st
import pandas as pd

st.title("📅 Calendar View")

uploaded_calendars = st.session_state.get("uploaded_calendars", {})
calendar_keys = list(uploaded_calendars.keys())

if not calendar_keys:
    st.warning("⚠️ No calendars uploaded. Please go to the 'Upload Calendar' page.")
else:
    selected_calendar = st.selectbox("Select calendar to view", calendar_keys)
    excel_file = uploaded_calendars.get(selected_calendar)

    if excel_file:
        try:
            # Read Excel file from 3rd row (header=2)
            df = pd.read_excel(excel_file, header=2, dtype=str)
            df = df.fillna("")

            # Format any dates to DD-MMM-YYYY
            for col in df.columns:
                try:
                    df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime('%d-%b-%Y').fillna(df[col])
                except:
                    pass

            # Collapse merged-looking cells: only first value shows
            def collapse_merged_cells(row):
                new_row = []
                prev = None
                for val in row:
                    if val == prev:
                        new_row.append("")
                    else:
                        new_row.append(val)
                        prev = val
                return new_row

            df = df.apply(collapse_merged_cells, axis=1, result_type='expand')

            # Fix column headers (remove 'Unnamed', keep blanks)
            cleaned_cols = []
            for col in df.columns:
                if "Unnamed" in str(col) or str(col).strip() == "":
                    cleaned_cols.append("&nbsp;")  # HTML blank
                else:
                    cleaned_cols.append(str(col))
            df.columns = cleaned_cols

            # Generate HTML table
            def style_row(row):
                return ''.join(
                    f"<td style='border:1px solid #ddd; padding:8px; min-width:90px; text-align:center'>{cell if cell else ''}</td>"
                    for cell in row
                )

            table_html = "<style>td, th {font-family: Poppins; font-size:14px;}</style>"
            table_html += "<table style='border-collapse:collapse; width:100%; background-color:#fef8f5'>"

            # Header
            table_html += "<tr>" + ''.join(
                f"<th style='border:1px solid #ddd; padding:8px; background-color:#f9e4e0'>{col}</th>"
                for col in df.columns
            ) + "</tr>"

            # Rows
            for _, row in df.iterrows():
                table_html += "<tr>" + style_row(row) + "</tr>"

            table_html += "</table>"

            st.markdown(table_html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Failed to load calendar: {e}")
