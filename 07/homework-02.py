with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\20k1026-06-register.txt",encoding="utf8") as file:
    total = 0
    count = 0
    for line in file:    # 1(商品名、単価、個数)   2(リンゴ、５０、１２)
        data = line.split(",")    # １(["商品名", "単価", "個数"])   2("")
        if count == 0:
            count = 1
            continue
        total = total + float(data[1]) * float(data[2])    # total = 0 + "単価" * 個数
    print(f"合計：{total}")
#