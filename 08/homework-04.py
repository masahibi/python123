
from dataclasses import *

# with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\08\20k1026-07-address.txt") as file:
#     for line in file:
#         data = line.split(",")
        # print(f"{data[0]}、{data[1]}、{data[2]}、{data[3]}、{data[4]}")
        # with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\08\20k1026-07-sample.txt",encoding="UTF8",mode="a") as file:
        #     file.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}\n")

def load():
    with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\08\20k1026-07-address.txt") as file:
        list = []
        for line in file:
            data = line.split(",")
            list.append(data)
            print(list)
    for x in list:
        print(x)
    return list
# load("男")

def save(data):
    with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\08\20k1026-07-sample.txt", encoding="UTF8", mode="a") as file:
        for x in data:
            file.write(f"{x}\n")
save(load())
"""
@dataclass
class TelephonBook:
    name: str
    mail: str
    tel: str
    remark: str
    member: str

i = input("name?")
# 初期化
tb = [
    TelephonBook("A", "a@aaa.com", "aaaa-aaaa", "2020/01/01", "サークルA"),
    TelephonBook("B", "b@bbb.com", "bbbb-bbbb", "2020/02/01", "サークルB"),
    TelephonBook("C", "c@ccc.com", "cccc-cccc", "2020/03/01", "サークルC")
]
for x in tb:
    if i == x.name:
        print(f"{x.name},{x.mail},{x.tel},{x.remark},{x.member}")
"""