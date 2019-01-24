#!/usr/local/bin/python3
from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry('400x400')
window.title('working with buttons')
window.configure(background='black') 
#working with check boxes
lbl1 = Label(window, text="please check a box")
lbl1.grid(column=0, row=0)

checkVar1 = StringVar()
check1 = Checkbutton(window, text="car", variable=checkVar1)

checkVar2 = StringVar()
check2 = Checkbutton(window, text="dog", variable=checkVar2)

checkVar3 = StringVar()
check3 = Checkbutton(window, text="cat", variable=checkVar3)


check1.grid(column=0, row=1)
check2.grid(column=1, row=1)
check3.grid(column=2, row=1)

def hasClicked():
    msg = "C1: " + checkVar1.get()
    msg += "C2: " + checkVar2.get()
    msg += "C3: " + checkVar3.get()
    lbl1.configure(text=msg)

btn1 = Button(window, text='submit', command=hasClicked)
btn1.grid(column=0, row=2)
window.mainloop()