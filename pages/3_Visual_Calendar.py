import streamlit as st
import pandas as pd

st.title("📅 Calendar View")

# Select the calendar to view
uploaded_calendars = st.session_state.get("uploaded_calendars", {})
calendar_keys = list(uploaded_calendars.keys())

if not calendar_keys:
    st.warning("⚠️ No calendars uploaded. Please go to the 'Upload Calendar' page.")
else:
    selected_calendar = st.selectbox("Select calendar to view", calendar_keys)

    # Read and display the selected Excel calendar
    excel_file = uploaded_calendars.get(selected_calendar)

    if excel_file:
        try:
            df = pd.read_excel(excel_file, header=2, engine="openpyxl")
            st.dataframe(df)
        except Exception as e:
            st.error(f"❌ Failed to read Excel file: {e}")
    else:
        st.warning("⚠️ Selected file not found.")
