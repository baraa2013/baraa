import streamlit as st
import wikipedia as w
import sys

sys.stdout.reconfigure(encoding='utf-8')
w.set_lang('ar')

st.title('Wiki-AI')
question = st.text_area('أكتب سؤالك', height=68)

if st.button('ارسال'):
     try:
      anser = w.summary(question)
      st.text(anser)
      if st.button('اعادة السؤال'):
         st.rerun()
     except w.exceptions.PageError:
        st.error('لم افمم ماذا تقصد')