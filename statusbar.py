from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Hello This is Window")
root.geometry("200x300")

status = Label(root, text="New Status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()
