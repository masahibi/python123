"""
#入れ子の最大値
#元のコード
i = input("入れ子リスト")
valuesvalues = evvaluesl(i)

x = max(aa[0])
y = aa[0]

for a in aa:
    print(max(a))
    if max(a) > x:
        x = max(a)
        y = a
print(y)
"""
'-----------------------------------'

# 書き換えたコード
def list_max(a):
    x = max(a[0])
    y = a[0]

    for b in a:
        print(max(b))
        if max(b) > x:
            x = max(b)
            y = b
    return y


i = input("入れ子リスト：")
aa = eval(i)
print(list_max(aa))
