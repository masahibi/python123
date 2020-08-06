import turtle

t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
t4 = turtle.Pen()

def position(t):  # 初期位置
    t.up()
    t.goto(-100, 0)
    t.down()

'-------------------------------------------------------------------------------'
# 縦軸
position(t2)
t2.left(90)
for x in range(5):
    t2.write(10 * x)
    t2.forward(50)  # 見やすいように５倍した

'-------------------------------------------------------------------------------'
# 横軸
position(t3)
for x in range(9):
    t3.forward(50)

'-------------------------------------------------------------------------------'
# グラフ記述
a = 0
position(t1)
with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\10\data.csv") as file:
    count = 0
    for line in file:
        data = line.split(",")
        if count < 6:  # 6行とばす
            count += 1
            continue
        t1.forward(20)
        '------------------------------------'
        # 最高気温
        for x in range(2):
            t1.color("red")
            t1.begin_fill()
            t1.forward(20)
            t1.left(90)
            t1.forward(float(data[1]) * 5)  # 見やすいように５倍した
            t1.left(90)
            t1.end_fill()
        t1.forward(20)

        '-------------------------------------'
        # 最低気温
        for x in range(2):
            t1.color("blue")
            t1.begin_fill()
            t1.forward(20)
            t1.left(90)
            t1.forward(float(data[4]) * 5)
            t1.left(90)
            t1.end_fill()
        t1.forward(20)

        '-------------------------------------------------------'
        # 日にち
        t4.up()
        t4.goto(-80 + a, -20)
        t4.write(data[0])
        a = a + 60
#