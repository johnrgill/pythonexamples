#!/usr/local/bin/python3
from tkinter import *
window = Tk()
window.title("Working with labels")
window.minsize(width = 300, height = 300)
window.maxsize(width=400, height = 400)

lbl_name1 = Label(window, text="Hello World", font=("Arial Bold", 20))
lbl_name2 = Label(window, text="")
lbl_name3 = Label(window, text="Over there")
lbl_name4 = Label(window, text="")
lbl_name5 = Label(window, text="wowie wow wow")
lbl_name6 = Label(window, text="another")

lbl_name1.grid(column=0, row=0)
lbl_name2.grid(column=1, row=0)
lbl_name3.grid(column=0, row=1)
lbl_name4.grid(column=1, row=1)
lbl_name5.grid(column=1, row=2)
lbl_name6.grid(column=1, row=2)

window.mainloop()
