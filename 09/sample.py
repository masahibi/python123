values = ["10,20,30", "40,50,60", "70,80,90"]
result = []
for x in values:
    list = x.split(",")
    total = int(list[0]) + int(list[1]) + int(list[2])
    result.append(total)

with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\09\text.txt",mode="w") as file:
    for x in result:
        file.write(f"{x}\n")
#