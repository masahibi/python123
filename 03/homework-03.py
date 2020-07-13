inputX = input("x = ?")
inputY = input("y = ?")
x = float(inputX)
y = float(inputY)
a = "PはR1とR2の両方の円の内側にある。"
b = "PはR1の内側にある。"
c = "PはR2の内側にある。"
d = "PはR1の内側でもなく、R2の内側でもない。"

if x**2 + y**2 < 10**2 and (x-10)**2 + y**2 < 10**2:
    print(a)
elif x**2 + y**2 < 10**2:
    print(b)
elif (x-10)**2 + y**2 < 10**2:
    print(c)
else:
    print(d)

"""
実験結果３(2)
(x,y)  |領域
-------+--------
(1,1)  |A
(1,5)  |B
(11,0) |C
(5,9)  |D
"""
#