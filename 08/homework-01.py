from dataclasses import *

@dataclass
class Item:
    name: str
    price: int
    tax: float

def total_price(item):
    total = 0
    for x in item:
        total = total + x.price * (1 + x.tax)    # 税込み計算　　x.price = 100   x.tax = 0.08
        print(f"商品名：{x.name}、価格：{x.price}")    # x.name = リンゴ　　x.price = 100
    print(f"合計：{total}")

items = [
    Item("リンゴ",100,0.08),    # Item(name,price,tax)
    Item("ブドウ",150,0.08),
     Item("オレンジ",200,0.10)
]
total_price(items)

