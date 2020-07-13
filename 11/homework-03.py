import random

count = 0  # 最後のbreak 用
index = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # def pc 専用
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # インデックス番号の調整がめんどくさいため、0を設けた"


def field(number):
    print(f"{number[1]} | {number[2]} | {number[3]}\nー  ー  ー")
    print(f"{number[4]} | {number[5]} | {number[6]}\nー  ー  ー")
    print(f"{number[7]} | {number[8]} | {number[9]}")
    print("---------------------------------------------------")


def player(number, mark):
    while True:
        locate = int(input("番号を入力してください："))
        if number[locate] == "〇" or number[locate] == "×":
            print("そこは選べません")
        else:
            break
    number[locate] = mark


def pc(number, mark, index):
    while True:
        locate = random.choice(index)
        if number[locate] != "〇" and number[locate] != "×":
            break
    number[locate] = mark


def result(number, mark, count):
    if number[5] == mark:
        if (number[4] == mark and number[6] == mark) or (number[2] == mark and number[8] == mark) or (
                number[1] == mark and number[9] == mark) or (number[3] == mark and number[7] == mark):
            count = 1
    elif number[1] == mark:
        if (number[2] == mark and number[3] == mark) or (number[4] == mark and number[7] == mark):
            count = 1
    elif number[9] == mark:
        if (number[3] == mark and number[6] == mark) or (number[7] == mark and number[8] == mark):
            count = 1
    return count


"-----------------------------------------------------------------------------"
# ゲームスタート
field(number)
while True:
    mark_player = input("○か×を指定してください:")
    if mark_player == "〇":
        mark_pc = "×"
        break
    elif mark_player == "×":
        mark_pc = "○"
        break
    else:
        print("もう一度入力してください")

while True:
    player(number, mark_player)
    field(number)
    count1 = result(number, mark_player, count)
    if count1 == 1:
        print("あなたの勝ちです")
        break

    pc(number, mark_pc, index)
    field(number)
    count2 = result(number, mark_pc, count)
    if count2 == 1:
        print("あなたの負けです")
        break
