import streamlit as st

st.title("📅 Visual Calendar View")

# Get stored selection
selection = st.session_state.get("calendar_selection")
if not selection:
    st.warning("No calendar selection found. Please go to the Selection page.")
    st.stop()

season = selection["season"]
launch_type = selection["launch_type"]
cp = selection["cp"]

# Determine correct sheet name
sheet_name = f"{'REGULAR CP' if launch_type == 'Regular' else 'QR'}_{cp}"

# Google Drive file ID mapping
drive_file_ids = {
    "SS26": "16XNqVsbEYVxUBvRyF9l6EgkT_p5lDvQy",
    "WN25": "1mXSf7Kx89WZb4Off7x3tPa3Buc6QF1Dj",
    "WN26": "1DioMTxZakUrLg5ZjElWo9DcxVPxcqhUN"
}

if season not in drive_file_ids:
    st.error("No file found for selected season.")
    st.stop()

# Final embed URL
embed_url = f"https://docs.google.com/spreadsheets/d/{drive_file_ids[season]}/preview"

# Display title and instructions
st.markdown(f"### Season: `{season}`  |  Sheet: `{sheet_name}`", unsafe_allow_html=True)
st.markdown(f"""
    <p>Please navigate to the tab named <strong>{sheet_name}</strong> in the embedded sheet below.</p>
    <iframe src="{embed_url}" width="100%" height="750" style="border: none;"></iframe>
""", unsafe_allow_html=True)
