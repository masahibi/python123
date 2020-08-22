# with open (r"sample.txt") as file:
#     goukei = 0
#     for line in file:
#         data = int(line)
#         # data = line.sprit("\n")    改行でスプリットはできない
#         if data % 2 == 0:
#             goukei += data
# print(goukei)
#
# '-----------------------------------------------------'
# # 日比野案
# n = input("1～３の5桁")
# one = 0
# three = 0
# for x in range(5):
#     if n[x] == "1":
#         one += 1
#     else:
#         three += 1
# if one > three:
#     print(1)
# else:
#     print(3)
#
# # 文字列はリストだったらしいｗｗ
# # a = "17324"
# # a[0] == "1"
# # a[1] == "7"
#
# # 川端案
# line = "13311"
# goukei = 0
# list = line.split("1")
# for x in list:
#     goukei += int(x)
# if goukei == 0 or goukei == 3 or goukei == 6 or goukei == 33:
#     print(1)
# else:
#     print(3)
#
# # 磯貝案
# i=input()
# x=int(i)
# a=0
# b=0
# for i in range(5):
#     x=int(x)
#     if x%10==1:
#         a=a+1
#     else:
#         b=b+1
#     x=x/10
# if a<b:
#     print(3)
# else:
#     print(1)

# 和市案
i = input(">>>")
count_1 = 0
count_3 = 0
for x in i:
    if x == "1":
        count_1 += 1
    elif x == "3":
        count_3 += 1
if count_1 > count_3:
    print(1)
else:
    print(3)