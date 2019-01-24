#!/usr/local/bin/python3
from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry('400x400')
window.title('working with buttons')
window.configure(background='black') 

lbl1 = Label(window, text="please click button")
lbl1.grid(column=0, row=0)

numbers = ("Choose number", 1, 2, "three", "four", 5)
select1 = ttk.Combobox(window, values=numbers, width=20)
select1.current(0)
select1.grid(column=1, row=0)



def hasClicked():
    msg = "I selected " + select1.get()
    lbl1.configure(text=msg)
btn1 = Button(window, text="submit", command=hasClicked)
btn1.grid(column=1, row=1)
window.mainloop()