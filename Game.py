from tkinter import *
import random
import time
ground_level = 5 #Change this to change the ground level

tk() = Tk()
tk.title("2d Pixel World")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=800, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
