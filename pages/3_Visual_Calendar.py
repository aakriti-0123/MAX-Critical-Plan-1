import streamlit as st
import pandas as pd
from io import BytesIO

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
            # Read Excel (start from row index 2, i.e., 3rd row), preserve all as string
            df = pd.read_excel(excel_file, header=2, dtype=str)

            # Clean headers: replace "Unnamed" and NaN with blank
            cleaned_cols = ["" if ("Unnamed" in str(col) or pd.isna(col)) else str(col) for col in df.columns]
            # Remove duplicates manually
            seen = set()
            final_cols = []
            for col in cleaned_cols:
                if col not in seen:
                    final_cols.append(col)
                    seen.add(col)
                else:
                    final_cols.append(col + " ")  # Add space to make it unique

            df.columns = final_cols

            # Format all valid dates to DD-MMM-YYYY, remove time
            for col in df.columns:
                try:
                    df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime('%d-%b-%Y').fillna(df[col])
                except:
                    pass

            # Display calendar cleanly
            st.dataframe(df.reset_index(drop=True), use_container_width=True)

        except Exception as e:
            st.error(f"❌ Failed to load calendar: {e}")
