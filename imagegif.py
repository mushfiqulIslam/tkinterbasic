from tkinter import *



root = Tk()
root.title("Window")
root.geometry("1300x500")

#GIF, PGM, PPM
imgicon = PhotoImage(file=r'image.gif')
img = Label(root, image=imgicon)
img.place(x=50, y=0)
root.mainloop()
