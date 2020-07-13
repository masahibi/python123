import turtle, time

t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
rotate = 1
delay = 0.01
screen = turtle.getscreen()
screen.tracer(0)

while True:
    for x in range(5):
        t1.forward(-100)
        t1.right(360 / 5 * 2)
    t1.right(rotate)

    for x in range(3):
        t2.forward(100)
        t2.left(360 / 3)
    t2.right(rotate)

    """for y in range(4):
        t3.goto(y,y)
        t3.forward(100)
        t3.left(90)
    t3.up()
    t3.goto(50,50)
    screen.update()
    t3.right(rotate)

    t3.goto(0,0)
    t3.down()
"""
    screen.update()
    time.sleep(delay)
    t1.clear()
    t2.clear()
    t3.clear()
#





