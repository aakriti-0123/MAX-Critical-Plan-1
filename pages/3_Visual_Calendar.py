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
            # Read Excel from 3rd row, preserve all values as string
            df = pd.read_excel(excel_file, header=2, dtype=str)

            # Clean column headers: blank out unnamed/NaN columns
            cleaned_cols = []
            blank_count = 0
            for col in df.columns:
                if pd.isna(col) or str(col).startswith("Unnamed"):
                    cleaned_cols.append(" " * blank_count)  # "", " ", "  ", ...
                    blank_count += 1
                else:
                    cleaned_cols.append(str(col))

            df.columns = cleaned_cols

            # Format dates: convert to '10-Jul-2026' if valid date
            for col in df.columns:
                try:
                    df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime('%d-%b-%Y').fillna(df[col])
                except:
                    pass

            # Show clean calendar
            st.dataframe(df.reset_index(drop=True), use_container_width=True)

        except Exception as e:
            st.error(f"❌ Failed to load calendar: {e}")
