import tkinter
from tkinter import *

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Hello This is Window")
    root.geometry("600x400")

    #checkbox
    v1 = tkinter.IntVar()
    v2 = tkinter.IntVar()
    Checkbutton(root, text="Male",variable=v1).grid(row=0, sticky=W)
    Checkbutton(root, text="Female",variable=v2).grid(row=1, sticky=W)

    root.mainloop()
