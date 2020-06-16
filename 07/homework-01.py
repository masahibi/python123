with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\20k1026-06-dictionary.txt",encoding="utf8") as file:
    dict = input("キーを入力してください：")    # input

    for line in file:
        data = line.split(":")   # ["input", "      "  ]
        if data[0] == dict:
            print(f"{data[1]}")



'--------------------------------------------'
