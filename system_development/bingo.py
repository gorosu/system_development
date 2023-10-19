import tkinter as tk
import random

def click_btn():
    r = random.randint(1,75)
    if r in rist:
        return click_btn()
        #item.delete('1.0', tk.END)
        #bingo_number['text'] = '??'
        #item.insert(tk.END, 'もう１度PUSHしてください')
    else:
        bingo_number['text'] = r
        bingo_number.update()
        rist.append(r)
        item.delete('1.0', tk.END)
        item.insert(tk.END, str(rist))

root = tk.Tk()
root.title('初めてのビンゴゲーム')
root.resizable(False, False)
root.geometry('1000x800')

label_title = tk.Label(root, text='ビンゴゲーム！', font=('Times New Roman', 24))
label_title.place(x=10, y=10)

bingo_title = tk.Label(root, text='番号', font=('Times New Roman', 30))
bingo_title.place(x=453, y=115)

bingo_number = tk.Label(root, text='??', font=('Times New Roman', 150), bg='white')
bingo_number.place(x=400, y=170)

button = tk.Button(root, text='PUSH', font=('Times New Roman', 35), command=click_btn)
button.place(x=420, y=420)

item = tk.Text(width=80, height=10, font=('Times New Roman', 16))
item.place(x=55, y=540)


rist = []

root.mainloop()





