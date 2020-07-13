with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\06-extract-in_SJIS.csv") as file:
    count = 0
    for line in file:
        data = line.split(",")
        if count <= 2:
            count = count + 1
            continue
        print(f"{data[0]}：{data[1]}")    # ここは無くても良い

        with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\07\20k1026-06-extract.txt",mode="a") as file:
            file.write(f"{data[0]},{data[1]}\n")
#

