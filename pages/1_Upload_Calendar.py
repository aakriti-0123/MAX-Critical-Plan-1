
import streamlit as st

st.title("Upload Calendar File")
st.markdown("Choose an Excel file to upload.")

password = st.text_input("Enter Admin Password", type="password")
admin_pass = st.secrets["ADMIN_PASS"] if "ADMIN_PASS" in st.secrets else "admin123"

if password == admin_pass:
    uploaded_file = st.file_uploader("Upload Excel Calendar", type=["xlsx"])
    if uploaded_file:
        st.success("File uploaded successfully.")
else:
    st.warning("Admins only.")
