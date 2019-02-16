import tkinter

if __name__=="__main__":
    root = tkinter.Tk()
    root.title("Window")
    root.geometry("400x500")

    label = tkinter.Label(root, text="hello").grid(row=0, column=0)
    label = tkinter.Label(root, text="hello2").grid(row=0, column=4)
    label = tkinter.Label(root, text="hello3").grid(row=5, column=0)

    root.mainloop()
