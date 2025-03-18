import streamlit as st

st.title('سلام')

text_empty = st.empty()

button_empty = st.empty()

if button_empty.button('إضغط'):
    text_empty.write('لقد ضغطت على الزر')
    
    if st.button('حذف'):
        button_empty.empty()
        text_empty.empty()
