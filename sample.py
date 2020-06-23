a = eval(input("入れ子リスト："))
b = max(a[0])
max_list = a[0]
c = min(a[0])
min_list = a[0]
for x in a:
    if max(x) > b:
        b = max(x)
        max_list = x

    if min(x) < c:
        c = min(x)
        min_list = x

print(f"最大値：{max}")
print(f"最大値を含むリスト：{max_list}")
print()
print(f"最小値：{min}")
print(f"最小値を含むリスト：{min_list}")