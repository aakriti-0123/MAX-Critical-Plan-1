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
            calendar_data = {}
            for f in uploaded_files:
                try:
                    calendar_data[f.name.split(".")[0]] = pd.read_excel(f, sheet_name=None)
                except Exception as e:
                    st.error(f"Failed to load {f.name}: {e}")
                    st.stop()
            
            st.session_state['uploaded_calendars'] = calendar_data
            st.success("Calendars uploaded and parsed successfully.")
else:
    st.warning("Admin access required to upload files.")
