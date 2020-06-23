
with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\09\text.txt") as file:
    for x in file:
        vs = x.split(",")
        r = int(vs[0]) * int(vs[1]) + r
print(r)