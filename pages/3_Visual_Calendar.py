import streamlit as st
import pandas as pd

st.title("Calendar View")
selection = st.session_state.get("calendar_selection", {})
calendars = st.session_state.get("uploaded_calendars", {})

if not selection or not calendars:
    st.warning("Please complete upload and selection before viewing calendar.")
    st.stop()

excel_file = calendars.get(selection['season'])
if not excel_file:
    st.error("Selected season file not found.")
    st.stop()

df = pd.read_excel(excel_file, header=2)

if selection['hit'] != "All":
    hit_number = selection['hit'].split(" ")[-1]
    hit_cols = [col for col in df.columns if f"Hit {hit_number}" in str(col)]
    display_cols = [df.columns[1]] + hit_cols
    df = df[display_cols]

st.dataframe(df, use_container_width=True)
