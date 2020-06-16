"""
for x in range (10000):
    print(f"ループ変数：{x}")
"""
"""
i = input("繰り返し回数>")
count = int(i)
for x in range(count):
    print(f"Hello,world{x + 1}")
"""
"""
count = int(input("繰り返し回数>"))
for x in range(count):
    print("Hello")
"""
"""
for x in range(5):
    print(f"残り{5-x}")
print("終了")
"""
"""
for x in range(5):
    for y in range(5):
            print(f"(x,y):({x},{y})")
"""
"""
values = [[1,2],[2,3]]
for x in values:
    print(f"要素：{x}")
    for y in x:
        print(f"要素：{y}")
"""
"""
i = input("リスト＞")
values = eval(i)
print(type(values))
for x in values:
    print(f"要素：{x}")
"""
"""練習問題１
i = input("リスト＞")
values = eval(i)    #intとおなじようにevalはリストにする
for x in values:
    print(x*2)
"""
"""
i = input("リスト＞")
values = eval(i)
for x in values:
    print(f"要素：{x}")
    if x < 10:
        print("OK")
    else:
        print("NG")
"""
"""
i = input("リスト＞")
values = eval(i)
current = 0
for x in values:
    print(f"ここまでの値(古い値):{current}+リスト要素：{x}")
    current= current + x
    print(f"これまでの値(新しい値):{current}")
print(f"合計：{current}")
"""
"""
i = input("リスト＞")
values = eval(i)
current = values[0]
for x in values:
    print(f"ここまでの値(古い値):{current}+リスト要素：{x}")
    if x > current:
        current = x
    print(f"これまでの値(新しい値):{current}")
print(f"最大値：{current}")
"""
"""
i = input("リスト＞")
values = eval(i)
for x in range(len(values)):
    print(f"index：{x}")
    print(f"要素数：{values[x]}")
"""
"""
i = input("リスト＞")
values = eval(i)
count = 0
total = 0
for x in values:
    count = count + 1
    total = total + x
print(f"平均値：{total/count}")
"""
"""
i = input("リスト＞")
values = eval(i)
current = values[0]
for x in values:
    print(f"ここまでの最小値(古い値):{current}+リスト要素：{x}")
    if x < current:
        current = x
    print(f"これまでの最小値(新しい値):{current}")
print(f"最小値：{current}")
"""
"""
values = eval(input("リスト＞"))
current = len(values[0])
for x in values:
    print(f"ここまでの最小値(古い値):{current}+リスト要素：{x}")
    if len(x) < current:
        current = len(x)
    print(f"これまでの最小値(新しい値):{current}")
print(f"最小値：{current}")
"""
"""
#課題１のヒント
import turtle
t = turtle.Pen()

current =0
for x in range(10):
    t.forward(50+current)
    t.right(90)
    current = current + 50
i = input()

for x in range(10):
    t.forward(100)
    t.left(90)
"""



