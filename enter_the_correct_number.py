import streamlit as st
import random as r

st.title('لعبة احزر الرقم')

x = r.randint(1, 50)

if 'x' not in st.session_state:
    st.session_state.x = x
print(st.session_state.x)

repeats2 = 0

if 'repeats2' not in st.session_state:
    st.session_state.repeats2 = repeats2

anser = st.text_area('أدخل الرقم الصحيح\nالرقم بين 1 و 50', height=68)

button = st.empty()

if button.button('إرسال'):
    try:
            anser = int(anser)
            
            if anser == st.session_state.x:
                button.empty()
                st.success('أحسنت الرقم صحيح\nأعد تشغيل الموقع لإعادة اللعب')

            elif anser > st.session_state.x:
                st.warning('العدد أصغر قليلا')
                st.session_state.repeats2 +=1

            elif anser < st.session_state.x:
                st.warning('العدد أكبر قليلا')
                st.session_state.repeats2 += 1

            if st.session_state.repeats2 == 5:
                st.warning('تبقت لك محاولة واحدة')

            elif st.session_state.repeats2 == 6:
                button.empty()
                st.error(f'انتهت محاولاتك, العدد هو {st.session_state.x}\nأعد تشغيل الموقع لإعادة اللعب')

    except ValueError:
        st.error('الرجاء كتابة عدد صحيح')