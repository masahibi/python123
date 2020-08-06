from tkinter import *

before = [100, 100]

def line(x1, y1, x2, y2):
    global canvas
    canvas.create_line(x1, y1, x2, y2)

def on_click(event):
    global canvas
    global before
    x = event.x
    y = event.y
    line(before[0], before[1], x, y)
    before[0] = x
    before[1] = y

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.bind("<Button-1>", on_click)

canvas.mainloop()
