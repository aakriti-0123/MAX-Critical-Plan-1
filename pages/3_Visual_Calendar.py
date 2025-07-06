import streamlit as st

# Replace with your actual Excel embed URL
excel_embed_url = "https://docs.google.com/spreadsheets/d/1e9pHXpKBoy5tSl-9MjHTYu0X4dGvoaaT/edit?usp=sharing&ouid=109548826197667239183&rtpof=true&sd=true"

iframe_code = f'''
<iframe src="{excel_embed_url}" width="1000" height="600" frameborder="0"></iframe>
'''

st.markdown(iframe_code, unsafe_allow_html=True)
