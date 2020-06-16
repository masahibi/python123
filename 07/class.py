# with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\example.txt", encoding="sjis") as file:
#    print(file.readline().rstrip("\n"))
#    print(file.readline().rstrip("\n"))
#    print(file.readline().rstrip("\n"))

with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\numbers.txt", encoding="sjis") as file:
    a = float(file.readline())
    b = float(file.readline())
    c = float(file.readline())
    print(a + b + c)

# line = "2015/4/1, 13.9, 8, 1"
# fields = line.split(",")
# print(fields)
# print(f"年月日：{fields[0]}")
# print(f"平均気温：{fields[1]}")
# print(f"品質情報：{fields[2]}")
# print(f"均質番号：{fields[3]}")

# data = input("年/月/日：")
# datas = data.split("/")
# print(f"{datas[0]}年{datas[1]}月{datas[2]}日")

# with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\numbers.txt", encoding="sjis") as file:
#     count = 0
#     total = 0
#     for line in file:
#         total += float(line)
#         print(total)
#         count += 1
#         print(count)
#     average = total / count
# print(f"average：{average}")

# with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\target.txt", mode="w") as file:
#     print(file.name)
#     file.write(str(100) + "\n")
#     number = 100
#     file.write(f"{number}")

#numbers = eval(input("リスト："))
#with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\target.txt", mode="w") as file:
#    for number in numbers:
#        file.write(f"{number}\n")





