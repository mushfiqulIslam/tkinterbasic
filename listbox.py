import tkinter
from tkinter import *


def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print ('You selected item %d: "%s"' % (index, value))

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Window")
    root.geometry("200x200")

    #ListBox
    lb = Listbox(root)
    lb.insert(1, "Dhaka")
    lb.insert(2, "Comilla")
    lb.insert(3, "Chittagong")
    lb.bind('<<ListboxSelect>>', onselect)
    lb.place(relx=0.5, rely=0.5, anchor="center")
    root.mainloop()
