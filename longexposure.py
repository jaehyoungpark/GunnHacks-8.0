import imageio
import threading
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image
from PIL import ImageTk
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
import cv2

dst = None
sample_image = None


def VideoPlay(video, label):
    print()

def select_video_file():
    global dst
    filetypes = (
        ('mp4 files', '*.mp4'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        filetypes=filetypes)
    print(filename)

    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    count = 0
    frames = []
    while success:
      frames.append(image)
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1

    dst = frames[0]

    for i in range(1, len(frames), 1):
        print('frame%d.jpg' % i)
        img = frames[i]
        dst = cv2.addWeighted(dst, 0.9, img, 0.1, 0)
    cv2.imshow("result", dst)

def select_image_file():
    filetypes = (
        ('jpg files', '*.jpg'),
        ('All files', '*.*')
    )

    filename = fd.asksaveasfile(
        title='Save as a file',
        filetypes=filetypes)
    print(filename.name)
    cv2.imwrite('%s.jpg' % filename.name, dst)

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Long Exposure photography Converter")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")


        open_button = ttk.Button(
            text='Open a Video File',
            command=select_video_file,
            width=30
        )

        open_button.place(x=150, y=100, height=50)

        save_button = ttk.Button(
            text='Save the Image File',
            command=select_image_file,
            width=30
        )
        save_button.place(x=600, y=100, height=50)
        lbl=Label(root, text="Please Read:", fg='black', bg="#e9e9e9", font=("arial", 30))
        lbl.place(x=100, y=450)
        lbl=Label(root, text='Click the "Open a Video File" button to start', fg='black', bg="#e9e9e9", font=("arial", 20))
        lbl.place(x=100, y=500)
        lbl=Label(root, text="If you have selected a long video(i.e. longer than 20sec), it will take some time", fg='black', bg="#e9e9e9", font=("arial", 20))
        lbl.place(x=100, y=535)
        lbl=Label(root, text='If you want to save the result, click the "Save the Image File" button', fg='black', bg="#e9e9e9", font=("arial", 20))
        lbl.place(x=100, y=570)
        lbl=Label(root, text='Made by: Jaehyoung Park, Kyuhyo Kwon, and Kai Lee', fg='dim gray', bg="#e9e9e9", font=("arial", 15))
        lbl.place(x=100, y=650)

if __name__ == "__main__":

    root = tk.Tk()
    root.title('Gunn Hacks 8.0')
    root.resizable(False, False)
    root.geometry('1000x700')
    app = Example()

    root.mainloop()

root.mainloop()
