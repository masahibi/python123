import turtle

t = turtle.Pen()


def draw_rect(t, x, y, w, h):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)


for x in range(10):
    p = (x + 1) * -5
    s = (x + 1) * 10
    draw_rect(t, p, p*2, s, s * 2)
#