while True:
    today = input("今日の曜日は？(例:月、火):")

    if today in ["月", "火", "水", "木", "金", "土", "日"]:
        question1 = f"問題１:今日は{today}曜日です。では昨日の曜日は何か?"
        selection1 = "a:水曜, b:月曜日, c:a,b以外:"
        answer1 = input(question1 + "\n" + selection1)

        if answer1 in ["a", "b", "c"]:
            if (today == "木" and answer1 == "a") or (today == "火" and answer1 == "b"):
                print("正解")
            elif today != "木" and today != "火" and answer1 == "c":
                print("正解")
            else:
                print("不正解")
            break
        else:
            print(f"入力された選択肢{answer1}は正しくありません")
    else:
        print(f"入力された「{today}」は正しくありません")
input()
while True:
    question2 = f"問題2:この中でスクリプト言語はどれか?"
    selection2 = "a:Java, b:C/C++, c:Pyhon:"
    answer2 = input(question2 + "\n" + selection2)
    if answer2 == "a" or answer2 == "b":
        print("不正解")
        break
    elif answer2 == "c":
        print("正解")
        break
    else:
        print(f"入力された選択肢{answer2}は正しくありません")
