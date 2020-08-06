from dataclasses import *

@dataclass
class TelephonBook:
    name: str
    mail: str
    tel: str
    remark: str
    member: str

def load(new):
    address = []
    with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\08\20k1026-07-address.txt", encoding="UTF8") as file:
        for line in file:
            info = line.rstrip("\n")    # 改行を消す
            data = info.split(",")    # リストにする
            address.append(data)
        print(address)  # 追加前
    new = [new.name, new.mail, new.tel, new.remark, new.member]
    address.append(new)
    print(address)  # 追加後
    return address

def save(address):
    # with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\08\20k1026-07-sample.txt", encoding="UTF8", mode="a") as file:
    with open(r"C:\Users\admin\OneDrive\デスクトップ\python1\08\20k1026-07-address.txt", encoding="UTF8", mode="w") as file:
        for x in address:
            file.write(f"{x[0]},{x[1]},{x[2]},{x[3]},{x[4]}\n")

def add():
    name = input("名前：")
    mail = input("メールアドレス：")
    tel = input("電話番号：")
    remark = input("誕生日：")
    member = input("サークル：")

    new_address = TelephonBook(name, mail, tel, remark, member)
    return new_address

new_address = add()
address = load(new_address)
save(address)
#
