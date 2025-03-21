import tkinter as tk

root = tk.Tk()
root.geometry('400x300')
root.title('Enter the BOT adress')

label = tk.Label(root,text='Enter the BOT adress', font=('Arial', 30))
label.pack(side='top')
text = tk.Text(root, width=20,height=1)
text.pack(expand=True)

def c():
    t = text.get('1.0', tk.END).strip()
    if '025498001' in t:
      root.destroy()

      bot = tk.Tk()
      bot.geometry('800x400')
      bot.title('BOT 0.2 ALPHA(New version)')

      user_text = tk.Text(bot,
                    width=60,
                    height=1
                    )
      user_text.pack(side='top')

      bot_text = tk.Text(bot,
                   width=90,
                   height=20,
                   state='disabled')
      bot_text.pack(expand=True)
 
      def bot_reponse():
       u = user_text.get('1.0', tk.END).strip()

       user_text.delete('1.0', tk.END)
       if 'سلام' in u:
        bot_text.config(state='normal')
        reponse = 'بوت : وعليكم السلام'
        bot_text.config(state='disabled')

       elif 'شكونك انتي' in u:
        bot_text.config(state='normal')
        reponse = 'انا اسمي بوت\n"v.num"كان تحب تعرف عليا أكثر اكتب'
        bot_text.config(state='disabled')

       elif 'v.num' in u:
        bot_text.config(state='normal')
        bot_text.delete('1.0', tk.END)
        reponse = 'BOT Name : BOT 001\nBOT Version : 0.2 ALPHA(New version)\nBOT Adress : 025498001\nBOT Maker : Baraa'
        bot_text.config(state='disabled')

       else:
        bot_text.config(state='normal')
        reponse = 'بوت : مافهمتش'
        bot_text.config(state='disabled')

       bot_text.config(state='normal')
       bot_text.insert(tk.END, f'أنت : {u}\n{reponse}\n\n')
       bot_text.config(state='disabled')

    else:
       label.config(text='Try again', font=('Arial', 30), fg='red')

       text.config(bg='red')

       co2.config(bg='red')

       root.config(root.title('Try again'))

    co = tk.Button(bot, text='ارسال', command= bot_reponse)
    co.pack(side='bottom')
    bot.mainloop()
   
co2 = tk.Button(root, text='ارسال', command= c)
co2.pack(side='bottom')

root.mainloop()