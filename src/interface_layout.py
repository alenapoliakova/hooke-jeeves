# -*- coding: utf8 -*-
import time
import tkinter
import random
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Combobox
from algorithm import HookJeeves

root = Tk() # окно приложения (x1 + x2) ^ 2 + (x2 - 1) ^ 2

def start_click():
    algo = HookJeeves(entry.get(), {"x1": random.randint(1, 10), "x2": random.randint(1, 10)}, 2, float(entry_accuracy.get()))
    algo.solve()
    display.insert(INSERT, f"{algo.current_point=} {algo.current_step}")
    answer_entry.insert(INSERT, f"{algo.current_point=} {algo.current_step}")


def stop_click():
    display.delete(1.0, END)
    display.insert(INSERT, 'Solution:\n')


root['bg'] = '#fafafa'
root.title("The Hooke-Jeeves")
root.wm_attributes('-alpha', 1)  # прозрачность
root.geometry('600x500')
root.resizable(width=False, height=False)

frame = Frame(root, bg='green')
frame.place(height=50, relwidth=1)

title = Label(
    text='Coded and Designed by Malinnik team',
    background='green',
    foreground='white',
    width=60,
)
title.place(x=260, y=16)
title = Label(
    text='The Hooke-Jeeves',
    background='green',
    foreground='white',
    font=40,
)
title.place(x=20, y=10)


display = scrolledtext.ScrolledText(bg="white")
display.place(x=20, y=60, width=560, height=300)
display.insert(INSERT, 'Solution:\n')

title = Label(
    text='Enter equality:', background='white', foreground='Black'
)
title.place(x=20, y=380)
entry = Entry(bg='white', width=40)
entry.place(x=140, y=382)
minimum = Radiobutton(text="Minimum", value="Minimum", background='white')
minimum.place(x=450, y=365)
maximum = Radiobutton(text="Maximum", value="Maximum", background='white')
maximum.place(x=450, y=385)

start = Button(
    text='Начать', bg='green', foreground='white', command=start_click
)
start.place(x=20, y=445, width=110, height=30)
stop = Button(
    text='Остановить', bg='red', foreground='white', command=stop_click
)
stop.place(x=140, y=445, width=110, height=30)

background1 = Label(text='', background='white smoke', foreground='Black')
background1.place(x=290, y=445, width=290, height=30)
answer = Label(text='Ответ:', background='white smoke', foreground='Black')
answer.place(x=300, y=450)
answer_entry = Entry(bg='white', width=37)
answer_entry.place(x=345, y=450)

title_accuracy = Label(
    text='Enter accuracy:', background='white', foreground='Black'
)
title_accuracy.place(x=20, y=410)
entry_accuracy = Entry(bg='white', width=40)
entry_accuracy.place(x=140, y=410)

root.mainloop()
