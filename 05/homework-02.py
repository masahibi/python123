def find(a, b):
    for x in a:
        if x == b:
            return a.index(x)    #インデックス番号

    return -1


i = input()
values = eval(i)
index = find(values, 100)

if index == -1:
    print("100は一つも含まれない")
else:
    print(f"100は{index}番目に含まれる")
#
