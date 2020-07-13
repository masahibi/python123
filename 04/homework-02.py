a = eval(input("単価のリスト"))
b = eval(input("個数のリスト"))

c = len(a)
y = 0

for x in range(c):
    y += a[x] * b[x]
print(y)
#