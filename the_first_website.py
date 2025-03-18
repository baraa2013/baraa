import streamlit as st

if st.button('إضغط'):
    text_empty.write('لقد ضغطت على الزر')
    
    if st.button('حذف'):
        text_empty.empty()

text_empty = st.empty()
st.title('سلام')
