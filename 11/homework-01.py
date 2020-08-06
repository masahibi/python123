def load_dictionary():
    results = {}
    with open(r"dictionary.txt", encoding="UTF8") as file:
        for line in file:
            words = line.strip("\n").split(":", 2)
            if len(words) == 2:
                k = words[0]
                v = words[1]
                results[k] = v
    return results

dict = load_dictionary()
while True:
    print("-------------------------------")
    key = input("単語を入力してください：")
    if key == "":
        break
    elif key in dict:
        print(dict[key])
    else:
        print("単語が登録されていません")
#