# 練習問題１
# from tkinter import *
#
#
# def triangle(x, y, w, h):
#     canvas.create_line(x, y, x + w, y)
#     canvas.create_line(x + w, y, x, y + h)
#     canvas.create_line(x, y + h, x, y)
#
#
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# triangle(100, 100, 200, 300)
# canvas.mainloop()  # 処理の後に書く


'-------------------------------------------------'
# # 練習問題２
# from tkinter import *
#
#
# def triangle(x, y, w, h):
#     canvas.create_line(x, y, x + w, y)
#     canvas.create_line(x + w, y, x, y + h)
#     canvas.create_line(x, y + h, x, y)
#
#
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# for x in range(5):
#     triangle(100 + x*5, 100 + x*5, 100 - x*15, 100 - x*15)
# canvas.mainloop()  # 処理の後に書く

'-------------------------------------------------'
# # 練習問題３
# from tkinter import *
#
#
# def tile(x, y, size):
#     global canvas  # グローバル変数canvasのキャンバスを使うことを明示
#     canvas.create_rectangle(x, y, x + size, y + size)
#     canvas.create_rectangle(x, y, x + size / 2, y + size / 2, fill="black")
#     canvas.create_rectangle(x + size / 2, y + size / 2, x + size, y + size, fill="black")
#
#
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# tile(100, 100, 200)
# canvas.mainloop()  # 処理の後に書く

'--------------------------------------------------------------'
# 練習問題4
# from tkinter import *
#
#
# def convert16(value):
#     return f"{int(value * 255) :02x}"  # 16進数に変換 02x=2桁
#
#
# def convertRGB(r, g, b):
#     return f"#{convert16(r)}{convert16(g)}{convert16(b)}"  # rgb の値をとれる
#
#
# def tile(x, y, size, lcolor, rcolor):
#     global canvas  # グローバル変数canvasのキャンバスを使うことを明示
#     canvas.create_rectangle(x, y, x + size, y + size)
#     canvas.create_rectangle(x, y, x + size / 2, y + size / 2, fill=rcolor)
#     canvas.create_rectangle(x + size / 2, y + size / 2, x + size, y + size, fill=lcolor)
#
#
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# tile(100, 100, 200, convertRGB(0, 0, 1), convertRGB(0, 1, 0))
# canvas.mainloop()  # 処理の後に書く

'--------------------------------------------------------------------'
# 練習問題５
# from tkinter import *
#
#
# def square(x, y, size):
#     global canvas  # グローバル変数canvasのキャンバスを使うことを明示
#     canvas.create_rectangle(x, y, x + size, y + size)
#
#
# def circle(x, y, size, start, extent):    # 四角形に内接する円（概念）
#     canvas.create_arc(x, y, x + size, y + size, start=start, extent=extent, style=ARC)    # start=始めの角度  extant=何度進むか
#                                                                                                       # style=とりあえず書く
#
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# square(100, 100, 200)
# circle(0, 100, 200, -90, 180)
# circle(200, 100, 200, 90, 180)
# canvas.mainloop()  # 処理の後に書く

'--------------------------------------------------'
# 練習問題６,7
# from tkinter import *
#
#
# def square(x, y, size):
#     global canvas  # グローバル変数canvasのキャンバスを使うことを明示
#     canvas.create_rectangle(x, y, x + size, y + size)
#
#
# def circle(x, y, size, start, extent):  # 四角形に内接する円（概念）
#     canvas.create_arc(x, y, x + size, y + size, start=start, extent=extent, style=ARC)  # start=始めの角度  extant=何度進むか
#     # style=とりあえず書く
#
#
# def polygon(ps, fill, outline):  # ps=リスト
#     global canvas
#     canvas.create_polygon(ps[0][0], ps[0][1], ps[1][0], ps[1][1], ps[2][0], ps[2][1], ps[3][0], ps[3][1], ps[4][0], ps[4][1],
#                           ps[5][0], ps[5][1], ps[6][0], ps[6][1], ps[7][0], ps[7][1], fill=fill, outline=outline)
#
#
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# # square(100, 100, 300)
# ps = [[200, 200], [250, 100], [300, 200], [400, 250], [300, 300], [250, 400], [200, 300], [100, 250]]
# polygon(ps, fill="gray", outline="gray")
# canvas.mainloop()  # 処理の後に書く

'-----------------------------------------------------------------'
# 練習問題８
# from tkinter import *
#
#
# def square(x, y, size):
#     global canvas  # グローバル変数canvasのキャンバスを使うことを明示
#     canvas.create_rectangle(x, y, x + size, y + size)
#
#
# def circle(x, y, size, start, extent):  # 四角形に内接する円（概念）
#     canvas.create_arc(x, y, x + size, y + size, start=start, extent=extent, style=ARC)  # start=始めの角度  extant=何度進むか
#     # style=とりあえず書く
#
#
# def polygon(ps, fill, outline):  # ps=リスト
#     global canvas
#     canvas.create_polygon(ps[0][0], ps[0][1], ps[1][0], ps[1][1], ps[2][0], ps[2][1], ps[3][0], ps[3][1], fill=fill, outline=outline)
#
#
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# ps = [[100, 100], [200, 100], [200, 200], [100, 200]]
# canvas.create_polygon(ps[0][0], ps[0][1], ps[1][0]-50, ps[1][1], ps[2][0]-50, ps[2][1], ps[3][0], ps[3][1], fill="", outline="black")
# canvas.create_polygon(ps[0][0], ps[0][1], ps[1][0], ps[1][1], ps[2][0], ps[2][1], ps[3][0], ps[3][1], fill="", outline="black")
# canvas.create_text(150, 120, text="左揃え", anchor=W)
# canvas.create_text(150, 150, text="中央揃え")
# canvas.create_text(150, 180, text="右揃え", anchor=E)
# canvas.create_text(150, 180, text="右揃えS", anchor=S)
# canvas.create_text(150, 180, text="右揃えN", anchor=N)
# canvas.mainloop()  # 処理の後に書く

'-----------------------------------------------------------------------'
# 演習問題１、ヒント
from tkinter import *


def on_click(event):    # イベントハンドラはon_をつける    # 書き方は決まり
    global counter    # global変数を使えるようになる(関数を出ても保持させる)
    counter += 1
    print(f"{counter}:{event.x},{event.y}")


tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.bind("<Button-1>", on_click)    # クリック処理     # 書き方は決まり    1=左クリック,2=中央クリック,3=右クリック
counter = 0


canvas.mainloop()  # 処理の後に書く
#