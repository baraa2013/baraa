import streamlit as st

st.title('سلام')

text_empty = st.empty()

if st.button('إضغط'):
    text_empty.write('لقد ضغطت على الزر')
    
    if st.button('حذف'):
        text_empty.empty()
