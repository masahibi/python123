"""
count = 0
while True:

        i = input("入力＞")
        if i == "":
            print("終了します")
            break
        print(f"入力：{i}")

    count += 1
    print(count)
"""
"""
while True:
    print("よろしいですか？")
    i = input("入力＞")
    if i == "YES" or i == "はい":
        print("終了します")
        break
    print(f"入力：{i}")
"""
"""
import turtle
t = turtle.Pen()
while True:
    i = input("turtle＞")
    if i == "forward":
        t.forward(100)
    elif i == "left":
        t.left(90)
    elif i == "right":
        t.right(90)
    elif i == "turn":
        t.left(180)
    elif i == "quit":
        break
"""
"""
import random
value = random.choice(range(0, 37))
print(value)
"""
"""
import random
value = random.choice([1, 2, 3, 4, 4, 5, 5, 6, 6, 6])
print(value)
"""
import random
number = random.choice(range(1, 100))
count = 0
while True:
    value = int(input("数字？"))
    count += 1
    if value == number:
        print("正解です")
        print(f"入力回数：{count}回")
        break
    elif value > number:
        print("大きすぎます")
    else:
        print("小さすぎます")

#    if value - number == 1 or value - number == -1:
    if abs(value - number) == 1:    # abs は絶対値
        print("1だけ違います")
    if value % number == 0:
        print("正解の数字で割り切れる")
    if number % value == 0:
        print("正解の数字の倍数")
#