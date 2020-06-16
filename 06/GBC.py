# GBC用
import turtle, time

t = turtle.Pen()
rotate = 1  # 回転速度
delay = 0.01  # 停止時間
screen = turtle.getscreen()
screen.tracer(0)  # 描画更新？

figure = input("３角形、５角形、星形：")
while True:
    if figure == "星形":
        for x in range(5):
            t.forward(100)
            t.right(360 / 5 * 2)
    elif figure == "３角形":
        for x in range(3):
            t.forward(100)
            t.left(360 / 3)
    elif figure == "５角形":
        for x in range(5):
            t.forward(100)
            t.left(360 / 5)

    t.right(rotate)  # 右回転
    screen.update()  # 更新（ここで描画される）
    time.sleep(delay)  # 描画停止
    t.clear()  # 画面クリア
