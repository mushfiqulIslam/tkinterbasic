from tkinter import *

root =Tk()

txtBox = Text(root, height=20, width=60, background="white", foreground="red", font=("Arial", 16))
txtBox.insert(END, "Welcome to text Editor")

scroller =Scrollbar(root)
scroller.pack(side=RIGHT, fill=Y)
scroller.config(command=txtBox.yview)

txtBox.config(yscrollcommand=scroller.set)
txtBox.pack()

root.mainloop()
