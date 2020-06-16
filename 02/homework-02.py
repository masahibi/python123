pat0 = "ーー"
pat1 = "＋＋"

pattern1 = ((pat0 + pat1) * 8 + "\n") * 2
pattern2 = ((pat1 + pat0) * 8 + "\n") * 2

flag = (pattern1 + pattern2) * 4

print(flag)
