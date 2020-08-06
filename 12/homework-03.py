from tkinter import *

color = "red"

def circle(x, y, size, start, extent, color):
    global canvas
    canvas.create_arc(x, y, x + size, y + size, start=start, extent=extent, style=CHORD, fill=color)

def on_click(event):
    global canvas
    global color

    x1 = 150    # 円の中心点ｘ座標
    y1 = 150    # 円の中心点ｙ座標
    x2 = event.x
    y2 = event.y
    inside = (x1 - x2) ** 2 + (y1 - y2) ** 2 <= 50 ** 2    # 2点間の距離 （True か False）
    print(inside)

    if inside:
        if color == "red":
            color = "green"
        elif color == "green":
            color = "blue"
        elif color == "blue":
            color = "red"
    circle(100, 100, 100, 0, 359, color)

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
circle(100, 100, 100, 0, 359, color)
canvas.bind("<Button-1>", on_click)
canvas.mainloop()
