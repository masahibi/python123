from tkinter import *

# カレンダー処理
def is_leap_year(year):
    # 閏年の判定
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def total_of_days(year, month):
    # 　該当月が何日か算出(閏年の時は2月に1日加える)
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days[1] = days[1] + 1
    return days[month - 1]

def day_of_week(year, month, day):
    # 該当日が何曜日か算出(日が０の符号化)
    return (year + int(year / 4) - int(year / 100) + int(year / 400) + int((13 * month + 8) / 5) + day) % 7

def create_list(year, month):
    # 開始曜日を加味して該当月のリスト作成
    values = []
    for x in range(day_of_week(year, month, 1)):
        values.append(" ")
    for x in range(1, total_of_days(year, month) + 1):
        values.append(f"{x:02}")
    return values

# canvas 表示
def print_text(x, y, year, month, values):
    tk = Tk()
    tk.title(f"{year}年{month}月")
    canvas = Canvas(tk, width=300, height=300)
    days = ["日", "月", "火", "水", "木", "金", "土"]
    dx = 0
    # 日（赤）、土（青）、それ以外（黒）
    for n in range(len(days)):
        if n == 0:
            color = "red"
        elif n == 6:
            color = "blue"
        else:
            color = "black"
        canvas.create_text(x + dx, y, text=days[n], fill=color, font=("Times", 20))
        dx = dx + 40
    dx = 0
    dy = 0
    # 日（赤）、土（青）、それ以外（黒）
    for n in range(len(values)):
        if n % 7 == 0:
            dx = 0
            dy += 40
            color = "red"
        elif n % 7 == 6:
            color = "blue"
        else:
            color = "black"
        canvas.create_text(x + dx, y + dy, text=values[n], fill=color, font=("Times", 20))
        dx = dx + 40
    canvas.pack()
    canvas.mainloop()

# 入力チェック
def check_num(values):
    for x in values:
        if not x.isdigit():
            return False
    return True

# ここからメイン
i = input("年/月\n")
values = i.split("/")
if check_num(values):
    print("数字が入力されました")
    year = int(values[0])
    month = int(values[1])
    values = create_list(year, month)
    print_text(30, 40, year, month, values)
else:
     print(tk,test="数字以外が入力されました")
