from tkinter import *
import time
from playsound import playsound
import pygame


class audio:
    def __init__(self, window):
        self.window   = window
        self.frame    = Frame(self.window)
        self.window.geometry('400x150')
        self.window.title("Audio Player")

        self.label    = Label(self.frame, text="steve.mp3", width=40)
        self.label.pack(side=LEFT)

        self.button   = Button(self.frame, text="play", width=10, height=50, command=self.play)
        self.button.pack(side=LEFT)
        self.frame.pack()

    def play(self):
        print("playing")

        #playsound("sound.mp3")#sound.mp3
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("sounds.mp3")
        pygame.mixer.music.play()
        print("finish")


def main():
    root  = Tk()
    app   = audio(root)
    root.mainloop()

if __name__ == '__main__':
    main()
