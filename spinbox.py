import tkinter
from tkinter import *


def show():
    print(sp.get())

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Window")
    root.geometry("200x200")

    #Spinbox
    sp =Spinbox(root, from_=0, to=100)
    sp.pack(anchor=CENTER)

    btn = Button(root, text="click", command=show)
    btn.pack(anchor=CENTER)

    root.mainloop()
