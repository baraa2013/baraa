import tkinter as tk
import random as rd

x = int(rd.randint(1, 98))
print(x)

f = False
t=True

repeat = 5

root = tk.Tk()
root.geometry('700x300')
root.title('خمن الرقم الصحيح')
root.resizable(f, f)

label = tk.Label(root,
                 text='خمن الرقم الصحيح',
                 font=('Arial', 20))
label.pack(side='top')

label2 = tk.Label(root,
                  text='الرقم من 1 إلى 98 \nلديك 5 محاولات',
                  font=('Arial', 9))
label2.pack(side='top')

text = tk.Text(root,
               width=20,
               height=1,
               state='normal')
text.pack(expand = t)

def press():
    global repeat

    text2 = text.get('1.0', tk.END)
    text2 = int(text2)

    if text2 == x:
        label.config(text='أحسنت الرقم صحيح')
        label2.config(text='أغلق التطبيق ثم أعد تشغيله لإعادة اللعبة')
        text.delete('1.0', tk.END)
        text.config(state='disabled')
        b.config(state='disabled')

    elif text2 > x:
        label.config(text='العدد أصغر قليلا')
        repeat -= 1
        print(repeat)
        text.delete('1.0', tk.END)
        label2.config(text=f'الرقم من 1 إلى 98 \nلديك {repeat} محاولات')

    elif text2 < x:
        label.config(text='العدد أكبر قليلا')
        repeat -= 1
        print(repeat)
        text.delete('1.0', tk.END)
        label2.config(text=f'الرقم من 1 إلى 98 \nلديك {repeat} محاولات')

    elif not text2:
        label.config(text='أكتب إجابة')

    if repeat == 0:
        label.config(text=f'لقد خسرت العدد هو {x}')
        b.config(state='disabled')
        label2.config(state='disabled', text='أغلق التطبيق ثم أعد تشغيله لإعادة اللعبة')
    
b = tk.Button(root,
              text='التأكد',
              width=7,
              height=1,
              state='normal',
              command=press)
b.pack(side='bottom')

root.mainloop()