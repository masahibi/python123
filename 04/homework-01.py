import turtle  # Turtleモジュールのインポート

t = turtle.Pen()

for x in range(50):
    t.left(90)
    t.forward(30 + x * 5)


