import turtle
t = turtle.Pen()

def blossom(t,red,green,blue,i):
    t.color(1,0,0)
    t.fillcolor(red,green,blue)
    t.begin_fill()
    t.left(90)
    for x in range(i):
        t.forward(40)
        t.right(135)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.right(135)
        t.forward(40)
        t.left(180 - 360 / i)
    t.end_fill()

i = int(input("回数："))
blossom(t,1,0.8,0.8,i)

