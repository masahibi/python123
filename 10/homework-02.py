import turtle
t = turtle.Pen()

def check(t,red,green,blue):
    for x in range(11):    # 11列
        t.up()
        t.goto(0, -x * 20)    # 1辺２０
        t.down()
        for y in range(11):    # 横１列
            t.color(red, green + (y * 0.1), blue - (x * 0.1))
            t.begin_fill()
            t.up()
            t.goto(y * 20, -x * 20)
            t.down()
            x_even = x % 2 == 0    # x=even を　true
            y_even = y % 2 == 0
            if x_even == y_even:
                for z in range(4):    # 四角１個
                    t.forward(20)
                    t.left(90)
            t.end_fill()

check(t,0,0,1)
#