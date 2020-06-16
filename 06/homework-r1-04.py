import turtle, random

t = turtle.Pen()

for x in range(0,100):
    a = random.uniform(0, 100)
    b = random.uniform(0, 360)

    t.forward(a)
    t.left(b)

