def is_recerved(a):
    b = len(a)
    for i in range(int(b / 2)):
        a[i], a[b - i - 1] = a[b - i - 1], a[i]    #これで入れ替わる
    return a


i = input()
rist = eval(i)
print(is_recerved(rist))


