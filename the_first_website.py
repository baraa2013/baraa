import streamlit as st

text_empty = st.empty()
st.text('سلام')
if st.button('إضغط'):
    text_empty.write('لقد ضغطت على الزر')
    if st.button('حذف'):
        text_empty.empty()