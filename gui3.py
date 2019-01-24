#!/usr/local/bin/python3
from tkinter import *
window = Tk()
window.geometry('400x400')
window.title('working with buttons')

lbl1 = Label(window, text='please click button', borderwidth=2, relief="groove")
lbl1.grid(column=0, row=0)

#define the hasClicked function (like actionPerformed from java)
def hasClicked():
    lbl1.configure(text='something happened')
#add the button, like JButton = new JButton("submit")
btn1 = Button(window, text="Submit", command=hasClicked)
btn1.grid(column=0,row=1)

window.mainloop()