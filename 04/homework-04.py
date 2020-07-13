i = input("入れ子リスト")
aa = eval(i)

x = max(aa[0])
y = aa[0]

for a in aa:
    print(max(a))
    if max(a) > x:
        x = max(a)
        y = a
print(y)

'-------------------------------'
x = min(aa[0])
y = aa[0]
for a in aa:
    print(min(a))
    if min(a) < x:
        x = min(a)
        y = a
print(y)
#


