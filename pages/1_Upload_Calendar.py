import streamlit as st

password = st.text_input("Enter Admin Password", type="password")
admin_pass = st.secrets.get("ADMIN_PASS")

# Debug lines (remove after testing)
st.write(f"Typed password: `{password}`")
st.write(f"Secret password: `{admin_pass}`")

if admin_pass is None:
    st.error("Secret ADMIN_PASS not set!")
elif password == admin_pass:
    uploaded_files = st.file_uploader("Upload up to 3 Excel calendar files", type="xlsx", accept_multiple_files=True)
    if uploaded_files:
        if len(uploaded_files) > 3:
            st.error("Please upload only up to 3 files.")
        else:
            st.session_state['uploaded_calendars'] = {f.name.split(".")[0]: f for f in uploaded_files}
            st.success("Calendars uploaded and stored successfully.")
else:
    st.warning("Admin access required to upload files.")
