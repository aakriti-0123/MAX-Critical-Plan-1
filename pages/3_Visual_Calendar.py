import streamlit as st
import pandas as pd
from pandas.io.parsers import ParserBase
from io import BytesIO

st.title("Calendar")

# Load uploaded files from session
uploaded_calendars = st.session_state.get("uploaded_calendars", {})
calendar_keys = list(uploaded_calendars.keys())

# Dropdown to select calendar
if not calendar_keys:
    st.warning("⚠️ No calendars uploaded. Please go to the 'Upload Calendar' page.")
else:
    selected_calendar = st.selectbox("Select calendar to view", calendar_keys)
    excel_file = uploaded_calendars.get(selected_calendar)

    if excel_file:
        try:
            # Read Excel (from 3rd row)
            df = pd.read_excel(excel_file, header=2, dtype=str)

            # Remove time from any datetime cells
            for col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='ignore').map(
                    lambda x: x.strftime('%d-%b-%Y') if pd.notna(x) and isinstance(x, pd.Timestamp) else x
                )

            # Clean column headers: show blank instead of "Unnamed" and remove suffixes
            cleaned_cols = [" " if "Unnamed" in str(c) or pd.isna(c) else c for c in df.columns]
            df.columns = ParserBase({'names': cleaned_cols})._maybe_dedup_names(cleaned_cols)

            # Display formatted calendar
            st.dataframe(df.reset_index(drop=True), use_container_width=True)

        except Exception as e:
            st.error(f"❌ Failed to read calendar: {e}")
