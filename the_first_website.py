import streamlit as st

st.title('سلام')

text_empty = st.empty()

button_empty = st.empty()

button2_empty = st.empty()

if button_empty.button('إضغط'):
    text_empty.write('لقد ضغطت على الزر')
    button2_empty.button('حذف')

    if button2_empty:
        button2_empty.empty()
        button_empty.button('إضغط')
        text_empty.empty()
