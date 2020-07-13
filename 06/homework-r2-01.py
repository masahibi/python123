values = [{"x" : x,  "y" : y,  "z" : z} for x in range(100) for y in range(100) for z in range(100) if x < y and y < z  if x**2 + y**2 == z**2]

for d in values:
    print(d)    #組み合わせ全部
print(len(values))    #個数
print(f"最小のペア：{values[0]}")    #最小値ペア
print(f"最大のペア{values[-1]}")    #最大値ペア
#
