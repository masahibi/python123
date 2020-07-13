"""
# 今までの書き方
from dataclasses import *

@dataclass
class Card:
    suit: str
    rank: int

def print_card(card):
    print(f"{card.suit}の{card.rank}")

card = Card("heart", 10)
print_card(card)
"""
"""
# メソッドを用いた書き方
from dataclasses import *

@dataclass
class Card:
    suit: str
    rank: int

    def print_card(self):
        print(f"{self.suit}の{self.rank}")

card = Card("heart", 10)
card.print_card()
"""
"""
# printなど、もともとある関数名を使えるようになる
from dataclasses import *

@dataclass
class Card:
    suit: str
    rank: int

    def print(self):
        print(f"{self.suit}の{self.rank}")

card = Card("heart", 10)
card.print()
"""
"""
# 引数が１つで書ける
from dataclasses import *

@dataclass
class Card:
    suit: str
    rank: int

    def print(self,count):
        for x in range(count):
            print(f"{self.suit}の{self.rank}")

card = Card("heart", 10)
card.print(10)
"""
"""
# コンストラクタ
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def print_card(card):
        print(f"{card.suit}の{card.rank}")

card = Card("haert",10)
card.print_card()
"""
"""
# ポリモーフィズム
from dataclasses import *

@dataclass
class Square:
    width: float
    height:float
    def area(self):
        return self.width * self.height

@dataclass
class Circle:
    radius: float
    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(3,4),Circle(5)]
for shape in shapes:
    print(f"{shape}の面積：{shape.area()}")
"""
# プロトコル
from dataclasses import *

@dataclass
class Card:
    suit: str
    rank: int

    def __str__(self):
        return f"{self.suit}の{self.rank}"

card = Card("spade",1)
print(f"カード：{card}")
#
