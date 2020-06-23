import random
from dataclasses import *


@dataclass
class Card:
    suit: str
    rank: int


def new_stock():  # 山札作成
    stock = []  # リストの初期化
    for suit in ["spade", "heart", "diamond", "club"]:
        for rank in range(1, 14):
            stock.append(Card(suit, rank))
    random.shuffle(stock)
    return stock


def new_hand(stock):  # 最初の手札
    cards = []
    for x in range(5):
        card = stock.pop()
        cards.append(card)
    return cards


def new_cards(stock, number, hand):  # 交換手札
    cards = hand  # 変える前の手札
    for x in number:    # [2,4]
        card = stock.pop()  # 山札を捨てる
        hand[x] = card    # ｘ番目のカードを山札のに変える
    return cards


stock = new_stock()  # 初期化   山札
first_hand = new_hand(stock)  # 最初の手札
print(f"最初の手札：{first_hand}")  # 最初の手札
number = eval(input("枚数目?\n"))  # [2,4]

hand = new_cards(stock, number, first_hand)  # 手札交換
print(f"山札の枚数：{len(stock)}")  # 山札の枚数
print(f"交換後の手札：{hand}")  # 交換後の手札
