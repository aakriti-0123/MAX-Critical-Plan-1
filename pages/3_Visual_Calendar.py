import streamlit as st

# Replace with your actual Excel embed URL
excel_embed_url = "https://landmarkgroup-my.sharepoint.com/:x:/p/aakriti_verma/EYKrNI1FBKlIou23O79LzvsBns1ocRAGS34jGYyqzCZIrw?e=CSd1jn"

iframe_code = f'''
<iframe src="{excel_embed_url}" width="1000" height="600" frameborder="0"></iframe>
'''

st.markdown(iframe_code, unsafe_allow_html=True)
