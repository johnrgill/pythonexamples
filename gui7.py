#!/usr/local/bin/python3
from tkinter import *
window = Tk()
window.geometry('400x400')
window.title('working with buttons')
#working with radio buttons
lbl1 = Label(window, text="please check a box")
lbl1.grid(column=0, row=0)

selected1 = StringVar()
radio1 = Radiobutton(window, text='car', value='1', variable=selected1)
radio2 = Radiobutton(window, text='dog', value='2', variable=selected1)
radio3 = Radiobutton(window, text='cat', value='3', variable=selected1)

radio1.grid(column=0, row=1)
radio2.grid(column=1, row=1)
radio3.grid(column=2, row=1)

def hasClicked():
    msg = 'you have selected ' + selected1.get()
    lbl1.configure(text=msg)
    from tkinter import messagebox
    messagebox.showinfo('Info', msg)

    fav = messagebox.askquestion("really?", "are you sure?")
    lbl1.configure(text=fav)



btn1 = Button(window,text='submit', command=hasClicked)
btn1.grid(column=0, row=2)
window.mainloop()