from tkinter import *
import notepad

class Notepad:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Notepad")
        self.master.geometry("400x600")
        self.menu(self.master)
        self.textbox(self.master)
        self.frame.pack()


    def textbox(self, root):
        self.txtBox = Text(root, height=20, width=60, background="white", foreground="red", font=("Arial", 16))

        self.scroller =Scrollbar(root)
        self.scroller.pack(side=RIGHT)
        self.scroller.config(command=self.txtBox.yview)

        self.txtBox.config(yscrollcommand=self.scroller.set)
        self.txtBox.pack(side=LEFT, fill=Y)

    def newFile(self):
        #self.txtBox.delete('1.0', END)
        notepad.main()

    def menu(self, root):
        menubar = Menu(root)
        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="New", command=self.newFile)#command=someFunc
        fileMenu.add_command(label="Open")
        fileMenu.add_command(label="Save")
        
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=fileMenu)

        aboutMenu = Menu(menubar, tearoff=0)
        aboutMenu.add_command(label="Help")

        root.config(menu=menubar)



def main():
    root = Tk()
    app = Notepad(root)
    root.mainloop()
