stations = {"静岡": [3350, 3300], "名古屋": [6260, 4620], "京都": [8210, 53990], "新大阪": [8750, 5390]}

place = int(input("降車駅を選んでください。\n (1)静岡、(2)名古屋、(3)京都、(4)新大阪："))
ticket = int(input("特急券の種類を選んでください。\n (1)指定席(2)自由席(3)今は購入しない："))

if place == 1:    # 静岡
    prices = stations["静岡"]
    print("東京から静岡まで")
    print(f"運賃{prices[0]}円")
    if ticket == 1:    # 指定席
        print(f"特急券(指定席):{prices[1]}円")
        print(f"合計{prices[0] + prices[1]}")
    elif ticket == 2:    # 自由席
        print(f"特急券(自由席):{prices[1] - 520}円")
        print(f"合計{prices[0] + prices[1] - 520}")
    else:    # 購入なし
        print(f"合計{prices[0]}円")

if place == 2:    # 名古屋
    prices = stations["名古屋"]
    print("東京から名古屋まで")
    print(f"運賃{prices[0]}円")
    if ticket == 1:    # 指定席
        print(f"特急券(指定席):{prices[1]}円")
        print(f"合計{prices[0] + prices[1]}")
    elif ticket == 2:    # 自由席
        print(f"特急券(自由席):{prices[1] - 520}円")
        print(f"合計{prices[0] + prices[1] - 520}")
    else:    # 購入なし
        print(f"合計{prices[0]}円")

if place == 3:    # 京都
    prices = stations["京都"]
    print("東京から京都まで")
    print(f"運賃{prices[0]}円")
    if ticket == 1:    # 指定席
        print(f"特急券(指定席):{prices[1]}円")
        print(f"合計{prices[0] + prices[1]}")
    elif ticket == 2:    # 自由席
        print(f"特急券(自由席):{prices[1] - 520}円")
        print(f"合計{prices[0] + prices[1] - 520}")
    else:    # 購入なし
        print(f"合計{prices[0]}円")

if place == 4:    # 新大阪
    prices = stations["新大阪"]
    print("東京から新大阪まで")
    print(f"運賃{prices[0]}円")
    if ticket == 1:    # 指定席
        print(f"特急券(指定席):{prices[1]}円")
        print(f"合計{prices[0] + prices[1]}")
    elif ticket == 2:    # 自由席
        print(f"特急券(自由席):{prices[1] - 520}円")
        print(f"合計{prices[0] + prices[1] - 520}")
    else:    # 購入なし
        print(f"合計{prices[0]}円")
#