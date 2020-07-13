"""
練習問題１
print(sum([1,2,3])/len([1,2,3]))
"""
"""
練習問題２
i = input()
score = int(i)
if score < 0:
    print(0)
else:
    print(score)
"""
"""
i = input()
score = int(i)
print(max(0,score))
print(min(100,score))
"""
"""
i = input()
score = int(i)
#print(max(0,score))
print(min(100,max(0,score)))
"""
"""
def plus1(a):
    return a + 1
result1 = plus1(100)
print(result1)
"""
"""
def zettai(x):
    if x < 0:
        return -x
    else:
        return x
print(zettai(-1))
print(zettai(100))
"""
"""
def mysum(vs):
    total = 0
    for x in vs:
        total += x
    return total
#values = [1,2,3]
values = eval(input("リスト："))             
print(f"total = {mysum(values)}")
"""
"""
def mymax(x,y):
    if x > y:
        return x
    else:
        return y
a = 200
b = 100
print(f"max={mymax(a,b)}")
"""
"""
def myprint(x,y):
    for i in range(y):
        print(x)    
myprint("Hello",10)
"""
"""
def f1(a):
    print(a)
    print(locals())    #ローカル領域の変数群の値を辞書型で返す
#    return
def f2(a,b):
    print(a+b)
    print(locals())
a = 100
f1(10)
f2(20,30)
print(a)
print(locals())
"""
"""
def is_positive(x):
    if x >= 0:
        return True
    else:
        return False
if is_positive(100):
    print("OK")
if is_positive(-100):
    print("NG")
"""
#
