import streamlit as st
import pandas as pd

st.title("Upload Calendar Files")

password = st.text_input("Enter Admin Password", type="password")
admin_pass = st.secrets.get("ADMIN_PASS")

if admin_pass is None:
    st.error("Secret ADMIN_PASS not set!")
    st.stop()

if password == admin_pass:
    uploaded_files = st.file_uploader("Upload up to 3 Excel calendar files", type="xlsx", accept_multiple_files=True)

    if uploaded_files:
        if len(uploaded_files) > 3:
            st.error("Please upload only up to 3 files.")
        else:
            if "uploaded_calendars" not in st.session_state:
                st.session_state['uploaded_calendars'] = {}

            for file in uploaded_files:
                season = file.name.split(".")[0]
                try:
                    parsed_data = pd.read_excel(file, sheet_name=None)
                    st.session_state['uploaded_calendars'][season] = {
                        "raw": file,
                        "data": parsed_data
                    }
                except Exception as e:
                    st.error(f"Failed to read {file.name}: {e}")

            st.success("Calendars uploaded and stored successfully.")

    # Display uploaded files
    if "uploaded_calendars" in st.session_state:
        st.subheader("📂 Uploaded Files:")
        for season_name in st.session_state['uploaded_calendars']:
            st.markdown(f"- `{season_name}.xlsx`")

        # Optional: Delete with re-authentication
        if st.checkbox("🗑️ Delete Uploaded Files"):
            del_pass = st.text_input("Re-enter Admin Password to Confirm Deletion", type="password")
            if del_pass == admin_pass:
                st.session_state.pop("uploaded_calendars", None)
                st.success("Uploaded calendars deleted.")
            else:
                st.warning("Incorrect password.")
else:
    st.warning("Admin access required to upload files.")
