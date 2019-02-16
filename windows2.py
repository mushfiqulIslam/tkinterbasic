#OO way
from tkinter import *

class Demo:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("This is Windows2")
        self.master.geometry("700x600")
        self.frame.pack()
        btn = Button(self.master, text="Click Here", command=self.mushfiq, width=6, height=2, background='blue', foreground='white', state=ACTIVE)
        btn.place(x=250, y=200)

    def mushfiq(self):
        print("This is Mushfiqul")

def main():
    root = Tk()
    app = Demo(root)
    root.mainloop()

if __name__ == '__main__':
    main()
