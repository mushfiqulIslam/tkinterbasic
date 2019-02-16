import tkinter
from tkinter import *


def show():
    print(var.get())

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Window")
    root.geometry("200x200")

    #scale
    var = DoubleVar()
    scale = Scale(root, variable=var)
    scale.pack(anchor=CENTER)

    btn = Button(root, text="Numer", command=show)
    btn.pack(anchor=CENTER)

    root.mainloop()
