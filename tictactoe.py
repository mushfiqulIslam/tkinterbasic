from tkinter import *

class Game:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("200x200")
        self.master.title("Tic Tac Toe")
        self.btnList = []
        self.player = 0

        count = 0
        for y in range(0, 3):
            for x in range(0, 3):
                btn = Button(self.frame, text=" ", width=5, height=3, command=lambda count= count:self.click(count))
                btn.grid(row=y, column=x, sticky='NSEW')
                count = count + 1
                self.btnList.append(btn)

        self.frame.pack()

    def click(self, index):
        if self.player == 0:
            self.btnList[index].config(text='X')
            self.player = 1
        else:
            self.btnList[index].config(text='O')
            self.player = 0

    


def main():
    root = Tk()
    app = Game(root)
    root.mainloop()

if __name__ == '__main__':
    main()
