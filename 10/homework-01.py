import turtle

t = turtle.Pen()


def star(t, red, green, blue):
    t.fillcolor(red, green, blue)  # 中だけが色
    t.begin_fill()
    for x in range(6):
        t.left(60)
        t.forward(50)
        t.right(60)
        t.circle(10)
        t.right(60)
        t.forward(50)
    t.end_fill()


star(t, 1, 1, 0)
