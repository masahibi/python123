import random

dice = [1, 2, 3, 4, 5, 6]  # サイコロの目
this_point = 100  # 初期ポイント

while True:
    print("----------------------------")
    dice1 = random.choice(dice)  # サイコロ1の目
    dice2 = random.choice(dice)  # サイコロ2の目

    print(f"現在のポイント：{this_point}")
    if this_point <= 0:
        print("賭けれるポイントがありません。")
        break

    choice = input("どっちに賭ける？(丁 or 半)：")
    betting_point = int(input("何ポイント賭ける？"))
    print(f"サイコロの目：{dice1}と{dice2}")

    if (dice1 + dice2) % 2 == 0:  # 和が偶数
        result = "丁"
        print(f"結果：{result}")
    else:
        result = "半"
        print(f"結果：{result}")

    if result == choice:
        print(f"あなたの勝ち：＋{betting_point}ポイント")
        this_point += betting_point
    else:
        print(f"あなたの負け：ー{betting_point}ポイント")
        this_point -= betting_point
#

