import tkinter

if __name__=="__main__":
    root = tkinter.Tk()
    root.title("Window")
    #root.geometry("400x500")

    label = tkinter.Label(root, background="red", width=50).grid(row=0, column=0, sticky='NSEW')
    label2 = tkinter.Label(root, background="green", width=50).grid(row=3, column=0, sticky='NSEW')
    label3 = tkinter.Label(root, background="yellow", width=50).grid(row=5, column=0, sticky='NSEW')


    for x in range(0,3):
        for y in range(0,2):
            root.grid_columnconfigure(x,weight=1)
            root.grid_rowconfigure(y,weight=1)
            
    root.mainloop()
