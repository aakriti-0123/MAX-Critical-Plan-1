import pandas as pd
import streamlit as st

# Assuming 'selected_calendar' is the dropdown selection and 'uploaded_calendars' has the files
excel_file = st.session_state['uploaded_calendars'][selected_calendar]

# Read Excel file (starting from the 3rd row) and load as string to preserve formatting
df = pd.read_excel(excel_file, header=2, dtype=str)

# Format dates and preserve blank cells
df = df.applymap(lambda x: pd.to_datetime(x).strftime('%d-%b-%Y') if pd.to_datetime(x, errors='coerce') is not pd.NaT else x)
df = df.fillna("")

# Remove 'Unnamed' headers
df.columns = ["" if "Unnamed" in str(col) else col for col in df.columns]

# Display styled table
st.dataframe(df.reset_index(drop=True), use_container_width=True)
