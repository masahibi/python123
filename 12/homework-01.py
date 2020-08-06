from tkinter import *
import random

def triangle(x, y, w, h):
    global canvas
    canvas.create_line(x, y, x + w, y)
    canvas.create_line(x + w, y, x, y + h)
    canvas.create_line(x, y + h, x, y)

def square(x, y, size):
    global canvas
    canvas.create_rectangle(x, y, x + size, y + size)

def circle(x, y, size, start, extent):
    global canvas
    canvas.create_arc(x, y, x + size, y + size, start=start, extent=extent, style=ARC)

def on_click(event):
    x = event.x
    y = event.y
    value = random.choice([1, 2, 3])
    if value == 1:
        triangle(x, y, 50, 50)
    elif value == 2:
        square(x, y, 50)
    elif value == 3:
        circle(x, y, 50, 0, 359)

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

canvas.bind("<Button-1>", on_click)
canvas.mainloop()


