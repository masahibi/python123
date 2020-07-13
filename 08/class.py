import random
from dataclasses import *
@dataclass
class Card:
    suit: str
    rank: int

@dataclass
class TelephonBook:
    name: str
    mail: str
    tel: str
    remark: str
    member: str

"""
i = input("name?")
# 初期化
tb = [
    TelephonBook("A", "a@aaa.com", "aaaa-aaaa", "2020/01/01", "サークルA"),
    TelephonBook("B", "b@bbb.com", "bbbb-bbbb", "2020/02/01", "サークルB"),
    TelephonBook("C", "c@ccc.com", "cccc-cccc", "2020/03/01", "サークルC")
]
for x in tb:
    if i == x.name:
        print(f"{x.name},{x.mail},{x.tel},{x.remark},{x.member}")
"""

# entity(実体)
def spade(rank):
    return Card("spade",rank)
def heart(rank):
    return Card("heart",rank)
def change_heart(hand):
    for x in hand:
        x.suit = "heart"
def new_stock():
    stock = []    # リストの初期化
    for suit in ["spade","heart","diamond","club"]:
        for rank in range(1,14):
            stock.append(Card(suit,rank))
    random.shuffle(stock)
    return stock
def print_card(card):
    print(f"トランプ[{card.suit}の{card.rank}]")
def is_flush(hand):
    first = hand[0]
    for card in hand:
        if first.suit != card.suit:
            return False
    return True
def new_hand(stock):
    cards = []
    for x in range(5):
        card = stock.pop()
        cards.append(card)
    return cards
def take_cards(stock,number):
    cards = []
    for x in range(number):
        card = stock.pop()
        cards.append(card)
    return cards

"""
c = Card("heart", 5)
print(f"トランプ[{c.suit},{c.rank}]")
hand = [
    Card("spade", 5),
    Card("heart", 6),
    Card("diamond", 7),
    Card("club", 8),
    Card("spade", 9)
]
print(f"トランプ[{hand[0].suit},{hand[0].rank}]")
for x in hand:
    print(f"トランプ[{x.suit},{x.rank}]")
"""


"""
# 初期化
hand1 = [
    Card("spade", 5),
    Card("heart", 6),
    Card("diamond", 7),
    Card("club", 8),
    Card("spade", 9)
]
hand2 = [
    Card("spade", 5),
    Card("spade", 6),
    Card("spade", 7),
    Card("spade", 8),
    Card("spade", 9)
]

print(is_flush(hand1))
print(is_flush(hand2))
"""
number = int(input("枚数?\n"))
stock = new_stock()    # 初期化
hand = take_cards(stock,number)
print(hand)
print(len(hand))
print(len(stock))
# change_heart(hand)
# print(hand)
#



