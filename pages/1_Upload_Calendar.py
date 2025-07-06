import streamlit as st
import pandas as pd

st.title("📤 Upload Calendar Files")

# Admin password input
password = st.text_input("Enter Admin Password", type="password")
admin_pass = st.secrets.get("ADMIN_PASS")

# Display already uploaded files
if "uploaded_calendars" in st.session_state:
    st.subheader("📂 Uploaded Files")
    for season in st.session_state["uploaded_calendars"]:
        st.markdown(f"- `{season}.xlsx`")

    # Admin-only delete section
    if password == admin_pass:
        if st.button("🗑️ Delete All Uploaded Files"):
            st.session_state.pop("uploaded_calendars", None)
            st.success("All uploaded files have been deleted.")
    else:
        st.info("To delete uploaded files, enter the correct admin password.")

# File upload section
if admin_pass is None:
    st.error("Secret ADMIN_PASS not set!")
elif password == admin_pass:
    uploaded_files = st.file_uploader("Upload up to 3 Excel calendar files", type="xlsx", accept_multiple_files=True)

    if uploaded_files:
        if len(uploaded_files) > 3:
            st.error("Please upload only up to 3 files.")
        else:
            st.session_state['uploaded_calendars'] = {}

            for file in uploaded_files:
                season = file.name.split(".")[0]
                try:
                    parsed_data = pd.read_excel(file, sheet_name=None, header=None)
                    st.session_state['uploaded_calendars'][season] = parsed_data
                except Exception as e:
                    st.error(f"Failed to read {file.name}: {e}")

            st.success("Calendars uploaded successfully.")
else:
    st.warning("Admin access required to upload files.")
