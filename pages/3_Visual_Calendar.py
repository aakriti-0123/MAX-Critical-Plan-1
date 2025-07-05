import streamlit as st
import pandas as pd

st.title("📅 Calendar View")

uploaded_calendars = st.session_state.get("uploaded_calendars", {})
calendar_keys = list(uploaded_calendars.keys())

if not calendar_keys:
    st.warning("⚠️ No calendars uploaded. Please go to the 'Upload Calendar' page.")
else:
    selected_calendar = st.selectbox("Select calendar to view", calendar_keys)
    excel_file = uploaded_calendars.get(selected_calendar)

    if excel_file:
        try:
            # Read Excel from row 3 onward, everything as string
            df = pd.read_excel(excel_file, header=2, dtype=str)

            # Clean up column headers (remove 'Unnamed' etc.)
            cleaned_cols = []
            blank_count = 0
            for col in df.columns:
                if pd.isna(col) or str(col).startswith("Unnamed"):
                    cleaned_cols.append(" " * blank_count)
                    blank_count += 1
                else:
                    cleaned_cols.append(str(col))
            df.columns = cleaned_cols

            # Convert all NaNs and None to empty string
            df = df.fillna("")

            # Format valid date cells to DD-MMM-YYYY
            for col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime('%d-%b-%Y').fillna(df[col])

            # Collapse repeated merged-looking values (left to right across columns)
            def collapse_merged_cells(row):
                new_row = []
                prev = None
                for val in row:
                    if val == prev:
                        new_row.append("")
                    else:
                        new_row.append(val)
                        prev = val
                return new_row

            df = df.apply(collapse_merged_cells, axis=1)

            # Display with clean formatting
            st.dataframe(df.reset_index(drop=True), use_container_width=True)

        except Exception as e:
            st.error(f"❌ Failed to load calendar: {e}")
