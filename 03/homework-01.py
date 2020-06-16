score = int(input("0点から100点までの得点を入力してください:"))

if score >= 0 and score < 60:
    print("不合格です")
elif score >= 60 and score <= 100:
    print("合格です")
    if score >= 80:
        print("素晴らしい成績ですね")
else:
    print("範囲外の得点です")

"""
実験結果1(2)
入力 score : メッセージ
-1,101     : 範囲外の得点です
0,1,59     : 不合格です
60,61,79   : 合格です
80,81,100  : 合格です　素晴らしい成績ですね

"""
