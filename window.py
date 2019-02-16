import tkinter

def mushfiq():
    # add label
    label = tkinter.Label(root, text="Mushfiqul Islam Chowdhury \n Passionate and Enthusiastic", fg='white', bg='black')
    label.pack(expand=tkinter.TRUE) #for middle
    #label.pack()

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Hello This is Window")
    root.geometry("600x400")

    #add button
    btn = tkinter.Button(root, text="Click Here", command=mushfiq, width=6, height=2, background='blue', foreground='white', state=tkinter.ACTIVE)
    btn.place(x=250, y=200)

    root.mainloop()
