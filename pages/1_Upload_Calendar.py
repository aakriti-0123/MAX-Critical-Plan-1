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
            processed = {}
            for f in uploaded_files:
                try:
                    df_dict = pd.read_excel(f, sheet_name=None)
                    season_key = f.name.split(".")[0]
                    processed[season_key] = df_dict
                except Exception as e:
                    st.error(f"Failed to read {f.name}: {e}")
            st.session_state['uploaded_calendars'] = processed
            st.success("Calendars uploaded and stored successfully.")
else:
    st.warning("Admin access required to upload files.")
