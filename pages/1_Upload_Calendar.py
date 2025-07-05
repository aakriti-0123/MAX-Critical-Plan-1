import streamlit as st

st.title("Upload Launch Calendar Files")
password = st.text_input("Enter Admin Password", type="password")

if password == st.secrets.get("ADMIN_PASS"):
    uploaded_files = st.file_uploader("Upload up to 3 Excel calendar files", type="xlsx", accept_multiple_files=True)
    if uploaded_files:
        if len(uploaded_files) > 3:
            st.error("Please upload only up to 3 files.")
        else:
            st.session_state['uploaded_calendars'] = {f.name.split(".")[0]: f for f in uploaded_files}
            st.success("Calendars uploaded and stored successfully.")
else:
    st.warning("Admin access required to upload files.")
