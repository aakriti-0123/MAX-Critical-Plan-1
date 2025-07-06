import streamlit as st
import pandas as pd

password = st.text_input("Enter Admin Password", type="password")
admin_pass = st.secrets.get("ADMIN_PASS")

if admin_pass is None:
    st.error("Secret ADMIN_PASS not set!")
elif password == admin_pass:
    uploaded_files = st.file_uploader("Upload up to 3 Excel calendar files", type="xlsx", accept_multiple_files=True)
    
    if uploaded_files:
        if len(uploaded_files) > 3:
            st.error("Please upload only up to 3 files.")
        else:
            uploaded_calendars = {}

            for file in uploaded_files:
                season_name = file.name.split(".")[0]  # e.g. "WN26"
                xls = pd.ExcelFile(file)
                sheet_data = {sheet: xls.parse(sheet, header=None) for sheet in xls.sheet_names}
                uploaded_calendars[season_name] = sheet_data

            st.session_state['uploaded_calendars'] = uploaded_calendars
            st.success("Calendars uploaded and stored successfully.")
else:
    st.warning("Admin access required to upload files.")
