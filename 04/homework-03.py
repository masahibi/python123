import turtle

t = turtle.Pen()

data = eval(input("データリスト："))

for x in data:
    for y in range(2):
        t.forward(10)
        t.left(90)
        t.forward(x)
        t.left(90)
    t.forward(20)

"""    t.forward(10)

    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(20)"""
#
