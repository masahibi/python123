import turtle
t = turtle.Pen()

for x in range(3):
    t.forward(100)
    t.left(360 / 3)
t.up()
t.goto(-150,0)
t.down()

for x in range(5):
    t.forward(100)
    t.left(360 / 5)
t.up()
t.goto(150,0)
t.down()

for x in range(5):
    t.forward(100)
    t.right(360 / 5 * 2)
