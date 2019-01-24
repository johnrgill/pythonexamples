#!/usr/local/bin/python3
from tkinter import *
window = Tk()
window.geometry('400x400')
window.title('working with buttons')
window.configure(background='black') 

lbl1 = Label(window, text="please click button")
lbl1.grid(column=0, row=0)

txtVar1 = StringVar()
txt1 = Entry(window, width=10, textvariable=txtVar1)
txt1.grid(column=1, row=0)
txt1.focus()

def hasClicked():
    msg = "Something has happened to " + txtVar1.get()
    txtVar1.set('')
    lbl1.configure(text=msg)
    
btn1 = Button(window, text="submit", command=hasClicked)
btn1.grid(column=1, row=1)

window.mainloop()