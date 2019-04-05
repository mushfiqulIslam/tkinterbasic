from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("XOXO Phone")

frame = Frame(root, bd=2, relief="sunken")
frame.place(x=30, y=30)

val = ['1','2','3','4','5','6','7','8','9','#','0','*']
index = 0
for x in range(0,4):
    for y in range(0,3):
        btn = Button(frame, text=val[index], width=2, height=2)
        btn.grid(row=x, column=y)
        index = index + 1


root.mainloop()
