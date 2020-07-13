import math

import turtle

t = turtle.Pen()

from dataclasses import *


@dataclass
class Stu:
    name: str
    math: int
    science: int
    eng: int


def sin(a):
    return math.sin(a * math.pi)


def cos(b):
    return math.cos(b * math.pi)


'--------------------------------------------'
# 　数学のグラフ（メモリ）
for x in range(11):
    y = x * 10  # 0,10,20,30,40,50,60,70,80,90,100
    t.goto(y * 3, 0)  # 見やすいように *3 した
    t.write(str(y))

t.up()
t.goto(y * 3 + 50, 0)  # 線の先端から +50 のところに書く
t.write("数学")
t.goto(0, 0)
t.down()

'--------------------------------------------'
# 　物理のグラフ（メモリ）
for x in range(11):
    y = x * 10
    t.goto(-(y * 3 * cos(0.33)), y * 3 * sin(0.33))  # 1/3だから、0.33
    t.write(str(y))

t.up()
t.goto(-((y * 3 + 50) * cos(0.33)), (y * 3 + 50) * sin(0.33))
t.write("物理")
t.goto(0, 0)
t.down()

'--------------------------------------------'
# 英語のグラフ（メモリ）
for x in range(11):
    y = x * 10
    t.goto(-(y * 3 * cos(0.33)), -(y * 3 * sin(0.33)))
    t.write(str(y))

t.up()
t.goto(-((y * 3 + 50) * cos(0.33)), -((y * 3 + 50) * sin(0.33)))
t.write("英語")

'--------------------------------------------'
stu = [Stu("Alice", 100, 65, 57),  # クラスのリスト
       Stu("Bob", 45, 98, 100),
       Stu("Charley", 50, 50, 50)]


def score(student):  # 実際に書くグラフ
    i = student - 1  # インデックス番号
    t.up()
    t.goto(150, 150)
    t.write(stu[i].name)    # 名前
    t.goto(stu[i].math * 3, 0)    # 数学
    t.down()
    t.goto(-(stu[i].science * 3 * cos(0.33)), stu[i].science * 3 * sin(0.33))    # 物理
    t.goto(-(stu[i].eng * 3 * cos(0.33)), -(stu[i].eng * 3 * sin(0.33)))    # 英語
    t.goto(stu[i].math * 3, 0)    # 数学


student = int(input("(1)Alice (2)Bob (3)Charley："))
score(student)
