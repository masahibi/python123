def has_negative(a):
    for x in a:
        if x < 0:
            return True
    return False


i = input()
values = eval(i)

if has_negative(values):
    print("負の値が含まれる")
else:
    print("負の値が含まれない")
#