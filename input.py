import tkinter
from tkinter import *


def show():
    label.config(text="Name is " +input.get() +"\n Email is "+input2.get())
    print(input.get())

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Window")
    root.geometry("200x200")

    label = Label(root, text="Name")
    label.grid(row=0, column=0, pady=2)
    #Input
    input = Entry(root)
    input.grid(row=0, column=1, pady=2)#pack(side=RIGHT)

    label2 = Label(root, text="Email")
    label2.grid(row=1, column=0, pady=2)
    #Input
    input2 = Entry(root)
    input2.grid(row=1, column=1, pady=2)

    btn = Button(root, text="show", background='blue', command=show)
    btn.grid(row=2, column=1, pady=2)
    root.mainloop()
