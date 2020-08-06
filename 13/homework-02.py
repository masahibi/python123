# 課題1
from dataclasses import *
from tkinter import *


@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int


def square(x, y, w, h):    # 長方形描写
    global canvas
    canvas.create_rectangle(x, y, x + w, y + h)


tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
rect = Rect(100, 100, 100, 200)
square(rect.x, rect.y, rect.w, rect.h)


# 課題2
def area_rect(rect):    # 長方形の面積
    area = rect.w * rect.h
    return area


print(area_rect(rect))


# 課題3
def map_area_square(rects):    # 複数の長方形の面積
    areas = []
    for x in rects:
        areas.append(area_rect(x))
    return areas


rectangles = [Rect(0, 0, 2, 4), Rect(0, 0, 4, 4), Rect(0, 0, 3, 2)]
print(map_area_square(rectangles))


# 課題4
def filter_rect_20(rects):
    areas = map_area_square(rects)
    result = []
    for x in areas:
        if x >= 20:
            result.append(x)
    return result


print(filter_rect_20(rectangles))

#
# 課題５
def fold_plus(values):
    result = 0
    for x in values:
        result += x
    return result


print(fold_plus(map_area_square(rectangles)))


# 問題1
def includes_point(r, x, y):    # 四角形の中か判定
    if x >= r.x and y >= r.y and x <= r.x + r.w and y <= r.y + r.h:
        return "含まれています"
    else:
        return "含まれていません"


print(includes_point(Rect(0,0,2,2), 1, 1))
print(includes_point(Rect(0,0,2,2), 3, 3))


# 問題2
def includes_rect(r1, r2):
    if includes_point(r1, r2.x, r2.y) == "含まれています" and includes_point(r1, r2.x+r2.w, r2.x+r2.h) == "含まれています":
        return True
    else:
        return False


r1 = Rect(-1, -1, 4, 4)
r2 = Rect(0, 0, 2, 2)
print(includes_rect(r1, r2))
print(includes_rect(r2, r1))
print(includes_rect(r1, r1))

canvas.mainloop()
