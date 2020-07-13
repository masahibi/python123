import turtle
t = turtle.Pen()

"""
def mycircle(t, size, red, green, blue, color):
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def square(t, size):
    for x in range(4):
        t.forward(size)
        t.left(90)


def filledsquare(t, size, red, green, blue, color):
    t.color(red,green,blue)
    t.begin_fill()
    square(t,size)
    t.end_fill()


def nonfillsquare(t, size, red, green, blue, color):
    t.color(color)
    square(t,size)


def colorsquare(t,size,red,green,blue,color,filled):
    t.color(red,green,blue)
    if filled == True:
        t.begin_fill()
    square(t,size)
    if filled == True:
        t.end_fill()


t = turtle.Pen()
# mycircle(t, 100, 1, 0.5, 0.5, "red")
# square(t, 50)
# filledsquare(t,50,0.5,1,0.5,"green")
# nonfillsquare(t,50,0,1,0,"blue")
colorsquare(t,50,0,0.5,0,"green",True)
colorsquare(t,50,0,1,0,"green",False)
"""

def practice1(t,length):
    for x in range(4):
        t.left(90)
        t.forward(length)
        t.right(90)
        t.forward(length)
        t.right(90)
        t.forward(length)

def practice2(t,length):
    for x in range(4):
        t.left(90)
        t.forward(length)
        t.right(135)
        t.forward(length / 2)
        t.left(90)
        t.forward(length / 2)
        t.right(135)
        t.forward(length)

def practice3(t,length):
    for x in range(5):
        t.left(108)
        t.forward(length)
        t.right(135)
        t.forward(length / 2)
        t.left(90)
        t.forward(length / 2)
        t.right(135)
        t.forward(length)


# practice1(t,40)
# practice2(t,40)
practice3(t,40)