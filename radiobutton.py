import tkinter
from tkinter import *


def cb():
    selected = "Selected " +v.get()
    #print(selected)
    label.config(text=selected)

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Hello This is Window")
    root.geometry("600x400")

    #radiobutton
    v = tkinter.StringVar()

    r1 = Radiobutton(root, text="A",variable=v,value="A", command=cb)#state=DISABLED
    r1.pack(anchor =W)
    r2 = Radiobutton(root, text="B",variable=v, value="B", command=cb)
    r2.pack(anchor =W)

    label =Label(root)
    label.pack()

    root.mainloop()
