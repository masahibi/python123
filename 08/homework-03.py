import random
from dataclasses import *
@dataclass
class Card:
    suit: str
    rank: int

def new_stock():    # 山札作成
    stock = []    # リストの初期化
    for suit in ["spade","heart","diamond","club"]:
        for rank in range(1,14):
            stock.append(Card(suit,rank))
    random.shuffle(stock)
    return stock

def new_hand(stock):    # 最初の手札
    cards = []
    for x in range(5):
        card = stock.pop()
        cards.append(card)
    return cards
"""
def take_cards(stock,number):    # 交換手札
    cards = []
    for x in range(number):
        card = stock.pop()
        cards.append(card)
    return cards
"""
def new_cards(stock,number,hand):    # 交換手札
    cards = hand    # 変える前の手札
    add_card = []    # 加える手札
    for x in range(number):
        cards.pop()    # 手札を捨てる
        card = stock.pop()    # 山札を捨てる
        add_card.append(card)    # 山札から捨てたカードを空リストに加える
    cards.append(add_card)    # 元の手札に加える
    return cards



number = int(input("枚数?\n"))
stock = new_stock()    # 初期化   山札
first_hand = new_hand(stock)    # 最初の手札
print(f"最初の手札：{first_hand}")    # 最初の手札

hand = new_cards(stock,number,first_hand)    # 手札交換
print(f"山札の枚数：{len(stock)}")    # 山札の枚数
print(f"交換後の手札：{hand}")    # 交換後の手札

