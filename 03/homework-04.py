import random

hands = ["グー", "チョキ", "パー"]

while True:
    r = random.random() * 3
    if r < 1.0:
        pc = hands[0]  # グー
    elif r < 2.0:
        pc = hands[1]  # チョキ
    else:
        pc = hands[2]  # パー

    player = input("0:グー,1:チョキ,2:パー:")

    if player in ["0", "1", "2"]:
        print(f"コンピュータが選んだのは{pc}")
        if pc == hands[0]:  # pcグー
            if player == "0":
                print("結果:あいこ")
            elif player == "1":
                print("結果:負け")
                break
            else:
                print("結果:勝ち")
                break
        if pc == hands[1]:  # pcチョキ
            if player == "0":
                print("結果:勝ち")
                break
            elif player == "1":
                print("結果:あいこ")
            else:
                print("結果:負け")
                break
        if pc == hands[2]:  # pcパー
            if player == "0":
                print("結果:負け")
                break
            elif player == "1":
                print("結果:勝ち")
                break
            else:
                print("結果:あいこ")

    else:
        print("正しく入力してください")
#

