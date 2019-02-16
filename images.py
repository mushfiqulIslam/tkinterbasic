from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Window")
root.geometry("1300x800")

#GIF, PGM, PPM
open = Image.open("Pokemon.png")
image = ImageTk.PhotoImage(open)
img = Label(root, image=image)
img.place(x=100, y=0)
root.mainloop()
