
#範囲コメントは「”””」とする

totvaluesl=0
print(totvaluesl)
totvaluesl=totvaluesl+1
# print(total)
total = 0
total=total+2
print(total)
total=total+3
print(total)
total=total+4
print(total)
total=total+5
print(total)

'--------------------------------------------'
#正三角形の面積を求めよ
length = 2
s1 = length * length * 1.732/2/2
print(s1)

import math
s2 = length * length * math.sqrt(3)/2/2
print(s2)

s3 = length**2 * 3**(1/2)/2 /2
print(s3)

'-------------------------------------------'
#0.2nの表記方法
print( .2)
#改行の書き方
print('''a
b''')
#文字列の結合
print("hello" + " " + "world" )
#文字列の繰り返し
print("a" * 3)
#クオーテーションを文字で使いたいとき
print('''He said,"Aren't can't shouldn't wouldn't."''')

'---------------------------------------------'
#フィボナッチ数列の０－４項をもとめよ。また、総和と平均値をもとめよ。
f0 = 0
f1 = 1
f2 = f0 + f1
print(f2)
f3 = f1 + f2
print(f3)
f4 = f2 + f3
print(f4)
#総和
total=f0+f1+f2+f3+f4
print(total)

print()
total=f0
total=total+f1
print(total)
total=total+f2
print(total)
total=total+f3
print(total)
total=total+f4
print(total)
#平均
ave=total/5
print(ave)

print()
count=0
total=0
#個数のカウント
total=total+f0
count=count+1
print(count)
total=total+f1
count=count+1
print(count)
total=total+f2
count=count+1
print(count)
total=total+f3
count=count+1
print(count)
total=total+f4
count=count+1
print(count)

ave=total/count
print(ave)
#横グラフ的な感じ
print()
print("*"*f0)
print("*"*f1)
print("*"*f2)
print("*"*f3)
print("*"*f4)

'----------------------------------'
#文字列を用いてフィボナッチ数列を求めよ。
s0=""
s1="*"
s2=s0+s1
s3=s1+s2
s4=s2+s3

print(s0)
print(s1)
print(s2)
print(s3)
print(s4)

'-------------------------------------'
#数値リスト
a=[1,2,3,4,5]
print(max(a))
print(min(a))
print(sum(a))

'-----------------------------------------'
messages=["Do ", "I ", "you ", "am ", "like ", "a ", "python ", "good ", "?", "programmer "]
print(messages)
print(messages[0])

message1= messages[0]+messages[2]+messages[4]+messages[6]+messages[8]
print(message1)

message2=""
message2=message2+messages[1]
message2=message2+messages[3]
message2=message2+messages[5]
message2=message2+messages[7]
message2=message2+messages[9]
print(message2)

print(messages[2:5])     #２以上５未満
print(messages[0:10:2])     #0以上10未満2の倍数

'-----------------------------------------'
#フィボナッチ数列の第０項から第１０項までの数値からなるリストで、和を求めよ。
fibonacci=[0,1,1,2,3,5,8,13,21,34,55]
print(len(fibonacci))     #lenでリストの個数(長さ)を返せる

print(max(fibonacci))
print(min(fibonacci))
print(sum(fibonacci))

'-------------------------------------------'
#リンゴ１５０円、いちご１２０円、さくらんぼ５８円の辞書を作成せよ。リンゴ２個、いちご２５個、さくらんぼ７２個をもとめよ。
fruits={"apple":150, "strawberry":120, "cherry":58}
print(fruits["apple"])
total=fruits["apple"]*2+fruits["strawberry"]*25+fruits["cherry"]*72
print(total)

qty_app=2
qty_str=25
qty_che=72
total=fruits["apple"]*qty_app+fruits["strawberry"]*qty_str+fruits["cherry"]*qty_che
print(total)

qty={"apple":2, "strawberry":25, "cherry":72}
total=0
name="apple"
total=total+fruits[name]*qty[name]
print(total)
name="strawberry"
total=total+fruits[name]*qty[name]
print(total)
name="cherry"
total=total+fruits[name]*qty[name]
print(total)








