"""
改行させたいときは
\nをつける。
この\nをエスケープエヌ
とよむ。
 """
"""
values="valuesbc\ndef"
print(values)
values="valuesbc\\ndef"
print(values)
 """
"""
print("10+20=")
i = input()
valuesnswer = 30
if valuesnswer == int(i):
    print("〇")
else:
    print("×")
 """
"""
block1 = 1    #Block1
block2 = 1    #Block1

if block1 == 1:    #Block1
    print("〇")    #Block1#Block2
    print("〇")    #Block1#Block2
    if block2 == 2:    #Block1#Block2
        print("×")    #Block1#Block2#Block3
        print("×")    #Block1#Block2#Block3
        print("×")    #Block1#Block2#Block3
    print("△")    #Block1#Block2
    print("△")    #Block1#Block2
 """
"""
block1 = 1    #Block1
block2 = 1    #Block1

if block1 == 1:    #Block1
    print("〇")    #Block1#Block2
    print("〇")    #Block1#Block2
    print("〇")    #Block1#Block2

block1 = 1    #Block1
block2 = 1    #Block1

if block2 == 2:    #Block1
        print("×")    #Block1#Block3
        print("×")    #Block1#Block3
        print("×")    #Block1#Block3
 """
"""
print("点数入力")
i = input()
if int(i) >= 60:
    print("合格")
else:
    print("不合格")
 """
"""
print("じゃんけん？\n（１）グー\n（２）チョキ\n（３）パー")
i = input()
if int(i) == 1:
    print("グー")
else:
    if int(i) == 2:
        print("チョキ")
    else:
        print("パー")
 """
"""
print("10+20=?\n(1)20\n(2)30")
i = input()
if int(i) == 1:
    print("不正解")
else:
    if int(i) == 2:
        print("正解")
    else:
        print("invvalueslid vvalueslue!")
 """
"""
print("じゃんけん？\n（１）グー\n（２）チョキ\n（３）パー")
i = input()
if int(i) == 1:
    print("グー")
elif int(i) == 2:
    print("チョキ")
elif int(i) == 3:
    print("パー")
else:
    print("invalid value!")
 """

print("点数入力？")
i = input()
if int(i) >= 80:
    print("素晴らしい")
elif int(i) >= 60:
    print("合格")
else:
    print("不合格")
#


