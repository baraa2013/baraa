t = True
f = False

import wikipedia as w
import sys
from tkinter import *

w.set_lang('ar')
sys.stdout.reconfigure(encoding = 'utf-8')

root = Tk()
root.geometry('700x500')
root.title('Wiki-AI')
root.resizable(f, f)

wiki_ai = Label(root,
                text='Wiki-AI',
                font=('Arial', 15))
wiki_ai.pack(side='top')

def wikipedia():
    النص_داخل_سؤال = سؤال.get('1.0', END)

    if النص_داخل_سؤال:
        try:
            إجابة2 = w.summary(f'\n{النص_داخل_سؤال}', sentences = 2)
        except Exception as e:
            إجابة2 = f'الخطأ : {e}'

        إجابة.config(state='normal')
        إجابة.insert(END, f'السؤال: {النص_داخل_سؤال}\n{إجابة2}')
        إجابة.config(state='disabled')

    if not النص_داخل_سؤال:
      try:
             إجابة.config(state='normal')
             إجابة.insert(END,'أكتب سؤالا')
             إجابة.config(state='disabled')
      except Exception:
          None

def حذف():
    إجابة.config(state='normal')
    إجابة.delete('1.0', END)
    إجابة.config(state='disabled')

    سؤال.delete('1.0', END)

إرسال = Button(root,
               text='إرسال',
               width=6,
               height=1,
               command=wikipedia)
إرسال.pack(side='bottom', pady=10)

delete = Button(root,
                text='حذف',
                width=4,
                height=1,
                command=حذف)
delete.pack(side='bottom')


سؤال = Text(root,
            width=55,
            height=1)
سؤال.pack(side='bottom', pady=40)

إجابة = Text(root,
             width=80,
             height=60,
             state='disabled')
إجابة.pack(expand=t)

root.mainloop()