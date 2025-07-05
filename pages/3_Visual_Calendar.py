import streamlit as st
import pandas as pd

st.title("Calendar View")

uploaded_calendars = st.session_state.get('uploaded_calendars', {})
calendar_keys = list(uploaded_calendars.keys())

if not calendar_keys:
    st.warning("⚠️ No calendars uploaded. Please go to the 'Upload Calendar' page.")
else:
    selected_calendar = st.selectbox("Select calendar to view", calendar_keys)
    excel_file = uploaded_calendars[selected_calendar]

    # Read Excel file (starting from the 3rd row) and load as string to preserve formatting
    df = pd.read_excel(excel_file, header=2, dtype=str)

    # Clean column names: remove 'Unnamed'
    df.columns = ["" if "Unnamed" in str(col) else col for col in df.columns]

    # Format cells to hide timestamps and empty cells
    def format_cell(val):
        try:
            parsed = pd.to_datetime(val)
            return parsed.strftime('%d-%b-%Y')
        except:
            return val if pd.notna(val) else ""

    df = df.applymap(format_cell)

    st.dataframe(df.reset_index(drop=True), use_container_width=True)

